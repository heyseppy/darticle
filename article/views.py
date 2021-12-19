from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import rsa

def view_article(request, pk):
    selectedArticle = Article.objects.get(id = pk)
    articleText = selectedArticle.article_text 
    return HttpResponse(articleText)

def create_author(request):
    KEY_LENGTH = 2048
    publickey, privatekey = rsa.newkeys(KEY_LENGTH)
    response = {
        "author": str(publickey).replace("PublicKey(", "").replace(")", ""),
        "reader": str(privatekey).replace("PrivateKey(", "").replace(")", ""),
    }
    return JsonResponse(response)
