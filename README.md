Rawdata Test:

</br>Dated: 11-01-2021

</br>Author: Deepa G Pillai

</br></br>**Api's to used:**

</br></br>/api/v1/auth/register
</br></br>/api/v1/auth/login
</br></br>/api/v1/auth/refresh
</br></br>/api/v1/tasks/addTasks
</br></br>/api/v1/tasks/reviewTask
</br></br>/api/v1/tasks/fetchAll

</br></br>django==3.0
</br>djangorestframework==3.11.1
</br>djangorestframework_simplejwt==4.4.0

</br></br>**Note to use application:**

Clone the application(master branch)
</br></br>Create virtual environment for python(python3 -m venv (already created in this project,Venv))
</br></br>Activate the virtual environment(/Scripts/activate (in windows))
</br></br>Install requirements mentioned in the requirement.txt file (pip install -r requirements.txt)
</br></br>In windows, set the project in any IDE(pycharm) with newly created Venv
</br></br>Create postgre dB(infodB) and add migrations(python manage.py makemigrations - for creating new migrations python manage.py migrate - to apply migrations)
</br></br>Create superuser (python manage.py createsuperuser)
</br></br>Apply styles to django ui(python manage.py collectstatic, (optional) )
</br></br>To run the application (python manage.py runserver)
</br></br>**Note:**

</br></br>Logger and config files are added
