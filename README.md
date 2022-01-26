# Milestone Full-Stack Framework Project

The following project was my attempt to create a fitness and nutrion website for users who are trying to get into better shape. 
Users can buy either nutrtion or exercise plans and view the purchased product in their profile page in the form of an instructional
video. A standard user can register a profile, purchase and view products, and track their order history. 
The superuser can add, edit, and delete the products through the Django admin portal. This site currently makes use of HTML, CSS, Python, 
Jinja, and Javascript.

Test Standard Account -> User: guest / Pass: code-tester

SuperUser Account -> User: superuser / Pass: admin

[View live project](https://fitlyfe.herokuapp.com/)

# UX

(NEED)

## User Stories

-   #### First Time User Goals

    1. As a First Time User, I  

-   #### Returning User Goals

    1. As a Returning User, I

# Wireframes:
<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/wireframes_orig.png">

# Database Schema:
The relationship between the models can be seen below:

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/wireframes_orig.png">

Each user has a name and password. When a user creates a film, their name is stored in the film. Likewise when a user 
creates a recommendation for a film their name, as well as the film's title, is stored in the recommendation. 

# Features

- Mobile, desktop, and tablet scalable.

- User can purchase video plans and view them on profile.

- Superuser can add/edit/delete products on the site or through Django. 

# Technology Used

## Languages

The following technologies have been used to achieve this project:

- HTML was used as the main writing language of this project.
- CSS was used for styling.
- JavaScript
    - Jquery is used for simplifying JavaScript.
- Jinja was utilized for templating Python in Django.

## Frameworks, Libraries, Websites & Programs Used

- [W3schools](https://www.w3schools.com/): This site provided many useful templates in their lessons.

- [Bootstrap](https://www.bootstrap.com/): Very helpful framework for figuring out initial design.

- [FontAwesome](https://fontawesome.com/): Provided icons for certain features.

- [Photoshop](https://photoshop.com/en): This was used to design the site's wireframes and database schema. 

- [FontMeme](https://www.fontmeme.com/): This was used to design the logo. 

- [Heroku](https://www.heroku.com/): Heroku was used to deploy the website.

- [Django](https://www.djangoproject.com/) is used as main web framework for the website.
    - Django Crispyforms
    - Django Allauth
    - Stripe
    - Gunicorn
    - Psycopg2
    - Django Countries
    
- [Amazon Web Services](https://aws.amazon.com/): Used to store all static files and images.

- [GitHub](https://github.com/): GitHub was used to code the program.
    - Dependencies List:
        - asgiref==3.4.1
        - boto3==1.20.42
        - botocore==1.23.42
        - dj-database-url==0.5.0
        - Django==3.2
        - django-allauth==0.41.0
        - django-countries==7.2.1
        - django-crispy-forms==1.13.0
        - django-storages==1.12.3
        - gunicorn==20.1.0
        - jmespath==0.10.0
        - oauthlib==3.1.1
        - Pillow==9.0.0
        - psycopg2-binary==2.9.3
        - python3-openid==3.2.0
        - pytz==2021.3
        - requests-oauthlib==1.3.0
        - s3transfer==0.5.0
        - sqlparse==0.4.2
        - stripe==2.64.0


# Testing
W3C Markup Validator, W3C CSS Validator, and Pep8Online were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - get_films.html - <a href="static/img/validation/get_films.html - Nu Html Checker.pdf"> Results PDF </a>
    - login.html - <a href="static/img/validation/login.html - Nu Html Checker.pdf"> Results PDF </a>
    - register.html - <a href="static/img/validation/register.html - Nu Html Checker.pdf"> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - style.css - <a href="static/img/validation/W3C CSS Validator (CSS level 3 + SVG).pdf">Results PDF </a>
- Python - [Link to site](http://pep8online.com/)
    - app. py
        - <a href="static/img/validation/PEP8 online check - Results.pdf">Results PDF </a>
        - <a href="static/img/validation/result_20210812_193900.txt">Results TXT </a>


## Testing User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to easily locate different films, either by title or genre. 
        - Site landing page clear presents links to available films.
            - Site landing page functions properly on all screen sizes. Only room for improvment
            would be the scalability of the images. At certain points the images become slightly
            distorted. 
        - Search bar is available to both registered and unregistered users, as is
        the genre selector.
            - Search bar functions on all screen sizes and scales properly to fit both search/exit button
            and genre search bar below it. 
    2. As a First Time User, I want to easily find the recommendations for the films. 
        - Upon selection the site displays all available recommendation for the film in question.
            - Film information is present and scalable, any overflow is visible through scrolling. 
    3. As a First Time User, I would like the option to register for an account.  
        - Register tab is visible in navigation bar on all pages. 

-   #### Returning User Goals

    1. As a Returning User, I want to be able to login to my account.
        - Login tab is visible in navigation bar on all pages and incorrect username/passwords will alert the user
        that a mistake has been made.
    2. As a Returning User, I would like to add films to the site so that others might offer 
    reading suggestions based on my preferences. 
        - The landing page for logged-in users clearly displays an add film feature as the first of the available 
        film selection options. 
        - Also includes feature on film profile for user to edit or delete any films they may have made.
    3. As a Returning User, I would like to be able to upload my own book suggestions for certain films. 
        - Film profile offers users the oppurtunity to add their own recommendations. 
        - Likewise includes a feature to edit/delete book recommendations.



## Further Testing

- Tested using Chrome/Firefox/Safari.

- Tested on iPhone 7.

# Known Bugs / Potential Improvements

- Minor Issue with error messages on profile page

(img)

# Deployment 

## GitHub Cloning/Coding Environment

1. Log into GitHub.

2. Go to the project's repository.

3. To open it in GitPod simply click the green GitPod button and a new workspace will open. 

To Create your own copy:

4. On the menu bar, click "Settings" which will redirect you to a separate page.

3. Above the menu bar containing the "Settings" tab notice the three buttons to the right: "Unwatch", "Star", and "Fork".
Click the "Fork" button and refresh your browser. You will now have a copy of the repository in your own account.


## Heroku Deployment 

0. (Open project in GitHub.)

1. To deploy from Heroku first note down all neccesary dependencies the project requires to function. To do this create a requirements.txt file in the terminal with the command: pip freeze > requirements.txt

2. Create Procfile with the commmand echo web: python app.py > Procfile. This will let Heroku know it's going to run a python file. 

3. Push these files to GitHub then go to the Heroku site. 

4. Login and create a new app. 

5. Go to deploy and select github as the method. You will then be asked to link the heroku app to a repository. Select the name of project. 

6. Then go to settings > "reveal config vars" which is where you will store the environment variables which were not pushed to github.  
    - "IP": "0.0.0.0")
    - "PORT": "5000")
    - "SECRET_KEY": "mYt905thou1W")
    - "MONGO_URI": "mongodb+srv://pokemongoDB:Pikachu25@myfirstcluster.4i2hj.mongodb.net/readflix?retryWrites=true&w=majority"
    - "MONGO_DBNAME": "readflix")

7. Then go back to the deployment section of the app and click "deploy branch". 


# Credits

- Code
    - Code Institute (Task Manager Project)
        - The mini Task Manager assignment served as a helpful jumping off point for developing my code.

- Content
    - I developed the code myself however many of the film and book recommendations were provided
    by friends and family I had test the site. 

- Media
    - [FontMeme](https://fontmeme.com/permalink/210729/7c4f14820fc13e73ba00a7ff096daf55.png) This was used to create the site logo.
    - [Google Images](https://google.com): This was used by myself, and presumbably, the testers to find images for the
    film posters. 


- Acknowledgements
    - Thank you to FontMeme!
    - Thank you to Code Institute!
