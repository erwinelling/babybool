from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from babypage.forms import UserProfileForm

def home(request):
    # url = request.user.profile.url
    user = request.user
    return render_to_response('home.html',
                              {},
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    # url = request.user.profile.url

    if request.method == 'POST': # If the form has been submitted...
        form = UserProfileForm(request.POST, instance=request.user.profile)
        # form = UserProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
    else:
        form = UserProfileForm(instance=request.user.profile) # An unbound form
    
    return render_to_response('profile.html',
                              {
                                  'form': form,
                              },
                              context_instance=RequestContext(request))