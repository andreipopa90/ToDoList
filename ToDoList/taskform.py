from django import forms


class TaskForm(forms.Form):
    # The form used for adding a new task
    name = forms.CharField(label='Task Name', max_length=255)
    description = forms.CharField(label='Task Description', max_length=2000)
