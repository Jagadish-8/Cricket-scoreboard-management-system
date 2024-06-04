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
#     if request.method == "POST":
#         match_number = request.POST.get('match_number')
#         match_location = request.POST.get('match_location')
#         match = Match(match_number=match_number, match_location=match_location)
#         match.save()

# #         request.session['match_number'] = match_number
# #         request.session['match_location'] = match_location

# #         return redirect('add_team')
# #     else:
# #         return render(request, 'add_match.html')

# # def add_team(request):
# #     if 'match_number' in request.session and 'match_location' in request.session:
# #         match_number = request.session['match_number']
# #         match_location = request.session['match_location']
# #         del request.session['match_number']
# #         del request.session['match_location']


#         team1_name = request.POST.get('team1_name')
#         team1_coach = request.POST.get('team1_coach')
#         team1_homeground = request.POST.get('team1_homeground')
#         team_number = request.POST.get('team_select')

#         team1 = Team(team_name = team1_name, team_coach = team1_coach, team_homeground = team1_homeground, match_number = match_number, team_number = team_number)
#         team1.save()

#         for i in range(1, 4):
#             player_name = request.POST.get(f'player{i}_team1')
#             if player_name:
#                 player = Player(player_team = team1, player_name = player_name)
#                 player.save()

#         team2_name = request.POST.get('team2_name')
#         team2_coach = request.POST.get('team2_coach')
#         team2_homeground = request.POST.get('team2_homeground')
#         team_number = request.POST.get('team_select')

#         team2 = Team(team_name = team2_name, team2_coach = team2_coach, team_homeground = team2_homeground, match_number = match_number, team_number = team_number)
#         team2.save()

#         for i in range(1, 4):
#             player_name = request.POST.get(f'player{i}_team2')
#             if player_name:
#                 player = Player(player_team = team2, player_name = player_name)
#                 player.save()

        return render(request, 'add_match.html')

    # else:
    #     return redirect('add_match')
