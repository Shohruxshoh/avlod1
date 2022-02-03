from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Courses, Post, Team
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_language, gettext
# Create your views here.

def TeamsView(request):
    teams = Team.objects.all().order_by('-created')[:4]
    courses = Courses.objects.all().order_by('-created')[:3]
    posts = Post.objects.all().order_by('-created')[:3]
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    trans = translate(language='ru')
    context = {'teams':teams, 'courses':courses, 'posts':posts, 'trans':trans}
    return render(request, 'index.html', context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text