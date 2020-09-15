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


