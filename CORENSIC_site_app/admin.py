from django.contrib import admin

from .models import CorensicSiteGuestVisitStatistic, CorensicSiteGuestsInfo, CorensicSiteErrorsStatistic


class AdminCorensicSiteGuestVisitStatistic(admin.ModelAdmin):
    model = CorensicSiteGuestVisitStatistic
    list_display = ('guests_ip', 'guests_location', 'guests_hostname', 'record_date')


class AdminCorensicSiteGuestsInfo(admin.ModelAdmin):
    model = CorensicSiteGuestsInfo
    list_display = ('guests_name', 'guests_email', 'interested_service', 'guests_project_description', 'record_date')


class AdminCorensicSiteErrorsStatistic(admin.ModelAdmin):
    model = CorensicSiteErrorsStatistic
    list_display = ('guests_ip', 'guests_location', 'guests_hostname',
                    'error_400', 'error_403', 'error_404', 'error_500', 'record_date')


admin.site.register(CorensicSiteGuestVisitStatistic, AdminCorensicSiteGuestVisitStatistic)
admin.site.register(CorensicSiteGuestsInfo, AdminCorensicSiteGuestsInfo)
admin.site.register(CorensicSiteErrorsStatistic, AdminCorensicSiteErrorsStatistic)
