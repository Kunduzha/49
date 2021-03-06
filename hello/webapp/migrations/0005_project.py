# Generated by Django 3.1.7 on 2021-03-29 07:59

from django.db import migrations, models
import webapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20210318_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('begin_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата начало')),
                ('created_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания')),
                ('title', models.CharField(max_length=30, validators=[webapp.validators.MinLengthValidators(2), webapp.validators.str_value], verbose_name='заголовка')),
                ('description', models.TextField(max_length=300, validators=[webapp.validators.MinLengthValidators(10), webapp.validators.str_value], verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'db_table': 'project',
            },
        ),
    ]
