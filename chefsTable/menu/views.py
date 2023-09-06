from django.shortcuts import render
from django.http import HttpResponse
from menu.forms import LogForm

# Create your views here.
def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle',
        'falafel': 'Falafel are deep fried patties',
        'cheesecake': 'Cheesecake is a type of desert',
    }

    description = items[dish]

    return HttpResponse(f"<h2>{dish}</h2>" + description)

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)