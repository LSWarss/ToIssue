from secrets import *
from todoist.api import TodoistAPI
from pprint import pprint

def find_project(name):
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
