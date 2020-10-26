import json
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@require_POST
def webhooks_endpoint(request):
    headers = request.headers
    body = request.body
    print(headers)
    print(json.dumps(body,indent=4, sort_keys=True))
    jsondata = request.body
    data = json.loads(jsondata)
    return HttpResponse(status=200)
