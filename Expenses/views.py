from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.template import RequestContext
from django.views.generic import ListView
from receipts.models import Receipt

__author__ = 'dreiMac'
from django.contrib.auth import logout
from django.shortcuts import redirect, render_to_response


def logout_view(request):
    logout(request)
    return redirect("/login?next=/")

@login_required
def view_expenses(request):
    user = request.user
    participations = user.participations.all().select_related('project')
    receipts = Receipt.objects.filter(participation__in=participations)
    return  render_to_response('expenses_home.html',
                               {'participations': participations, 'receipts': receipts },
                               context_instance=RequestContext(request))