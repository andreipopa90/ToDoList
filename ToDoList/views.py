from django.http import HttpResponse
from django.shortcuts import render, redirect

from ToDoList.models import Task
from ToDoList.taskform import TaskForm


# Create your views here.


def list_tasks(request):
    # Lists all the tasks
    if request.method == 'GET':
        my_tasks = Task.objects.all().values()
        context = {
            'myTasks': my_tasks
        }
        # Return the webpage and set as context the list of tasks
        # The context is used to show the tasks on the webpage
        return render(request, template_name='ToDoList/listAllTasks.html', context=context)


def load_new_task_page(request):
    # Load the HTML page to create a new task
    if request.method == 'GET':
        page_form = TaskForm()
        context = {
            'form': page_form
        }
        # Return the webpage and set as context the form which will be used to collect the data for the new task
        # The generated form is empty at first
        return render(request, template_name='ToDoList/newTask.html', context=context)


def add_task(request):
    # Adds a new task
    # The data of the task is found in the body of the request
    if request.method == 'POST':
        # Convert the body of the request into a TaskForm object
        # The returned body contains the data of the form
        requested_form = TaskForm(request.POST)
        if requested_form.is_valid():
            # Extract the data from the form and save the new Task into the db
            task_name = requested_form.cleaned_data['name']
            task_description = requested_form.cleaned_data['description']
            new_task = Task(name=task_name, description=task_description)
            new_task.save()
        # After the task was added, redirect to the home page
        return redirect('/')


def complete_task(request, task_id):
    # Sets the completed boolean field of a task to true
    if request.method == 'PUT':
        # Find the task by id and then update the completed field in the db
        task_to_complete = Task.objects.get(id=task_id)
        task_to_complete.completed = True
        task_to_complete.save()
        # Return HttpResponse('OK') because I do not want to load a new page
        # The main page will be refreshed in the scripts.js, CompleteTask function
        return HttpResponse('OK')


def delete_task(request, task_id):
    # Sets the deleted boolean field of a task to true
    # While the request should've been a DELETE, the data is not removed from the db, so I decided to make it a PUT
    if request.method == 'PUT':
        # Find the task by id and then update the completed field in the db
        task_to_delete = Task.objects.get(id=task_id)
        task_to_delete.deleted = True
        task_to_delete.save()
        # Return HttpResponse('OK') because I do not want to load a new page
        # The main page will be refreshed in the scripts.js, DeleteTask function
        return HttpResponse('OK')


def erase_data(request):
    # Delete all tasks
    # Used to clean the mock data from the db using the webpage
    if request.method == 'DELETE':
        Task.objects.all().delete()
        # Return HttpResponse('OK') because I do not want to load a new page
        # The main page will be refreshed in the scripts.js, RemoveAllData function
        return HttpResponse('OK')
