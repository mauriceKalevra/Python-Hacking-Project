# Python-Hacking-Project
Application that simulates an attack on a Http server via python

Prerequesites:

- Docker installed

Run the victims http server:  

~$ docker build -t victim .
~$ docker run -p 22:22 victim

Use the Webapplication:

In browser open 173.17.0.1(your dockerip):1337
