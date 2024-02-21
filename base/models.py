from django.db import models
from django.utils.translation import gettext as _

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.snippets.models import register_snippet
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
    introduction = models.TextField(
        blank=True,
        null=True,
        help_text="Provide a brief introduction or overview for this page.",
    )
    body = StreamField(
        BaseStreamBlock(),
        verbose_name="Page body",
        blank=True,
        use_json_field=True,
        help_text="Compose the main content for this page. Utilize various content blocks to structure and format the information effectively.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("body"),
    ]

    page_description = "This page type allows you to create standard content pages with an introduction and a flexible body."


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", related_name="form_fields", on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):

    introduction = models.TextField(
        null=True,
        blank=True,
        help_text=" Provide a brief introduction or overview for this form page.",
    )
    body = StreamField(
        BaseStreamBlock(),
        use_json_field=True,
        verbose_name="Page Body",
        help_text="Compose the main content for this form page using various content blocks.",
    )

    thank_you_text = RichTextField(
        verbose_name="Thank You Text",
        blank=True,
        help_text="Customize the message displayed to users after submitting the form.",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("body"),
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel([FieldPanel("from_address"), FieldPanel("to_address")]),
                FieldPanel("subject"),
            ],
            heading="Email",
        ),
    ]

    page_description = "Create interactive forms with ease. Customize the page with images, introductions, and a flexible body. Manage form fields, set email notifications, and provide a personalized thank-you message."


@register_snippet
class FooterInfo(models.Model):
    links_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Enter a title for the links section in the footer.",
    )
    services_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter a title for the services section in the footer.",
    )
    subscribe_email_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Enter a title for the email subscription section in the footer.",
    )
    subscribe_email_body = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Enter the text or body content for the email subscription section in the footer.",
    )

    class Meta:
        verbose_name = "Footer Information"
        verbose_name_plural = "Footer Information"


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = models.CharField(
        verbose_name="Logo Text",
        max_length=20,
        help_text="Enter the text for the website's logo. This is the displayed logo text.",
        default="Buzzy",
    )


@register_setting
class GenericSettings(ClusterableModel, BaseGenericSetting):
    twitter_url = models.URLField('Twitter URL',blank=True, null=True)
    facebook_url = models.URLField('Facebook URL',blank=True, null=True)
    instagram_url = models.URLField('Instagram URL',blank=True, null=True)
    tiktok_url = models.URLField('Tiktok URL',blank=True, null=True)
    whatsapp_url = models.URLField('WhatsApp Business URL',blank=True, null=True)
    telegram_url = models.URLField('Telegram URL',blank=True, null=True)
    linkedin_url = models.URLField('LinkedIn URL',blank=True, null=True)

    email = models.CharField('Contact Email',max_length=100, blank=True, null=True)
    phone = models.CharField('Contact Phone',max_length=100, blank=True, null=True)

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
            ],
            "Social Media URLs",
        ),
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("phone"),
            ],
            "Email & Phone",
        ),
    ]
