# Generated by Django 3.2.9 on 2021-12-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='1QlTi22Dkj', max_length=1000),
        ),
    ]
