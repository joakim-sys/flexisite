from django.db import models
from django.utils.translation import gettext as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)


from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

from wagtail.fields import RichTextField, StreamField
from wagtail.models import (
    Page,
    WorkflowMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    TranslatableMixin,
    PreviewableMixin,
)

from wagtail.search import index

from .blocks import BaseStreamBlock


class StandardPage(Page):
    pass


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = models.CharField(
        verbose_name="Logo Text",
        max_length=20,
        help_text="This is the logo text of the website",
        default="Striker",
    )


@register_setting
class GenericSettings(ClusterableModel, BaseGenericSetting):
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    whatsapp_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("twitter_url"),
                FieldPanel("facebook_url"),
                FieldPanel("instagram_url"),
                FieldPanel("tiktok_url"),
                FieldPanel("whatsapp_url"),
                FieldPanel("telegram_url"),
                FieldPanel("linkedin_url"),
                FieldPanel("email"),
                FieldPanel("phone"),
            ]
        )
    ]
