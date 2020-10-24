# Local imports
from secrets import *
from todoist_help_functions import *

# Outbound imports
from todoist.api import TodoistAPI
from github import Github
import os
from pprint import pprint

gitApi = Github(GITHUB_API_TOKEN)
api = TodoistAPI(TODOIST_API_TOKEN)
api.sync()

def getAllMyIssues(repo, username):
    """ This function adds all "open" issues that are assigned to given username

    Args:
        repo ([Repository]): [github repository we want to get the issues from]
        username ([str]): [username that we want all the issues to be added to our "Todoist App"]
    """
    repo = gitApi.get_repo(f"{username}/{repo}")
    todoProject = api.projects.get_by_id(find_project(repo.full_name))
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