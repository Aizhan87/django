from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.

# def menuitems(request):
#     menuitem = {'mains':[
#         {'name': 'falafel', 'price': '12'},
#         {'name': 'shawarma', 'price': '15'},
#         {'name': 'gyro', 'price': '10'},
#         {'name': 'humus', 'price': '5'},
#     ]}
#     return render(request, 'menu.html', menuitem)

def menu_by_id(request): 
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)