"""

Gathering API data from GitHub, on top Python repos.
Will be storing data in dictionary 'response_dict', which is accessed for analyzing key/value pairs.

"""

#Processing API response
import requests

#Make API call and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) #Information from API call is stored as a dictionary
print(f"\nStatus Code: {r.status_code}") #200 = successful

#Store API response in a variable
response_dict = r.json()
#Generating output to display what information API called

print(f"Total Repositories: {response_dict['total_count']}") #Print value attached to 'total_count'

#Explore information about repositories
repo_dicts = response_dict['items'] #value associated with 'items' is a list containing a number of dictionaries
print(f"Repositories returned: {len(repo_dicts)}")

"""
#Examine first repository to see what keys exist and gather their names
repo_dict = repo_dicts[0]
print(f"Keys: {len(repo_dict)}") #Will print number of keys from dictionary[0]

Code below is used to see name of keys from API call

#display all keys associated with repo_dict[0]
for key in sorted(repo_dict.keys()):
    print(key)
"""
#Looking at all repositories, so we can create visualization of collected data
print("\nSelected information from each repository.")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")

    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
