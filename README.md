# LearnAPI

 LearnAPI is the backend service utilized by the [Art 
   Application](https://github.com/Graciekan21/arts).
<hr>                                         
<br>

## Table of Contents
* [Development Goals](#Development-Goals)
* [Agile Planning](#Agile-Planning)
    * [Epics](#Epics)
    * [User Stories](#User-Stories)
* [API End Points](#API-End-Points)
* [Future Features](#Features-Left-to-Implement)
* [Database Design](#Database-Design)
* [Security](#Security)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Run Locally](#Run-Locally)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

## Development Goals

The purpose of this API is to provide a backend service for the Arts front-end application, enabling it to perform Create, Read, Update, and Delete operations through the user interface.
<hr>
<br>

## Agile Planning

This project was developed using agile methodologies, delivering small features in incremental sprints. The Kanban board is one for the all project, It was created using GitHub Project and is integrated with the React frontend.

All stories were assigned to epics and prioritized under the labels: Must have, Should have, and Could have, and then assigned to sprints. "Must have" stories were completed first, followed by "Should haves," and finally "Could haves." This approach ensured that all core requirements were completed first, giving the project a complete feel, with the nice-to-have features being added if there was capacity.

The Kanban board can be viewed to see more information on the project cards. All stories, except for the documentation tasks, have a full set of acceptance criteria to define the functionality that marks that story as complete.
All user stories can be viewed on the frontend README.  

![Kanban](/readme/kanban%20(2).png)
<hr>
<br>

### Epics

**Setup**

This Epic covers all the initial setup of the Django application and Django REST Framework in order to begin coding the features.

**Posts**

This Epic encompasses the creation of all API endpoints and database connections related to the CRUD functionality for user posts, including like activity.

**Comments**

This Epic includes the creation of all API endpoints and database connections related to the CRUD functionality for user comments on posts

**Profiles**

This Epic encompasses the creation of all API endpoints and database connections related to the CRUD functionality for user-created profiles, including the following functionality.

**report abuse**

This Epic encompasses the creation of all API endpoints and database connections related to the CRUD functionality for user-created report abuse, including the following functionality.

**Notifications**

This Epic encompasses the creation of all API endpoints and database connections related to the CRUD functionality for user-created notifications , including the following functionality.

### User Stories

**By Epics** 

**Setup**

* As a developer, I need to create the base project set up so that I can build out the features.

* As a developer, I need to create the google cloud bucket and create the connection to the project so that static images can be uploaded by users.

* As a user I can create a new account so that I can access all the features for signed up users
   
**reports**   
        
* As a user, i want to create a form to report a postS
     
**Posts**

* As a user, I want to be able to view, edit, or delete a post.
* As a user, I want to be able to create and list posts

**Profiles**

* As a developer, I want to create a new blank profile with a default image when a user is created.

* As a user, I want to be able to get a list of profiles.


### API Endpoints

User Story:

`As a developer, I need to create the base project set up so that I can build out the features.`

Implementation:

The base project was created, and a virtual environment was set up with all necessary packages installed and frozen into the requirements file. The settings were also configured to hide any secret variables and differentiate between development and production environments.

User Story:
    

Implementation:

Django Rest Framework and dj_rest_auth were installed and added to the URL patterns and site packages to utilize their built-in authentication system.

User Story:

`As a user I can create a new account so that I can access all the features for signed up users`

Implementation:     

Django rest framework and dj_rest_auth were installed and added to the url patterns and site packages to make use of their built in authentication system.

User Story: 

`As a developer, I want to create api views for artists so that they are available to the front end`

Implementation:     
     
Endpoint: /artists/        
Methods:
* POST - Used to create an users
* GET - Used to retrieve a list of users

Endpoint: /arts/<int:pk>/

Methods:
* GET - Used to view single users profile
* PUT - Used to update an users profile
* DELETE - Used to delete an users profile

User Story:
             

`As a developer, I want to create a contact model and API view so that users can contact the site owner with issues`
     
Implementation:

Endpoint: /notifications/

Methods:
* POST - Used to create notifications request
* GET - Used to get a list of notifications requests

Endpoint: /notifications/<int:pk>/

Methods:
* GET - Get a single notification request
* PUT - Used to update a single notification request
* DELETE - Used to delete a notification  request

User Story:

`As a user, I want to be able to view edit or delete a post`

`As a user, I want to able to create a post and list posts`

Implementation:

Endpoint: /posts/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /posts/<int:pk>/

Methods:
* GET - Get a single post
* PUT - Used to update a single post
* DELETE - Used to delete a post


User Story:

`As a developer, I want to create a new blank profile with default image when a user is created.`

Implementation:

In the profiles app, a signal was created in order to create a new user profile on signup.


User Story:

`As a user, I want to able to get a list of profiles`

Implementation:

Endpoint: /profiles/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /profiles/<int:pk>/

Methods:
* GET - Get a single profile
* PUT - Used to update a single profile
* DELETE - Used to delete a profile

## Database Design

I used Lucid to generate the database diagrams
![lucid](https://www.lucidchart.com/)

![ER database Diagram](/readme/database_daigrams.png)

## Security

A permissions class named IsOwnerOrReadOnly was added to ensure that only the users who create the content can edit or delete it.

GCP IAM permissions for the service account were configured for create and read-only access to ensure that only the minimum necessary permissions were granted.
          
## Technologies      
           
* Django
    * Main framework used for application creation
* Django REST Framework
    * Framework used for creating API
* Cloudinary Platform
    * Used for static image hosting
* Heroku
    * Used for hosting the application
* Git
    * Used for version control
* Github
    * Repository for storing code base and docs

<hr>
<br>

## Python Packages
<details open>
<summary> Details of packages </summary>


* asgiref==3.6.0
* cloudinary==1.36.0
* cryptography==3.4.8
* dj-database-url==0.5.0
* dj-rest-auth==2.1.9
* Django==4.2
* django-allauth==0.54.0
* django-cloudinary-storage==0.3.0
* django-cors-headers==4.3.1
* django-filter==2.4.0
* djangorestframework==3.15.1
* djangorestframework-simplejwt==4.7.2
* gunicorn==22.0.0
* oauthlib==3.1.1
* Pillow==8.2.0
* psycopg2==2.9.9
* PyJWT==2.1.0
* python3-openid==3.2.0
* pytz==2021.1
* requests-oauthlib==1.3.0
* sqlparse==0.4.1
* whitenoise==6.7.0


* For creating the Python Json Web Tokens for authentication

Installed as package dependcies with above installations:

<hr>
<br>

## Testing

Unit tests 
       
The API's were tested locally during development but the core testing was done as part of the front end repos and testing to the real API's manually via form inputs and page loads.
    
The results can be found in [LearnAPI](https://github.com/Graciekan21/learnAPI)

**Validator Results**

All folders were run through pep8ci. Several issues appeared with various reasons, lines too long, blank spaces, indentation, white space and expect 2 lines.

All issues were resolved with the exception of lines too long in migration files (these are auto generated so I did not fix) and the auth validator lines in the settings.py which seem to be unbreakable but are framework code.

A warning appeared for env.py being imported but unused although this is being used in the development version, so this was ignored.
      
![comments](/readme/comments_validation%20(2).png)

![learnapi](/readme/settings_validation.png)

![followers](/readme/followers_validation.png)

![likes](/readme/likes_validation.png)

![posts](/readme/posts_validation.png)

![profiles](/readme/profiles_validation.png)

![notifications](/readme/notifications_validation%20(2).png)

![report abuse](/readme/report_validations.png)

**Bugs and their fixes**
         
All issues were resolved except for lines too long in Settings.py, notifications, files (since these are auto-generated, they were not fixed) and the auth validator lines in settings.py, is unbreakable.    
                    
                    
<hr>
<br>

## Deployment

## Gitpod Editor

The site was created using the Gitpod editor and pushed to github to the remote repository ‘Graciekan21’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.
    
<hr>
<br>

## Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
  * SECRET_KEY: (Your secret key)
  * DATABASE_URL: (This should already exist)
  * ALLOWED_HOST:
  * CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
  * CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
  * GOOGLE_APPLICATION_CREDENTIALS:
  * GOOGLE_CREDENTIALS: json file with authentication keys and tokens to access the google cloud bucket where images are stored
  * cloudinary: name of the storage to upload images to.

* Click the deploy tab
* Scroll down to Connect to GitHub and sign in / authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

<hr>
<br>
                               
        
**Heroku**

1. Log in to heroku and open the boody-doodle-api app
2. Click settings
3. Click Config vars
4. Add the following variables:

<hr>
<br>

### Run Locally 

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

In order to run, you will need to create an env.py file and add the config vars as used in heroku steps above.

[Create local Environment ](https://codeinstitute-ide.net/workspaces)

```
python -m venv venv \
venv/Scripts/activate \
pip install -r requirements.txt
```
```
python -m venv venv \
venv/Scripts/activate \
pip install -r requirements.txt
```

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

## Credits

Alan, Sean, Thomas, Roo, John, Roman, Rebecca and at Code Institute's tutor support for the help and guidance with my implementing brain melts and also for the  database reset guidance.

[CodeInstitute](https://learn.codeinstitute.net/courses/) CodeInstitute

### Content:    
         
    
                                  
<br>    
<br>     
                         
This  article was followed in order to implement average rating calculations in the correct way
* [How to calculate average of some field in Dango models and send it to rest API?](https://django.fun/en/qa/16172/)
