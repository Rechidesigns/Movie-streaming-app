# Generated by Django 4.2 on 2023-04-28 21:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_reviews', to='watchlist_app.watchlist')),
            ],
        ),
    ]
