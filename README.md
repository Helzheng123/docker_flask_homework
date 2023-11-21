# docker_flask_homework
This assignment aims to provide hands-on experience in Dockerizing Flask applications, first individually and then using Docker Compose for managing multiple applications.

## Part One: Dockerizing a Single Flask Application
### 1. Setting Up and Dockerizing a Flask App:
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
5. When you are done with your Docker image, you can stop the image from running with ```docker stop <container ID>
6. If needed, you can delete images with ```docker system prune -a -f```

Importance of each step in the Dockerfile:
```FROM``` specifies which base operating system from the hub.docker.com with python installed in it
```WORKDIR``` folder that houses this code
```COPY``` copies the content of the current directory of the Dockerfile into the app directory within the container
```RUN``` requirements.txt is to just install the python dependencies in requirements.txt (flask)
```EXPOSE 5000``` is to show that the docker container will be designed to listen on port 5000
```CMD``` is to run the app.py through python when the container starts to run

