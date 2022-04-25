from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print(request)
    return HttpResponse("This is the index page.")

@csrf_exempt
def devices(request, device_id):
    if request.method == "GET":
        print(request.body)
        return HttpResponse("This is the devices page.")
    elif request.method == "POST":
        print(request.body)
        return HttpResponse("This is the devices page.")