from django.shortcuts import render_to_response
from thxyew_note.models import Note, NoteForm
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    all_notes = Note.objects.all().order_by('-pub_date')
    return render_to_response('index.html', {'all_notes': all_notes}, context_instance=RequestContext(request))
    
def write_note(request):
    form = NoteForm()

    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response('write-note.html', variables, context_instance=RequestContext(request))

def submit_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NoteForm()    

    variables = RequestContext(request, {
        'form': form
    })
    
    return render_to_response('write-note.html', variables, context_instance=RequestContext(request))

def single_note(request, pk):
    note = Note.objects.get(pk=pk)
    return render_to_response('note.html', {'single_note': note}, context_instance=RequestContext(request))
    