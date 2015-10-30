from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views import generic
from django.core.mail import send_mail
from django.shortcuts import render
from . import models
from .forms import ContactForm
from .models import Profile


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
    
def contactUs(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message =None
    
    if request.method == 'POST' and form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['last_name']
        subject = "thank you fo your preorder"
        messages = '%s%s' %(comment, name)
        from_email = form.cleaned_data['email']
        to_us = [settings.EMAIL_HOST_USER]
        print subject, messages, from_email, to_us
        send_mail(subject, messages, from_email, to_us, fail_silently = True)
        title = "thank you"
        confirm_message = '''
        Thanks for your message. We will answer as soon as possible.
        '''
        form = None
    context = {
            'title': title,
            'form':form,
            'confirm_message':confirm_message
        }
        
    # context = locals()
    template = 'contact.html'
    return render(request, template, context)

@login_required
def user_profile(request):
	if request.user.is_authenticated():
		user = request.user
	else:
		user = None
	context = {'user': user}
	template = 'profile.html'
	return render(request, template, context)




