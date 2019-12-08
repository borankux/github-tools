import initialize
import yaml

g = initialize.get_github()
repos = g.get_user().get_repos()
repoList = []

for repo in repos:
    r = {}
    r["id"] = repo.id
    r["name"] = repo.name
    r["remove"] = False
    repoList.append(r)

f = open('repos.yaml', "w")
f.write(yaml.dump(repoList))
f.close()
