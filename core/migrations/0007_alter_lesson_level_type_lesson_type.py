# Generated by Django 4.1 on 2022-09-18 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_socialaccount_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='level',
            field=models.CharField(choices=[('All', 'All'), ('Beginner', 'Beginner'), ('Elementary', 'Elementary'), ('Pre-Intermediate', 'Pre-Intermediate'), ('Intermediate', 'Intermediate'), ('Upper-Intermediate', 'Upper-Intermediate'), ('Advanced', 'Advanced')], default='All', max_length=64, verbose_name='level'),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='slug')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.type', verbose_name='type'),
            preserve_default=False,
        ),
    ]
