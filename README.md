downes/grsshopper
==========

![docker_logo](https://raw.githubusercontent.com/downes/grsshopper/master/docker_139x115.png)![docker_fauria_logo](https://raw.githubusercontent.com/downes/grsshopper/master/docker_fauria_161x115.png)![grsshopper_logo](https://raw.githubusercontent.com/downes/grsshopper/master/grsshopper_header.jpg)

[![Docker Pulls](https://img.shields.io/docker/pulls/downes/grsshopper.svg?style=plastic)](https://hub.docker.com/r/downes/grsshopper-ple/)
[![Docker Build Status](https://img.shields.io/docker/build/downes/grsshopper.svg?style=plastic)](https://hub.docker.com/r/downes/grsshopper-ple/builds/)
[![](https://images.microbadger.com/badges/image/downes/grsshopper.svg)](https://microbadger.com/images/downes/grsshopper-ple "downes/grsshopper-ple")

Note: still being set up, these instructions don't work yet

gRSShopper is a tool that aggregates, organizes and distributes resources to support online learning. Read more here: https://grsshopper.downes.ca/

Docker image is here: https://hub.docker.com/r/downes/grsshopper-ple

To run:
```
docker pull downes/grsshopper

docker run --publish 80:80 --detach --name gr1 grsshopper
```


OR, run from the GitHub repository as follows:

Process:

```
git clone  https://github.com/Downes/grsshopper
```

        (or git pull origin master if reloading the changed repo)


```
cd grsshopper

docker build --tag grsshopper .

docker run --publish 80:80 -p 443:443 --detach --name gr2 grsshopper
```

Testing the server on localhost

http://localhost  (should show gRSShopper start page)

http://localhost/cgi-bin/server_test.cgi  (should show Perl test page)     

(Note: on localhost you will run into CORS problems running the PLE
engine at PLE.htm - the Docker image should be placed in the cloud and run under SSL) 

If Perl CGI isn't running properly, try:
```
docker exec -it gr1 /etc/init.d/apache2 reload
```

   (you can't docker exec -it bb3 apache2ctl restart because it crashes the entire container - see https://stackoverflow.com/questions/37523338/how-to-restart-apache2-without-terminating-docker-container )

   ( if you crash it, docker start bb3 )

Open a shell inside
```
docker exec -i -t gr1 bash
```

(A lot of sites say ```docker exec -it gr1 bash``` but I find it generates an error)

Credits
=======

I did the coding, etc., but here are some resources that really helped along the way

https://mariadb.com/kb/en/making-backups-with-mysqldump/ - Maria db making backups with mysqldump

https://hub.docker.com/r/fauria/lamp - Fauria LAMP Docker image

https://www.edureka.co/community/10534/copying-files-from-host-to-docker-container

https://www.reclaim.cloud

https://www.drdobbs.com/web-development/session-management-with-cgisession/184415974

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie - Set Cookie

https://metacpan.org/

https://metacpan.org/pod/CGI::Cookie - CGI::Cookie

https://docs.jelastic.com/

https://www.server-world.info/en/note?os=Ubuntu_18.04&p=httpd&f=2

https://registry.hub.docker.com/r/mattrayner/lamp/

https://alysivji.github.io/php-mysql-docker-containers.html

https://stackoverflow.com/questions/1443210/updating-a-local-repository-with-changes-from-a-github-repository - Stack Overflow

https://stackoverflow.com/questions/37523338/how-to-restart-apache2-without-terminating-docker-container

https://stackoverflow.com/questions/22720763/how-to-use-perl-to-change-a-mysql-password

https://stackoverflow.com/questions/25920029/setting-up-mysql-and-importing-dump-within-dockerfile

https://stackoverflow.com/questions/13154552/javascript-set-cookie-with-expire-time

https://docs.docker.com/get-started/

https://docs.docker.com/get-started/part2/

https://docs.docker.com/get-started/part3/

https://gist.github.com/gcrawshaw/1071698/fe4a2ac69d845a65a093a23c4899fd9d80d5c466 - Using bcrypt to secure passwords in a Perl application 

https://gist.github.com/gcrawshaw/1071698/53f042e5e3bf399bdf2e5e023ffa057d3a15467a - Using bcrypt to secure passwords in a Perl application 

https://rosettacode.org/wiki/SHA-256#Perl - SHA 256

https://www.digitalcitizen.life/how-view-remove-cookies-mozilla-firefox

https://metacpan.org/pod/release/SHERZODR/CGI-Session-3.95/Session.pm

https://metacpan.org/pod/release/SHERZODR/CGI-Session-3.95/Session/CookBook.pm

https://blog.ouseful.info/2020/06/09/first-forays-into-the-reclaim-cloud-beta-running-a-personal-jupyter-notebook-server/

https://www.effectiveperlprogramming.com/2020/06/turn-off-indirect-object-notation/ - Perl - Turn off indirect object notation

