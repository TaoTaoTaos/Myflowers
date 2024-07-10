# Generated by Django 3.2.25 on 2024-07-10 03:30

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app01', '0004_auto_20240709_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowermaterial',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.category'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='chinese_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='color',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.color'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='english_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_height',
            field=models.FloatField(blank=True, default=0.0, help_text='高度，单位：cm'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_length',
            field=models.FloatField(blank=True, default=0.0, help_text='长度，单位：cm'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='outer_box_width',
            field=models.FloatField(blank=True, default=0.0, help_text='宽度，单位：cm'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='packing_quantity',
            field=models.IntegerField(blank=True, default=0, help_text='单位：qty'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='price_one',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='price_two',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='process',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.process'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='sale_spec_quantity',
            field=models.FloatField(blank=True, default=0.0, help_text='数量'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='sale_spec_unit',
            field=models.CharField(blank=True, choices=[('pcs', 'pcs'), ('g', 'g'), ('box', 'box'), ('kg', 'kg')], default='pcs', max_length=10),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='scientific_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='size',
            field=models.FloatField(blank=True, default=0.0, help_text='单位：cm'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='stock',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='supplier',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.supplier'),
        ),
        migrations.AlterField(
            model_name='flowermaterial',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, help_text='单位：g'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
