from django.db import models
from django.utils.translation import gettext_lazy as _


class Principle(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=250,
    )
    content = models.TextField(
        _("Content"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Principle")
        verbose_name_plural = _("Principles")


class Value(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=250,
    )
    content = models.TextField(
        _("Content"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Value")
        verbose_name_plural = _("Values")
