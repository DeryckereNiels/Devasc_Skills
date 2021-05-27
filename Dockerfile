FROM debian
RUN apt-get update
RUN apt-get -y install tzdata
RUN apt-get install -y apache2
RUN sudo sed -i '0,/Listen [0-9]*/s//Listen 8081/' /etc/apache2/ports.conf
EXPOSE 8081
CMD ["apachectl","-D","FOREGROUND"]
