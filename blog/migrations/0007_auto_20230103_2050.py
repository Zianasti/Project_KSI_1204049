# Generated by Django 3.1 on 2023-01-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230103_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('Jurnal', 'jurnal'), ('Blog', 'blog'), ('Berita', 'berita'), ('Buku', 'buku')], default='Pilih Category', max_length=100),
        ),
    ]
