#!/usr/bin/perl
 

#    gRSShopper 0.7  Server Test  0.2  -- gRSShopper server test module
#    26 April 2017 - Stephen Downes


#    Copyright (C) <2008>  <Stephen Downes, National Research Council Canada>

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

##########################################################################
# Servertest.pl
##########################################################################
	use CGI;
	use CGI::Carp qw(fatalsToBrowser);
	use CGI::Session;
	use CGI::Session::Auth;


my $query = CGI->new();
CGI::Session->name("SID");
my $session = CGI::Session->new($query);
$session->expire('+1h');
if ($session) { 
   $CGISESSID = $session->id();

   # Send proper HTTP header with cookies:
   print $session->header();
   # Storing data in the session:
#$session->param('f_name', 'Sherzod');
# or
#$session->param(-name=>'l_name', -value=>'Ruzmetov');
 
# Flush the data from memory to the storage driver at least before your
# program finishes since auto-flushing can be unreliable.
$session->flush();
   
   print "Content-type: text/html\n\n";   
      print "Session creation successful: ".$CGISESSID.$newline;
   print "Session save info:$newline";

# Retrieving data:
my $f_name = $session->param('f_name');
# or
my $l_name = $session->param(-name=>'l_name');
print "$f_name $l_name <p>";

   my $cookie = $query->cookie( -name   => $session->name,value  => $session->id );
   print $query->header( -cookie=>$cookie );

} else {
   print "Content-type: text/html\n\n";
   print "Session error.<p>";
}


	
	
# ---------------------------------
# Let's see what our environment is
if (!$ENV{'SERVER_SOFTWARE'}) {
  $newline = "\n";$h1 = ""; $h1f="";
}
else {
  print "Content-type: text/html\n\n";
  $newline = "<br>"; $h1 = "<h1>"; $h1f = "</h1>";
 }
print $h1."gRSShopper web server environment test.".$h1f.$newline.$newline;

# --------------------------------------
# Check for the required version of PERL
eval "require 5.004";
print "Checking PERL version...";
if ($@) {
  print "$newline"."This program requires at least PERL version 5.004 or greater.$newline";
  exit;
} else {
print " <span style='color:green;'> OK</span>$newline";
}

# use local::lib; # sets up a local lib at ~/perl5

# -----------------------------------------------------
# Check that all of the required modules can be located



$|++;
my $missing = 0;
my @lissing_list;
my @modules = qw(CGI CGI::Carp CGI::Session File::Basename File::stat File::Find DBI LWP LWP::UserAgent
LWP::Simple MIME::Types MIME::Lite::TT::HTML HTML::Entities Scalar::Util Text::ParseWords Lingua::EN::Inflect
Net::Twitter::Lite::WithAPIv1_1 Image::Resize DateTime DateTime::TimeZone Time::Local Digest::SHA1
XML::OPML REST::Client JSON JSON::Parse JSON::XS URI::Escape Email::Stuffer Email::Sender::Transport::SMTP
Mastodon::Client);


foreach my $module (@modules) {
  print "Checking for $module. ";
  eval "use $module";
  if ($@) {
    print "<span style='color:red;'>The $module module could not be located.</span>$newline";
    $missing=1;
    push @missing_list,$module;
  } else {
    print "<span style='color:green;'> OK</span>$newline";
  }
}



# -------------
# Provide CPAN help

if ($missing eq "1") {



	print qq|$newline You are missing the following required Perl modules.<ul>|;
  foreach my $module (@missing_list) { print qq|<li>$module</li>|; }

  print qq|</ul>		$newline$newline
		<b>Getting Perl Modules</b>$newlineFor more information, please see:$newline
		<a href="http://www.cpan.org/modules/INSTALL.html">http://www.cpan.org/modules/INSTALL.html</a> $newline
		<a href="http://www.rcbowen.com/imho/perl/modules.html">http://www.rcbowen.com/imho/perl/modules.html</a> $newline|;

}

# -------------
# Test database access (from default config in Dockerfile)

print "<p>Testing database access (from default config in Dockerfile)</p>";
use DBI;

    	# Make variables easy to read :)
    	my $dbname = "grsshopper";
    	my $dbhost = "localhost";
    	my $usr = "grsshopper_user";
    	my $pwd = "user_password";

	# Connect to the Database
  	my $dbh = DBI->connect("DBI:mysql:database=$dbname;host=$dbhost;port=3306",$usr,$pwd);

	# Catch connection error
	if( ! $dbh ) {

              print "Content-type: text/html\n\n";
	      print "Database connection error for db '$dbname'. Please contact the site administrator.<br>";   

		# Print error report and exit
		print "Error String Reported: $DBI::errstr <br>";
		exit;

	# I'll put more error-checking here
	} else {
	
	        print "<p>Database successfully connected.</p>";
		eval {
		#$dbh->do( whatever );
		#$dbh->{dbh}->do( something else );
		};

		if( $@ ) {
			print "Ugg, problem: $@\n";
		}
	}

# -------------
# Test sessions
print "<p>Testing user authentication</p>";


exit;
