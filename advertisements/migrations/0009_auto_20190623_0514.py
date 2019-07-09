# Generated by Django 2.2.2 on 2019-06-23 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_auto_20190619_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='adv_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.AdvTypes'),
        ),
        migrations.AlterField(
            model_name='images',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.Advertisement'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
