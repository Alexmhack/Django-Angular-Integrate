# Django-Angular-Integrate
Integrating Django and Angular by creating REST API and running both the servers separately

# Project Initialization
1. Create virtualenv using pipenv
	```
	pipenv install django djangorestframework django-cors-headers python-decouple
	```

2. Activate virtualenv using
	```
	pipenv shell
	```

3. Start Django project
	```
	django-admin startproject backend .
	```

4. Run migrations and create super user
	```
	python manage.py migrate
	python manage.py createsuperuser
	```

5. Start frontend Angular project
	```
	ng new frontend --style=scss --routing
	```

	**NOTE:** I assume that you have NodeJS and NPM installed in your local computer

	```--style=scss``` creates the styling file in ```scss``` format.
	```--routing``` creates the routing module for the angular project

6. Run angular server
	```
	ng serve --open
	```

### Detialed Instructions On Project Coming Soon...
