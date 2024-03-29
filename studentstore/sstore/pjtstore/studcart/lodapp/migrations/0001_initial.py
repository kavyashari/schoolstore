# Generated by Django 5.0.1 on 2024-01-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                    ),
                ),
                ("phone_number", models.CharField(max_length=15)),
                ("email_id", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("CS", "Computerscience"),
                            ("IT", "Information Technology"),
                            ("BS", "BiologyScience"),
                            ("CM", "Commerce"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "course",
                    models.CharField(
                        choices=[
                            ("BBA", "Bachelor of business administration"),
                            ("Bcom", "Bachelor of commerce"),
                            ("CHEM", "Chemistry"),
                            ("BIO", "Biology"),
                            ("ENG", "English"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "purpose",
                    models.CharField(
                        choices=[
                            ("Enquiry", "Enquiry"),
                            ("Placeorder", "Placeorder"),
                            ("Return", "Return"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
