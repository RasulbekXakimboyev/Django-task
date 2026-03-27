from django.shortcuts import render

# 1. Functions based views
# 2. Class based views

def bosh_sahifa(request):
    context = {
        "username": "Ali",
        "is_admin": True,
        "title": "Django + Jinja darsi",
        "tech_list": ["Python", "Django", "HTML", "CSS", "JavaScript"],
    }
    return render(request, "index.html", context)
