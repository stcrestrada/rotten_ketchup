# Rotten Ketchup data

### Setup

    pip install inenv
    inenv init rotten_ketchup
    inenv rotten_ketchup
    
    # Generate Django secret key:
    from root directory run python base/utils.py
    This will return a randomly generated 'SECRET_KEY'
    export SECRET_KEY="your_secret_key"
    
    # Create local psql database
    psql
    CREATE DATABASE movies;
    
    # Migrations
    python manage.py migrate
    
    # Create a superuser
    python manage.py createsuperuser
    
    # Run server
    python manage.py runserver

### Usage

#### Pull data
 
    # Begin pulling data in another process/session
    python manage.py shell_plus
    from rotten_ketchup.utils import load_movies

    # Process Data
    load_movies()
### Endpoints

    # Login:
    http://127.0.0.1:8000/api-auth-login/
    
    # Returns a list of movies
    http://127.0.0.1:8000/api/v1/movies
    
    # Returns #movie_uuid
    http://127.0.0.1:8000/api/v1/movies/movie_uuid
    
    # Returns a list of reviews for movie #movie_uuid
    http://127.0.0.1:8000/api/v1/movies/movie_uuid/reviews/
    
    # Returns review #review_uuid for movie #movie_uuid
    http://127.0.0.1:8000/api/v1/movies/movie_uuid/reviews/review_uuid
    
    # Returns a list of genres
    http://127.0.0.1:8000/api/v1/genres
    
    # Returns genre #genre_uuid
    http://127.0.0.1:8000/api/v1/genres/genre_uuid
    
    # Returns a list of movies for genre #genre_uuid
    http://127.0.0.1:8000/api/v1/genres/genre_uuid/movies
    
    # Returns movie #movie_uuid for genre #genre_uuid
    http://127.0.0.1:8000/api/v1/genres/genre_uuid/movies/movie_uuid
    
    # Returns genres with greatest film count for that year
    http://127.0.0.1:8000/api/v1/genres/?year=2012
    
    # How many movie titles are the prefix of another movie title ?  
    eg: "A Haunting" is a prefix of "A Haunting We Will Go"
    http://127.0.0.1:8000/api/v1/movies/?title=A Haunting
     
    
### Postman
    
    # Token
    http://127.0.0.1:8000/admin - view token and/or create a token if needed
    
    # Postman Credentials
    headers: 
    key: Authorization value: Token 4132286bfaa881030cf4a9151f036194134dced0
                    
    
    
### Custom Configuration In settings.py
 
### Rest Framework 
    # Adjust Throttle Rates
    In settings.py an anonymous user and authenticated user throttle
    rate is configurable. 
    Currently set at 
    'DEFAULT_THROTTLE_RATES': {
            'anon': '5/minute',
            'user': '25/minute'
        }
    
    # Change Pagination
    'PAGE_SIZE': 5,
    
    # Switch to SessionAuthentication
    Currently Set to token authentication:
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        )
    Session authentication allows you to use CRUD operation in the rest application versus token authentication where
    you must use postman for crud operations.
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        )
     and remove 'rest_framework.authtoken' from INSTALLED_APPS
    
### Project Instructions:
    #Attached is a text file mapping movie information to it's genre information. 
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
    

    

    