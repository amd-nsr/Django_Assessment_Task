# To make this project up and running, you need to follow instructions bellow
At first, I suggest that you create an isolated virtual environment
    -> pip install virtualenv
    -> virtualenv venv
    -> then activate the virtualenv
1- Install the requirements.txt file 
    -> You can use this command "pip install -r /path/to/requirements.txt"
2- Be sure that you have MySql DB
    -> I am using the default user "root" and a password="root"
3- Create a database "assessment_task"
    -> use this command to create the database "create database assessment_task"
4- Make the database migrations
    -> Be sure that you are in the root dirctory (where the manage.py file is located)
    -> run this command "python manage.py makemigrations"
    -> then run "python manage.py migrate"
5- After applying the migrations to the database you can now switch on the server
    -> run this command "python manage.py runserver"
and now you should have the project run on your local host