from django.db import models


# Communication type model
class CommunicationType(models.Model):
    tsid = models.CharField(max_length=36, db_index=True, blank=True)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=6)
    is_phone = models.BooleanField(default=False)
