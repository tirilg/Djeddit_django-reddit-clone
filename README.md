# Djeddit

A Django discussion web application inspired by reddit

## Installation
Create and activate a new environment

Open the directory of the project, which contains a requirements.txt file

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed packages to run the project.

```bash
pip install -r requirements.txt
```

In settings.py update the Email setup with your own Gmail credentials, for the reset password functionality to work. Make sure its an email for testing purposes and that  the setting "allow less secure apps" is turned on. 


Download Docker to run the Redis server needed for task queues. 

## Run the project
Run the following commands to run Redis and Django-RQ.  

```bash
$ docker run -p 6379:6379 redis
```
```bash
python manage.py rqworker
```

Finally, run the server

```bash
python manage.py runserver
```
