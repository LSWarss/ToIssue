# Local imports
from todoist_help_functions import *
from secrets import *

# Outbound imports
import os
from pprint import pprint
from todoist.api import TodoistAPI
from github import Github


gitApi = Github(GITHUB_API_TOKEN)
api = TodoistAPI(TODOIST_API_TOKEN)
api.sync()

# TODO: Add if for the object added to the todolist, while right now it's all added no matter 
# if is in the list or nah
def getAllMyIssuesFromProject(repo, username):
    """ This function adds all "open" issues that are assigned to given username

    Args:
        repo ([Repository]): [github repository we want to get the issues from]
        username ([str]): [username that we want all the issues to be added to our "Todoist App"]
    """
    repo = gitApi.get_repo(f"{username}/{repo}")
    todoProject = api.projects.get_by_id(find_project_by_name(repo.full_name))
    issues = repo.get_issues(state="open")
    if(todoProject != None):
        for issue in issues:
            if issue.assignee.login == 'LSWarss':
                pprint(issue.title)
                if(api.items.get_by_id(find_task_by_name(issue['content'])) != None):
                    task = api.items.add(f'{issue.title}', project_id=todoProject['id'])
                    api.commit()
                else:
                    pass
            else:
                pass
    else:
        todoProject = api.projects.add(f"{repo.full_name}")
        for issue in issues:
            if issue.assignee.login == 'LSWarss':
                if(api.items.get_by_id(find_task_by_name(issue['content'])) != None):
                    task = api.items.add(f'{issue.title}', project_id=todoProject['id'])
                    api.commit()
                else:
                    pass
            else:
                pass
    

getAllMyIssuesFromProject("ToIssue", "LSWarss")
