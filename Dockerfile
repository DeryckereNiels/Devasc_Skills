FROM debian
RUN apt-get update
RUN apt-get -y install tzdata
RUN apt-get install -y apache2
EXPOSE 8081
CMD ["apachectl","-D","FOREGROUND"]
