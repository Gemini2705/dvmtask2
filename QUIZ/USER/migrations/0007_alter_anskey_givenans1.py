# Generated by Django 4.1.6 on 2023-02-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0006_alter_anskey_username_alter_result_inquiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anskey',
            name='givenAns1',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]