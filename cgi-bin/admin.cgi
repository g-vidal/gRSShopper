#!/usr/bin/perl

#    gRSShopper 0.7  Admin  0.62  -- gRSShopper administration module
#    05 June 2017 - Stephen Downes

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
#           Admin Functions
#
#-------------------------------------------------------------------------------
# print "Content-type: text/html\n\n";

# Diagnostics

	our $diag = 0;
	if ($diag>0) { print "Content-type: text/html\n\n"; }
	
	

# Forbid bots

	die "HTTP/1.1 403 Forbidden\n\n403 Forbidden\n" if ($ENV{'HTTP_USER_AGENT'} =~ /bot|slurp|spider/);

# Load gRSShopper

	use File::Basename;
      #use local::lib; # sets up a local lib at ~/perl5
	my $dirname = dirname(__FILE__);
	require $dirname . "/grsshopper.pl";


# Load modules

	our ($query,$vars) = &load_modules("page");
	
	
# Load Site
	
	our ($Site,$dbh) = &get_site("page");		
	

	my ($session,$username) = &check_user();
	
	
	our $Person = {}; bless $Person;
	&get_person($Person,$username);
	my $person_id = $Person->{person_id};
	
	#print "Person title is: ".$Person->{person_title}." and status is ".$Person->{person_status}."<p>";
	print &show_login($session);
	
	#if ($username) { print $username.qq| [<a href="//|.$ENV{'SERVER_NAME'}.$ENV{'SCRIPT_NAME'}.qq|?action=logout">Logout</a>]<p>|; }
	#else { $login_window; }


	my $vars = $query->Vars;
	my $page_dir = "../";
	
	# Admin Only
	die "Admin Only" unless (&admin_only());
	
print "Admin";

	# Initialize system variables

		my $options = {}; bless $options;
		our $cache = {}; bless $cache;


	# Option to call initialize functions

		if ($vars->{action} eq "initialize") {  $Site->__initialize("command"); }
	#    print "Content-type: text/html\n\n";
	#    while (my($fx,$fy) = each %$vars) { print "$fx = $fy<br>";}   #{%}

	# Restrict to Admin

# Analyze Request --------------------------------------------------------------------

	# Determine Action ( assumes admin.cgi?action=$action&id=$id )

		my $action = $vars->{action};
		my $id = $vars->{id};



	# Determine Request Table, ID number ( assumes admin.cgi?$table=$id and not performing action other than list, edit or delete)

		my @tables = &db_tables($dbh);
		foreach $t (@tables) {

			if ((!$action || $action =~ /^edit$/i || $action =~ /^list$/i || $action =~ /^Delete$/i || $action =~ /^extract_nouns$/i ) && $vars->{$t}) {
				$table = $t;
				$id = $vars->{$t};
				$vars->{id} = $id;
				last;
			}
		}


	# Direct Request Table, ID number, and list requests ( required for most actions, assumes admin.cgi?db=$table&id=$id or admin.cgi?table=$table&id=$id , no $id for action=list )

	if ($vars->{db} || $vars->{table}) {
		$table = $vars->{table} || $vars->{db};
		if ($vars->{id}) {
			$id = $vars->{id};
		} else {
			unless ($action) {
				$action = "list";
			}
		}
	}

	# Determine Output Format  ( assumes admin.cgi?format=$format )

	if ($vars->{format}) { 	$format = $vars->{format};  }
	if ($action eq "list") { $format = "list"; }
	$format ||= "html";		# Default to HTML

# Actions ------------------------------------------------------------------------------

	# Perform Action, or





	if ($action) {

		for ($action) {
			print "Action: $action <p>";												# Main admin menu nav

			/start/ && do { &admin_start($dbh,$query); last;			};	# 	- Start Menu
			/general/ && do { &admin_general($dbh,$query); last;			};	# 	- General Menu
			/harvester/ && do { &admin_harvester($dbh,$query); last;		};	# 	- Harvester Menu
			/users/ && do { &admin_users($dbh,$query); last;			};	# 	- Users Menu
			/newsletters/ && do { &admin_newsletters($dbh,$query); last;	};		#	- Newsletters Menu
			/database/ && do { &admin_database($dbh,$query); last;		};		#	- Database Menu
			/meetings/ && do { &admin_meetings($dbh,$query); last;		};		#	- Meetings Menu
			/logs/ && do { &admin_logs($dbh,$query); last;		};			#	- Logs Menu
			/accounts/ && do { &admin_accounts($dbh,$query); last;		};		#	- Accounts Menu
			/permissions/ && do { &admin_permissions($dbh,$query); last;		};	#	- Permissions Menu




															# Editing Functions

			/list/ && do { &admin_list_records($dbh,$query,$table); last;		};		#	- List records
			/edit/i && do { &edit_record($dbh,$query,$table,$id); last; 	};		#	- Edit Record - Show the Editing form
			/update/ && do { &update_record($dbh,$query,$table,$id);
				&edit_record($dbh,$query,$table, $id_number);last; };		# 	- Edit Record - Update with input data
			/Delete/i && do	{ &record_delete($dbh,$query,$table,$id);last; };		#	- Delete Record
			/Spam/i && do { &record_delete($dbh,$query,$table,$id);  last; };		#	- Delete Record and log creator IP to Spam
			/multi/i && do { &admin_multi($dbh,$query); last;		};		#	- Multi-Delete Record (FIXME needs work)



															# Feed Functions

			/approve/i && do { &record_approve($dbh,$query,$table,$id); last; };		#	- Approve Feed
			/retire|reject/i && do { &record_retire($dbh,$query,$table,$id); last; };	#	- Reject / Retire Feed


															# Site Configuration

			/config/ && do { &admin_update_config($dbh,$query); last;	};		#	- Update config data
			/export_table/ && do { &admin_db_export($dbh,$query); last;	};		#	- export a table
			/db_pack/ && do {&admin_db_pack($dbh,$query); last;		};		#	- Make a new pack
			/db_add_column/ && do { my $msg = &db_add_column($vars->{stable},$vars->{col});
				&showcolumns($dbh,$query,$msg); last; };				#	- Add new column to a table
			/removecolumnwarn/ && do { &removecolumnwarn($dbh,$query); last; };		#	- Remove column - warn user
			/removecolumndo/ && do { &removecolumndo($dbh,$query); last; };			#	- Remove column - remove it



															# Newsletter and Page Functions

			/publish/ && do {
					if ($table eq "badge"){ &publish_badge($dbh,$query,$id,"verbose"); last;}
					else { &publish_page($dbh,$query,$vars->{page},"verbose"); last; } };
	    /verify_email/ && do { &admin_verify_emails(); last; };
			/rollup/ && do { &news_rollup($dbh,$query); last;			};	#	- Show posts allocated to future newsletters
			/autosub/ && do { &autosubscribe_all($dbh,$query); last;   };			#	- Auto-subscribe all users to newsletter
			/autounsub/ && do { &autounsubscribe_all($dbh,$query); last; };			#	- Auto-unsubscribe all users from newsletter
			/send_nl/ && do { &send_nl($dbh,$query); last;	};				#	- Send newsletter to email subscribers


															# Cron Tasks (FIXME make a separate file? )

			/rotate/ && do { &rotate_hit_counters($dbh,$query,"post"); last;};		#	- Reset daily hits counter to '0'

			/remove_key/ && do { &remove_key($dbh,$query,$table,$id);
				&edit_record($dbh,$query,$table,$id); last;};

													#		# Database Functions

			/backup_db/ && do { &admin_db_backup($vars->{backup_table},"verbose"); last; };	#	- Back up database
			/showcolumns/ && do { &showcolumns($dbh,$query); last; };			#	- Show the columns in a table
			/add_table/ && do { admin_db_add_table($vars->{add_table}); last; };		#	- Add table
			/drop_table/ && do { admin_db_drop_table($vars->{drop_table}); last; };		#	- Drop table

			/fixmesubs/ && do { &fixmesubs($dbh,$query,$table); last;		};

	                       # API Functions

	    /access_api/ && do { &access_api($dbh,$query); last; };

			/export_users/ && do { &export_user_list($dbh,$query); last;			};
			/import/ && do { &import($dbh,$query,$table); last;		};
			/remove_all/ && do { &delete_all_users($dbh,$query); last; };


			/youtubepost/ && do { &parse_youtube($dbh,$query); last; };
			/autopost/ && do { &autopost($dbh,$query); last; };
			/postedit/ && do { &postedit($dbh,$query); last; };

			/eduser/ && do { &admin_users_edit($dbh,$query); last;			};
			/subs/ && do { &edit_subs($dbh,$query); last;			};

												 # Analyze
			/analyze_text/ && do {
				&analyze_text($dbh,$query,$table,$id); last; };
			/extract_nouns/ && do {
				&extract_nouns($dbh,$query,$table,$id); last; };
			/show_graph/ && do {
				&show_graph($dbh,$query,$table,$id); last; };

			/make_icon/ && do { &auto_make_icon($table,$id);
					&edit_record($dbh,$query,$table,$id); last;};
			/logview/ && do { &log_view($dbh,$query); last; };
			/logreset/ && do { &log_reset($dbh,$query); last; };
			/reindex_topics/ && do { &reindex_topics($dbh,$query,$id); last; };
			/refield/ && do { &refield($dbh,$query); last; };
			/recache/ && do { &recache($dbh,$query); last; };
			/reindex/ && do { &reindex_matches($dbh,$query,$table,$id); };

			/count/ && do { &count_feed($dbh,$query); last; };

			/cache_clear/ && do { print "Content-type: text/html\n\n"; &cache_clear($dbh,$query); last; };
			#/stats/ && do { &calculate_stats($dbh,$query); last;  };
			/graph/ && do { &make_graph($dbh,$query); last;  };
			/sendmsg/ && do { &admin_users_send_message($dbh,$query); last; };
			/moderate_meeting/ && do { &moderate_meeting($dbh,$query); last;			};	# 	- General
			/test_rest/ && do { api_send_rest($dbh,$query); last; };
			/cstats/ && do { &calculate_cstats($dbh,$query); last; };

		}

	# Output Record, or

	} elsif ($table) {					# Default Data Output

		&output_record($dbh,$query,$table,$id,$format);

	} 
	
	# Previous processes should all terminate internally; this is the default
	# Show Admin Menu

	&admin_general($dbh,$query);

	exit; # And we're done
	
	

	#---------------------------------------------------------------------------------------------
	#
	#                 Functions
	#
	#---------------------------------------------------------------------------------------------




	# -----------------------------------   Admin: General   -----------------------------------------------
	#
	#   Initialization and editing of general site configuration data
	#   Expects and requires access to a 'config' table in the database
	#   The config table in turn is used by init_site() in grsshopper.pl
	#
	# ------------------------------------------------------------------------------------------------------

	sub admin_general {

		my ($dbh,$query) = @_;
print "Admin General";
	        my $content = &printlang("General Information");

		$content .= &admin_update_grsshopper($dbh,$query);

		$content .= &admin_configtable($dbh,$query,"Site Information",
			("Site Name:st_name","Site Tag:st_tag","Email:st_email","Description:st_desc","Publisher:st_pub","Creator:st_crea","License:st_license","Time Zone:st_timezone","Reset Key:reset_key","Cron Key:cronkey"));


		$content .= &admin_api($dbh,$query);

		$content .= &admin_configtable($dbh,$query,"Base URLs and Directories",
			("Base URL:st_url","Base Directory:st_urlf","CGI URL:st_cgi","CGI Directory:st_cgif","Login URL:st_login"));

		$content .= &admin_configtable($dbh,$query,"Media Directories",
			("Images:st_img","Photos:st_photo","Files:st_file","Icons:st_icon"));

		$content .= &admin_configtable($dbh,$query,"Upload Directories",
			("Uploads:st_upload","Images:up_image","Documents:up_docs","Slides:up_slides","Audio:up_audio","Videos:up_video"));

		&admin_frame($dbh,$query,"Admin General",$content);					# Print Output
		exit;



	}
	
	


# --------------------------------------   Update gRSShopper -----------------------------------------------
#
#    Option to calls a shell script that downloads most recent gRSShopper code from
#    GitHub and installs it in cgi-bin
#
# ------------------------------------------------------------------------------------------------------


sub admin_update_grsshopper{

	my ($dbh,$query) = @_;

	return unless (&is_viewable("admin","update")); 		# Permissions

  my $update_string = "";

  my $local_version = &read_text_file('version.txt');
	my $remote_version = get("https://raw.githubusercontent.com/Downes/gRSShopper/master/version");

  if ($local_version eq  $remote_version) {
    $update_string = "gRSShopper is up to date at version $local_version."
	} else {
		$update_string = qq|<p>Local version is $update_string and master version is $remote_version</p>
			<button onClick="update_grsshopper('$Site->{st_cgi}'+'api.cgi?cmd=gRSShopper_update')">Update gRSShopper</button>|;
	}

	return qq|<div class="menubox">

		<h3>Update gRSShopper</h3>
		<script src="$Site->{st_url}/assets/js/jquery.js"></script>
		<script>
		function update_grsshopper(url) {


			\$('#gRSShopper_update').load(url, function(response, status, xhr) {
	        if (status == "error") {
	            var msg = "Sorry but there was an error: ";
	            alert(msg + xhr.status + " " + xhr.statusText);
	        }
	     });

		}

		</script>
		<p><ul>
		<div id="gRSShopper_update">$update_string</div>
		</ul></p>

	</div>|;

}



	# -----------------------------------   Admin: Config Table   -----------------------------------------------

	sub admin_configtable {

		my ($dbh,$query,$title,@vals) = @_;

		my $content = qq|

			<h3>$title</h3>
			<div class="adminpanel">
			<ul><form method="post" action="$Site->{st_cgi}admin.cgi">
			<input type="hidden" name="action" value="config">
			<input type="hidden" name="title" value="$title">
			<table cellspacing="0" cellpadding="2" border="0">
		|;
		foreach my $v (@vals) {
			my ($t,$v,$f,$o,$h) = split ":",$v;    # Title, variable name, format   #"
			if ($f eq "yesno") {
				my $yesselected=""; my $noselected="";
				if ($Site->{$v} eq "yes") { $yesselected = qq| selected="selected"|; }
				else { $noselected = qq| selected="selected"|; }
				$content .= qq|<tr><td align="right">$t : </td><td>
				<select name="$v">
				<option value="yes" $yesselected >Yes</option>
				<option value="no" $noselected >No</option>
				</select>
				</td></tr>\n|;
			} elsif($f eq "dir") {
				my $vfval; $vfval = $Site->{$v} || $o;
				$content .= qq|<tr><td align="right">$t : </td><td>
				$Site->{st_urlf}<input type="text" size="60" name="$v" value="$vfval"></td></tr>\n|;
			} elsif($f eq "url") {
				my $vuval; $vuval = $Site->{$v} || $o;
				$content .= qq|<tr><td align="right">$t : </td><td>
				$Site->{st_url}<input type="text" size="60" name="$v" value="$vuval"></td></tr>\n|;
			} else {
				my $vval; $vval = $Site->{$v} || $f;
				$content .= qq|<tr><td align="right">$t : </td><td>
				<input type="text" size="60" name="$v" value="$vval"></td></tr>\n|;
			}
		}


		$content .= qq|<tr><td colspan="2"><input type="submit" class="button" value="Submit $title"></tr></td>|;
		$content .= "</table>\n</form></ul>
			</div>\n";
	}



	sub admin_api {

		my ($dbh,$query) = @_;



		my $content = qq|<h2>Access API</h2><p>
		 <ul><table cellspacing="0" cellpadding="2" border="0"><tr><td>
	   <form method="post" action="$Site->{st_cgi}admin.cgi">
		 <input type="hidden" name="action" value="access_api">
		 Method: <select name="method"><option value="get"> GET </option> <option value="post" selected> POST </option></select><br>
		 URL: <input type="text" name="url" size="40" value="http://www.mooc.ca/cgi-bin/api.cgi">
		 JSON: <textarea rows=10 cols="40" name="postdata">
	{
	 "action": "search",
	 "table": "course",
	 "query": "agriculture",
	 "language": "en",
	 "sort": "course_title"
	}
		 </textarea>
		 <input type="submit">
		 </form>
	   </table></ul>

		|;

	   return $content;

		exit;



	}







