FROM python:3

WORKDIR /Users/carolina/Desktop/udemy

#Docker basic commands:

#Build and run docker image: docker build -t udemy . //Every time I change my dockerfile I should do it too.

#Create a container and start the container. Docker run is a combination of docker create and docker start: docker run -v `pwd`:/project -it -p 3001:3001 -p 3000:3000 bookshelf bash
#docker run -it udemy bash

#Come out of the container: exit
#Disconnect from container: ctrl + d
#List my containers: docker ps -a
#start container: docker start <name of the container>
#Get into my container: docker attach <name of the container>
