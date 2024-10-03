# Generated by Django 5.0.7 on 2024-08-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cardId', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(default='', max_length=300)),
                ('answer', models.CharField(default='', max_length=300)),
                ('hint', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
