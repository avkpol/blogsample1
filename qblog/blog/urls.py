
from django.conf.urls import patterns, include, url
from django.conf.urls import patterns, url
from . import views, feed
from checkout.views import checkout
from management import load_fixture, create
# # from management.user import create_model
# # from blog import views
# from management import forms
# from management.models.user_model import UserDataForm
# from management import autofillform_view

urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$',views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^contact/$', views.contactUs, name="contact"),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^checkout/$',checkout, name='checkout'),
    # url(r'^create/$',load_fixture.load_fixture1, name='create'),
    # url(r'^create/$',create.model_from_json, name='create'),
    # url(r'^edit/$',create.FormUpdate().edit, name='create'),
    # url(r'^autofill/$',autofillform_view.test_dict, name='autofill'),
    # url(r'^create/$',create_model, name='create'),
    # url(r'^create/$',UserDataForm().populate_form, name='create'),
    # url(r'^sessions/$',test, name='test'),
    # url(r'^sessions/$',Test().process_request, name="index"),
    # url(r'^create/$',forms.ContactForm, name='create'),
    url(r'^create/$', 'management.create.form_edit', {}, name='create'),
    url(r'^(?P<id>\d+)/$', 'management.create.form_edit', {}, name='create'),
    
)
