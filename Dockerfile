FROM debian
RUN apt-get update
RUN apt-get -y install tzdata
RUN apt-get install -y apache2
RUN sed -i '0,/Listen [0-9]*/s//Listen 8081/' httpd.conf
EXPOSE 8081
CMD ["apachectl","-D","FOREGROUND"]
