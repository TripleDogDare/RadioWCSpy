FROM ubuntu:14.10
MAINTAINER Calvin Behling <calvin.behling@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

#Make sure we have this repository
RUN echo "deb http://ch.archive.ubuntu.com/ubuntu/ utopic universe" >> /etc/apt/sources.list 
RUN echo "deb http://download.rethinkdb.com/apt utopic main" | tee /etc/apt/sources.list.d/rethinkdb.list

#working directories from project
RUN mkdir -p  /app/logs
ADD ./backend /app/backend
ADD ./www/    /app/www
ADD ./config  /config

#Add gpg key
RUN cat /config/rethinkdb.gpg | apt-key add -

#update the things
RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y openssh-server
RUN apt-get install -y supervisor
RUN apt-get install -y nginx
RUN apt-get install -y python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y rethinkdb


#update teh pythonic things
RUN . /app/backend/env/bin/activate && pip install --upgrade uwsgi WebOb Paste webapp2

#Remove things
RUN apt-get remove -y python-dev
RUN apt-get autoclean -y

# SEUP nginx
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /config/nginx.conf /etc/nginx/sites-enabled/

# SETUP ssh
RUN mkdir -p /root/.ssh
RUN cd /config && ./generate-auth-keys
RUN cp /config/authorized_keys /root/.ssh/authorized_keys


#Secure
# http://www.rethinkdb.com/docs/security/
# Secure rethinkdb web interface
iptables -A INPUT -i eth0 -p tcp --dport 8080 -j DROP
iptables -I INPUT -i etho0 -s 127.0.0.1 -p tcp --dport 8080 ACCEPT

# Secure rethinkdb driver port
iptables -A INPUT -i eth0 -p tcp --dport 28015 -j DROP
iptables -I INPUT -i eth0 -s 127.0.0.1 -p tcp --dport 28015 -j ACCEPT

EXPOSE 22
EXPOSE 80
EXPOSE 8080
CMD ["supervisord", "-n", "-c","/config/supervisord.conf"]
