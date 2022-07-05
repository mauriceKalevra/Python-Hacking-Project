FROM ubuntu:latest

RUN apt update && apt install  openssh-server sudo -y

RUN apt install git -y

RUN apt install nodejs -y

RUN apt install npm -y

RUN npm install express

RUN npm install better-sqlite3

RUN npm install morgan

RUN echo "PermitRootLogin yes">etc/ssh/sshd_config

RUN  echo 'root:root' | chpasswd

RUN service ssh start

EXPOSE 22

RUN git clone https://github.com/mauriceKalevra/Node.js-web-application 

WORKDIR Node.js-weNode.js-web-applicationn

RUN npm install

RUN echo  "/usr/sbin/sshd -D & node app.js">entrypoint.sh

RUN chmod 700 entrypoint.sh

CMD ./entrypoint.sh
