from django.shortcuts import render_to_response
from twitter.models import Twitter, User
from django.contrib import auth
from django.core.paginator import Paginator






def twit(request, page_number=1):
    if 'q' in request.GET:
        t = Twitter()
        t.text = request.GET['q']
        try:
            user_name = User.objects.get(name=str(auth.get_user(request).username))
        except:
            user_name = User(name=str(auth.get_user(request).username))
            user_name.save()
        t.name = User.objects.get(name=str(auth.get_user(request).username))
        t.save()
    all_texts=Twitter.objects.all()
    current_page = Paginator(all_texts,4)
    return render_to_response('twit.html', {'text': current_page.page(page_number), 'username': auth.get_user(request).username})


def filter(request, onename):
    idname=User.objects.get(name=onename)
    return render_to_response('twit.html', {'text': Twitter.objects.all().filter(name=idname), 'username': auth.get_user(request).username})