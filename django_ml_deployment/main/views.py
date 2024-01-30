from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "index.html")


def user_form(request):
    if request.method == "POST":
        username = request.POST['username']
        context = {'name': username}
        
        return render(request, "index.html", context=context)
    else:
        context = {}

    return render(request, "user.html", context=context)