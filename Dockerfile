FROM ubuntu:latest

USER root
RUN apt-get -y update
RUN apt-get -y install sudo
RUN sudo apt-get -y install nodejs
RUN sudo apt-get -y install npm
RUN nodejs -v
