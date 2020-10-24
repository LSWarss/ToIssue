from secrets import *
from todoist.api import TodoistAPI
from github import Github
import os
from pprint import pprint


gitApi = Github(GITHUB_API_TOKEN)
api = TodoistAPI(TODOIST_API_TOKEN)
api.sync()

projects = api.state['projects']
pprint(projects)

def find_project(name):
    for project in projects:
        if project['name'] == name:
            return(project['id'])

print(find_project('LSWarss/ToIssue'))