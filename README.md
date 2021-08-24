# renderThing

Render things is a cutting edge app using render.com.

## Knowledge Requirements

Find a smart developer who knows these tools

* Flask
* Python
* Psycopg2

## Setup

### Database
1. Create a database on render.com using the instructions [here](https://render.com/docs/databases#getting-started) and setup with your desired parameters
1. Connect to the database using the provided connection details and use the code within `db.sql` to create and test the table

### Webservice

1. Create a public repo on GitHub or GitLab and duplicate this repo there
1. Create a render.com account
1. Create a web service using Flask for the frontend
1. Create an environment variable in your web service of the name `db_conn` equal to the internal connection string provided by the dashboard of the database you created
1. Spin up a new flask web service pointing at repo you created above
1. Wait for web service to start
1. Bask in your initial success

### CI / CD
1. Edit `.github\workflows\main.yml` and replace the url with the Deploy Hook provided in your web service settings to enable auto deployment on commit to main