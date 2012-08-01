from django.shortcuts import render_to_response
from thxyew_note.models import Note, Author

def index(request):
    all_notes = Note.objects.all().order_by('-pub_date')
    template_data = {'notes' : all_notes}

    return render_to_response('index.html', template_data)