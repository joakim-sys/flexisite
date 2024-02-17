from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel


class Service(models.Model):
    icon = models.CharField(
        max_length=100, help_text="Icon such as bx-world", null=True, blank=True
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    page = ParentalKey(
        "home.HomePage",
        related_name="services",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("icon"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("link"),

    ]
