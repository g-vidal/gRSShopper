#!/usr/bin/env perl

#    gRSShopper 0.7  API 0.01  -- gRSShopper api module
#    7 May 2017 - Stephen Downes

#    Copyright (C) <2011>  <Stephen Downes, National Research Council Canada>
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#-------------------------------------------------------------------------------
#
#	    gRSShopper 
#           API Functions 
#
#-------------------------------------------------------------------------------
print "Content-type: text/html\n\n";


# Forbid bots

	die "HTTP/1.1 403 Forbidden\n\n403 Forbidden\n" if ($ENV{'HTTP_USER_AGENT'} =~ /bot|slurp|spider/);	
						

# Load gRSShopper

	use File::Basename;												
	use CGI::Carp qw(fatalsToBrowser);
	my $dirname = dirname(__FILE__);								
	require $dirname . "/grsshopper.pl";	
								

# Load modules

	our ($query,$vars) = &load_modules("api");


# Load Site

	our ($Site,$dbh) = &get_site("api");									





# Get Person  (still need to make this an object)

	our $Person = {}; bless $Person;				
	&get_person($dbh,$query,$Person);		
	my $person_id = $Person->{person_id};
	



# Restrict to Admin

	&admin_only();		
		



my $str; while (my ($x,$y) = each %$vars) 	{ $str .= "$x = $y <br>\n"; }
&send_email('stephen@downes.ca','stephen@downes.ca', 'api in',$str); 


	


if ($vars->{updated}) { 


	if ($vars->{type} eq "text" || $vars->{type} eq "textarea"  || $vars->{type} eq "wysihtml5" || $vars->{type} eq "select") {  &api_textfield_update(); }

	elsif ($vars->{type} eq "keylist") { &api_keylist_update();  }
	
	elsif ($vars->{type} eq "data") { &api_data_update();  }

	elsif ($vars->{type} eq "file") { &api_file_upload(); }

	elsif ($vars->{type} eq "file_url") { &api_url_upload(); }
	
	elsif ($vars->{type} eq "publish") { &api_publish(); }

	elsif ($vars->{type} eq "commit") { &api_commit(); }

    # Identify, Save and Associate File

#	my $file;
#	if ($query->param("file_name")) { $file = &upload_file($query); }		# Uploaded File
#	elsif ($vars->{file_url}) { $file = &upload_url($vars->{file_url}); }		# File from URL
	


#my $return = &form_graph_list("post","60231","author");

	


	print $return;
	exit;

}


	print "Content-type: text/html\n\n";
	print "ok";
	exit;



# API Keylist Update
#
# Find or, if not found, create a new $key record named $value
# Then create a graph entry linking the new $key with $table $id
#

sub api_keylist_update {

	my ($table,$key) = split /_/,$vars->{name};
	die "Field does not exist" unless &__check_field($table,$vars->{name}); 
	
	my $id = $vars->{table_id};
	my $value = $vars->{value};

	# Split list of input $value by ;
	my @keynamelist = split /;/,$value;

	# For each member of the list...
	foreach my $keyname (@keynamelist) {			

		# Trim leading, trailing white space 
		$keyname =~ s/^ | $//g;	 			

		# Are we looking for _name, _title ...?
		my $keyfield = &get_key_namefield($key);

		# can we find a record with that name or title?
		my $keyrecord = &db_get_record($dbh,$key,{$keyfield=>$keyname});	

		# Record wasn't found, create a new record, eg., a new 'author'
		unless ($keyrecord) {

			# Initialize values				
			$keyrecord = {
				$key."_creator"=>$Person->{person_id},
				$key."_crdate"=>time,
				$keyfield=>$keyname
			};

			# Save the values and obtain new record id
			$keyrecord->{$key."_id"} = &db_insert($dbh,$query,$key,$keyrecord);
		}	

		# Error unless we have a new record id
		print &error() unless $keyrecord->{$key."_id"};

		# Save Graph Data
		my $graphid = &db_insert($dbh,$query,"graph",{
			graph_tableone=>$key, graph_idone=>$keyrecord->{$key."_id"}, graph_urlone=>$keyrecord->{$key."_url"},
			graph_tabletwo=>$table, graph_idtwo=>$id, graph_urltwo=>"",
			graph_creator=>$Person->{person_id}, graph_crdate=>time, graph_type=>"", graph_typeval=>""}); 
	}
	
	# Return new graph output for the form		
	print &form_graph_list($table,$id,$key);

}



sub api_textfield_update {

#my $str; while (my ($x,$y) = each %$vars) 	{ $str .= "$x = $y <br>\n"; }
#&send_email('stephen@downes.ca','stephen@downes.ca', 'textfield update',$str."$vars->{table_name}, {$vars->{name} => $vars->{value}}, $vars->{table_id}"); 


	die "Field does not exist" unless (&__check_field($vars->{table_name},$vars->{name})); 
	my $id_number = &db_update($dbh,$vars->{table_name}, {$vars->{name} => $vars->{value}}, $vars->{table_id});
	if ($id_number) { &api_ok();   } else { &api_error(); }
	die "api failed to update $vars->{table_name}  $vars->{table_id}" unless ($id_number);


}

sub api_publish {

	die "Field $vars->{table_name},$vars->{name} does not exist" unless (&__check_field($vars->{table_name},$vars->{name})); 
	#my $id_number = &db_update($dbh,$vars->{table_name}, {$vars->{name} => $vars->{value}}, $vars->{table_id});
	$vars->{twitter} = &twitter_post($dbh,"post",$vars->{table_id});
	print $vars->{twitter}; exit;
	if ($id_number) { &api_ok();   } else { &api_error(); }
	die "api failed to update $vars->{table_name}  $vars->{table_id}" unless ($id_number);	
	
}

#
#             API Commit
#
#             Commits changes saved in the 'Form' table to the database
#             - creates table if necessary
#             - creates columns if necessary
#             - alters column to new type if necessary
#


sub api_commit {

	# Get the Form record from database
	my $record = &db_get_record($dbh,$vars->{table_name},{$vars->{table_name}."_id" => $vars->{table_id}});
	unless ($record) { print "<span style='color:red;'>Error: API failed to update $vars->{table_name}  $vars->{table_id}</span>"; exit; }		
	
	# Standardize form names to lower case (because some operations are case insensitive)
	$record->{form_title} = lc($record->{form_title});
	
	
	# Create table if table doesn't exist
	&db_create_table($dbh,$record->{form_title});

	# Get the existing columns from the table
	my $columns;
	my $showstmt = qq|SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = ? AND table_schema = ? ORDER BY column_name|;
	my $sth = $dbh -> prepare($showstmt)  or die "Cannot prepare: $showstmt FOR $record->{form_title} in $Site->{db_name} " . $dbh->errstr();
	$sth -> execute($record->{form_title},$Site->{db_name})  or die "Cannot execute: $showstmt " . $dbh->errstr();
	while (my $showref = $sth -> fetchrow_hashref()) {

		# Stash Columkn Data for future reference
		$columns->{$showref->{COLUMN_NAME}}->{type} = $showref->{DATA_TYPE};
		$columns->{$showref->{COLUMN_NAME}}->{size} = $showref->{CHARACTER_MAXIMUM_LENGTH};
	
	}
	
	# Go though the table structure defined in $record->{form_data}
	my @fcols = split /;/,$record->{form_data};
	my $titles = 0;
	
	# For each of the columns defined in the form data 
	foreach my $fcol (@fcols) {
		my ($fname,$ftype,$fsize) = split /,/,$fcol; 	# This assumes an order which could be a problem
		if ($titles == 0) { 
								# Fix that problem here
			$titles = 1; next; 			# Skip past titles
		}	
		
		# Does the column exist?
		my $columntitle = $record->{form_title}."_".$fname;
		
		# No
		unless ($columns->{$columntitle}) {  
		
			next if (&__map_field_types($ftype) eq "none"); 
		
			# Create New Column as per the Form Data
			my $sql;
			if (&__map_field_types($ftype) eq "text") { 
				$sql = qq|alter table |.$record->{form_title}.qq| add column $columntitle text;|; 
			} elsif (&__map_field_types($ftype) eq "int") { 
				unless ($fsize) { $fsize=15; }
				$sql = qq|alter table |.$record->{form_title}.qq| add column $columntitle int ($fsize);|; 
			} elsif (&__map_field_types($ftype) eq "varchar") { 
				unless ($fsize) { $fsize = 256; }
				$sql = qq|alter table |.$record->{form_title}.qq| add column $columntitle varchar ($fsize);|; 
			}
						
			$dbh->do($sql) or die "error creating $fname";	
			
		
		# Yes
		} else {		       		
		
			# Check for increased varchar size
			if (&__map_field_types($ftype) eq "varchar") {   		
				if ($columns->{$columntitle}->{size} < $fsize) {
					
					# And alter column size if necessary
					
					my $sql = qq|alter table |.$record->{form_title}.qq| modify $columntitle VARCHAR($fsize);|;
					$dbh->do($sql) or die "error embiggening $fname";	
	
				}
				
			}
		
		}
		
 	
	}


	my $id_number = &db_update($dbh,$vars->{table_name}, {$vars->{name} => 1}, $vars->{table_id});
	if ($id_number) { &api_ok();   } else { &api_error(); }
	die "api failed to update $vars->{table_name}  $vars->{table_id}" unless ($id_number);	
	
}

sub __map_field_types {
	
	my ($field) = @_;
	if ($field eq "select" || $field eq "date" || $field eq "varchar") { return "varchar"; }
	elsif ($field eq "text" || $field eq "textarea" || $field eq "wysihtml5" || $field eq "data") { return "text"; }
	elsif ($field eq "commit" || $field eq "publish" || $field eq "int") { return "int"; }	
	else { return "none"; }	
		
}


	
sub api_data_update {



    my $data = "";
    for (my $i=-1; $i < 100; $i++) {
    	my $row = "";
    	for (my $j=-1; $j < 100; $j++) { 
    	   my $slot = $i."-".$j;	
	   if ($vars->{$slot}) { 
	   	if ($row) { $row .= ","; }   
	   	$row .= $vars->{$slot};
	   }		
        }
        if ($data && $row) { $data .= ";"; }   
	$data .= $row;
    }

#$data = qq|name,type,size;name,textarea,256;nickname,textarea,256|;
    my $id_number = &db_update($dbh,$vars->{table_name}, {$vars->{field_name} => $data}, $vars->{table_id});


#my $str; while (my ($x,$y) = each %$vars) 	{ $str .= "$x = $y <br>\n"; }
#&send_email('stephen@downes.ca','stephen@downes.ca', 'data  update',$str.$data);    

	# Reset commit flag in case the table is 'form'
	if ($vars->{table_name} eq "form") {
#		&db_update($dbh,$vars->{table_name}, {form_commit => 0}, $vars->{table_id});		
	}
    
    if ($id_number) { &api_ok();   } else { &api_error(); }



#	my $id_number = &db_update($dbh,$vars->{table_name}, {$vars->{name} => $vars->{value}}, $vars->{table_id});
#	if ($id_number) { &api_ok();   } else { &api_error(); }
	#die "api failed to update $vars->{table_name}  $vars->{table_id}";
    #enless ($id_number);


}

sub api_ok {

	print qq|&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:green;">ok!</a>|;
	exit;

}

sub api_error {


	print "300 API Error - failed to update $vars->{table_name}  $vars->{table_id} \n";
	exit;

}

sub api_file_upload {

			



	# Upload the file

	my $file = &upload_file(); 
	&api_save_file($file);

	# Return new graph output for the form		
	print &form_graph_list($vars->{graph_table},$vars->{graph_id},"file");



	

	
}


sub api_url_upload {

			
#my $str; while (my ($x,$y) = each %$vars) 	{ $str .= "$x = $y <br>\n"; }
#&send_email('stephen@downes.ca','stephen@downes.ca', 'url upload '.$vars->{value},$str); 


	# Upload the file

	my $file = &upload_url($vars->{value}); 
	&api_save_file($file);

	# Return new graph output for the form	
	if ($vars->{msg}) { print $vars->{msg}; }	
	print &form_graph_list($vars->{graph_table},$vars->{graph_id},"file");




	

	
}


sub api_save_file {

	my ($file) = @_;

	# Reject unless there's a full file name
	return unless ($file->{fullfilename});

	# Save the file
	my $file_record = &save_file($file);
	if ($file_record) { $vars->{msg} .= qq|&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:green;">ok!</a><br><br>|; }
	else { $vars->{msg} .= qq|<span style="color:red;">Error saving file. $!</span>|; die "Error saving file $!"; }
	

	# Set up Graph Data
	return unless ($vars->{graph_id} && $vars->{graph_table});
	my $urltwo = $Site->{st_url}.$vars->{graph_table}."/".$vars->{graph_id};
	my $graph_typeval = "";
	if ($file_record->{file_type} eq "Illustration") { $graph_typeval = $vars->{file_align} . "/" . $vars->{file_width}; } 
	else { $graph_typeval = $file_record->{file_mime}; }

	# Save Graph Data
	my $graphid = &db_insert($dbh,$query,"graph",{
		graph_tableone=>'file', graph_idone=>$file_record->{file_id}, graph_urlone=>$file_record->{file_url},
		graph_tabletwo=>$vars->{graph_table}, graph_idtwo=>$vars->{graph_id}, graph_urltwo=>$urltwo,
		graph_creator=>$Person->{person_id}, graph_crdate=>time, graph_type=>$file_record->{file_type}, graph_typeval=>$graph_typeval}); 

	# Make Icon (from smallest uploaded image thus far)
	
	if ($file_record->{file_type} eq "Illustration") { 
		
		my $icon_image = &item_images($vars->{graph_table},$vars->{graph_id},"smallest");
		
		my $filename = $icon_image->{file_title};
		my $filedir = $Site->{st_urlf}."files/images/";
		my $icondir = $Site->{st_urlf}."files/icons/";
		my $iconname = $vars->{graph_table}."_".$vars->{graph_id}.".jpg";
		
		my $tmb = &make_thumbnail($filedir,$filename,$icondir,$iconname);
	}



}

#
#   	Saves file
#	
#   	Expects input from either upload_file() or upload_url()
#       input hash $file needs:
# 		$file->{fullfilename}   - full directory and file name of upload file


sub save_file {
	
	my ($file) = @_;
	
	my ($ffdev,$ffino,$ffmode,$ffnlink,$ffuid,$ffgid,$ffrdev,$ffsize, $ffatime,$ffmtime,$ffctime,$ffblksize,$ffblocks)
			= stat($file->{fullfilename});
	my $ffwidth = "400";

			
	my $mime; 
	if (&new_module_load($query,"MIME::Types")) { 
		use MIME::Types;
		my MIME::Types $types = MIME::Types->new;
			my MIME::Type  $m = $types->mimeTypeOf($file->{fullfilename});	
			$mime = $m;		
	} else {
		$mime="Unknown; install MIME::Types module to decode upload file mime types";
		$vars->{msg} .= "Could not determine mime type of upload file; install MIME::types module<br>";
	}				
	
	my $file_type; if ($mime =~ /image/) { 
		$file_type = "Illustration"; 
	


	} else { $file_type = "Enclosure"; }		


		
	my $file_record = gRSShopper::Record->new(
		file_title => $file->{file_title},
		file_dirname => $file->{file_dir}.$file->{file_title},
		file_url => $Site->{st_url}.$file->{file_dir}.$file->{file_title},
		file_dir => $file->{file_dir},
		file_mime => $mime,
		file_size => $ffsize,
		file_post => $id_number,
		file_link => $vars->{$table."_link"},
		file_crdate => time,
		file_creator => $Person->{person_id},
		file_type => $file_type,
		file_width => $ffwidth,
		file_align => "top");
		
		
		
	# Create File Record
	$file_record->{file_id} = &db_insert($dbh,$query,"file",$file_record);
	
	if ($file_record->{file_id}) { return $file_record; }
	else { &error($dbh,"","","File save failed: $! <br>"); }
	
	
}

sub __check_field {
	my ($table,$field) = @_;
	
	my @columns = &db_columns($dbh,$table);
	return 1 if (&index_of($field,\@columns)>-1);
	return 0;
	
}