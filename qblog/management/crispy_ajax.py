"""need to istall django-jsonview
	pip install django-jsonview
"""

from crispy_forms.utils import render_crispy_form

@json_view
def save_example_form(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # You could actually save through AJAX and return a success code here
        form.save()
        return {'success': True}

    # RequestContext ensures CSRF token is placed in newly rendered form_html
    request_context = RequestContext(request)
    form_html = render_crispy_form(form, context=request_context)
    return {'success': False, 'form_html': form_html}