# Generated by Django 5.0.6 on 2024-05-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('post', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='media')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
