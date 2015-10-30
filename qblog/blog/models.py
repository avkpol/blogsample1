from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from allauth.account.signals import user_logged_in, user_signed_up
# import stripe


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
        
 
 
        

# stripe.api_key = settings.STRIPE_SECRET_KEY

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	name = models.CharField(max_length=120)
	description = models.TextField(default='My description', null=True, blank=True)


	def __unicode__(self):
		return self.name


# class UserStripe(models.Model):
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL)
# 	stripe_id = models.CharField(max_length=200, null=True, blank=True)
# 
# 	def __unicode__(self):
# 		if self.stripe_id:
# 			return str(self.stripe_id)
# 		else:
# 			return self.user.username
# 
# 
# def stripe_callback(sender, request, user, **kwargs):
# 	user_stripe_account, created = UserStripe.objects.get_or_create(user=user)
# 	if created:
# 		print "created for %s" %(user.username)
# 
# 	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
# 		new_stripe_id = stripe.Customer.create(email=user.email)
# 		user_stripe_account.stripe_id = new_stripe_id['id']
# 		user_stripe_account.save()
# 
# 
# 
def profile_callback(sender, request, user, **kwargs):
	profile, is_created = Profile.objects.get_or_create(user=user)
	if is_created:
		profile.name = user.username
		profile.save() 
# 
# 
# user_logged_in.connect(stripe_callback)
# user_signed_up.connect(stripe_callback)
user_signed_up.connect(profile_callback)
#         
