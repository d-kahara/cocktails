# Generated by Django 3.1.1 on 2021-05-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210507_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='dateModified',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsDE',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsES',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsFR',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsIT',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsZH_HANS',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='strInstructionsZH_HANT',
            field=models.TextField(blank=True, null=True),
        ),
    ]
