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

RUN git clone https://github.com/mauriceKalevra/Web2-Projekt.git

COPY entrypoint.sh /entrypoint.sh

RUN chmod 700 entrypoint.sh

RUN mv entrypoint.sh Web2-Projekt

WORKDIR Web2-Projekt

RUN npm install

CMD ./entrypoint.sh
