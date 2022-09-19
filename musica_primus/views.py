from django.shortcuts import render

def musica_primus(request):
    return render(request, 'musica_primus.html', {})