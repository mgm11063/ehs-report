from django.db import models


class CreatedAndUpdateModel(models.Model):
    """타임스탬프 코어 모델"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
