FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install wget -y
RUN apt-get install -y unzip
RUN apt-get install -y libaio-dev

RUN mkdir /opt/app
COPY ConexionOracle /opt/app/ConexionOracle
COPY Gestion /opt/app/Gestion
COPY myvenv /opt/app/myvenv
COPY * /opt/app/
COPY requirements.txt /opt/app/requirements.txt
RUN pip3 install -r /opt/app/requirements.txt

#### INSTALACION ORACLE
#RUN mkdir -p /opt/oracle
#RUN cd /opt/oracle
#RUN wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip
#RUN unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip
#RUN sh -c "echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf"
#RUN ldconfig
#RUN export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_9:$LD_LIBRARY_PATH


COPY docker-entrypoint.sh /
COPY docker-install-oracle.sh /
EXPOSE 8000

#ENTRYPOINT "/install-oracle.sh"
#ENTRYPOINT "/docker-entrypoint.sh"