import initialize
import yaml

g = initialize.get_github()
f = open('repos.yaml', 'r')
repos = yaml.unsafe_load(f.read())

deleted = []
for i in range(len(repos)):
    repo = repos[i]
    remove = repo['remove']
    if remove:
        name = repo['name']
        confirm = input('Are you sure to delete ' + name + ' ?\n(Y/n)')
        if confirm == 'y':
            g.get_repo("borankux/" + name).delete()
            deleted.append(i)
            print("repo" + name + " deleted 👌")


for i in range(len(repos)):
    for j in deleted:
        if i == j:
            repos.pop(i)
c = open('repos.yaml', 'w')
c.write(yaml.dump(repos))
c.close()
