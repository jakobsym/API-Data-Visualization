"""
Visualize data from GitHub API call
Will be using bar graph to organize collected data via Plotly/Matplotlib

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
response_dict = r.json() #Keys from dictionary 'r' are 'total_count', 'incomplete_results', and 'items'
repo_dicts = response_dict['items'] #'items' is a key from dictionary 'response_dict'
repo_links, stars, labels = [],[],[] #creating empty list named 'repo_names', and 'stars', and 'labels'

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner} <br />{description}" # '<br />' indicates a line break
    labels.append(label)

#Making Visualization
# 'data' is what affects apperance of bars 
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 150, 110)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.7,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository Name',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos_visual.html')
