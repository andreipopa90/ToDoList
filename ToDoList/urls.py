from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='My Tasks'),
    path('newTask/', views.load_new_task_page, name='New Task'),
    path('addTask/', views.add_task, name='My Tasks'),
    path('deleteTask/<int:task_id>', views.delete_task, name='My Tasks'),
    path('completeTask/<int:task_id>', views.complete_task, name='My Tasks'),
    path('eraseTasks/', views.erase_data, name='My Tasks'),
]
