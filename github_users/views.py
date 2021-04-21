from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    # values passed to the template will be stored in context dictionary
    context = {}
 
    # check if a GET request is made
    if 'username' in request.GET:
        username = request.GET['username']
        # url accessed to get a response
        url = 'https://api.github.com/users/%s' % username
        # get the response from the api
        response = requests.get(url)
        # determine whether the response is successful
        # if response is 200 then it is successful 
        is_search_successful = (response.status_code == 200)
        context['success'] = is_search_successful
        # there exists a limited number of calls that can be done in an hour
        # the maximum number of responses and the remaining number of responses
        # are strored in context:'rate' 
        context['rate'] = {
            'max': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }

        context['response'] = response.json()
        
        if is_search_successful:
            url_repos = context['response']['repos_url']
            response_repos = requests.get(url_repos)

            context['stars_count'] = getTotalStargazerCount(response_repos.json())
            context['repos'] = getGitHubRepositories(response_repos.json())

    return render(request, 'github_users/index.html', context)

def getTotalStargazerCount(response):
    stars_count = 0
    for repo in response:
        stars_count += repo['stargazers_count']
    return stars_count

def getGitHubRepositories(response):
    repos_data = {}
    for repo in response:
        # Since repository names are unique for a user, those names can be used as keys to the dictionary
        repos_data[repo['name']] = {
            'stars' : repo['stargazers_count'],
            'url' : repo['html_url'],
        }

    return repos_data


