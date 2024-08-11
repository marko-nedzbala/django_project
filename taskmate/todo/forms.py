from django import forms
from todo.models import TaskList

# field to edit
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
        




