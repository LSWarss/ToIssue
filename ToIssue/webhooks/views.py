import json
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@require_POST
def webhooks_endpoint(request):
    jsondata = request.body
    data = json.loads(jsondata)
    return HttpResponse(status=200)

@csrf_exempt
def payload_endpoint(request):
    if request.method == 'POST':
        incoming_msg = request.POST['Body'].lower()
    print(incoming_msg)

    return HttpResponse(status=200)