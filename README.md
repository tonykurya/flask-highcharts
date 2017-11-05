## Flask Highcharts

[![Build Status](https://travis-ci.org/andela-amutava/Bucketlist.svg?branch=develop)](https://travis-ci.org/andela-amutava/Bucketlist)
|
[![Coverage Status](https://coveralls.io/repos/github/andela-amutava/Bucketlist/badge.svg?branch=master)](https://coveralls.io/github/andela-amutava/Bucketlist?branch=master)

Flask Highcharts is a simple application built using the flask microframework and highcharts. It's an application that helps users visualize Temper's user onboarding retention stats through Highcharts' multiline series charts.


## Functionalities
```
View each weekly Cohort's retention stats.
Compare all Cohorts data in a multiline series chart.
```

## Installation
1. Create a folder.

2. Clone the repository into that folder.<br/>
    `https://github.com/tonykurya/flask-highcharts.git`<br/>

3. Navigate to the project folder.<br/>
   `flask-highcharts` 

4. Install project dependencies in your virtual environment.<br/>
    ` pip install -r requirements.txt`

5.Set up project development. Run db migrations.<br/>
     ```export FLASK_APP=charts.py
        python manage.py db migrate
        python manage.py db upgrade
      ```
6. Run the server.<br/>
   `flask run`


## Nginx Setup
1. Create Nginx configuration for the app.
  ```
	sudo nano /etc/nginx/sites-available/flask-highcharts

	sudo ln -s /etc/nginx/sites-available/flask-highcharts.conf /etc/nginx/sites-enaled

	sudo service nginx reload
  ```

2. Set up Supervisor for process control and monitoring.
  ```
	sudo apt install supervisor
	
	sudo vim /etc/supervisor/conf.d/flask-highcharts.conf

2. Kill gunicorn and restart the process using Supervisor.

  ```
  	sudo pkill gunicorn

    sudo supervisorctl reread
    
    sudo supervisorctl update
    
	sudo supervisorctl start flask-highcharts
  ```

  ### Testing
      You can run the tests nosetests --with-coverage