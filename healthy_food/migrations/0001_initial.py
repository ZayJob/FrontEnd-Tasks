# Generated by Django 3.0.4 on 2020-03-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_col', models.CharField(db_index=True, default='test', max_length=150)),
            ],
        ),
    ]
