from django.contrib import admin
from rsvp.models import Rsvp

class RsvpAdmin(admin.ModelAdmin):
    list_display = ["invitation_name", "email", "dinner_dancing"]
    list_filter = ["dinner_dancing",]

admin.site.register(Rsvp, RsvpAdmin)
