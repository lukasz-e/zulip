

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0496_alter_scheduledmessage_read_by_sender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="archivedmessage",
            name="subject",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="draft",
            name="topic",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="message",
            name="subject",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="scheduledmessage",
            name="subject",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="usertopic",
            name="topic_name",
            field=models.CharField(max_length=128),
        ),
    ]
