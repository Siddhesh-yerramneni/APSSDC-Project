# Generated by Django 3.2.4 on 2021-07-24 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderhistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=5000000)),
                ('billamoubt', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant_app.order')),
            ],
        ),
    ]
