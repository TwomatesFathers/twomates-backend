from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from config import PRINTFUL_API_BASE_URL, PRINTFUL_API_ORDERS_URL, PRINTFUL_API_TOKEN, PRINTFUL_API_PRODUCTS_URL

GENERIC_SUCCESS_RESPONSE = lambda data: JsonResponse(
    {"code": 200, "status": "success", "data": json.dumps(data)}
)

GENERIC_FAIL_RESPONSE = JsonResponse(
    {"code": 400, "status": "fail", "message": "Invalid request method"}
)


@csrf_exempt
def orders(request):
    try:
        data = json.loads(request.body)
    except:
        return GENERIC_FAIL_RESPONSE
    if request.method == "GET":
        return JsonResponse(data)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if data.get("admin_fields", {}).get("forward_to_printshop") == "True":
                target_url = PRINTFUL_API_BASE_URL + PRINTFUL_API_ORDERS_URL
                headers = {
                    "Content-Type": request.META.get('CONTENT_TYPE'),
                    "Content-Length": request.META.get('CONTENT_LENGTH'),
                    "Authorization": "Bearer " + PRINTFUL_API_TOKEN,
                }
                payload = json.dumps(
                    {"recipient": data.get("recipient"), "items": data.get("items")}
                )
                printful_response = requests.post(
                    target_url, headers=headers, data=payload
                )
                return JsonResponse(printful_response.json(), safe=False)
            return GENERIC_SUCCESS_RESPONSE(data)
        except:
            return GENERIC_FAIL_RESPONSE
    else:
        return GENERIC_FAIL_RESPONSE
    

@csrf_exempt
def products(request, id=None):
    try:
        if request.method == "GET":
            target_url = PRINTFUL_API_BASE_URL + PRINTFUL_API_PRODUCTS_URL
            headers = {
                "Authorization": "Bearer " + PRINTFUL_API_TOKEN,
                    }
            if id:
                target_url += "/" + str(id)
                return JsonResponse(requests.get(target_url, headers=headers).json())
            else:
                return JsonResponse(requests.get(target_url, headers=headers).json())
    except:
        return GENERIC_FAIL_RESPONSE
