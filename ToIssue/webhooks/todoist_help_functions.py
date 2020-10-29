from pprint import pprint
from .secrets import *

from todoist.api import TodoistAPI

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


