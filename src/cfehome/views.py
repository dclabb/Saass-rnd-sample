import pathlib
from django.shortcuts import render #for template
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0
    my_title = "My Page"
    my_context = {
        "page_title" : my_title,
        "page_visit_count" : page_qs.count(),
        "percent" : percent,
        "total_visit_count" : qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path) #it creates stamp automatically for the row, and the path is like the resume
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title" : my_title
    }
    html_ = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{page_title} anything?</h1>
</body>
</html>
""".format(**my_context)
    return HttpResponse(html_)

https://www.youtube.com/watch?v=WbNNESIxJnY&t=30284s