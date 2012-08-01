from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=64)
    twitter = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Note(models.Model):
    to_person = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField()
    subject = models.CharField(max_length=200)
    note_body = models.TextField()

    def __str__(self):
        return self.subject