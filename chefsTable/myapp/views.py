from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    path = request.path
    schema = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Schema: {schema}
        <br>Method: {method}
        <br>User Agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')