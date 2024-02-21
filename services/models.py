from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel


class Service(models.Model):
    icon = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter the icon code for this service. This field uses Boxicons, and you can find a variety of icons with the class "bx". For example, use "bx-world" for a world icon. Leave it blank if no icon is needed.',
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Provide a title for the service",
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Enter a brief description of the service.",
    )
    link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Choose a page to link to when users interact with this service.",
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
