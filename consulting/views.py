from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from consulting.models import Practice

# Practices listing view
def index(request):
    practice = Practice.objects.all().order_by('id') 
    return render(request, 'practices/index.html', {'practice':practice}) 

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


# Consulting Dashboard
# /consulting/dashboard
# Voir les stats de thunes
# Voir ses prochains rendez-vous
# L'url n'est accesible qu'au praticien

#login_required
def dashboard(request):
    return HttpResponse("Hello, world. You're at the consulting dashboard.")


# /consulting/dashboard/edit
# Modifier son cabinet


# /consulting/dashboard/slots
# Générer des rendez-vous


# /consulting/dashboard/billing
# Voir ses facturations


# /consulting/dashboard/calendar
# Voir son calendrier de rendez-vous



# /consulting/dashboard/messages
# Voir ses messages