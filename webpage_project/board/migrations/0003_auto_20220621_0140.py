# Generated by Django 3.2.7 on 2022-06-20 16:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_article_write_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='회사id')),
                ('company_pw', models.CharField(max_length=50, verbose_name='회사pw')),
                ('company_name', models.CharField(max_length=20, verbose_name='회사명')),
                ('nation', models.CharField(max_length=20, verbose_name='국가')),
                ('region', models.CharField(max_length=20, null=True, verbose_name='지역')),
            ],
            options={
                'verbose_name': '회사 정보',
                'db_table': 'company_info',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '채용공고 정보'},
        ),
        migrations.AlterField(
            model_name='article',
            name='awards',
            field=models.IntegerField(verbose_name='취업보상금'),
        ),
        migrations.AlterField(
            model_name='article',
            name='contents',
            field=models.TextField(verbose_name='채용내용'),
        ),
        migrations.AlterField(
            model_name='article',
            name='position_name',
            field=models.CharField(max_length=50, verbose_name='포지션명'),
        ),
        migrations.AlterField(
            model_name='article',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='공고id '),
        ),
        migrations.AlterField(
            model_name='article',
            name='skills',
            field=models.CharField(max_length=50, verbose_name='사용기술'),
        ),
        migrations.AlterField(
            model_name='article',
            name='write_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일자'),
        ),
        migrations.AlterModelTable(
            name='article',
            table='articles',
        ),
        migrations.AlterField(
            model_name='article',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.company', verbose_name='회사id'),
        ),
    ]
