# Generated by Django 5.0 on 2024-09-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organs", "0002_alter_organ_systems_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organs",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
