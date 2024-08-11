from django.contrib import admin

from .views import *
from . models import ContactMessage

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
# admin.site.register(Client)
admin.site.register(ContactMessage)
