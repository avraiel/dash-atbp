# HTTPResponse for webpages, JsonResponse for json output
from django.http import HttpResponse, JsonResponse

# django decorator so we don't need csrf tokens when making requests
from django.views.decorators.csrf import csrf_exempt

# This method is to be able to parse the JSON objects involved in create and update functions
from rest_framework.parsers import JSONParser

# To add to the views, you need to import the models and the serializers so they can be json objects
from snippets.models import Snippet, Employee
from snippets.serializers import SnippetSerializer, EmployeeSerializer

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    
    # apparently the code below is for updating a snippet but let's see how it goes
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

'''
After doing all of these, these views were put inside the urls of the app and then the project.
'''

@csrf_exempt
def employee_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    Employee.objects.get gets the employee data based on the employee_id variable, pk is the variable passed through the url.
    """
    try:
        employee = Employee.objects.get(employee_id=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=204)
