from asyncio.log import logger
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from apps.consulting.models import Practice
from apps.consulting.documents import PracticeDocument

# Practices listing view
def index(request):
    practice = Practice.objects.all().order_by('id') 
    return render(request, 'practices/index.html', {'practice':practice}) 

def search(request):
    query = request.GET.get('q')
    localisation = request.GET.get('localisation')

    practices = PracticeDocument.search().query(
        'multi_match',
        query=query,
        fuzziness='5' # should be changed to improve search results
    )

    return render(request, 'practices/search.html', {
        'query': query,
        'localisation': localisation,
        'practices': practices,
    })

# Practice detail view
# On affiche les services
# On propose un calendar de slot pour lancer le process de réservation
# Un bouton contacter pour avoir le système de messagerie
def detail(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    context = {
        'practice': practice,
    }
    return render(request, 'practices/details.html', context)