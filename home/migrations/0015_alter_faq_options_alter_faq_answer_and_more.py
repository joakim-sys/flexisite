# Generated by Django 4.2.9 on 2024-02-21 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("home", "0014_homepage_cta_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="faq",
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "Frequently Asked Questions",
            },
        ),
        migrations.AlterField(
            model_name="faq",
            name="answer",
            field=models.TextField(
                help_text=" Provide the answer to the corresponding FAQ question."
            ),
        ),
        migrations.AlterField(
            model_name="faq",
            name="question",
            field=models.TextField(
                help_text=" Enter the question for the Frequently Asked Questions (FAQ) section"
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_body",
            field=models.TextField(
                blank=True,
                help_text="Compose the main content for the About section, providing detailed information and insights.",
                null=True,
                verbose_name="About Body",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_cta_link",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose a page to link to when the CTA button in the About section is clicked.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="About CTA Link",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_cta_text",
            field=models.CharField(
                blank=True,
                help_text="Enter the text to display on the Call-to-Action (CTA) button associated with the About section.",
                max_length=15,
                null=True,
                verbose_name="About CTA Text",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a heading for the About section that succinctly describes its purpose or content.",
                max_length=100,
                null=True,
                verbose_name="About Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_intro",
            field=models.TextField(
                blank=True,
                help_text="Introduce the About section with a brief overview or introductory text.",
                null=True,
                verbose_name="About Introduction",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_subheading",
            field=models.TextField(
                blank=True,
                help_text="Add a subheading to offer additional context or information for the About section.",
                null=True,
                verbose_name="About Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="about_title",
            field=models.CharField(
                blank=True,
                help_text="Enter a title for the About section, providing a concise label for the content that follows.",
                max_length=100,
                null=True,
                verbose_name="About Section Title",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="contact_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a heading for the Contact section that succinctly describes its purpose or content.",
                max_length=100,
                null=True,
                verbose_name="Contact Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="contact_subheading",
            field=models.TextField(
                blank=True,
                help_text="Add a subheading to offer additional context or information for the Contact section.",
                null=True,
                verbose_name="Contact Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="contact_title",
            field=models.CharField(
                blank=True,
                help_text="Enter a title for the Contact section, providing a concise label for the content that follows.",
                max_length=20,
                null=True,
                verbose_name="Contact Section Title",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_descr",
            field=models.TextField(
                blank=True,
                help_text="Provide a description for the Call to Action (CTA) section, offering additional context or information.",
                null=True,
                verbose_name="CTA Description",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose an image to visually represent the Call to Action (CTA) section, capturing attention and enhancing engagement.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="CTA Image",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_link",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose a page to link to when the CTA button in the Call to Action (CTA) section is clicked.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="CTA Link",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_text",
            field=models.CharField(
                blank=True,
                help_text="Enter the text to display for the Call to Action (CTA) button in this section.",
                max_length=50,
                null=True,
                verbose_name="CTA Text",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="cta_title",
            field=models.CharField(
                blank=True,
                help_text=" Enter a title for the Call to Action (CTA) section, providing a label for the content that follows.",
                max_length=100,
                null=True,
                verbose_name="CTA Section Title",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="faq_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a heading for the FAQ section that succinctly describes its purpose or content.",
                max_length=100,
                null=True,
                verbose_name="FAQ Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="faq_subheading",
            field=models.TextField(
                blank=True,
                help_text="Add a subheading to offer additional context or information for the FAQ section.",
                null=True,
                verbose_name="FAQ Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="faq_title",
            field=models.CharField(
                blank=True,
                help_text="Enter a title for the Frequently Asked Questions (FAQ) section, providing a concise label for the content that follows.",
                max_length=20,
                null=True,
                verbose_name="FAQ Section Title",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_cta_link",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose a page to link to when the CTA button in the hero section is clicked.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Call-to-Action Link",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_cta_text",
            field=models.CharField(
                blank=True,
                help_text="Enter the text to display on the Call-to-Action (CTA) button in the hero section.",
                max_length=255,
                null=True,
                verbose_name=" Call-to-Action Text",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a descriptive heading for the hero section that introduces and summarizes the business.",
                max_length=255,
                null=True,
                verbose_name="Hero Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_image",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose an image to visually represent the hero section, capturing attention and conveying the essence of the business.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Hero Image",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_subheading",
            field=models.CharField(
                blank=True,
                help_text="Add a subheading to complement the hero heading, providing additional context or information",
                max_length=255,
                verbose_name=" Hero Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="hero_welcome_text",
            field=models.CharField(
                blank=True,
                help_text="Enter a welcome message for the hero section, displayed prominently to visitors. like 'Welcome to Mars'",
                max_length=255,
                null=True,
                verbose_name="Hero Welcome Text",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="pricing_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a heading for the Pricing section that succinctly describes its purpose or content.",
                max_length=100,
                null=True,
                verbose_name="Pricing Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="pricing_subheading",
            field=models.TextField(
                blank=True,
                help_text="Add a subheading to offer additional context or information for the Pricing section.",
                null=True,
                verbose_name="Pricing Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="pricing_title",
            field=models.CharField(
                blank=True,
                help_text="Enter a title for the Pricing section, providing a clear label for the content that follows.",
                max_length=100,
                null=True,
                verbose_name="Pricing Section Title",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="services_heading",
            field=models.CharField(
                blank=True,
                help_text="Provide a heading for the Services section that succinctly describes its purpose or content.",
                max_length=100,
                null=True,
                verbose_name="Services Heading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="services_subheading",
            field=models.TextField(
                blank=True,
                help_text="Add a subheading to offer additional context or information for the Services section.",
                null=True,
                verbose_name="Services Subheading",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="services_title",
            field=models.CharField(
                blank=True,
                help_text="Enter a title for the Services section, providing a clear label for the content that follows.",
                max_length=100,
                null=True,
                verbose_name="Services Section Title",
            ),
        ),
    ]