from django.db import migrations
from django.utils.text import slugify


def assign_generated_images(apps, schema_editor):
    Product = apps.get_model('menu', 'Product')

    for product in Product.objects.select_related('category').all():
        filename = f"{slugify(product.category.name)}-{slugify(product.name)}.png"
        product.image = f"products/generated/{filename}"
        product.save(update_fields=['image'])


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0004_seed_pitsiyalar_products'),
    ]

    operations = [
        migrations.RunPython(assign_generated_images, migrations.RunPython.noop),
    ]
