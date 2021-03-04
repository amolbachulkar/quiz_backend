# Generated by Django 3.1.7 on 2021-03-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Quiz name')),
                ('description', models.CharField(max_length=3000, verbose_name='Quiz description')),
            ],
        ),
    ]
