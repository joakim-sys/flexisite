# Generated by Django 4.2.9 on 2024-02-24 08:39

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_sitesettings_branding_favicon_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sitesettings",
            name="branding_favicon",
        ),
        migrations.AlterField(
            model_name="formpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading_text",
                                    wagtail.blocks.CharBlock(
                                        form_classname="title", required=True
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        blank=True,
                                        choices=[
                                            ("", "Select a header size"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                        ],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "paragraph_block",
                        wagtail.blocks.RichTextBlock(
                            features=["bold", "italic", "link"],
                            icon="pilcrow",
                            template="blocks/paragraph_block.html",
                        ),
                    ),
                    (
                        "image_block",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                ("caption", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "block_quote",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.TextBlock()),
                                (
                                    "attribute_name",
                                    wagtail.blocks.CharBlock(
                                        blank=True,
                                        label="e.g. Marvin Paul",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "embed_block",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text="Insert an embed URL",
                            icon="media",
                            template="blocks/embed_block.html",
                        ),
                    ),
                ],
                blank=True,
                help_text="Compose the main content for this form page using various content blocks.",
                null=True,
                use_json_field=True,
                verbose_name="Page Body",
            ),
        ),
    ]