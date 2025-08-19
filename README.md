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

#### Allow any Host connect to DB
```
sudo vi /etc/my.cnf
```
ADD these Under [mysqld]
```
bind-address = 0.0.0.0
```
Restart MYSQL DB
```
sudo systemctl restart mysqld
```

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
Check the DB created or Not
```
SHOW DATABASES LIKE 'user';
```
<img width="286" height="114" alt="image" src="https://github.com/user-attachments/assets/44822257-352a-4828-b9c5-d6c164d6c9b4" />

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

Check the Permissions of the "appuser" in DB

```
SELECT user, host FROM mysql.user WHERE user='appuser';
```
I showing like these, then your Configuration is right

<img width="508" height="110" alt="image" src="https://github.com/user-attachments/assets/f0649488-b5b1-40c7-a46d-5d7f53ec4240" />

Check the Grants of the "appuser" in DB

```
SHOW GRANTS FOR 'appuser'@'%';
```
<img width="443" height="130" alt="image" src="https://github.com/user-attachments/assets/9b78491c-4db2-4b7f-ab6d-aa331090c636" />







# Application server Setup

Create "t2.nicro" EC2 Instance and Open port "8080" for Python Application server

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
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database=os.getenv("MYSQL_DATABASE", "test")
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
git clone https://github.com/digistackops-python-org/Python-2-tier-UMS-Local.git
cd Python-2-tier-UMS-Local
```
### switch to PROD Branch

```
sudo git checkout 02-Local-setup-Prod
```

## Export DB Credentials as Environment Variables for DB Connection

```
export MYSQL_HOST="<your-DB-Private-IP>"
export MYSQL_USER="appuser"
export MYSQL_PASSWORD="P@55Word"
export MYSQL_DATABASE="user"
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Start the App
```
python3 app.py
```
### Open browser abd check your App

```
http://<AWS-Public-IP>:8080
```

<img width="1079" height="153" alt="image" src="https://github.com/user-attachments/assets/4d175f5e-ffce-4bcf-a702-43a639891b77" />

<img width="1065" height="147" alt="image" src="https://github.com/user-attachments/assets/954b0f0c-cf97-44f0-beca-b3b5c9c79150" />

# Check data saved in DB or Not

Login to your MYSQL
```
mysql -u root -p
```
Show the List of DBs
```
SHOW DATABASES;
```
Switch to your "user" DB
```
USE user;
```

See the Tables under "user" DB
```
SHOW TABLES;
```
To see Data stored under "user" DB or Not
```
SELECT * FROM user;
```
<img width="967" height="124" alt="image" src="https://github.com/user-attachments/assets/4a100684-4265-4ea3-bc11-95b51a66dbd6" />




