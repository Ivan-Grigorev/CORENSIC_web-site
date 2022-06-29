from django.db import models


class CorensicSiteGuestVisitStatistic(models.Model):
    guests_ip = models.TextField(null=True)
    guests_location = models.TextField(null=True)
    guests_hostname = models.TextField(null=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guests_ip or self.guests_location or self.guests_hostname or self.record_date

    class Meta:
        db_table = 'corensic_site_guest_visit_statistic'


class CorensicSiteGuestsInfo(models.Model):
    guests_name = models.TextField(null=True)
    guests_email = models.TextField(null=True)
    guests_project_description = models.TextField(null=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guests_name or self.guests_email or self.guests_project_description or self.record_date

    class Meta:
        db_table = 'corensic_site_guests_info'
