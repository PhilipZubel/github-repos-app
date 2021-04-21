from django.shortcuts import render
import requests

def index(request):
    # values passed to the template will be stored in context dictionary
    context = {}
 
    # check if a GET request is made
    if 'username' in request.GET:
        context['GET_request_exists'] = True
        username = request.GET['username']
        context['username'] = username
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
        
        # get the values for each repository if the api call is successful
        if is_search_successful:
            # get a response from the url which contains data about repositories
            url_repos = context['response']['repos_url']
            response_repos = requests.get(url_repos)

            # get total number of stars
            context['stars_count'] = getTotalStargazerCount(response_repos.json())
            # get repository names, stars, and urls
            context['repos'] = getGitHubRepositories(response_repos.json())

            # update the remaining responses count since a new response was created
            context['rate']['remaining'] = response_repos.headers['X-RateLimit-Remaining']
    else:
        context['GET_request_exists'] = False
    
    return render(request, 'github_users/index.html', context)

# returns the total number of stars of all repositories
def getTotalStargazerCount(response):
    stars_sum = 0
    # loop through all repositories and add the stars count for each repo to the sum
    for repo in response:
        stars_sum += repo['stargazers_count']
    return stars_sum

# returns the name, stargazer count, and url link for all user's repositories
def getGitHubRepositories(response):
    repos_data = {}
    for repo in response:
        # since repository names are unique for a single user, 
        # those names can be used as keys to the dictionary
        repos_data[repo['name']] = {
            'stars' : repo['stargazers_count'],
            'url' : repo['html_url'],
        }
    return repos_data


