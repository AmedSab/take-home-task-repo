# Generated by Django 5.1 on 2024-08-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyChangingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_IntegerField', models.IntegerField()),
                ('main_CharField', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('main_BooleanField', models.BooleanField(default=True)),
                ('main_EmailField', models.EmailField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
