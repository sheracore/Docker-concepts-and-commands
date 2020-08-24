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
### Can download images from docker hub or make images with Dockfile
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
#### When you run a docker image on special port(e.i 6379 --> redis) you con connect it to your lacal's ip and use redis your local (e.i use it in your flask app)
```
sudo docker run --rm --name redis -p6379:6379 redis
```
#### Above methods had a problem, that is when you disconnect your redis, its data removed and when you run it again you haven't previous data of redis.
#### To resolve this type of problem you should read image on docker hub and find "persistent storage" section that creator told us how to use his image to maintain data, for example in redis we have this command:
```
docker run --rm --name  redis -p6379:6379 redis redis-server --appendonly yes
```
#### When you run docker  by above command after exitition of redis and go to bash you can see appendonly.aof is created in /data
#### But again we hava a problem that is data stored is in docker not in your local the solution is 'VOLUM' :
![docker volume](/pics/pic1)
