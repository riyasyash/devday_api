# devday_api
backend apis for devday in python falcon

## Run migrations
  1. `cd` in to project directory
  2. `$ alembic init alembic` will initialise and create an alembic directory.
  3. `$ alembic upgrade head` will run all the migrations.
  
## Run falcon app
* Install requirements `$ pip install -r requirements.pip`
* To run the app:
  1. `cd` in to project directory
  2. `$ gunicorn app:app` will start the application on port 8000
  
