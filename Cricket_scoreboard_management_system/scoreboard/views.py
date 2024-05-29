from django.shortcuts import render, HttpResponse

# Create your views here.

class Pages:
    def index(self, request):
        return render(request, 'index.html')
    
    def newsandupdates(self, request):
        return HttpResponse("News and updates page")
    
    def about(self, request):
        return HttpResponse("About page called")
    
    def contact(self, request):
        return HttpResponse("Contact page called")
    
    def help(self, request):
        return HttpResponse("Help page called")
