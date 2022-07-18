# Runar
Cryptographic messaging platform that generates links to encrypted messages hiding privacy of sender, and recipient.  

## Project Documentation

Project documentation stored here: 
https://github.com/runar-org/Runar-docs

## How To Run Locally

- install python, postgres, pip

- pip install -r requirements.txt

- Set up your .env file in the same directory as example.env

- Collect static files from messenger app to the root location

``` 
> python manage.py collectstatic 
> this will overwrite files in [root]/static are you sure (y/n)?
> Y
```

- run app with manage.py runserver

## Run locally against a google cloud sql instance

- Initialize google cloud:

` gcloud init `

- Initialize Proxy:

` cloud_sql_proxy -instances "connectionname"=tcp:3306`

## To deploy to google cloud

- Change .env file to google cloud connection properties

- Set local instance to run from local.env

- Initialize google cloud:

` gcloud init `

- Deploy to gcloud 

` gcloud app deploy app.yaml`

### For more information

See the documentation repository linked above.