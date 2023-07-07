# Generated by Django 4.2.1 on 2023-05-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0015_alter_postinteraction_type"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="emoji",
            new_name="activities__state_r_aa72ec_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="fanout",
            new_name="activities__state_r_aae3b4_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="hashtag",
            new_name="activities__state_r_5703be_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="post",
            new_name="activities__state_r_b8f1ff_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="postattachment",
            new_name="activities__state_r_4e981c_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="postinteraction",
            new_name="activities__state_r_981d8c_idx",
            old_fields=("state_ready", "state_locked_until", "state"),
        ),
        migrations.RenameIndex(
            model_name="postinteraction",
            new_name="activities__type_75d2e4_idx",
            old_fields=("type", "identity", "post"),
        ),
        migrations.RenameIndex(
            model_name="timelineevent",
            new_name="activities__identit_0b93c3_idx",
            old_fields=("identity", "type", "subject_post", "subject_identity"),
        ),
        migrations.RenameIndex(
            model_name="timelineevent",
            new_name="activities__identit_cc2290_idx",
            old_fields=("identity", "type", "subject_identity"),
        ),
        migrations.RenameIndex(
            model_name="timelineevent",
            new_name="activities__identit_872fbb_idx",
            old_fields=("identity", "created"),
        ),
        migrations.AddIndex(
            model_name="emoji",
            index=models.Index(
                fields=["state", "state_attempted"], name="ix_emoji_state_attempted"
            ),
        ),
        migrations.AddIndex(
            model_name="emoji",
            index=models.Index(
                condition=models.Q(("state_locked_until__isnull", False)),
                fields=["state_locked_until", "state"],
                name="ix_emoji_state_locked",
            ),
        ),
        migrations.AddIndex(
            model_name="postinteraction",
            index=models.Index(
                fields=["state", "state_attempted"],
                name="ix_postinterac_state_attempted",
            ),
        ),
        migrations.AddIndex(
            model_name="postinteraction",
            index=models.Index(
                condition=models.Q(("state_locked_until__isnull", False)),
                fields=["state_locked_until", "state"],
                name="ix_postinterac_state_locked",
            ),
        ),
    ]