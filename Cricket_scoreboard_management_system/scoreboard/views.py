from django.shortcuts import render, HttpResponse

# Create your views here.

class HomePage:
    def index(self, request):
        return render(request, 'index.html')
