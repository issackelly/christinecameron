from django import forms
from form_utils.forms import BetterModelForm

from rsvp.models import Rsvp

class RsvpForm(BetterModelForm):
    dinner_dancing = forms.TypedChoiceField(
        coerce=int,
        choices=((0, 'No'), (1, 'Yes')),
        widget=forms.RadioSelect,
        label="Will you be joining us on February 4th?"
    )

    class Meta:
        model = Rsvp
        fieldsets = [
            ("", {"fields":
                ["invitation_name", "dinner_dancing", "email", "comments"], "legend": ""
            }),
        ]
