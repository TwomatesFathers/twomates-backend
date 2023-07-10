from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from config import PRINTFUL_API_BASE_URL, PRINTFUL_API_ORDERS_URL, PRINTFUL_API_TOKEN


@csrf_exempt
def orders(request):
    if request.method == "GET":
        return JsonResponse(data)
    if request.method == "POST":
        data = json.loads(request.body)
        if bool(data.get("admin_fields", {}).get("forward_to_printshop")):
            target_url = PRINTFUL_API_BASE_URL + PRINTFUL_API_ORDERS_URL
            headers = {
                "Content-Type": "application/json",
                "Content-Length": "542",
                "Authorization": "Bearer " + PRINTFUL_API_TOKEN,
            }
            payload = json.dumps(
                {"recipient": data.get("recipient"), "items": data.get("items")}
            )
            printful_response = requests.post(target_url, headers=headers, data=payload)
        return JsonResponse(printful_response.json(), safe=False)
    else:
        return JsonResponse({"message": "Invalid request method"})
