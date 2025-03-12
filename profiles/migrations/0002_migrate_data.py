from django.db import migrations

def forwards_func(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city
        )

    # OldProfile.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
