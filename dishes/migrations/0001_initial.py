# Generated by Django 2.1.4 on 2019-05-17 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DishName', models.CharField(max_length=20, verbose_name='菜名')),
                ('CostPrice', models.FloatField(verbose_name='成本价')),
                ('Price', models.FloatField(verbose_name='标价')),
                ('Sales', models.IntegerField(verbose_name='销量')),
                ('Moral', models.CharField(blank=True, default='', max_length=100, verbose_name='寓意')),
                ('img', models.CharField(blank=True, default='', max_length=500, verbose_name='图片地址')),
            ],
            options={
                'verbose_name_plural': '单菜详情',
            },
        ),
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='菜型')),
            ],
            options={
                'verbose_name_plural': '菜型',
            },
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='菜系')),
            ],
            options={
                'verbose_name_plural': '菜系',
            },
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=15, null=True)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('Dish', models.ManyToManyField(blank=True, null=True, to='dishes.Dish')),
            ],
            options={
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PackageName', models.CharField(default=None, max_length=20, verbose_name='套餐名')),
                ('CostPrice', models.FloatField(verbose_name='成本价')),
                ('Price', models.FloatField(verbose_name='标价')),
                ('Sales', models.IntegerField(verbose_name='销量')),
                ('img', models.CharField(blank=True, max_length=500, null=True, verbose_name='图片地址')),
                ('Dish', models.ManyToManyField(to='dishes.Dish')),
            ],
            options={
                'verbose_name_plural': '套餐详情',
            },
        ),
        migrations.CreateModel(
            name='PackageTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themeName', models.CharField(max_length=20, null=True, verbose_name='套餐主题名')),
            ],
            options={
                'verbose_name_plural': '套餐主题',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='PackageTheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.PackageTheme'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='Package',
            field=models.ManyToManyField(blank=True, null=True, to='dishes.Package'),
        ),
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dishes.DishCategory'),
        ),
        migrations.AddField(
            model_name='dish',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.DishType', verbose_name='菜系'),
        ),
    ]
