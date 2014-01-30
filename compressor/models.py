from django.db import models, IntegrityError

from compressor.conf import CompressorConf  # noqa


class ManifestEntry(models.Model):
    hexdigest = models.CharField(max_length="255", unique=True)
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    @staticmethod
    def create(**kwargs):
        try:
            ManifestEntry.objects.create(**kwargs)
        except IntegrityError:
            ManifestEntry.objects.filter(hexdigest=kwargs.get('hexdigest')).update(**kwargs)
