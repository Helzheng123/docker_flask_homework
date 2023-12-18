# docker_flask_homework
This assignment aims to provide hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple applications.

## Part One: Dockerizing a Single Flask Application
### Setting Up and Dockerizing a Flask App:
I used my previous Flask App for the [```base.html```](https://github.com/Helzheng123/docker_flask_homework/blob/main/Part1/templates/base.html) file and added in new things for the [```contactus.html```](https://github.com/Helzheng123/docker_flask_homework/blob/main/Part1/templates/contactus.html) file. 

  - I first created a Dockerfile that contains the following:
```
FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
 - Then I created an [```app.py```](https://github.com/Helzheng123/docker_flask_homework/blob/main/Part1/app.py) file
 - Lastly, I created a [```requirements.txt```](https://github.com/Helzheng123/docker_flask_homework/blob/main/Part1/requirements.txt) file with flask in it

To **Dockerize** my FLask Application, I did the following steps:
1. First build the docker image with ```docker build -t <name> .```
2. Then do ```docker images``` to show the docker images. Make sure your <name> is there.
3. Then run the command with ```docker run -d -p 5001:5000 <name>```
4. Type in ```docker ps``` to check your docker container information.
5. When you are done with your Docker image, you can stop the image from running with ```docker stop <container ID>```
6. If needed, you can delete images with ```docker system prune -a -f```

Importance of each step in the Dockerfile:
 - ```FROM``` specifies which base operating system from the hub.docker.com with python installed in it
 - ```WORKDIR``` folder that houses this code
 - ```COPY``` copies the content of the current directory of the Dockerfile into the app directory within the container
 - ```RUN``` requirements.txt is to just install the python dependencies in requirements.txt (flask)
 - ```EXPOSE 5000``` is to show that the docker container will be designed to listen on port 5000
 - ```CMD``` is to run the app.py through python when the container starts to run

## Part Two: Multi-Container Setup with Docker Compose:
### Prepare Two Flask Applications:
 - I created two folders under the Part2 Folder for the two flask applications: flask1 and flask2
 - In each folder contains:
     - Dockerfile that contains:
       ```
       FROM python:3.10-slim-buster
       WORKDIR /app
       COPY . /app
       RUN pip install -r requirements.txt
       EXPOSE 5000
       CMD ["python", "app.py"]
       ```
     - app.py file
     - requirements.txt file with flask in it
     - templates folder for HTML
  - In the Part2 Folder, I have a ```docker-compose.yml``` file that contains:
```
version: '3'
services:
  flask_app_1:
    build: ./flask1
    ports:
      - "7000:5000"
    volumes:
      - ./flask1:/app
  flask_app_2:
    build: ./flask2
    ports:
      - "5020:5000"
    volumes:
      - ./flask2:/app
```

Explanation of each section of the [```docker-compose.yml```](https://github.com/Helzheng123/docker_flask_homework/blob/main/Part2/docker-compose.yml) file:
 - ```version``` is the version of the Docker Compose file that is being used (we are using version 3)
 - ```services``` is the section with the different services/containers for this application
 - ```flask_app_1``` is the first flask app
 - ```build: ./flask1``` directs the image built to flask1's dockerfile
 - ```ports``` maps port 5000 from the conatiner to port 7000 for the host.
 - ```volumes``` any changes that occur in the local files will be brought to the container here
(same concept for flask_app_2 as well)

To run this, I did the following steps:
1. Start off by building the images: ```docker-compose up --build```
2. If i need to reconnect to it, I did ```docker-compose up```
3. If you want to see a list of your containers, use ```docker-compose ps```
4. If needed, you can stop it with ```docker-compose down```

## How is Docker Compose different from Docker?
Docker Compose helps orchestrate multiple containers without running each container separately while Docker will run individually. If you have multiple containers and you only use Docker alone, then you will need to start and command each container separately while Docker Compose contains a ```docker-compose.yml``` file that helps you run your entire application at the same time, making it easier for you to run and stop each application. 

## Challenges:
No challenges encountered.
