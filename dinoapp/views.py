from django.shortcuts import render
from .models import Fossil, Meteor, Mineral, Rock

# Create your views here.
def fossil_view(request):

    fossils = Fossil.objects.order_by('classification').all()
    minerals = Mineral.objects.order_by('classification').all()
    meteors = Meteor.objects.order_by('classification').all()
    rocks = Rock.objects.order_by('classification').all()

    info = {
        'fossils': fossils,
        'fossils_size': len(fossils),
        'minerals': minerals,
        'minerals_size': len(minerals),
        'meteors': meteors,
        'meteors_size': len(meteors),
        'rocks': rocks,
        'rocks_size': len(rocks)
    }

    return render(request, 'index.html', info)