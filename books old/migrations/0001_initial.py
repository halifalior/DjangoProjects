# Generated by Django 3.1.7 on 2021-04-15 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('image', models.FilePathField(path='/img')),
                ('genre', models.CharField(choices=[('DR', 'דרמה'), ('BI', 'ביוגרפיה'), ('CH', 'ילדים'), ('FA', 'פנטזיה'), ('RO', 'רומן')], default='DR', max_length=2)),
            ],
        ),
    ]