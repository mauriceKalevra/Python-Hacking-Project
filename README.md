# Python-Hacking-Project
Uni project that should simulate an attack on an HTTP server via python.

**Prerequesites:**

- Docker, Python installed

**Run the victims http server:**  
~$ cd victim-http-server  
~$ docker build -t victim .  
~$ docker run -p 22:22 victim  

**Use the Webapplication:**

In browser open 173.17.0.2(your dockerip):1337

SSH into the 'Host-Server'(Docker container):

~$ ssh root@172.17.0.2(docker container ip)  
pw : root

**Execute attack:**  
cd Angriffe  
python attack.py
