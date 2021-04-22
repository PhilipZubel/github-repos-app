# github-repos-app

## Aim of the application:

This app makes calls to the GitHub API and retrieves data about repositories for a given github user.
After entering a username in the search box, if there is a match with a valid github user account, you will see:

- the total number of repositories
- the total number of stars for all repositories
- a table displaying the names of repositories with their coresponding star counts and links
- the number of remaining API calls (the number of API calls per hour is limited)

## Technologies used:

- the application was built using the Django REST framework which is based on the Python programming language.
- Bootstrap 5 was used for styling the app.
- Fontawesome was used for importing icons.
- the github api used for this project has the following link: https://api.github.com/

## How to run the project:

- clone the project on your local machine
- create a virtual environment and install the dependencies listed in the requirements.txt file. On a linux machine the dependencies can be imported using the following command:

```bash
pip install -r requirements.txt
```

- open a terminal, activate your environment, go into the directory which contains the manage.py file and run the following command:

```bash
python manage.py runserver
```

- you will receive a similar message on the terminal: 'Starting development server at http://127.0.0.1:8000/'. Enter the http link in your browser to run the application

## Future improvements:

- The number of API calls is limited to only 60 calls per hour for anonymous users. This value can be increased if the application provides login functionality for a user (a github user can perform 5000 calls per hour).
- Two API calls are made to retrieve information about each user and their repositories. Since the number of calls is limited, it would be more efficient to merge two API calls into one.

## Additional info:

- The view which handles the GET request can be found inside github_users/views.py
- Inside github_users/views.py you will find the following methods:
  - getTotalStargazerCount - returns the total number of repository stars
  - getGitHubRepositories - returns basic information about all repositories

## Screenshots of the app:

![alt text](https://github.com/PhilipZubel/github-repos-app/blob/main/screenshots_readme/screenshot1.PNG)

![alt text](https://github.com/PhilipZubel/github-repos-app/blob/main/screenshots_readme/screenshot2.PNG)
