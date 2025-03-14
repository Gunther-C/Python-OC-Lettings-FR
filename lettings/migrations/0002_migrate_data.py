from django.db import migrations

def forwards_func(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    for old_letting in OldLetting.objects.all():
        new_address = NewAddress.objects.get(id=old_letting.address_id)
        NewLetting.objects.create(
            title=old_letting.title,
            address=new_address
        )

    # OldAddress.objects.all().delete()
    # OldLetting.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
