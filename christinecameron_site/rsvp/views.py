from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from rsvp.models import Rsvp
from rsvp.forms import RsvpForm


def rsvp(request):
    # Handles the RSVP
    form = RsvpForm(request.POST or None)

    if form.is_valid():
        rsvp = form.save()

        messages.success(request, "Your RSVP was received.")
        return redirect("/")

    return render_to_response("rsvp/form.html", {
        "form": form
    }, context_instance=RequestContext(request))
