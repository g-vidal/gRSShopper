downes/grsshopper
==========

![docker_logo](https://raw.githubusercontent.com/downes/grsshopper/master/docker_139x115.png)![docker_fauria_logo](https://raw.githubusercontent.com/downes/grsshopper/master/docker_fauria_161x115.png)![grsshopper_logo](https://raw.githubusercontent.com/downes/grsshopper/master/grsshopper.jpg)

[![Docker Pulls](https://img.shields.io/docker/pulls/downes/grsshopper.svg?style=plastic)](https://hub.docker.com/r/downes/grsshopper/)
[![Docker Build Status](https://img.shields.io/docker/build/downes/grsshopper.svg?style=plastic)](https://hub.docker.com/r/downes/grsshopper/builds/)
[![](https://images.microbadger.com/badges/image/downes/grsshopper.svg)](https://microbadger.com/images/downes/grsshopper "downes/grsshopper")

Note: still being set up, these instructions don't work yet

gRSShopper is a tool that aggregates, organizes and distributes resources to support online learning

Docker image is here: https://hub.docker.com/r/downes/grsshopper

To run:
```
docker pull downes/grsshopper

docker run --publish 80:80 --detach --name bb3 grsshopper
```


OR, run from thw GitHub repository as follows:

Process:

```
git clone  https://github.com/Downes/grsshopper
```

        (or git pull origin master if reloading the changed repo)


```
cd docker-lamp

docker build --tag downeslamp .

docker run --publish 80:80 --detach --name bb3 downeslamp
```

Testing the server

http://localhost  (should show Apache index page)

http://localhost/index.php  (should show PHP index page)

http://localhost/cgi-bin/server_test.cgi  (should show Perl test page)     

 

If Perl CGI isn't running properly, try:
```
docker exec -it bb3 /etc/init.d/apache2 reload
```

   (you can't docker exec -it bb3 apache2ctl restart because it crashes the entire container - see https://stackoverflow.com/questions/37523338/how-to-restart-apache2-without-terminating-docker-container )

   ( if you crash it, docker start bb3 )

Open a shell inside
```
docker exec -i -t bb3 bash
```
