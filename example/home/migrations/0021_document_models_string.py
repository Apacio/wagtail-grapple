# Generated by Django 3.1.7 on 2021-04-01 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
        ("home", "0020_correct_cover_model_fk"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="book_file",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="documents.customdocument",
            ),
        ),
    ]
