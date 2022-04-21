from django.shortcuts import render
from food_app.models import Chef, Gallery, Specials

def index(request):
    obj_special = Specials.objects.all()
    obj = Chef.objects.all()
    obj_1 = Gallery.objects.all()
    results = {
        'result': obj,
        'result_2': obj_1,
        'result_special':obj_special
    }
    return render(request, 'index.html', results)

