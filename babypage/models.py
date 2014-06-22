from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
import hashlib
from django.utils.translation import ugettext_lazy as _

BOOL_CHOICES = ((True, _('Yes')), (False, _('No')))

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    # url = models.URLField("Website", blank=True)
    # company = models.CharField(max_length=50, blank=True)
    babythere = models.BooleanField(default=True, choices=BOOL_CHOICES)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
  
    # def account_verified(self):
    #     if self.user.is_authenticated:
    #         result = EmailAddress.objects.filter(email=self.user.email)
    #         if len(result):
    #             return result[0].verified
    #     return False
         
    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
 
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
 
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())
        
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         widgets = {
#             'babythere': forms.RadioSelect
#         }