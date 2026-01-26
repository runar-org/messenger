# Runar
Cryptographic messaging platform that generates links to encrypted messages hiding privacy of sender, and recipient.  

## Project Documentation

Project documentation stored here: 
https://github.com/runar-org/Runar-docs

## How To Run Locally

- install python 3.14, then setup venv

```
python3.14 -m venv myenv 

source myenv/bin/activate 
```

- pip install -r requirements.txt

- Set up your .env file in the same directory as example.env

- Collect static files from messenger app to the root location

``` 
> python manage.py collectstatic 
> this will overwrite files in [root]/static are you sure (y/n)?
> Y
```

- python manage.py migrate

- run app with ` python manage.py runserver `

### For more information

See the documentation repository linked above.