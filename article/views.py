from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import rsa

def index(request):
    return HttpResponse("Hello User, this is an article.")

def create_author(request):
    KEY_LENGTH = 2048
    publickey, privatekey = rsa.newkeys(KEY_LENGTH)
    response = {
        "author": str(publickey).replace("PublicKey(", "").replace(")", ""),
        "reader": str(privatekey).replace("PrivateKey(", "").replace(")", ""),
    }
    return JsonResponse(response)
