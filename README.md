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


# Application server Setup

Create "t2.micro" EC2 Instance and Open port "8080" for Python Application server

## Setup your Application Database by executing "initdb.sql" script from Application-server

Step:1 ==> install "MYSQL-Client" for communicate with MYSQL Database
```
sudo yum update -y
sudo wget https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm
sudo dnf install mysql80-community-release-el9-1.noarch.rpm -y
sudo rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023
sudo dnf install mysql-community-client -y
```
Step:2 ==> Execute your "init.sql" script for your Application DB setup

```
mysql -h <DB-Private-IP> -u root -p <DB-Root-Password> < initdb.sql
```
why We use root user HERE => because we just launch MYSQL DB so no other user in DB

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




