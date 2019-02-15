# django-rest-api

Example extracted from:
* https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
* https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2

And slightly adapted for Django 2.x. 

Added many fixes mentioned on the comments of the post.
Fixed many things that were not working (like logout and token authentication).

## Useful commands

### Create and Migrate Database

python3 manage.py makemigrations

python3 manage.py migrate

python manage.py migrate --run-syncdb

### Run tests

python3 manage.py test

### Create a super user

python3 manage.py createsuperuser

### Run the server

python3 manage.py runserver

Server will be exposed at http://127.0.0.1:8000/bucketlists/v1


### Get authentication token example

Using a super user with admin/admin as credentials:

curl -v -X POST http://localhost:8000/bucketlists/get-token/ -d "password=admin&username=admin"

Sample response body:

{"token":"a7520a2c098951aeef9aa27fa7e859aaa2ada1a2"}