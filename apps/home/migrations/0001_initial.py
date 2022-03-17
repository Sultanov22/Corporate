# Generated by Django 3.2 on 2022-02-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сайта')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('time_work', models.CharField(help_text='9:00 PM - 12:00 AM', max_length=20, verbose_name='Время работы')),
                ('email', models.CharField(max_length=35, verbose_name='E-mail')),
                ('facebook', models.CharField(help_text='https://www.facebook.com/friends/suggestions/?profile_id=100024268353113', max_length=150)),
                ('instagram', models.CharField(help_text='https://www.instagram.com/edzn_bey/', max_length=150)),
                ('youtube', models.CharField(help_text='https://www.youtube.com/c/selfedu_rus', max_length=150)),
                ('whatsapp', models.CharField(help_text='+996771494083', max_length=150)),
                ('telegram', models.CharField(help_text='https://t.me/edzn21', max_length=150)),
            ],
        ),
    ]
