from enum import auto
from django.db import models
from django.conf import settings


class TinyStore(models.Model):
    key = models.CharField(max_length=32, primary_key=True)
    value = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    # delete all tinystores
    def clear():
        TinyStore.objects.all().delete()

    # delete a given tinystore
    def delete(key):
        TinyStore.objects.filter(key=key).delete()

    # does a tinystore exist?
    def exists(key):
        return TinyStore.objects.filter(key=key).count() > 0

    # retrieves the value of a tinystore, returns a default if it doesn't exist
    def get(key):
        ts = TinyStore.objects.filter(key=key).first()
        return ts.value if ts else getattr(settings, "TINY_STORE", {}).get(key, {})

    # list all the available tinystores
    def keys():
        return list(
            TinyStore.objects.all().order_by("key").values_list("key", flat=True)
        )

    # write a tinystore to the database
    def set(key, value):
        ts = TinyStore.objects.filter(key=key).first()
        if ts is None:
            ts = TinyStore(key=key, value=value)
        else:
            ts.value = value
        ts.save()
