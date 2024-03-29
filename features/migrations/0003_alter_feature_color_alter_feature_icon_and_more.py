# Generated by Django 4.2.9 on 2024-02-21 11:48

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0014_homepage_cta_image"),
        ("features", "0002_feature_color_alter_feature_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="color",
            field=models.CharField(
                blank=True,
                help_text=" Enter a color code for this feature, such as a hex value (e.g., ',  #e80368') or a color name (e.g., 'red'). Leave it blank if no specific color is needed.",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="feature",
            name="icon",
            field=models.CharField(
                blank=True,
                help_text="Enter the icon code for this feature. We are using Remix Icons (ri) URL: https://remixicon.com/, and you can find a list of icons on their website. Use icons such as 'ri-store-line'. Leave it blank if no icon is needed.",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="feature",
            name="name",
            field=models.CharField(
                help_text="Enter a name for the feature.",
                max_length=50,
                verbose_name="Feature Name",
            ),
        ),
        migrations.AlterField(
            model_name="feature",
            name="page",
            field=modelcluster.fields.ParentalKey(
                blank=True,
                help_text="Choose a page to link to when users interact with this feature.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="features",
                to="home.homepage",
            ),
        ),
    ]
