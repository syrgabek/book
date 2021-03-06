# Generated by Django 4.0.4 on 2022-05-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_gengre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='createa_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='gengre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updeted_data',
            new_name='updated_date',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
