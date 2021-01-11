Rawdata Test:

Dated: 11-01-2021

Author: Deepa G Pillai

Api's to used:

/api/v1/auth/register
/api/v1/auth/login
/api/v1/auth/refresh
/api/v1/tasks/addTasks
/api/v1/tasks/reviewTask
/api/v1/tasks/fetchAll

django==3.0
djangorestframework==3.11.1
djangorestframework_simplejwt==4.4.0

Note to use application:

Clone the application(master branch)
Create virtual environment for python(python3 -m venv (already created in this project,Venv))
Activate the virtual environment(/Scripts/activate (in windows))
Install requirements mentioned in the requirement.txt file (pip install -r requirements.txt)
In windows, set the project in any IDE(pycharm) with newly created Venv
Create postgre dB(infodB) and add migrations(python manage.py makemigrations - for creating new migrations python manage.py migrate - to apply migrations)
Create superuser (python manage.py createsuperuser)
Apply styles to django ui(python manage.py collectstatic, (optional) )
To run the application (python manage.py runserver)
Note:

Logger and config files are added
