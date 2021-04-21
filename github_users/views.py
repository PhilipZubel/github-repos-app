from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    # values passed to the template will be stored in context
    context = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        context['response'] = response.json()
        context['success'] = search_was_successful
        context['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'github_users/index.html', context)