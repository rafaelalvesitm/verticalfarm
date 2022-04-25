from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.body)
    print(request)
    return HttpResponse("Hello, world. You're at the vfarm index")