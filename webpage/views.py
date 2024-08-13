from django.shortcuts import render, HttpResponse

# Create your views here.
def indexPage(request):
    return render(request, "index.html")

def aboutUs (request):
    return render(request, "about.html")

def contactUs (request):
    return render(request, "contact.html")

def forPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'for_test.html',context)

def cardPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, "card.html", context)

def CardcolorPage(request):
    context = {
        'color': 'all',
        
    }
    
    if request.method == "GET" and request.GET.get('color') != None :
        context['color'] = request.GET['color']
        
    return render(request, 'card_color.html', context)