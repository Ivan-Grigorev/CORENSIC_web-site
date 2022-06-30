from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CorensicSiteGuestVisitStatistic, CorensicSiteGuestsInfo, CorensicSiteErrorsStatistic

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
                                 interested_service=request.POST.get('interested-service'),
                                 guests_project_description=request.POST.get('project-description'))
        record.save()
        return render(request, template_name='homepage.html')


class Error400Page(TemplateView):
    model = CorensicSiteErrorsStatistic
    template_name = 'errors_views/error_view.html'

    def get(self, request, *args, **kwargs):
        record = self.model(guests_ip=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().ip,
                            guests_location=[ipinfo.getHandler('c3ef7fe9b908a3').getDetails().city,
                                             ipinfo.getHandler('c3ef7fe9b908a3').getDetails().country_name],
                            guests_hostname=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().hostname,
                            error_400=True)
        record.save()
        return render(request, template_name='errors_views/400.html', status=400)


class Error403Page(TemplateView):
    model = CorensicSiteErrorsStatistic
    template_name = 'errors_views/error_view.html'

    def get(self, request, *args, **kwargs):
        record = self.model(guests_ip=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().ip,
                            guests_location=[ipinfo.getHandler('c3ef7fe9b908a3').getDetails().city,
                                             ipinfo.getHandler('c3ef7fe9b908a3').getDetails().country_name],
                            guests_hostname=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().hostname,
                            error_403=True)
        record.save()
        return render(request, template_name='errors_views/403.html', status=403)


class Error404Page(TemplateView):
    model = CorensicSiteErrorsStatistic
    template_name = 'errors_views/error_view.html'

    def get(self, request, *args, **kwargs):
        record = self.model(guests_ip=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().ip,
                            guests_location=[ipinfo.getHandler('c3ef7fe9b908a3').getDetails().city,
                                             ipinfo.getHandler('c3ef7fe9b908a3').getDetails().country_name],
                            guests_hostname=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().hostname,
                            error_404=True)
        record.save()
        return render(request, template_name='errors_views/404.html', status=404)


class Error500Page(TemplateView):
    model = CorensicSiteErrorsStatistic
    template_name = 'errors_views/error_view.html'

    def get(self, request, *args, **kwargs):
        record = self.model(guests_ip=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().ip,
                            guests_location=[ipinfo.getHandler('c3ef7fe9b908a3').getDetails().city,
                                             ipinfo.getHandler('c3ef7fe9b908a3').getDetails().country_name],
                            guests_hostname=ipinfo.getHandler('c3ef7fe9b908a3').getDetails().hostname,
                            error_500=True)
        record.save()
        return render(request, template_name='errors_views/500.html', status=500)
