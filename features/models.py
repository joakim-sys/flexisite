from django.db import models
from wagtail.admin.panels import FieldPanel, FieldRowPanel
from modelcluster.fields import ParentalKey


class Feature(models.Model):
    name = models.CharField(
        max_length=50, help_text="Feature name should be about 2 words"
    )
    icon = models.CharField(
        max_length=30, null=True, blank=True, help_text="Such as ri-store-line"
    )
    color = models.CharField(
        max_length=20, null=True, blank=True, help_text="Such as #e80368"
    )
    page = ParentalKey(
        "home.HomePage",
        related_name="features",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel("name"),
        FieldRowPanel(
            [FieldPanel("icon"), FieldPanel("color")], heading="Feature Icon"
        ),
        FieldPanel("link"),
    ]
