#  SentinelShield - Advanced Intrusion Detection & Web Protection System


##  Project Overview

SentinelShield is a cybersecurity monitoring platform designed to detect and analyze malicious web attack patterns in real-time.

The system scans user requests, identifies suspicious payloads, categorizes threats, and stores detected attack details inside a security dashboard.


##  Features

- Real-Time Web Threat Detection
- SQL Injection Detection
- Cross Site Scripting (XSS) Detection
- Command Injection Pattern Analysis
- Attack Logging System
- SOC Style Security Dashboard
- Threat Severity Classification
- Source IP Tracking


##  Technology Stack

- Python
- Flask Framework
- SQLite Database
- SQLAlchemy ORM
- HTML5
- CSS3


##  How It Works

1. User submits request payload
2. Detection engine scans the input
3. Security patterns are matched
4. Threat category is identified
5. Attack details are stored
6. Dashboard displays security logs


##  Project Structure


SentinelShield/

│── app.py

│── database.py

│── detector.py

│── requirements.txt

│── README.md

│

├── templates/

│   ├── index.html

│   └── dashboard.html

│

└── static/

    └── style.css



##  Installation


Clone Repository


git clone <repository-link>


Install Requirements


pip install -r requirements.txt


Run Application


python app.py



Open Browser:


http://127.0.0.1:5000



##  Security Modules


### SQL Injection Detection

Detects malicious database manipulation attempts.


Example:

' OR '1'='1



### XSS Detection

Detects script based web attacks.


Example:

<script>alert("hack")</script>



##  Dashboard Information

The dashboard displays:

- Attack ID
- Source IP Address
- Threat Category
- Severity Level
- Malicious Payload
- Detection Time



##  Future Improvements

- Email Alert System
- Machine Learning Based Detection
- IP Blocking System
- Advanced Threat Intelligence Integration



##  Developed By

Sayan Dutta