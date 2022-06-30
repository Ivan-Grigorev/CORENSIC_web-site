from django.db import models


class CorensicSiteGuestVisitStatistic(models.Model):
    guests_ip = models.TextField(null=True)
    guests_location = models.TextField(null=True)
    guests_hostname = models.TextField(null=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guests_ip\
               or self.guests_location\
               or self.guests_hostname\
               or self.record_date

    class Meta:
        db_table = 'corensic_site_guest_visit_statistic'


class CorensicSiteGuestsInfo(models.Model):
    guests_name = models.TextField(null=True)
    guests_email = models.TextField(null=True)
    interested_service = models.TextField(null=True)
    guests_project_description = models.TextField(null=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guests_name\
               or self.guests_email\
               or self.interested_service\
               or self.guests_project_description\
               or self.record_date

    class Meta:
        db_table = 'corensic_site_guests_info'


class CorensicSiteErrorsStatistic(models.Model):
    guests_ip = models.TextField(null=True)
    guests_location = models.TextField(null=True)
    guests_hostname = models.TextField(null=True)
    error_400 = models.BooleanField(default=False)
    error_403 = models.BooleanField(default=False)
    error_404 = models.BooleanField(default=False)
    error_500 = models.BooleanField(default=False)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guests_ip\
               or self.guests_location\
               or self.guests_hostname\
               or self.error_400\
               or self.error_403\
               or self.error_404\
               or self.error_500\
               or self.record_date

    class Meta:
        db_table = 'corensic_site_errors_statistic'
