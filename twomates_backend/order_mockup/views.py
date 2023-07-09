from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_endpoint(request):
    if request.method == 'POST':
        # Handle the POST request here
        data = request.POST.get('data')
        # Process the data and return a response
        print(data)
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'Invalid request method'})


