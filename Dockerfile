FROM ubuntu:latest
MAINTAINER c15341261  c15341261
RUN apt-get update
RUN apt-get install -y python3 python3-pip mysql-client libmysqlclient-dev
ADD /myapp /myapp
RUN pip3 install --upgrade pip
RUN pip3 install -r /myapp/requirements.txt
EXPOSE 5000
WORKDIR /myapp
CMD python3 app.py
