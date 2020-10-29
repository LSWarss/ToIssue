from secrets import *

# Outbound imports
import os
from pprint import pprint
from todoist.api import TodoistAPI
from github import Github


def find_project_by_name(name):
    """ Help function to find specific projects ID by given name

    Args:
        name ([str]): [Project name]
    """
    api = TodoistAPI(TODOIST_API_TOKEN)
    api.sync()
    projects = api.state['projects']
    for project in projects:
        if project['name'] == name:
            return(project['id'])

def find_task_by_name(content):
    api = TodoistAPI(TODOIST_API_TOKEN)
    api.sync()
    items = api.state['items']
    for item in items:
        if item['content'] == content:
            return(item['id'])


# TODO: Add if for the object added to the todolist, while right now it's all added no matter 
# if is in the list or nah
def getAllMyIssuesFromProject(repo, username):
    """ This function adds all "open" issues that are assigned to given username

    Args:
        repo ([Repository]): [github repository we want to get the issues from]
        username ([str]): [username that we want all the issues to be added to our "Todoist App"]
    """

    gitApi = Github(GITHUB_API_TOKEN)
    api = TodoistAPI(TODOIST_API_TOKEN)
    api.sync()

    repo = gitApi.get_repo(f"{username}/{repo}")
    todoProject = api.projects.get_by_id(find_project_by_name(repo.full_name))
    issues = repo.get_issues(state="open")
    if(todoProject != None):
        for issue in issues:
            if issue.assignee.login == 'LSWarss':
                if(api.items.get_by_id(find_task_by_name(issue['content'])) != None):
                    task = api.items.add(f'{issue.title}', project_id=todoProject['id'])
                    api.commit()
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

def addNewIssueToTodoist(repoFullName, username, issueTitle):
    api = TodoistAPI(TODOIST_API_TOKEN)
    api.sync()
    todoProject = api.projects.get_by_id(find_project_by_name(repoFullName))
    print(todoProject)
    if(todoProject != None):
        if username == 'LSWarss':
            if api.items.get_by_id(find_task_by_name(issueTitle) != None):
                task = api.items.add(issueTitle, project_id=todoProject['id'])
                print(task)
                api.commit()
        else:
            pass
    else:
        todoProject = api.projects.add(repoFullName)
        if username == 'LSWarss':
            if api.items.get_by_id(find_task_by_name(issueTitle) != None):
                task = api.items.add(issueTitle, project_id=todoProject['id'])
                api.commit()
        else:
            pass


addNewIssueToTodoist("LSWarss/ToIssue","LSWarss","Testing issue 10")
getAllMyIssuesFromProject("LSWarss/ToIssue","LSWarss")