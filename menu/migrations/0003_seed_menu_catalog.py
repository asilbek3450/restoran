from django.db import migrations


CATALOG = [
    {
        'name': 'Milliy taomlar',
        'icon': '🍛',
        'order': 1,
        'products': [
            {'name': 'Osh', 'price': 38000, 'is_popular': True, 'description': 'An’anaviy toshkentcha osh, noxat, sabzi va yumshoq go‘sht bilan.'},
            {'name': 'Choyxona palov', 'price': 42000, 'is_popular': True, 'description': 'Ustiga qazi va bedana tuxumi bilan tortiladigan to‘yona palov.'},
            {'name': 'Dimlama', 'price': 46000, 'description': 'Mol go‘shti, kartoshka va mavsumiy sabzavotlardan sekin pishirilgan taom.'},
            {'name': 'Qozon kabob', 'price': 54000, 'description': 'Qarsildoq kartoshka va ziravorli mol go‘shti bilan qozonda qovurilgan taom.'},
            {'name': 'Manti', 'price': 36000, 'description': 'Go‘shtli va piyozli bug‘da pishgan sharqona manti.'},
            {'name': 'Xonim', 'price': 32000, 'description': 'Yupqa xamir orasiga go‘sht va sabzavot solib o‘ralgan xonim.'},
            {'name': 'Lag‘mon', 'price': 41000, 'description': 'Qo‘l cho‘zma ugra, sabzavot va ziravorli qayla bilan tayyorlangan lag‘mon.'},
            {'name': 'Norin', 'price': 39000, 'description': 'Ot go‘shti, uy ugrosi va xushbo‘y ziravorlardan tayyorlangan klassik norin.'},
            {'name': 'Moshxo‘rda', 'price': 31000, 'description': 'Mosh, guruch va mol go‘shti bilan pishirilgan quyuq milliy taom.'},
            {'name': 'Tovuq say', 'price': 35000, 'description': 'Sabzavotlar bilan qovurilgan tovuqli say, non bilan juda mos.'},
        ],
    },
    {
        'name': 'Kaboblar',
        'icon': '🔥',
        'order': 2,
        'products': [
            {'name': 'Qo‘y go‘shti shashlik', 'price': 28000, 'is_popular': True, 'description': 'Ko‘mirda pishirilgan suvli qo‘y go‘shti six kabob.'},
            {'name': 'Mol go‘shti shashlik', 'price': 30000, 'description': 'Marinadlangan mol go‘shti va piyoz bilan tayyorlangan six kabob.'},
            {'name': 'Tovuq shashlik', 'price': 24000, 'description': 'Yengil ziravorlangan tovuq filesidan yumshoq kabob.'},
            {'name': 'Qiymali lula kabob', 'price': 26000, 'is_popular': True, 'description': 'Qo‘y va mol go‘shti qiyma aralashmasidan tayyorlangan lula kabob.'},
            {'name': 'Jigar kabob', 'price': 22000, 'description': 'Mayin jigar bo‘laklari va dumba bilan tayyorlangan kabob.'},
            {'name': 'Assorti kabob', 'price': 62000, 'description': 'Bir likopchada turli kaboblar jamlanmasi.'},
            {'name': 'Sabzavotli kabob', 'price': 19000, 'description': 'Baqlajon, qalampir, pomidor va qo‘ziqorin bilan yengil kabob.'},
            {'name': 'Bifshteks gril', 'price': 68000, 'description': 'Steyk usulida grilda pishirilgan mol go‘shti va sous bilan.'},
            {'name': 'Qanotcha BBQ', 'price': 29000, 'description': 'BBQ sousda qovurilgan va ko‘mirda pishirilgan qanotchalar.'},
            {'name': 'Dumba kabob', 'price': 21000, 'description': 'Ko‘mirda tayyorlangan xushbo‘y dumba bo‘laklari.'},
        ],
    },
    {
        'name': 'Sho‘rvalar',
        'icon': '🍲',
        'order': 3,
        'products': [
            {'name': 'Mastava', 'price': 26000, 'is_popular': True, 'description': 'Guruch, sabzavot va mol go‘shti bilan tayyorlangan klassik mastava.'},
            {'name': 'Shurva', 'price': 32000, 'description': 'Katta bo‘lak go‘sht va sabzavotlar bilan pishirilgan to‘yimli sho‘rva.'},
            {'name': 'Tovuq sho‘rva', 'price': 24000, 'description': 'Tovuq go‘shti va uy ugrosi bilan tayyorlangan yengil sho‘rva.'},
            {'name': 'Moxora', 'price': 25000, 'description': 'No‘xat, go‘sht va ziravorlar bilan quyuq pishirilgan sho‘rva.'},
            {'name': 'Qaynatma sho‘rva', 'price': 34000, 'description': 'Suyakli mol go‘shti, kartoshka va ko‘katlar bilan pishiriladi.'},
            {'name': 'Chuchvara sho‘rva', 'price': 29000, 'description': 'Mayda go‘shtli chuchvaralar solingan uycha sho‘rva.'},
            {'name': 'Sabzavotli krem sho‘rva', 'price': 27000, 'description': 'Qovoq, sabzi va qaymoqli teksturadagi zamonaviy sho‘rva.'},
            {'name': 'Qo‘ziqorin sho‘rva', 'price': 28000, 'description': 'Qo‘ziqorin, qaymoq va xushbo‘y o‘tlar bilan tayyorlangan sho‘rva.'},
            {'name': 'Achchiq ramen uslubida sho‘rva', 'price': 33000, 'description': 'Tuxum, ugra va achchiq bulon bilan tayyorlangan fusion sho‘rva.'},
            {'name': 'Loviya sho‘rva', 'price': 23000, 'description': 'Qizil loviya, mol go‘shti va ziravorlar bilan to‘yimli sho‘rva.'},
        ],
    },
    {
        'name': 'Salatlar',
        'icon': '🥗',
        'order': 4,
        'products': [
            {'name': 'Achichuk', 'price': 14000, 'description': 'Pomidor, piyoz va rayhon bilan tayyorlangan yengil milliy salat.'},
            {'name': 'Sezar tovuqli', 'price': 34000, 'is_popular': True, 'description': 'Tovuq filesi, parmesan va xrustik non bo‘laklari bilan.'},
            {'name': 'Grekcha salat', 'price': 28000, 'description': 'Feta, zaytun va yangi sabzavotlardan tayyorlangan klassik salat.'},
            {'name': 'Olivye', 'price': 22000, 'description': 'Kartoshka, tuxum, kolbasa va mayonez bilan tayyorlangan sevimli salat.'},
            {'name': 'Shakarob', 'price': 16000, 'description': 'Pomidor va piyozdan tayyorlangan oshga mos salat.'},
            {'name': 'Tuna salati', 'price': 36000, 'description': 'Tuna, salat bargi, tuxum va limonli dressing bilan.'},
            {'name': 'Rukola beef salat', 'price': 39000, 'description': 'Rukola, mol go‘shti bo‘laklari va balsamik sous bilan.'},
            {'name': 'Qarsildoq baqlajon salati', 'price': 31000, 'description': 'Qovurilgan baqlajon, sous va ko‘katlar bilan tayyorlanadi.'},
            {'name': 'Bahor salati', 'price': 18000, 'description': 'Bodring, rediska, ko‘kat va smetana bilan yengil salat.'},
            {'name': 'Mevali salat', 'price': 26000, 'description': 'Mavsumiy mevalar va yengil yogurtli sous bilan desert-salat.'},
        ],
    },
    {
        'name': 'Fast food',
        'icon': '🍔',
        'order': 5,
        'products': [
            {'name': 'Classic burger', 'price': 32000, 'is_popular': True, 'description': 'Mol go‘shti kotleti, pishloq va maxsus sous bilan burger.'},
            {'name': 'Double cheeseburger', 'price': 42000, 'description': 'Ikki qavatli kotlet va erigan pishloqli to‘yimli burger.'},
            {'name': 'Chicken burger', 'price': 30000, 'description': 'Qarsildoq tovuq filesi va yangi sabzavotlar bilan.'},
            {'name': 'Lavash classic', 'price': 27000, 'is_popular': True, 'description': 'Go‘sht, fri va sous bilan tayyorlangan mashhur lavash.'},
            {'name': 'Lavash mini', 'price': 22000, 'description': 'Yengil va tez tamaddi uchun mini formatdagi lavash.'},
            {'name': 'Donar box', 'price': 26000, 'description': 'Go‘sht, fri va sous bir qutida tortiladigan box format.'},
            {'name': 'Hot-dog', 'price': 18000, 'description': 'Sosiska, karam va sous bilan tayyorlangan hot-dog.'},
            {'name': 'Nuggets set', 'price': 24000, 'description': 'Qarsildoq tovuq nuggets va souslar jamlanmasi.'},
            {'name': 'Fri kartoshka', 'price': 15000, 'description': 'Tashqarisi qarsildoq, ichi yumshoq oltinrang fri.'},
            {'name': 'Klub sendvich', 'price': 29000, 'description': 'Tovuq, pishloq va sabzavotlardan tayyorlangan ko‘p qavatli sendvich.'},
        ],
    },
    {
        'name': 'Nonushta',
        'icon': '🍳',
        'order': 6,
        'products': [
            {'name': 'Syrniki', 'price': 24000, 'description': 'Tvorogli yumshoq syrniki, smetana va murabbo bilan.'},
            {'name': 'Pancake set', 'price': 26000, 'description': 'Asal, murabbo va qaymoq bilan tortiladigan pankeyklar.'},
            {'name': 'Omlet klassik', 'price': 21000, 'description': 'Yumshoq tuxumli omlet, ko‘kat va non bilan.'},
            {'name': 'Omlet pishloqli', 'price': 24000, 'description': 'Mozzarella va ko‘katlar bilan tayyorlangan omlet.'},
            {'name': 'Shakshuka', 'price': 28000, 'is_popular': True, 'description': 'Pomidorli sousda pishirilgan tuxum va xushbo‘y ziravorlar bilan.'},
            {'name': 'Kasha assorti', 'price': 18000, 'description': 'Sutli suli yormasi, meva va yong‘oq qo‘shib beriladi.'},
            {'name': 'Breakfast combo', 'price': 36000, 'description': 'Tuxum, sosiska, tost va salat bilan to‘liq nonushta.'},
            {'name': 'Tvorogli blinchik', 'price': 23000, 'description': 'Tvorog solingan yupqa blinchiklar va smetana bilan.'},
            {'name': 'Fransuzcha tost', 'price': 25000, 'description': 'Dolchin va meva bilan qovurilgan yumshoq tostlar.'},
            {'name': 'Mini samsa set', 'price': 22000, 'description': 'Issiq mini somsa va choy bilan nonushta uchun qulay to‘plam.'},
        ],
    },
    {
        'name': 'Shirinliklar',
        'icon': '🍰',
        'order': 7,
        'products': [
            {'name': 'Cheesecake', 'price': 28000, 'is_popular': True, 'description': 'Qaymoqli pishloqli klassik cheesecake.'},
            {'name': 'Medovik', 'price': 24000, 'description': 'Asalli yupqa qatlamli tort bo‘lagi.'},
            {'name': 'Napoleon', 'price': 25000, 'description': 'Qarsildoq qatlamlar va qaymoqli krem bilan.'},
            {'name': 'Tiramisu', 'price': 30000, 'description': 'Qahva singdirilgan savoyardi va mascarpone krem bilan.'},
            {'name': 'Brauni', 'price': 22000, 'description': 'Qora shokoladli yumshoq desert va muzqaymoq bilan.'},
            {'name': 'Qatlama baklava', 'price': 27000, 'description': 'Yong‘oq va asal bilan tayyorlangan sharqona desert.'},
            {'name': 'Muzqaymoq assorti', 'price': 18000, 'description': 'Vanil, shokolad va qulupnay ta’mlaridan tanlov.'},
            {'name': 'Mevali tort', 'price': 29000, 'description': 'Yengil krem va mavsumiy mevalar bilan bezatilgan tort.'},
            {'name': 'Ekler', 'price': 17000, 'description': 'Ichiga qaymoqli krem to‘ldirilgan klassik ekler.'},
            {'name': 'Qulupnayli panna cotta', 'price': 23000, 'description': 'Yengil italyancha sutli desert, qulupnay sous bilan.'},
        ],
    },
    {
        'name': 'Ichimliklar',
        'icon': '🥤',
        'order': 8,
        'products': [
            {'name': 'Limonad classic', 'price': 16000, 'is_popular': True, 'description': 'Limon, yalpiz va muz bilan tayyorlangan tetiklantiruvchi ichimlik.'},
            {'name': 'Moxito', 'price': 19000, 'description': 'Yalpiz, лайм va gazli asos bilan tayyorlangan alkogolsiz moxito.'},
            {'name': 'Ays tea shaftoli', 'price': 15000, 'description': 'Sovuq shaftolili choy, muz bilan tortiladi.'},
            {'name': 'Amerikano', 'price': 14000, 'description': 'Tabiiy qovurilgan donlardan tayyorlangan qora qahva.'},
            {'name': 'Kapuchino', 'price': 18000, 'description': 'Espresso va sutli ko‘pik bilan tayyorlangan yumshoq qahva.'},
            {'name': 'Latte', 'price': 20000, 'description': 'Ko‘proq sut va yumshoq ta’mli qahva ichimligi.'},
            {'name': 'Ko‘k choy', 'price': 12000, 'description': 'Damlangan ko‘k choy choynakda beriladi.'},
            {'name': 'Qora choy', 'price': 10000, 'description': 'An’anaviy qora choy limon bilan yoki limonsiz.'},
            {'name': 'Apelsin fresh', 'price': 26000, 'description': '100% yangi siqilgan apelsin sharbati.'},
            {'name': 'Ayran', 'price': 13000, 'description': 'Yengil, salqin va milliy taomlarga juda mos ichimlik.'},
        ],
    },
]


def seed_catalog(apps, schema_editor):
    Category = apps.get_model('menu', 'Category')
    Product = apps.get_model('menu', 'Product')

    for category_data in CATALOG:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'icon': category_data['icon'],
                'order': category_data['order'],
            },
        )

        if created:
            category.icon = category_data['icon']
            category.order = category_data['order']
            category.save(update_fields=['icon', 'order'])

        for product_data in category_data['products']:
            Product.objects.update_or_create(
                category=category,
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'is_available': True,
                    'is_popular': product_data.get('is_popular', False),
                },
            )


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0002_reservation'),
    ]

    operations = [
        migrations.RunPython(seed_catalog, migrations.RunPython.noop),
    ]
