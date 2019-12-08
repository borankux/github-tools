from github import Github
import yaml

f = open('conf.yaml', 'r')
conf = yaml.unsafe_load(f.read())

def get_github():
    token = conf['token']
    g = Github(token)
    return g
