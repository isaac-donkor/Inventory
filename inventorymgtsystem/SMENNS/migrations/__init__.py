from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations=[
        migrations.CreateModel(
            name='SMENNS',
            fields=[
                 ('item_name',models.CharField(max_length=255)),
                 ('weight_pounds',models.FloatField()),
                 ('karat', models.FloatField()),
                 ('amount_gold', models.FloatField())
            ]
        )

    ]
