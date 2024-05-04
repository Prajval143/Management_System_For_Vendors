FROM python:3.11
# setup environment variable
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /Django-Vendor-Management-System

# where your code lives
WORKDIR  /Django-Vendor-Management-System

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . /Django-Vendor-Management-System
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs

