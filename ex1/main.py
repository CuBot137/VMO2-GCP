from flask import request, jsonify
import functions_framework

@functions_framework.http
def ex1(request):
    method = request.method

    if method == 'GET':
        return handle_get(request)
    elif method == 'POST':
        return handle_post(request)
    elif method == 'DELETE':
        return handle_delete(request)
    else:
        return ('Unkown method', 405)


def handle_get(request):
    response = {
        'message': 'This is a GET request',
        'status': 'Success'
    }

def handle_post(request):
    response = {
        'message': 'This is a POST request',
        'status': 'Success'
    }

def handle_delete(request):
    response = {
        'message': 'This is a DELETE request',
        'status': 'Success'
    }