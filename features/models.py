from django.db import models
from wagtail.admin.panels import FieldPanel, FieldRowPanel
from modelcluster.fields import ParentalKey


class Feature(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a name for the feature.",
        verbose_name="Feature Name",
    )
    icon = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text="Enter the icon code for this feature. We are using Remix Icons (ri) URL: https://remixicon.com/, and you can find a list of icons on their website. Use icons such as 'ri-store-line'. Leave it blank if no icon is needed.",
    )
    color = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text=" Enter a color code for this feature, such as a hex value (e.g., ',  #e80368') or a color name (e.g., 'red'). Leave it blank if no specific color is needed.",
    )
    page = ParentalKey(
        "home.HomePage",
        related_name="features",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Choose a page to link to when users interact with this feature.",
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
