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
