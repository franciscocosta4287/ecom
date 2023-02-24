from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("Helo")
    return render(request,"app/index.html")