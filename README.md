# LearnAPI

 LearnAPI is the backend service utilized by the [ Application](https://github.com/Graciekan21/arts).
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
    * [GCP](#Google-Cloud-Platform)
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


<hr>
<br>

### User Stories

**By Epics** 

**Setup**

* As a developer, I need to create the base project setup so that I can build out the features.

* As a developer, I need to create the Google Cloud bucket and establish the connection to the project so that static images can be uploaded by users.

* As a user, I can create a new account to access all the features available to registered users.

**LearnAPI**

* As a developer, I want to create API views for artists so that they are accessible from the front end.

* As a developer, I want to create API views for artists so that they are accessible from the front end.

**reports**
* As a user, I want to create a report for a post
* As a user, i want to create a form to report a postS

**Posts**

* As a user, I want to be able to view, edit, or delete a post.
* As a user, I want to be able to create and list posts

**Profiles**

* As a developer, I want to create a new blank profile with a default image when a user is created.

* As a user, I want to be able to get a list of profiles.


### API Endpoints

User Story:

`As a user, I can create a new account to access all the features available to signed-up users.`

Implementation:

The base project was created, and a virtual environment was set up with all necessary packages installed and frozen into the requirements file. The settings were also configured to hide any secret variables and differentiate between development and production environments.

User Story:

`As a developer, I need to create the Google Cloud bucket and establish the connection to the project so that static images can be uploaded by users.`
       
User Story:
`As a user, I can create a new account so that I can access all the features for signed-up users.`

Implementation:
Django Rest Framework and dj_rest_auth were installed and added to the URL patterns and site packages to utilize their built-in authentication system.

User Story:
`As a developer, I want to create API views for artists so that they are available to the front end`.

Implementation:
Endpoint: /arts/

Methods:
* POST - Used to create an arts
* GET - Used to retrieve a list of arts

Endpoint: /arts/<int:pk>/

Methods:
* GET - Used to view single art profile
* PUT - Used to update an art profile
* DELETE - Used to delete an art profile

User Story:


`As a developer, I want to create a contact model and API view so that users can contact the site owner with issues`

Implementation:

Endpoint: //

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

![DataBase Design](https://lucid.app/lucidchart/a7f04448-2b4c-43d0-bb9a-f30b26363064/edit?viewport_loc=-1730%2C-711%2C1585%2C642%2C0_0&invitationId=inv_432a3a2b-3be2-4e5e-9ef6-ac66def26e72)

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
cloudinary==1.36.0
cryptography==3.4.8
dj-database-url==0.5.0
dj-rest-auth==2.1.9
Django==4.2
django-allauth==0.54.0
django-cloudinary-storage==0.3.0
django-cors-headers==4.3.1
django-filter==2.4.0
djangorestframework==3.15.1
djangorestframework-simplejwt==4.7.2
gunicorn==22.0.0
oauthlib==3.1.1
Pillow==8.2.0
psycopg2==2.9.9
PyJWT==2.1.0
python3-openid==3.2.0
pytz==2021.1
requests-oauthlib==1.3.0
sqlparse==0.4.1
whitenoise==6.7.0


    * For creating the Python Json Web Tokens for authentication

Installed as package dependcies with above installations:

<hr>
<br>

## Testing


**Validator Results**

All folders were run through . Several issues appeared with various reasons, lines too long, blank spaces, indentation, white space and expect 2 lines.

All issues were resolved with the exception of lines too long in migration files (these are auto generated so I did not fix) and the auth validator lines in the settings.py which seem to be unbreakable but are framework code.

A warning appeared for env.py being imported but unused although this is being used in the development version, so this was ignored.
      
 
        
The API's were tested locally during development but the core testing was done as part of the front end repos and testing to the real API's manually via form inputs and page loads.

The results can be found in [Graciekan-learnapi](https://github.com/Graciekan21/learnAPI)

**Validator Results**

All folders were checked using CI python Linter, revealing several issues such as lines too long, blank spaces, indentation, and missing docstrings.

|  Folders      |   Files   |      Validator    | Pass |
|---------------|-----------|-------------------|------|
| comments      | All files | CI python Linter  | Pass |
| followers     | All files | CI python Linter  | Pass |
| learnapi      | All file  | CI python Linter  | Pass |
| likes         | All file  | CI python Linter  | Pass |
| notifications | All files | CI python Linter  | Pass |
| posts         | All files | CI python Linter  | Pass |
| profiles      | All files | CI python Linter  | Pass |
| reports       | All files | CI python Linter  | Pass |


**Bugs and their fixes**
All issues were resolved except for lines too long in Settings.py and in env.py, files (since these are auto-generated, they were not fixed) and the auth validator lines in settings.py, is unbreakable.

A warning about env.py being imported but unused was ignored because it is used in the development version.

![setting.py](/readme/settings_validator.PNG)
![url.py](/readme/env_validator.PNG)
<hr>
<br>

## Deployment

## Version Control

The site was created using Gitpod and then pushed to the remote repository 'Graciekan21' on GitHub
The following git commands were used throughout development to push code to the remote repo:

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

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
  * 

## **Final Changes**

1. Add `ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost"]` in **settings.py**
2. Create a **Procfile** file in the base directory
3. Add to **Procfile**:
    - `release: python manage.py makemigrations && python manage.py migrate`
    - `web: gunicorn <name>.wsgi`
4. In your **Heroku app**: 
   - Go to the *Deploy tab* and connect your GitHub repository
   - Click on *Deploy Branch* at the bottom of the page

<hr>
<br>

## **Cloudinary Setup**

1. Log in to your [Cloudinary](https://console.cloudinary.com/) account
2. At the dashboard, copy the link from the **API Environment variable**

## **Heroku Setup**

1. Log in to your [Heruko](https://www.heroku.com/) account
2. On the dashboard click *New* - *Create new app*
3. Give the app a unique name
4. Select the region closest to you and click *Create app*
5. Select your created app and open the *Settings* tab 
6. At the *Config Vars* section click *Reveal Config Vars* and add the following:
   - **DATABASE_URL** with the copied URL from ElephantSQL
   - **SECRET_KEY** with your secret key
   - **CLOUDINARY_URL** with the copied URL from Cloudinary
   - **DISABLE_COLLECTSTATIC** with the value 1
   - **ALLOWED_HOST** with the value of your deployed Heroku application URL


  ## **Forking**

Forking creates a copy of the project on GitHub. Follow these steps to fork this repository:
1. Log in to your GitHub account and navigate to [LearnAPI repository](https://github.com/Graciekan21/arts).
2. Click the **Fork** button on the top right of the repository.
3. You can now open the forked copy of this project as your own repository.
4. Follow the above steps to work on the project.

## Credits

### Content:
<br>

I followed articles used in the walkthrough by CI in order to impement django  models API 