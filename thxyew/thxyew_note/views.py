from django.shortcuts import render_to_response
from thxyew_note.models import Note, NoteForm
from django.template import RequestContext
from django.http import HttpResponseRedirect

def index(request):
    all_notes = Note.objects.all().order_by('-pub_date')
    return render_to_response('index.html', {'all_notes': all_notes})
    
def write_note(request):
    form = NoteForm()

    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response('write-note.html', variables)

def submit_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NoteForm()    

    return HttpResponseRedirect('/write-note')

def single_note(request, pk):
    #t = get_template('post.html')
    #html = t.render(RequestContext(request,{'post': BlogPost.objects.get(id = pk)}))
    #return HttpResponse(html)
    note = Note.objects.get(pk=pk)
    return render_to_response('note.html', {'single_note': note})
    