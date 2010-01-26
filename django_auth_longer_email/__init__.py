from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

if User._meta.local_fields[4].name == 'email':
    User._meta.local_fields[4] = models.EmailField(_('e-mail address'), blank=True, max_length=254)
    User._meta.local_fields[4].set_attributes_from_name('email')

    #This works too... but either way, we had to assume that the 4th field was email.
    #The problem with this method is that the email field is now created at the end
    #of the table, which is valid, but not elegant.
    #del User._meta.local_fields[4]
    #email = models.EmailField(_('e-mail address'), blank=True, max_length=254)
    #email.contribute_to_class(User, 'email')
else:
    raise Exception('Could not find the email field in the django User object!')

