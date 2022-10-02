from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from matplotlib.pyplot import title
# Create your views here.

monthly_challenges_values = {
    "january" : "Wake up early every morning!",
    "february" : "Go to bed early everynight!",
    "march" : "Study at least 1hour every day!",
    "april" : "Do Exercise every day!",
    "may"  : "Wake up early every morning!",
    "june" : "Go to bed early everynight!",
    "july" :  "Study at least 1hour every day!",
    "august": "Do Exercise every day!",
    "september" : "Wake up early every morning!",
    "october" :"Go to bed early everynight!",
    "november" : "Study at least 1hour every day!",
    "december": None
} 
def index(request):
    months = list(monthly_challenges_values.keys())
    return render(request,'list.html',{"months":months})

def number_month(request,month):
    months = list(monthly_challenges_values.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Page")
    result = months[month-1]
    redirect_path = reverse("month-challenge",args = [result])
    return HttpResponseRedirect(redirect_path)

def string_month(request,month):
    try:
        
        content = monthly_challenges_values[month]
        return render(request,'challenges.html',{"title":month, "text": content})
    except:
        raise Http404

