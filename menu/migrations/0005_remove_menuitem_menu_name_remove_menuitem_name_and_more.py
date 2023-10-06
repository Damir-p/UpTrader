# Generated by Django 4.2.5 on 2023-10-06 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitem_menu_name_alter_menuitem_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='name',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]