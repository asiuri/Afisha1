# Generated by Django 4.0.5 on 2022-07-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_director_movie_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.tag'),
        ),
    ]