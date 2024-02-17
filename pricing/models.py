from django.db import models
from django import forms
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import MultiFieldPanel, FieldRowPanel, FieldPanel
from wagtail.snippets.models import register_snippet


class PricingTier(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveSmallIntegerField()
    is_special = models.BooleanField(default=False)
    special_name = models.CharField(max_length=100, default="Recommended")

    cta_text = models.CharField(max_length=100, default="Buy Now")
    cta_link = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True,
        null=True,
    )
    pricing_features = ParentalManyToManyField(
        "PricingFeature", related_name="+", blank=True
    )

    page = ParentalKey(
        "wagtailcore.Page",
        related_name="pricing_tiers",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("price"),
        FieldRowPanel([FieldPanel("is_special"), FieldPanel("special_name")]),
        MultiFieldPanel(
            [FieldPanel("pricing_features", widget=forms.CheckboxSelectMultiple)],
            heading="Features",
        ),
        FieldRowPanel([FieldPanel("cta_text"), FieldPanel("cta_link")]),
    ]

    def __str__(self):
        return self.name

    def get_excluded_features(self):
        all_features = PricingFeature.objects.all()
        excluded_features = all_features.exclude(
            id__in=self.pricing_features.values_list("id", flat=True)
        )
        return excluded_features


@register_snippet
class PricingFeature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # tier = models.ForeignKey(PricingTier, related_name='pricing_features',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
