# Generated by Django 3.2.7 on 2022-06-21 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20220621_0140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '채용공고 정보', 'verbose_name_plural': '채용공고 정보'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '회사 정보', 'verbose_name_plural': '회사 정보'},
        ),
    ]
