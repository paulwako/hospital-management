# Generated by Django 4.2.4 on 2023-10-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HMSTRACKER", "0008_alter_prescrition_availablemedicine_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicineRecommendations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prescriptions", models.TextField()),
            ],
        ),
    ]