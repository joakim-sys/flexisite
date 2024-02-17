from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel, FieldRowPanel
from wagtail.fields import RichTextField, StreamField

from modelcluster.fields import ParentalKey

from services.models import Service


class HomePage(Page):
    # ********************* Hero Section ***********************
    hero_welcome_text = models.CharField(
        max_length=255, blank=True, null=True, help_text="Welcome to Striker"
    )
    hero_heading = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Heading that describes the business",
    )
    hero_subheading = models.CharField(max_length=255, blank=True)
    hero_cta_text = models.CharField(
        max_length=255, null=True, blank=True, help_text="Text to display on CTA Button"
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        help_text="Page to link to",
        related_name="+",
        on_delete=models.SET_NULL,
    )

    # ******************** About Section **************************
    about_title = models.CharField(max_length=100, null=True, blank=True)
    about_heading = models.CharField(max_length=100, blank=True, null=True)
    about_subheading = models.TextField(null=True, blank=True)
    about_intro = models.TextField(null=True, blank=True)

    about_body = models.TextField(null=True, blank=True)
    about_cta_text = models.CharField(max_length=15, null=True, blank=True)
    about_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    # **************** Services Section **************************
    services_title = models.CharField(max_length=100, null=True, blank=True)
    services_heading = models.CharField(max_length=100, blank=True, null=True)
    services_subheading = models.TextField(null=True, blank=True)

    # ************* Call to Action Section ******************
    cta_title = models.CharField(
        max_length=100, null=True, blank=True, help_text="Such as Call to Action"
    )
    cta_descr = models.TextField(blank=True, null=True)
    cta_text = models.CharField(max_length=50, null=True, blank=True)
    cta_link = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # ************** Pricing Section ***********************
    pricing_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Should be one word such as, Pricing",
    )
    pricing_heading = models.CharField(max_length=100, null=True, blank=True)
    pricing_subheading = models.TextField(blank=True, null=True)

    # *************** F.A.Q Section **************************
    faq_title = models.CharField(max_length=20, null=True, blank=True)
    faq_heading = models.CharField(max_length=100, null=True, blank=True)
    faq_subheading = models.TextField(blank=True, null=True)

    # ************ Contact Section **********************
    contact_title = models.CharField(max_length=20, null=True, blank=True)
    contact_heading = models.CharField(max_length=100, null=True, blank=True)
    contact_subheading = models.TextField(blank=True, null=True)
    

    content_panels = Page.content_panels + [
        # *********** Hero Section **************
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("hero_welcome_text"),
                        FieldPanel("hero_heading"),
                        FieldPanel("hero_subheading"),
                    ],
                    heading="Hero Headings",
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("hero_cta_text"),
                        FieldPanel("hero_cta_link"),
                    ],
                    heading="Hero CTA",
                ),
            ],
            heading="Hero Section",
        ),
        # ************ About Section ***********
        MultiFieldPanel(
            [
                FieldPanel("about_title"),
                FieldPanel("about_heading"),
                FieldPanel("about_subheading"),
                FieldPanel("about_intro"),
                InlinePanel("about_listed_services", max_num=4, heading="Services"),
                FieldPanel("about_body"),
                MultiFieldPanel(
                    [FieldPanel("about_cta_link"), FieldPanel("about_cta_text")]
                ),
            ],
            heading="About Section",
        ),
        # ************* Services Section **********************
        MultiFieldPanel(
            [
                FieldPanel("services_title"),
                FieldPanel("services_heading"),
                FieldPanel("services_subheading"),
                InlinePanel("services", max_num=4, heading="Services", label="Service"),
            ],
            heading="Services Section",
        ),
        # ************** Features Section ********************
        InlinePanel(
            "features", heading="Features Section", label="Feature", max_num=12
        ),
        # ************ CTA Section ********************
        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_descr"),
                FieldRowPanel(
                    [FieldPanel("cta_text"), FieldPanel("cta_link")], heading="button"
                ),
            ],
            heading="CTA Section",
        ),
        # ************** Pricing Section **********************
        MultiFieldPanel(
            [
                FieldPanel("pricing_title"),
                FieldPanel("pricing_heading"),
                FieldPanel("pricing_subheading"),
                InlinePanel(
                    "pricing_tiers", max_num=3, heading="Tiers", label="Pricing Tier"
                ),
            ],
            heading="Pricing Section",
        ),
        # ************* F.A.Q Section ***********************
        MultiFieldPanel(
            [
                FieldPanel("faq_title"),
                FieldPanel("faq_heading"),
                FieldPanel("faq_subheading"),
                InlinePanel("faqs", heading="Frequent Questions", label="Question"),
            ],
            heading="F.A.Q Section",
        ),
    ]


class AboutList(models.Model):
    text = models.TextField()
    page = ParentalKey(
        HomePage, related_name="about_listed_services", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    page = ParentalKey(HomePage, related_name="faqs", on_delete=models.CASCADE)
