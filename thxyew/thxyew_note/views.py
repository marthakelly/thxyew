from django.shortcuts import render_to_response
from thxyew_note.models import Note, Author, NoteForm
from django.template import RequestContext

def index(request):
    all_notes = Note.objects.all().order_by('-pub_date')
    template_data = {'notes' : all_notes}

    return render_to_response('index.html', template_data)
    
def write_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NoteForm()

    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response('write-note.html', variables)