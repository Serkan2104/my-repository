#!/bin/bash

#run sudo su and below command is for update the system. 
# we use -y not to interacted
yum update -y

# installling apache server
yum install httpd -y

# pushed the files to github and to run server we get index.html from out github directory
# we have to change directory this is apache content folder
cd /var/www/html 
# simdi burada variable kullaniyoruz. diger dosyalari da indiriyoruz
FOLDER="https://raw.githubusercontent.com/Serkan2104/my-repository/main/101-kittens-carousel-static-website-ec2/static-web"
wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg

#start and enable apache server

systemctl start httpd
systemctl enable httpd
# Bu komutlardan sonra Aws Dns address tikladiginda kedicikleri goruyorsun