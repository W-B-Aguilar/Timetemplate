from django.shortcuts import render, HttpResponse, redirect




def index(request):
    context = {
    
        "email" : "blog@gmail.com",
        "name" : "mike"
    
    }
    return render(request, 'timedisplay/something.html',context)
    






#  context = {
#         "email" : "blog@gmail.com",
#         "name" : "mike"
#     }
#     return render(request, "ourApp/index.html", context)
  

    