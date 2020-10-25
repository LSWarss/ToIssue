import json
import pprint
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@require_POST
def webhooks_endpoint(request):
    jsondata = request.body
    data = json.loads(jsondata)
    pprint(data)
    return HttpResponse(status=200)
