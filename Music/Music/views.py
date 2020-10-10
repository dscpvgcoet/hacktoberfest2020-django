from django.http import HttpResponse
def index(request):
    return HttpResponse("<h2 align=+center>Hello,Welcome to Music app<h2>")