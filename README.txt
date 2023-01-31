# To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option

flask --app app run

# deployment
https://flask.palletsprojects.com/en/2.2.x/deploying/
https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/

# or

cd hello-app
python -m venv venv
. venv/bin/activate
pip install .  # install your application
pip install waitress

# equivalent to 'from app import app'
waitress-serve --host 127.0.0.1 app:app

Serving on http://127.0.0.1:8080