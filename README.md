<h2>How to setup back-end</h2>

<h4>To install dependencies: </h4>
<pre>
  pipenv install
</pre>

<h4>Inside the command line, to create database: </h4>

<pre>
  from api import db,create_app
  db.create_all(app=create_app())
</pre>

<h4>To run the flask application: </h4>

<pre>
  pipenv shell
  set FLASK_APP=api
  set FLASK_DEBUG=1
  set FLASK_ENV=development
  flask run
</pre>
