# Rotten Ketchup data

### Setup
    # Installation
    git clone https://github.com/stcrestrada/rotten_ketchup.git
    cd rotten_ketchup
    
    '''sh
    # initialize inenv
    pip install inenv
    inenv init rotten_ketchup
    '''
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
    

### Usage

#### Pull data
 
    # Begin pulling data in another process/session
        python manage.py shell_plus
    from rotten_ketchup.utils import load_data

    # Process Data
    load_data()
    exit()
    
    # Run serverer
     python manage.py runserver
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
     
                       
   
### Custom Configuration In settings.py
 
### Rest Framework 

     
    # Change Pagination
    'PAGE_SIZE': 5,
 
    # Switch to TokenAuthentication
    Currently Set to session authentication:
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        )
    # add to installed apps
    INSTALLED_APPS = [
       
        # Third party apps
        'rest_framework.authtoken',
        'rest_framework',
       
    ]
    
    # Add Throttle
    'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '5/minute',
            'user': '25/minute'
        }

     
### Using Postman
    http://127.0.0.1:8000/dev/rt-admin - create a token for your
    user(s).
    # Re-run migrations
    python manage.py makemigrations
    python manage.py migrate
    
    # run server
    python manage.py runserver
    
    # Postman Credentials
    headers: 
    key: Authorization value: Token 4132286bfaa881030cf4a9151f036194134dced0
    
    
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
    

    

    