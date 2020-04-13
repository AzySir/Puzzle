# Operating System Image from Docker
FROM centos:latest 

#Copy source code
COPY ./src /app/src

#Working directory where source code is
WORKDIR /app/src

#Install Python3 & Flask
RUN /bin/bash -c 'yum -y install python3'
RUN /bin/bash -c 'pip3 install flask'

#Run API
CMD python3 main.py