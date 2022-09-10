import os
from sqlite3 import Timestamp
from uuid import uuid4
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.conf import settings
from .models import Search
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from utils.search_utils import search_one_face_from_file

def index(request):
    return redirect('search')
    return HttpResponse("Hello, world. You're at the facer index.")

# @login_required
def search(request):
    recent = []
  
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
  
        if form.is_valid():
            search_entry = form.save()
            search_entry.uuid = uuid4()
            search_entry.user = request.user
            res = search_one_face_from_file(search_entry.search_img.path, settings.FACE_CONFIG['tolerance'], settings.LABELLED_FACES)
            search_entry.results = res[:50]
            search_entry.save()
            print(len(res))
            print(res)
            return redirect('/results/%s/' % search_entry.uuid)
    else:
        recent = Search.objects.all().order_by("-timestamp")[:10]
        form = SearchForm()
    return render(request, 'search.html', {'form' : form, "recent": recent})

# @login_required
def results(request, token):
    search_entry = Search.objects.get(uuid=token)
    results = [{
        "path": os.path.join("/media/thumbs", ("_".join(x.split("_")[:-1]).replace("/", "_"))),
        "date": x.split("/")[-2],
        "name": x.split("/")[-1]
        } for x in search_entry.results]
    return render(request, 'results.html', {'search' : search_entry, "config": settings.FACE_CONFIG, "results": results})

# @login_required
def protected_serve(request, path):
    # name = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(name):
    #     return serve(request, path, settings.MEDIA_ROOT)
    return serve(request, path, settings.MEDIA_ROOT)

# from scripts.thumbnail_gen import handle
# handle("/media/melman/Legacy/0 G/OLD PHOTOS", "/home/melman/face-search/backend/media/thumbs")