#!/bin/bash
yum install git wget epel-release python3 python3-pip firewalld centos-release-scl devtoolset-7-gcc* gcc-c++ cmake3 -y
cd /home/ec2-user && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/tasks && pip3 install -r model_requirements.txt
rpm –import https://artifacts.elastic.co/GPG-KEY-elasticsearch
yum install  -y
echo 'server.host: "0.0.0.0"' >> /etc/kibana/kibana.yml
systemctl daemon-reload
systemctl enable firewalld
firewall-cmd --permanent --add-port 80/tcp
firewall-cmd --reload