# Rotten Ketchup data

## Setup
### Installation

```sh
git clone https://github.com/stcrestrada/rotten_ketchup.git
cd rotten_ketchup
```
    
### initialize inenv

```sh
$ pip install inenv
$ inenv init rotten_ketchup
$ inenv rotten_ketchup

```
    
### Generate Django secret key:

```sh
$ python base/utils.py
$ export SECRET_KEY="your_secret_key"
```


### Create local psql database
```sh
psql
CREATE DATABASE movies;
```

### Migrations

```sh
$ python manage.py migrate
```

### Create a superuser
```sh
$ python manage.py createsuperuser
```

# Usage

## Pull data
 
### Begin pulling data in another process/session

```sh
$ python manage.py shell_plus
```


### Process Data

```sh
from rotten_ketchup.utils import load_data

load_data()
exit()
```

### Run server

```sh
 python manage.py runserver
```

# Endpoints

### Login:
http://127.0.0.1:8000/api-auth/login/

### Returns a list of movies
http://127.0.0.1:8000/api/v1/movies

### Returns #movie_uuid
http://127.0.0.1:8000/api/v1/movies/movie_uuid

### Returns a list of reviews for movie #movie_uuid
http://127.0.0.1:8000/api/v1/movies/movie_uuid/reviews/

### Returns review #review_uuid for movie #movie_uuid
http://127.0.0.1:8000/api/v1/movies/movie_uuid/reviews/review_uuid

### Returns a list of genres
http://127.0.0.1:8000/api/v1/genres

### Returns genre #genre_uuid
http://127.0.0.1:8000/api/v1/genres/genre_uuid

### Returns a list of movies for genre #genre_uuid
http://127.0.0.1:8000/api/v1/genres/genre_uuid/movies

### Returns movie #movie_uuid for genre #genre_uuid
http://127.0.0.1:8000/api/v1/genres/genre_uuid/movies/movie_uuid

### Returns genres with greatest film count for that year
http://127.0.0.1:8000/api/v1/genres/?year=2012

### How many movie titles are the prefix of another movie title ?  
eg: "A Haunting" is a prefix of "A Haunting We Will Go"
http://127.0.0.1:8000/api/v1/movies/?title=A Haunting
 
                   

### Custom Configuration In settings.py
 
## Rest Framework 

     
### Change Pagination

```python
'PAGE_SIZE': 5,
```

### Switch to TokenAuthentication

```python
Currently Set to session authentication:
'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
```

### add to installed apps

```python
INSTALLED_APPS = [
   
    # Third party apps
    'rest_framework.authtoken',
    'rest_framework',
   
]
```

### Add Throttle

```python
'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/minute',
        'user': '25/minute'
    }
```

### Run migrations again:

```sh
$ python manage.py makemigrations
$ python manage.py migrate

# runserver
$ python manage.py runserver
```
 
# Using Postman

```sh
http://127.0.0.1:8000/dev/rt-admin - create a token for your
user(s).
```

### Postman Credentials
```sh
headers: 
key: Authorization value: Token 4132286bfaa881030cf4a9151f036194134dced0
```
    
## Project Instructions:
```sh
Attached is a text file mapping movie information to it's genre information. 
Using Django we would like you to do the following:

 Load the `movies_genres.tsv` into the Django database
 Create a JSON REST API that would allow someone to browse the information
  
 Minimum API functionality
 Should be able to create, list, update, and delete movies and genres
 Should be able to filter movies by genre
 Should be able to see a count of movies by genre
 Be sure to document and test your code!
  
 Other questions (Include the code used to determine your answers)
 By year, which genre had the most movies?
 How many movie titles are the prefix of another movie title ?  eg: "A Haunting" is a prefix of "A Haunting We Will Go"


```

    