from django.db import models
from django.forms import ModelForm

class Note(models.Model):
    to_person = models.CharField(max_length=100)
    from_person = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    subject = models.CharField(max_length=200)
    note_body = models.TextField()

    def __str__(self):
        return self.subject
        
class NoteForm(ModelForm):
    class Meta:
        model = Note

