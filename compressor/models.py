from django.db import models

from compressor.conf import CompressorConf  # noqa


class ManifestEntries(models.Model):
    key = models.CharField(max_length="256")
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
