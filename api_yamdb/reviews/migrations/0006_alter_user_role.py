# Generated by Django 3.2 on 2023-02-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'юзер'), ('moderator', 'модератор'), ('admin', 'админ')], default='user', max_length=50, verbose_name='Уровень доступа'),
        ),
    ]
