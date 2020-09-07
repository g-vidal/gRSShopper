#!/usr/bin/perl

#    gRSShopper 0.7  Page  0.7  -- gRSShopper administration module
#    26 April 2017 - Stephen Downes

WORK IN PROGRESS 07 September 2020


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
#
#-------------------------------------------------------------------------------
#
#	    gRSShopper
#           Public Page Script
#
#-------------------------------------------------------------------------------



# Load CGI

	use CGI;
	use CGI::Carp qw(fatalsToBrowser);
	my $query = new CGI;
	my $vars = $query->Vars;
	my $page_dir = "../";


# Load gRSShopper

	use File::Basename;
	my $dirname = dirname(__FILE__);
	require $dirname . "/grsshopper.pl";




print "Content-type: text/html\n\n";
print "page.cgi loaded ok <p>";
