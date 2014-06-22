from django import forms
from babypage.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('babythere',)
        widgets = {
            'babythere': forms.RadioSelect
        }

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class ProfileForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         # magic
#         self.user = kwargs['instance'].user
#         user_kwargs = kwargs.copy()
#         user_kwargs['instance'] = self.user
#         self.uf = UserForm(*args, **user_kwargs)
#         # magic end
#
#         super(ProfileForm, self).__init__(*args, **kwargs)
#
#         self.fields.update(self.uf.fields)
#         self.initial.update(self.uf.initial)
#
#         # define fields order if needed
#         self.fields.keyOrder = (
#             'last_name',
#             'first_name',
#             'second_name',
#
#             'birthdate',
#             'position',
#             'contacts',
#
#             'about',
#         )
#
#     def save(self, *args, **kwargs):
#         # save both forms
#         self.uf.save(*args, **kwargs)
#         return super(ProfileForm, self).save(*args, **kwargs)
#
#     class Meta:
#         model = Profile