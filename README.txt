# To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option

flask --app app run

# deployment
https://flask.palletsprojects.com/en/2.2.x/deploying/
https://flask.palletsprojects.com/en/2.2.x/deploying/waitress/

# or

cd py_flask
python -m venv venv
. venv/bin/activate
pip install -e .
pip install waitress

# equivalent to 'from app import app'
waitress-serve --host 127.0.0.1 --port 5555 app:app

Serving on http://127.0.0.1:5555