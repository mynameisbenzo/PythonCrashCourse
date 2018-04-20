import requests

# make an api call and store the response
url = ("https://api.github.com/search/repositories?q=language:" +
		"python&sort=stars")
r = requests.get(url)
print("Status code: ", r.status_code)

# store api response in a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)