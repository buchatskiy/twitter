from django.shortcuts import render_to_response
from twitter.models import Twitter
from django.contrib import auth

def twit(request):
    return render_to_response('twit.html',{'text':Twitter.objects.all(),'username':auth.get_user(request).username})
