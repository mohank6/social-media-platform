from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from . import bussiness
from . import accessor


@csrf_exempt
def signup(request):
    if not request.method == 'POST':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        data = json.loads(request.body)
        validated_data = bussiness.validate_data_signup(data=data)
        if not validated_data:
            return JsonResponse({"message": "Validation error"}, status=400)
        user = accessor.create_user(validated_data)
        return JsonResponse(user, status=201)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def update_profile(request, id):
    if not request.method == 'PATCH':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        data = json.loads(request.body)
        validated_data = bussiness.validate_data_update(data=data, id=id)
        if not validated_data:
            return JsonResponse({"message": "User doesnot exists"}, status=400)
        updated_user = accessor.update_user(validated_data, id)
        return JsonResponse(updated_user, status=201)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def get_user_profile_by_id(request, id):
    if not request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        user = accessor.get_user_by_id(id)
        if not user:
            return JsonResponse({"message": "User doesnot exists"}, status=404)
        return JsonResponse(user, status=200)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def get_user_profile_by_username(request, username):
    if not request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        user = accessor.get_user_by_username(username)
        if not user:
            return JsonResponse({"message": "User doesnot exists"}, status=404)
        return JsonResponse(user, status=200)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)


@csrf_exempt
def delete_user(request, id):
    if not request.method == 'DELETE':
        return JsonResponse({"message": "Method not allowed"}, status=400)
    try:
        user = accessor.get_user_by_id(id)
        if not user:
            return JsonResponse({"message": "User doesnot exists"}, status=404)
        accessor.delete_user(id)
        return JsonResponse(user, status=204)
    except:
        return JsonResponse({'message': 'Server Error'}, status=500)
