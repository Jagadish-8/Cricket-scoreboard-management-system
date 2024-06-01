from django.shortcuts import render, HttpResponse, redirect
from .models import Match, Team, Player, Score
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def newsandupdates(request):
    return HttpResponse("News and updates page")
    
def about(request):
    return HttpResponse("About page called")
    
def contact(request):
    return HttpResponse("Contact page called")
    
def help(request):
    return HttpResponse("Help page called")
    

def add_match(request):
    if request.method == "POST":
        match_number = request.POST.get('match_number')
        match_location = request.POST.get('match_location')
        match = Match(match_number=match_number, match_location=match_location)
        match.save()

        request.session['match_number'] = match_number
        request.session['match_location'] = match_location

        return redirect('add_team')
    else:
        return render(request, 'add_match.html')

def add_team(request):
    if 'match_number' in request.session and 'match_location' in request.session:
        match_number = request.session['match_number']
        match_location = request.session['match_location']
        del request.session['match_number']
        del request.session['match_location']

        team1_name = request.POST.get('team1_name')
        team1_coach = request.POST.get('team1_coach')
        team1_homeground = request.POST.get('team1_homeground')

        team = Team(team)

        return render(request, 'add_team.html', {'match_number': match_number, 'match_location': match_location})

    else:
        messages.error(request, 'Please add match number and location first.')
        return redirect('add_match')
