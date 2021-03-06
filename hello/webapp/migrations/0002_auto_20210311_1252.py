# Generated by Django 3.1.7 on 2021-03-11 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=50, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='list',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lists', to='webapp.type'),
        ),
    ]
