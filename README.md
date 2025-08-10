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
HERE % => any Host will connect

## Allow any Host connect to DB

```
sudo vi /etc/my.cnf
```
ADD these Under [mysqld]
```
bind 0.0.0.0
```

# Application server Setup

Create "t2.nicro" EC2 Instance and Open port "" for Python Application server

## Note ==> HERE in our PROD Branch Code we alredy Edit these Code in "app.py", so no need to Change any thing HERE

### Good-To-Know
```
we Create "config.py" and mention our DB credentials and push it to GIT. It expose our Credentials to everyone
Which is Not recommended in PROD as well

So we need to Pass our DB Credentials as Environment Variables
For that we need to Change our Code 


#### Don't Follow these steps these code is already edited

Open your "app.py" Edit MYSQL configuration


# MySQL configurations
db = mysql.connector.connect(**DATABASE_CONFIG)
cursor = db.cursor()


Edit and replace with these Lines

# Read DB credentials directly from environment variables
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASS", ""),
    database=os.getenv("DB_NAME", "test")
)
cursor = db.cursor()
```

## Install Python3
```
sudo yum update -y
sudo yum install git -y
sudo yum install python3 -y
sudo yum install python3-pip -y
```
## Get the Code
```
git clone https://github.com/techizone-Small-Project-org/Python-2-tier-UMS-App.git
cd Python-2-tier-UMS-App
git 02-Local-setup-Prod
```
## Export DB Credentials as Environment Variables for DB Connection

```
export DB_HOST="<your-DB-Private-IP>"
export DB_USER="appuser"
export DB_PASS="p@55Word"
export DB_NAME="user"
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Start the App
```
python3 app.py
```
<img width="1760" height="414" alt="image" src="https://github.com/user-attachments/assets/f646bfb1-ba0a-467e-8659-ae21b4c5b36b" />


