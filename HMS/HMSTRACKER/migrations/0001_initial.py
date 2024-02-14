# Generated by Django 4.2.4 on 2023-09-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HospitalData",
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
                ("firstName", models.CharField(max_length=50)),
                ("middleName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("IDno", models.IntegerField()),
                ("birthCertificate", models.BigIntegerField(max_length=13, null=True)),
                ("firstContact", models.IntegerField()),
                ("secondContact", models.IntegerField()),
                ("village", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=50)),
                ("residence", models.CharField(max_length=50)),
                ("county", models.CharField(max_length=50)),
                ("NHIF", models.BigIntegerField(max_length=30, null=True)),
            ],
        ),
    ]