# Docker-concepts-and-commands
## concepts
## Docker VS VM's
### VMWare, VitualaBox 
#### Has VM's that this vm's is complete vm's that has cernel and ultimate virtual infrastructure(Resources like ram,cpu,.. and cernel files)
#### Using hypervisor to interpretaion between vm's and HW/OS 
#### Isolate
#### Load is high

### Docker
#### Has containers that using needed os infrastructure and have not complete infrastracture(Resources like ram,cpu,.. and cernel files) itself
#### Has containers
#### Using docker engine
#### Scalable
#### Less complex
#### Easy to deploy

## Docker
### In docker images can be downloaded from docker hub or make images with Dockfile
## Docker command lines and utilities
```
sudo docker pull <docker name>
sudo docker images
```
#### show running containers
```
sudo docker ps 
```
#### show all containers that were runned and exited
```
sudo docker ps -a
sudo docker run <docker name> if doesn't exist it pulls it
sudo docker run busybox [collection of common linux commands(ls, cat, sleep,...)] ------  > like sudo docker run busybox ls
sudo docker rm <CONTAINER ID> ---> delete contaiers that exited in <sudo docker ps -a>
```
#### Killed all containers (Than ones not running but were runned before)
```
sudo docker container prune
sudo docker rmi <image name> ---> remove image
sudo docker container prune ---> delete all contaiers that exited in <sudo docker ps -a>
```
#### Automatically remove the container when it exits
```
sudo docker run --rm 
-i = --interactive:     Keep STDIN open even if not attached
-t = --tty:                  Allocate a pseudo-TTY
sudo docker run --rm -it busybox
```
#### When the above command is running you can use this command to run sum commad with busybox commands
```
sudo docker exec 9f14f56a57d1 touch /hi  ------> 
sudo docker exec -it f6ee306b43b7 bash (Go to the image running shell or connect to f6ee306b43b7(This is running redis container) by bash (This is like ssh))
sudo docker stop f6ee306b43b7 (stop running images)
```
#### If you want to set name to docker run and use it by ecex
```
sudo docker run --rm --name redis redis
```
#### Connect to above run image by its name
```
sudo docker exec -it redis bash
sudo docker exec -it redis bash redis-cli (run command line directly)
```

#### When you run a docker image on special port(e.i 6379 --> redis) you con connect it to your lacal's ip
```
sudo docker run --rm --name redis -p6379:6379 redis
```
#### When you run a docker image on special port(e.i 6379 --> redis) you con connect it to your lacal's ip and use redis your local (e.i use it in your flask app)
```
sudo docker run --rm --name redis -p6379:6379 redis
```
### Persistence data
#### Above methods had a problem, that is when you disconnect your redis, its data removed and when you run it again you haven't previous data of redis.
#### To resolve this type of problem you should read image on docker hub and find "persistent storage" section that creator told us how to use his image to maintain data, for example in redis we have this command:
```
docker run --rm --name  redis -p6379:6379 redis redis-server --appendonly yes
```
#### When you run docker  by above command after exitition of redis and go to bash you can see appendonly.aof is created in /data
#### But again we hava a problem that is data stored is in docker not in your local the solution is 'VOLUM' :
![docker volume](/pics/pic1)
#### As you can see in this picture you can store piece of your stored data of docker in your local by -v or --mount([more information](https://docs.docker.com/storage/volumes/)) this command connect your local /tmp/data/redis(your create it) to /data(from your redis conrainer):
```
docker run --rm --name  redis -p6379:6379 -v /tmp/data/redis:/data redis redis-server --appendonly yes
```
#### Now to run our app.py by docker we shoul use ubunto or Alpine (light linux), python, flask, nginx, wsgi(for connect nginx to our flask) dockers but a docker to this, its name is tiagolo/uwsgi-nginx-flask [tiangolo](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) :)
#### We create a Dockfile contain below content and build it with ``` sudo docker build .```:
```
# use this tiangolo image
FROM tiangolo/uwsgi-nginx-flask 
# Add flask requirements to run flask                                          
COPY ./requirements.txt /tmp/      
# By RUN you can run any linux commands
RUN pip install -r /tmp/requirements.txt  
                                                                                    
# Copy our app.py to app/main.py(from tiangolo docker image that tiangolo made it)
COPY app.py /app/main.py
```
#### To add name to your image you can use ``` sudo docker build -t myapp:v1 . ```
#### As you can see in below picture we have two containers myapp and redis and two contaiers can be seen by OS but thay can't see each gether and now we want to connect them by create a network:
![redis and myapp container](/pics/dokcer)
![redis and myapp container](/pics/docker2.png)
#### Using this command you can create a network
```
sudo docker network create flask
# You can see your network by
sudo docker network ls
```
#### Now you should run your dockers on this network like this
```
sudo docker run --rm --name  redis -p6379:6379 --network flask -v /tmp/data/redis:/data redis redis-server --appendonly yes
sudo docker run --rm -p80:80 --name myapp --network flask myapp:v3
```
#### But it doesn't work because two container connect to OS that it's not necessary anymore and dockers can see each other by container names.
```
# removing p6379:6379
docker run --rm --name  redis --network flask -v /tmp/data/redis:/data redis redis-server --appendonly yes
# Notic that we dont change p80:80 in our image
```
#### we should change our app to:
```
localhost ---> redis
r = redis.Redis(host='redis', port=6379, db=0)
```
### And Done and you can run ``` curl 0.0.0.0:80 ``` and see your result also you can ping redis in your myapp bash like this:
```
sudo docker exec -it myapp bash
> ping redis
```

### Docker-compose
#### Docker-compose is for managing containers.
#### By docker-compose we can use some different containers in one service
#### It's format is yml look at the sample --> docker-comose.yml

```
version: "3"

services: 
  app: 
    build: 
      context: .
    ports: 
      - "8000:8000"
    volumes: 
      - ./app:/app
    command: >
      sh -c "python manage.py runserver 0.0.0.0:8000"

```
