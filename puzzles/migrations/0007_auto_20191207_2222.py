# Generated by Django 2.2.7 on 2019-12-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0003_auto_20191204_2308'),
        ('puzzles', '0006_auto_20191207_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='is_meta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='metas',
            field=models.ManyToManyField(related_name='_puzzle_metas_+', to='puzzles.Puzzle'),
        ),
        migrations.DeleteModel(
            name='MetaPuzzle',
        ),
    ]