# django-squaring-server

this server works with https://github.com/sobrien-banyan/simple-frontend


## To start app run the following:
in root directory
1. install venv run `python3 -m venv venv`
2. activate venv run `source venv/bin/activate` or `. venv/bin/activate`
3. to start server in django-squaring-server/squaring_api `python3 manage.py runserver`


Django starting steps

1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip install django’ and install 'pip install django-cors-headers'
4. Create a django project with ‘Django-admin start project <project-name>’
5. Run ‘python manage.py runserver’ to see if it worded
6. Create an ‘app’ inside your project with ‘python manage.py startapp <app-name>’
7. Install your new app in your projects setting file
8. Follow the steps
    1. URL —— home
    2. Data to send back. <- ‘hello’
    3. Logic to connect them HelloWorldView
    




## Terminal print out for reference:

seanobrien@Seans-MacBook-Air squaring-api-container % python3 -m venv venv
seanobrien@Seans-MacBook-Air squaring-api-container % ls
venv
seanobrien@Seans-MacBook-Air squaring-api-container % django-admin --version
zsh: command not found: django-admin
seanobrien@Seans-MacBook-Air squaring-api-container % django-admin --version
4.1.3
seanobrien@Seans-MacBook-Air squaring-api-container % source venv/bin/activate
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % ;s
zsh: command not found: s
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % django-admin --version
4.1.3
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % python3 --version
Python 3.10.8
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % deactivate
seanobrien@Seans-MacBook-Air squaring-api-container % deactivate
zsh: command not found: deactivate
seanobrien@Seans-MacBook-Air squaring-api-container % activate
zsh: command not found: activate
seanobrien@Seans-MacBook-Air squaring-api-container % source venv/bin/activate
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % ls
venv
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % django-admin startproject squaring-api-container

CommandError: 'squaring-api-container' is not a valid project name. Please make sure the name is a valid identifier.
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % mkdir squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % django-admin startproject squaring_api
CommandError: '/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api' already exists
(venv) seanobrien@Seans-MacBook-Air squaring-api-container % cd squaring_api 
(venv) seanobrien@Seans-MacBook-Air squaring_api % django-admin startproject squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring_api % ls
squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring_api % ls
squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring_api % cd squaring_api 
(venv) seanobrien@Seans-MacBook-Air squaring_api % ls
manage.py	squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring_api % pthon3 manage.py
zsh: command not found: pthon3
(venv) seanobrien@Seans-MacBook-Air squaring_api % python3 manage.py
Traceback (most recent call last):
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 22, in <module>
    main()
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
(venv) seanobrien@Seans-MacBook-Air squaring_api % python3 manage.py runserver
Traceback (most recent call last):
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 22, in <module>
    main()
  File "/Users/seanobrien/Documents/jtcClass/Django-projects/squaring-api-container/squaring_api/squaring_api/manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
(venv) seanobrien@Seans-MacBook-Air squaring_api % clear

(venv) seanobrien@Seans-MacBook-Air squaring_api % ls
manage.py	squaring_api
(venv) seanobrien@Seans-MacBook-Air squaring_api % python3 --version
Python 3.10.8
(venv) seanobrien@Seans-MacBook-Air squaring_api %  pip install Django==4.1.3
Collecting Django==4.1.3
  Using cached Django-4.1.3-py3-none-any.whl (8.1 MB)
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.3-py3-none-any.whl (42 kB)
Installing collected packages: sqlparse, asgiref, Django
Successfully installed Django-4.1.3 asgiref-3.5.2 sqlparse-0.4.3

[notice] A new release of pip available: 22.2.2 -> 22.3.1
[notice] To update, run: pip install --upgrade pip
(venv) seanobrien@Seans-MacBook-Air squaring_api % python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 08, 2022 - 01:02:14
Django version 4.1.3, using settings 'squaring_api.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[08/Nov/2022 01:02:56] "GET / HTTP/1.1" 200 10681
[08/Nov/2022 01:02:56] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[08/Nov/2022 01:02:56] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[08/Nov/2022 01:02:56] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[08/Nov/2022 01:02:56] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[08/Nov/2022 01:02:56] "GET /favicon.ico HTTP/1.1" 404 2116