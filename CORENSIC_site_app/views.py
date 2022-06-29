from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import CorensicSiteGuestVisitStatistic, CorensicSiteGuestsInfo

import ipinfo


class HomePage(TemplateView):
    model_visit = CorensicSiteGuestVisitStatistic
    model_info = CorensicSiteGuestsInfo
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        record = self.model_visit(guests_ip=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().ip,
                                  guests_location=[ipinfo.getHandler('c3ef7fe9b908a3').getDetails().city,
                                                   ipinfo.getHandler('c3ef7fe9b908a3').getDetails().country_name],
                                  guests_hostname=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().hostname)

        record.save()
        return render(request, template_name='homepage.html')

    def post(self, request, *args, **kwargs):
        record = self.model_info(guests_name=request.POST.get('name'),
                                 guests_email=request.POST.get('email'),
                                 guests_project_description=request.POST.get('project-description'))
        record.save()
        return render(request, template_name='homepage.html')
