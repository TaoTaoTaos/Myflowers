# Generated by Django 3.2.25 on 2024-07-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20240708_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowermaterial',
            name='chinese_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='english_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='model',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_height',
            field=models.FloatField(blank=True, default=0.0, help_text='高度，单位：cm', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_length',
            field=models.FloatField(blank=True, default=0.0, help_text='长度，单位：cm', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_width',
            field=models.FloatField(blank=True, default=0.0, help_text='宽度，单位：cm', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='packing_quantity',
            field=models.IntegerField(blank=True, default=0, help_text='单位：qty', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='price_one',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='price_two',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='sale_spec_quantity',
            field=models.FloatField(blank=True, default=0.0, help_text='数量', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='sale_spec_unit',
            field=models.CharField(blank=True, choices=[('pcs', 'pcs'), ('g', 'g'), ('box', 'box'), ('kg', 'kg')], default='pcs', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='scientific_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='size',
            field=models.FloatField(blank=True, default=0.0, help_text='单位：cm', null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, help_text='单位：g', null=True),
        ),
    ]
