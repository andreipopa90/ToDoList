from django.test import TestCase, RequestFactory

import ToDoList.views as views
from ToDoList.models import Task


class TodoListTest(TestCase):
    def setUp(self) -> None:
        # Create a RequestFactory object
        # The database used in unittests is a mock one created by Django
        # Populate the database with 3 tasks
        self.factory = RequestFactory()
        Task.objects.create(name='Task 1', description='Task description 1')

        task_to_delete = Task(name='Task d', description='Task to delete')
        task_to_delete.save()

        task_to_complete = Task(name='Task c', description='Task to complete')
        task_to_complete.save()

    def test_list_tasks(self):
        # Send a request to list all the tasks
        request = self.factory.get('')
        response = views.list_tasks(request)
        # Check if the contents of the page contain all initial tasks from the db
        # Check if the response has status code 200
        self.assertIn('Task to complete', str(response.content))
        self.assertIn('Task c', str(response.content))

        self.assertIn('Task to delete', str(response.content))
        self.assertIn('Task d', str(response.content))

        self.assertIn('Task description 1', str(response.content))
        self.assertIn('Task 1', str(response.content))
        self.assertEquals(response.status_code, 200)

    def test_delete_task(self):
        # Send a request to delete a task, by making the deleted field True
        task_to_delete_id = Task.objects.get(name='Task d').id
        # Check that at first it is not deleted, deleted field if False
        self.assertFalse(Task.objects.get(id=task_to_delete_id).deleted)
        request = self.factory.put('deleteTask/' + str(task_to_delete_id))
        response = views.delete_task(request, task_to_delete_id)
        # Check if the status code of the response is 200
        # Check if the updated task has now the deleted field True
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Task.objects.get(id=task_to_delete_id).deleted)

    def test_complete_task(self):
        # Send a request to complete a task, by making the completed field True
        task_to_complete = Task.objects.get(name='Task c')
        # Check that at first it is not completed, completed field if False
        self.assertFalse(task_to_complete.completed)
        request = self.factory.put('completeTask/' + str(task_to_complete.id))
        response = views.complete_task(request, task_to_complete.id)
        # Check if the status code of the response is 200
        # Check if the updated task has now the completed field True
        self.assertEquals(response.status_code, 200)
        self.assertTrue(Task.objects.get(id=task_to_complete.id).completed)

    def test_add_task(self):
        # Send a request to add a new task to the tasks list
        # Create a dictionary to mock the form data and include it in the request
        new_task = {'name': 'New Task', 'description': 'This is the new task'}
        request = self.factory.post('addTask', new_task)
        response = views.add_task(request)
        # Status code should be 302 because the method redirects to the home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')
        # Check whether the new task was added into the database
        self.assertIn(Task.objects.get(name='New Task'), Task.objects.all())

    def test_erase_all_tasks(self):
        # Send a request to erase all the data from the database
        request = self.factory.delete('eraseTasks')
        response = views.erase_data(request)
        # Check if status code is 200
        # Check if there are no tasks by comparing the length of the list of tasks to 0
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(Task.objects.all()), 0)
