# github-repos-app

Aim of the application:
This app makes calls to the GitHub API and retrieves data about github repositories for a given user.
After entering a valid github username, you will see:
- if a user with the following username exists on github
- if the username is valid:
  - the number of repositories for the given user
  - the sum of stars for all of the user's repositories
  - a table displaying the name and star count for each repository as well as links for those repositories
- the number of remaining API calls (the number of API calls per hour is limited)

Technologies used:
- the application was built using the Django REST framework which is based on the Python programming language. 
- Bootstrap 5 was used for styling the app. 
- fontawesome was used for importing icons. 
- the github api used for this project has the following link: https://api.github.com/

How to run the project:
- clone the project on your local machine
- create a virtual environment and install the dependencies listed in the requirements.txt file (on a linux machine the dependencies can be imported using the following command: pip install -r requirements.txt )
- open a terminal, activate your environment, go into the directory which contains the mangage.py file and run the following command: python manage.py runserver
- you will receive a similar messege in the terminal: 'Starting development server at http://127.0.0.1:8000/'. Enter the http link in your browser to run the application

Future improvements:
- The number of API calls is limited for anonymous users to only 60 calls per hour. This value can be increased if the appliaction provides login functionality for a user (a github user can perform 5000 calls per hour). 
- Two API calls are made to retrieve information about the user and the repositories. Since the number of calls is limited, it would be useful if the two calls could be merged into one.

