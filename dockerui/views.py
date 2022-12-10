from http.client import HTTPResponse
from django.http import HttpResponse

def error_404_view(request, exception):
    return HTTPResponse('Error handler content', status=404)
