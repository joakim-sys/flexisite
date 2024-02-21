# Generated by Django 4.2.9 on 2024-02-21 11:48

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("pricing", "0004_remove_pricingtier_features_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pricingfeature",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Provide a description for this pricing feature.",
                null=True,
                verbose_name="Feature Description",
            ),
        ),
        migrations.AlterField(
            model_name="pricingfeature",
            name="name",
            field=models.CharField(
                help_text="Enter a name for this pricing feature.",
                max_length=100,
                verbose_name="Feature Name",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="cta_link",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose a page to link to when the CTA button is clicked.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="CTA Link",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="cta_text",
            field=models.CharField(
                default="Buy Now",
                help_text="Enter the text for the Call-to-Action (CTA) button.",
                max_length=100,
                verbose_name=" CTA Text",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="is_special",
            field=models.BooleanField(
                default=False,
                help_text="Check this box if this tier is special or recommended.",
                verbose_name=" Special Tier",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="name",
            field=models.CharField(
                help_text="Enter a name for this pricing tier.",
                max_length=50,
                verbose_name="Tier Name",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="price",
            field=models.PositiveSmallIntegerField(
                help_text="Enter the price for this tier", verbose_name="Price"
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="pricing_features",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True,
                help_text="Select features associated with this pricing tier.",
                related_name="+",
                to="pricing.pricingfeature",
                verbose_name="Pricing Features",
            ),
        ),
        migrations.AlterField(
            model_name="pricingtier",
            name="special_name",
            field=models.CharField(
                default="Recommended",
                help_text='Enter a name for the special tier, e.g., "Recommended"',
                max_length=100,
                verbose_name="Special Tier Name",
            ),
        ),
    ]
