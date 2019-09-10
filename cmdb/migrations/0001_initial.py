# Generated by Django 2.2.4 on 2019-09-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answerques',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kid', models.IntegerField(max_length=30)),
                ('kanwers', models.CharField(max_length=2000)),
                ('kanwersid', models.IntegerField(max_length=30)),
                ('ksubdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='kjtype',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('kname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='kmtype',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('kname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='knowlageinfo',
            fields=[
                ('kid', models.AutoField(primary_key=True, serialize=False)),
                ('kname', models.CharField(max_length=1000)),
                ('kanwers', models.CharField(max_length=1000)),
                ('kanwersid', models.IntegerField(max_length=30)),
                ('ktype1', models.IntegerField(max_length=30)),
                ('ktype2', models.IntegerField(max_length=30)),
                ('ktype3', models.IntegerField(max_length=30)),
            ],
        ),
    ]