import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse({'on': 'Valve open'}, status = 200)
    else:
        print(request)
        return HttpResponse("Hello, world. You're at the vfarm index")