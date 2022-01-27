# Milestone Full-Stack Framework Project

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/laptop-ipad_orig.png">

The following project was my attempt to create a fitness and nutrition website for users who are trying to get into better shape. 
Users can search through various nutrition or exercise plans and view the purchased product in their profile page in the form of an instructional
video. A standard user can register a profile, purchase and view products, and track their order history. 
The superuser can add, edit, and delete the products through the Django admin portal. This site currently makes use of HTML, CSS, Python, 
Jinja, and Javascript.

Test Standard Account -> User: guest / Pass: code-tester

SuperUser Account -> User: superuser / Pass: admin

[View live project](https://fitlyfe.herokuapp.com/)

# UX

My goal was to create a website that would allow users interested in improving their health to find
the ideal workout/nutrition plan for their own personal needs. Specifically my goals were to:
- Allow unregistered users to search for nutrition and diet plans.
- Allow registered users to add users to their checkout cart and view them in their profile. 
- Allow registered superusers to add, edit, delete products from the site. 
    - [The superuser login is username: superuser / password: admin]

## User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to be able to register and make an account.
    2. As a First Time User, I'd like to be able to search the site for specific exercise programs and nutritions plans.
    3. As a First Time Superuser, I'd like to be able to easily add, edit, or delete exsisting products. 

-   #### Returning User Goals

    1. As a Returning User, I want to be able to purchase and checkout specific products and eventually view them in my profile. 
    2. As a Returning User, I'd like to be able to easily navigate the site without confusion or an extensive reintroduction. 
    3. As a Returning User, I'd like to review my previous orders and set default contact information for my account.

# Wireframes:
<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/wireframes_orig.png">

# Database Schema:
The relationship between the models can be seen below:

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/database-schema-image_orig.png">

Each user has a username and password, with a confirmation email being sent to confirm the account. When a confirmed user makes a purchase the product is put into an order and the order is then stored to a specified user account.

# Features

- Working email validation for registered users.

- Active stripe payment system.

  - Note: You should only use the trial credit card number (4242 4242 4242 4242)

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
W3C Markup Validator, W3C CSS Validator, JSHint, and Pep8Online were used to test the code. 

- WSC Markup - [Link to site](https://validator.w3.org/)
    - get_films.html - <a href="static/img/validation/get_films.html - Nu Html Checker.pdf"> Results PDF </a>
- W3C CSS - [Link to site](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - base.css - <a href="documentation/css_testing/Base - W3C CSS Validator.pdf">Results PDF </a>
    - checkout.css - <a href="documentation/css_testing/Checkout - W3C CSS Validator.pdf">Results PDF </a>
    - profile.css - <a href="documentation/css_testing/Profile - W3C CSS Validator.pdf">Results PDF </a>
- Javascript [Link to site](https://jshint.com/)
    - countryfield.js
        - <a href="documentation/js_testing/countryfield.png">countryfield.js</a>
    - stripe_elements.js
        - <a href="documentation/js_testing/stripe_elements.png">stripe_elements.js</a>
- Python - [Link to site](http://pep8online.com/)
    - Bag
        - <a href="documentation/python_testing/bag_context.png">context.py</a>
        - <a href="documentation/python_testing/bag_url.png">urls.py</a>
        - <a href="documentation/python_testing/bag_views.png">views.py</a>
    - Checkout
        - <a href="documentation/python_testing/checkout_admin.png">admin.py</a>
        - <a href="documentation/python_testing/checkout_forms.png">forms.py</a>
        - <a href="documentation/python_testing/checkout_models.png">models.py</a>
            - Models code was too long on certain lines.
        - <a href="documentation/python_testing/checkout_signals.png">signals.py</a>
        - <a href="documentation/python_testing/checkout_urls.png">urls.py</a>
        - <a href="documentation/python_testing/checkout_views.png">views.py</a>
        - <a href="documentation/python_testing/checkout_webhooks.png">webhooks.py</a>
        - <a href="documentation/python_testing/checkout_webhooks_handlers_error.png">webhooks_handlers.py</a>
            - Webhook handler code was too long on certain lines.
    - Home
        - <a href="documentation/python_testing/home_url.png">urls.py</a>
        - <a href="documentation/python_testing/home_views.png">views.py</a>
    - Products
        - <a href="documentation/python_testing/products_admin.png">admin.py</a>
        - <a href="documentation/python_testing/products_forms.png">forms.py</a>
        - <a href="documentation/python_testing/products_models.png">models.py</a>
        - <a href="documentation/python_testing/products_urls.png">urls.py</a>
            - Url code was too long on certain lines.

        - <a href="documentation/python_testing/products_views.png">views.py</a>
    - Profiles
        - <a href="documentation/python_testing/profiles_forms.png">forms.py</a>
        - <a href="documentation/python_testing/profiles_models.png">models.py</a>
        - <a href="documentation/python_testing/profiles_urls.png">urls.py</a>
            - Url code was too long on certain lines.
        - <a href="documentation/python_testing/profiles_views.png">views.py</a>


## Testing User Stories

-   #### First Time User Goals

    1. As a First Time User, I want to be able to register and make an account.
        - Login/Registrations tabs are visible in navigation bar on all pages and incorrect username/passwords will alert the user
        that a mistake has been made.
    3. As a First Time User, I'd like to be able to search the site for specific exercise programs and nutritions plans.
        - Site home page clearly presents links to nutrition and exercise plans.
            - The home page functions properly on all screen sizes. 
        - Search bar is available to both registered and unregistered users. 
            - Search bar functions on all screen sizes. 
    4. As a First Time Superuser, I'd like to be able to easily add, edit, or delete exsisting products.
        - Superuser is granted the ability to edit or delete products when viewing them in the product landing page
        or their specified product details page.
        - Includes feature on within member dropdown for superuser to create new products.

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/canvas_orig.png">

-   #### Returning User Goals

    1. As a Returning User, I want to be able to purchase and checkout specific products and eventually view them in my profile. 
       - All purchases are immediately stored in the user profile and available for viewing without restriction. 
    3. As a Returning User, I'd like to be able to easily navigate the site without confusion or an extensive reintroduction. 
       - Site layout is extremely simple and scales well on all devices with little to no errors. 
    4. As a Returning User, I'd like to review my previous orders and set default contact information for my account.
       - User profile has information tab dropdown which shows not only their preferred contact informatio but also
       a summary of all their prior orders. 

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/canvas2_orig.png">


## Further Testing

- Tested using Chrome/Firefox/Safari.

- Tested on iPhone 7.

# Known Bugs / Potential Improvements

- Minor issue with error messages on profile page as a result of youtube links. It doesn't appear to affect the speed or functionality of the page though. It seems to me this error has to do with the embedding method I used for the videos. As a potential solution I plant to experiment with other embedding methods in the future.

<img src="http://moviewatchlist.weebly.com/uploads/8/6/4/2/86429426/fitlyfe-error_orig.png">

# Deployment 

## GitHub Cloning/Coding Environment

1. Log into GitHub.

2. Go to the project's repository.

3. To open it in GitPod simply click the green GitPod button and a new workspace will open. 

To Create your own copy:

4. On the menu bar, click "Settings" which will redirect you to a separate page.

3. Above the menu bar containing the "Settings" tab notice the three buttons to the right: "Unwatch", "Star", and "Fork".
Click the "Fork" button and refresh your browser. You will now have a copy of the repository in your own account.

## Local Deployment

1. Install the neccesary dependencies by typing the following into the terminal: pip3 install -r requirements.txt

2. Environment variables will then need to be set up. This can be done in the terminal:

    export DEVELOPMENT = True
  
    export SECRET_KEY = "Your Secret Key"
  
    export STRIPE_PUBLIC_KEY = "Your Stripe Public Key"
  
    export STRIPE_SECRET_KEY = "Your Stripe Secret Key"
  
    export STRIPE_WH_SECRET = "Your Stripe WH Secret Key"

3. You will then need to migrate the database models. In the terminal type:

python3 manage.py makemigrations
  
python3 manage.py migrate
  
4. To load the product fixtures into the database type the following into the terminal: 

python3 manage.py loaddata categories 

Followed by:

python3 manage.py loaddata products

5. You will then be able to run the app locally using the following command: python3 manage.py runserver

## Heroku Deployment

1. Create Heroku Account and create an app for the project.

2. Go to the app's settings and click on "reveal config vars". Then set the following the variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, and USE_AWS

3. Go to the settings file of the main fitness app and add your own Postgres database url to the DATABASES section where it says:

default': dj_database_url.parse("Here")  

4. Make the migrations to the PostgreSQL Database by typing the following into the terminal:

python3 manage.py makemigrations 

Then:

python3 manage.py migrate

5. Then finally login into heroku in the terminal (heroku login) and commit your changes so as to push the code to the live app. 

6. Open App in Heroku


# Credits

- Code
    - Code Institute (Boutique Ado Project)
        - The mini Boutique Ado assignment served as a helpful jumping off point for developing my code.

- Content
    - Men/Women Nutrition Videos:
        - Fit Father Project - Fitness For Busy Fathers (https://www.youtube.com/channel/UCKvJ_vxZZoN5yeWBU2CVGcQ)
        - Thomas DeLauer (https://www.youtube.com/channel/UC70SrI3VkT1MXALRtf0pcHg)
    - Strength Videos
        - Juice & Toya (https://www.youtube.com/channel/UCwrXi5ZknKThspJc-Gai04g)
    - Strength Videos
        - HASfit (https://www.youtube.com/channel/UCXIJ2-RSIGn53HA-x9RDevA)
    - Flexability Videos
        - Tom Merrick (https://www.youtube.com/channel/UCU0DZhN-8KFLYO6beSaYljg)

- Media
    - [FontMeme](https://fontmeme.com/permalink/210729/7c4f14820fc13e73ba00a7ff096daf55.png) This was used to create the site logo.
    - [Google Images](https://google.com): This was used by myself, and presumbably, the testers to find images icons for the products. 


- Acknowledgements
    - Thank you to FontMeme!
    - Thank you to Code Institute!
    - Thank you Slack users!
