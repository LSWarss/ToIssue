import json
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .logic import *

@csrf_exempt
@require_POST
def webhooks_endpoint(request):
    jsondata = request.body
    data = json.loads(jsondata)
    if('issue' in data):
        print(data)
        print(f"Repository full name: {data['repository']['full_name']} \n"
                f"Issue sender: {data['sender']['login']} \n"
                f"Issue title: {data['issue']['title']}")
        addNewIssueToTodoist(data['repository']['full_name'],data['sender']['login'],data['issue']['title'])
    
    return HttpResponse(status=200)
