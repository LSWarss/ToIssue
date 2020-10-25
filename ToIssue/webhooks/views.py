from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def example(request):
    return HttpResponse('Hello, world. This is the webhook response. ')