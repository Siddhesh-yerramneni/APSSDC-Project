# Generated by Django 3.2.4 on 2021-07-24 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_app', '0002_orderhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
