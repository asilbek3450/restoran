from django.db import migrations


PIZZA_PRODUCTS = [
    {'name': 'Margarita pitsa', 'price': 48000, 'description': 'Pomidor sousi, mozzarella va oregano bilan klassik pitsa.'},
    {'name': 'Go‘shtli pitsa', 'price': 62000, 'description': 'Mol go‘shti, pishloq va maxsus sous bilan tayyorlangan to‘yimli pitsa.'},
    {'name': 'Tovuqli pitsa', 'price': 56000, 'description': 'Tovuq filesi, qo‘ziqorin va mozzarella bilan yumshoq ta’m.'},
    {'name': 'Assorti pitsa', 'price': 68000, 'description': 'Bir pitsada bir nechta topping va boy ta’m uyg‘unligi.'},
    {'name': 'BBQ pitsa', 'price': 64000, 'description': 'BBQ sous, tovuq va qarsildoq piyoz bilan tayyorlanadi.'},
    {'name': 'Vegetarian pitsa', 'price': 52000, 'description': 'Bolgar qalampiri, zaytun, qo‘ziqorin va pishloq bilan.'},
    {'name': 'Four cheese pitsa', 'price': 66000, 'description': 'To‘rt xil pishloq bilan tayyorlangan yumshoq va boy pitsa.'},
    {'name': 'Qazi pitsa', 'price': 70000, 'description': 'Milliy uslubdagi qazi, pishloq va sous bilan tayyorlangan maxsus pitsa.'},
    {'name': 'Achchiq pitsa', 'price': 59000, 'description': 'Achchiq kolbasa, jalapeno va maxsus pomidor sous bilan.'},
]


def seed_pitsiyalar_products(apps, schema_editor):
    Category = apps.get_model('menu', 'Category')
    Product = apps.get_model('menu', 'Product')

    category, _ = Category.objects.get_or_create(
        name='pitsiyalar',
        defaults={'icon': '🍕', 'order': 9},
    )

    for index, product_data in enumerate(PIZZA_PRODUCTS, start=1):
        Product.objects.update_or_create(
            category=category,
            name=product_data['name'],
            defaults={
                'description': product_data['description'],
                'price': product_data['price'],
                'is_available': True,
                'is_popular': index <= 2,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0003_seed_menu_catalog'),
    ]

    operations = [
        migrations.RunPython(seed_pitsiyalar_products, migrations.RunPython.noop),
    ]
