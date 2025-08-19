# Database Setup
Create "t2.micro" EC2 Instance and open port "3306" for DB 

## Install MYSQL DB
```
sudo yum update -y
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install mysql80-community-release-el9-1.noarch.rpm -y
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023
sudo dnf install mysql-community-client -y
sudo dnf install mysql-community-server -y
sudo systemctl start mysqld
sudo systemctl enable mysqld
sudo systemctl status mysqld
```

## Setup MYSQL DB

Get your temporary root Password
```
sudo grep 'temporary password' /var/log/mysqld.log
```
Setup your root Password
```
sudo mysql_secure_installation
```
Login to your MYSQL
```
mysql -u root -p
```
Test it is working or Not
```
SELECT VERSION();
```
## Create our Application DB 'user'
```
CREATE DATABASE user;
```
## Create one system User for our Application in DB
These user can login to DB to do Tasks
```
CREATE USER '<user-name>'@'Host-IP' IDENTIFIED BY 'Password-HERE';

GRANT ALL PRIVILEGES ON <DB-Name>.* TO '<user-name>'@'Host-IP';

FLUSH PRIVILEGES;
```

```
CREATE USER 'appuser'@'%' IDENTIFIED BY 'P@55Word';
GRANT ALL PRIVILEGES ON user.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
```
#### HERE "%" => means any Host will connect

## Allow any Host connect to DB

```
sudo vi /etc/my.cnf
```
ADD these Under [mysqld]
```
bind-address = 0.0.0.0
```

# Application server Setup

Create "t2.nicro" EC2 Instance and Open port "" for Python Application server
## Install Python3
```
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
sudo yum install python3-pip -y
```
## Get the Code
```
git clone https://github.com/digistackops-python-org/Python-2-tier-UMS-Local.git
cd Python-2-tier-UMS-Local
git checkout 01-Local-setup-Dev
```
## Create "config.py" file for DB Connection

```
sudo vim config.py
```
Add these Lines
```
DATABASE_CONFIG = {
    'host': '<your-DB-Private-IP>',
    'user': 'appuser',
    'password': 'p@55Word',
    'database': 'user'
}
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Start the App
```
python3 app.py
```
### Access Your Application in Browser
```
http://<Your-AWS-Public-IP>:8080
```
<img width="1079" height="153" alt="image" src="https://github.com/user-attachments/assets/1a30da40-03a1-4072-aa23-4df8db607392" />
<img width="1065" height="147" alt="image" src="https://github.com/user-attachments/assets/d03318b9-00b3-4de9-a0da-26d7a2a4fd54" />




