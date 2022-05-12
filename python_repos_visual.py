"""
Visualize data from GitHub API call
Will be using bar graph to organize collected data via Plotly

"""
import requests
from plotly.graph_objs import Bar
from plotly import offline

#Make API call and store reponse
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) #Information from API call is stored as a dictionary
print(f"\nStatus Code: {r.status_code}") #200 = successful

#Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [],[] #creating empty list named 'repo_names', and 'stars'

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#Making Visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')