from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AcadInfo
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.

def index(request):   
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "gradstud/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "gradstud/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "gradstud/login.html")

def logout_view(request):
    logout(request)
    return render(request, "gradstud/login.html", {
                "message": "Logged Out"
            })

def addinfo(request):
    if request.method == "POST":
        form = request.POST
        obj = AcadInfo()
        obj.uid = request.user.id
        obj.firstname = request.user.first_name
        obj.lastname = request.user.last_name
        obj.university = form.get("unis")
        obj.ugmajor = form.get("major")
        obj.gpa = form["gpa"]
        obj.greq = form["greq"]
        obj.grev = form["grev"]
        obj.greawa = form["greawa"]
        obj.lor1n = form["lor1n"]
        obj.lor1 = form["lor1"]
        obj.lor2n = form["lor2n"]
        obj.lor2 = form["lor2"]
        obj.lor3n = form["lor3n"]
        obj.lor3 = form["lor3"]
        obj.wmonths = form["moe"]
        obj.wtype = form.get("type")
        obj.rmonths = form["moer"]
        obj.pubven = form.get("pubven")
        obj.score = calc_score(form)
        obj.save()
        return render(request, "gradstud/index.html")
    return render(request, "gradstud/addinfo.html")

def calc_score(form):
    uni_score = int(form.get("unis"))*4
    major_score = int(form.get("major"))*3.3*4
    greq_score = int(form["greq"])/5
    grev_score = int(form["grev"])/5
    greawa_score = int(form["greawa"])/5
    lor1_score = calc_lor_score(form["lor1"], form["lor1n"])
    lor2_score = calc_lor_score(form["lor2"], form["lor2n"])
    lor3_score = calc_lor_score(form["lor3"], form["lor3n"])
    wmonths_score = int(form.get("moe"))
    wtype_score = int(form.get("type"))*2.5*2
    rmonths_score = int(form["moer"])*3
    pubven_score = int(form.get("pubven"))*2.5*4
    raw_score = (uni_score+major_score+greq_score+grev_score+greawa_score+lor1_score+lor2_score+lor3_score+wmonths_score+wtype_score+rmonths_score+pubven_score)/41
    return raw_score

def calc_lor_score(emailid, fullname):
    edomain = re.search("\@(.*)", emailid).group(1)
    fname = fullname.split()[0]
    lname = fullname.split()[1]
    URL = "https://scholar.google.com/citations?view_op=search_authors&mauthors="+fname+" "+lname+" "+edomain
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='gs_ai_cby')
    citations = int(results.prettify().splitlines()[1].split()[2])
    if (10 < citations <= 100):
        return 1
    elif (100 < citations <= 1000):
        return 2
    elif (1000 < citations <= 2000):
        return 3
    elif (2000 < citations <= 3000):
        return 4
    elif (3000 < citations <= 4000):
        return 5
    elif (4000 < citations <= 5000):
        return 6
    elif (5000 < citations <= 6000):
        return 7
    elif (6000 < citations <= 7000):
        return 8
    elif (7000 < citations <= 8000):
        return 9
    elif (8000 < citations):
        return 10
    else:
        return 1


