from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.FileField(default=None, upload_to='bookEx/static/uploads'),
        ),
    ]