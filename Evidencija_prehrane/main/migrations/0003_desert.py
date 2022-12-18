# Generated by Django 4.1.4 on 2022-12-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hrana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desert_name', models.CharField(max_length=20, null=True, verbose_name='Naziv deserta')),
                ('choco', models.BooleanField(default=True, null=True, verbose_name='Cokoladno')),
                ('kcal', models.CharField(max_length=3, null=True, verbose_name='Kalorije')),
            ],
        ),
    ]