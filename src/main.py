from secrets import *
from todoist.api import TodoistAPI
from github import Github
import os
from pprint import pprint

gitApi = Github(GITHUB_API_TOKEN)
api = TodoistAPI(TODOIST_API_TOKEN)
api.sync()

def getAllMyIssues(repo, username):
    repo = gitApi.get_repo(f"{username}/{repo}")
    todoProject = api.projects.get(f'{repo}')
    issues = repo.get_issues(state="open")
    if(todoProject != None):
        for issue in issues:
            if issue.assignee.login == 'LSWarss':
                pprint(issue.title)
                task = api.items.add(f'{issue.title}', project_id=todoProject['id'])
                api.commit()
            else:
                pass
    else:
        todoProject = api.projects.add(f"{repo.full_name}")
        for issue in issues:
            if issue.assignee.login == 'LSWarss':
                pprint(issue.title)
                task = api.items.add(f'{issue.title}', project_id=todoProject['id'])
                api.commit()
            else:
                pass
    

getAllMyIssues("ToIssue", "LSWarss")