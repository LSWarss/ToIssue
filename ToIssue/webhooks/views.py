import json
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@require_POST
def webhooks_endpoint(request):
    headers = request.headers
    jsondata = request.body
    data = json.loads(jsondata)
    print(type(data))
    print(data['sender'])
    for x in data['sender']:
        print(x)
    
    return HttpResponse(status=200)
