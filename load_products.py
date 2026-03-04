import os
import django

# Настройка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yogadoeba.settings')
django.setup()

from YogaShop.models import Category, Manufacturer, Product

# Данные товаров для йога-магазина
products_data = [
    {
        'name': 'Коврик Manduka PRO',
        'description': 'Профессиональный коврик для йоги из натурального каучука. Толщина 6мм, отличное сцепление с полом. Премиум качество для серьезной практики.',
        'price': 7990.00,
        'stock_quantity': 15,
        'category': 'Коврики для йоги',
        'manufacturer': 'Manduka',
        'image': 'products/manduka_pro.jpg'
    },
    {
        'name': 'Коврик Jade Harmony',
        'description': 'Экологичный коврик из натурального каучука. Толщина 5мм, отличная амортизация. Самый популярный коврик среди инструкторов йоги.',
        'price': 5990.00,
        'stock_quantity': 20,
        'category': 'Коврики для йоги',
        'manufacturer': 'JadeYoga',
        'image': 'products/jade_harmony.jpg'
    },
    {
        'name': 'Коврик Liforme',
        'description': 'Инновационный коврик с разметкой для правильной постановки рук и ног. Выравнивание тела во время практики.',
        'price': 8990.00,
        'stock_quantity': 10,
        'category': 'Коврики для йоги',
        'manufacturer': 'Liforme',
        'image': 'products/liforme_mat.jpg'
    },
    {
        'name': 'Леггинсы для йоги',
        'description': 'Дышащие леггинсы с высокой талией из мягкого материала. Не сковывают движения, отводят влагу.',
        'price': 4990.00,
        'stock_quantity': 25,
        'category': 'Одежда для йоги',
        'manufacturer': 'Lululemon',
        'image': 'products/leggings.jpg'
    },
    {
        'name': 'Топ для йоги',
        'description': 'Удобный топ на тонких бретелях со встроенным бюстгальтером. Дышащий материал.',
        'price': 2990.00,
        'stock_quantity': 30,
        'category': 'Одежда для йоги',
        'manufacturer': 'Alo Yoga',
        'image': 'products/yoga_top.jpg'
    },
    {
        'name': 'Штаны для йоги',
        'description': 'Свободные штаны из хлопка с эластичным поясом. Идеальны для хатха-йоги и медитации.',
        'price': 3590.00,
        'stock_quantity': 18,
        'category': 'Одежда для йоги',
        'manufacturer': 'Pranamat',
        'image': 'products/yoga_pants.jpg'
    },
    {
        'name': 'Блоки для йоги (2 шт)',
        'description': 'Легкие и прочные блоки из пеноматериала. Помогают в выполнении асан, особенно для начинающих.',
        'price': 890.00,
        'stock_quantity': 50,
        'category': 'Аксессуары',
        'manufacturer': 'Gaiam',
        'image': 'products/yoga_blocks.jpg'
    },
    {
        'name': 'Ремень для йоги',
        'description': 'Хлопковый ремень с металлической пряжкой. Длина 2.5 метра. Помогает в растяжке и удержании поз.',
        'price': 690.00,
        'stock_quantity': 40,
        'category': 'Аксессуары',
        'manufacturer': 'Hugger Mugger',
        'image': 'products/yoga_strap.jpg'
    },
    {
        'name': 'Валик для йоги',
        'description': 'Мягкий валик для расслабления и восстановительных практик. Чехол съемный, легко стирается.',
        'price': 1990.00,
        'stock_quantity': 15,
        'category': 'Аксессуары',
        'manufacturer': 'Yogamatters',
        'image': 'products/bolster.jpg'
    },
    {
        'name': 'Сумка для коврика',
        'description': 'Удобная сумка из натурального хлопка для переноски коврика. Есть карман для телефона и ключей.',
        'price': 2490.00,
        'stock_quantity': 22,
        'category': 'Сумки и чехлы',
        'manufacturer': 'Manduka',
        'image': 'products/mat_bag.jpg'
    },
    {
        'name': 'Чехол для коврика',
        'description': 'Защитный чехол из плотной ткани. Подходит для ковриков до 6мм толщиной.',
        'price': 1590.00,
        'stock_quantity': 15,
        'category': 'Сумки и чехлы',
        'manufacturer': 'Gaiam',
        'image': 'products/mat_cover.jpg'
    },
    {
        'name': 'Полотенце для йоги',
        'description': 'Микрофибровое полотенце с силиконовыми вставками против скольжения. Размер 60x180см.',
        'price': 1290.00,
        'stock_quantity': 35,
        'category': 'Аксессуары',
        'manufacturer': 'JadeYoga',
        'image': 'products/yoga_towel.jpg'
    }
]

def load_products():
    print("🚀 Начинаем загрузку товаров для йога-магазина...")
    print("=" * 50)
    
    products_created = 0
    products_skipped = 0
    
    for product_data in products_data:
        try:
            # Получаем или создаем категорию
            category_name = product_data.pop('category')
            category, category_created = Category.objects.get_or_create(
                name=category_name,
                defaults={
                    'description': f'Категория {category_name} для йоги'
                }
            )
            if category_created:
                print(f"📁 Создана новая категория: {category_name}")
            
            # Получаем или создаем производителя
            manufacturer_name = product_data.pop('manufacturer')
            manufacturer, manufacturer_created = Manufacturer.objects.get_or_create(
                name=manufacturer_name,
                defaults={
                    'country': 'Не указана',
                    'description': f'Производитель {manufacturer_name}'
                }
            )
            if manufacturer_created:
                print(f"🏭 Создан новый производитель: {manufacturer_name}")
            
            # Извлекаем данные для товара
            name = product_data['name']
            description = product_data['description']
            price = product_data['price']
            stock = product_data['stock_quantity']
            image = product_data['image']
            
            # Создаем товар
            product, created = Product.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'price': price,
                    'stock_quantity': stock,
                    'category': category,
                    'manufacturer': manufacturer,
                    'image': image
                }
            )
            
            if created:
                products_created += 1
                print(f"✅ Создан товар: {name} - {price}₽ (в наличии: {stock})")
            else:
                products_skipped += 1
                print(f"⚠️ Товар уже существует: {name}")
                
        except Exception as e:
            print(f"❌ Ошибка при создании товара {product_data.get('name', 'Unknown')}: {str(e)}")
    
    print("=" * 50)
    print(f"📊 Итоги загрузки:")
    print(f"   ✅ Создано новых товаров: {products_created}")
    print(f"   ⚠️ Пропущено (уже существуют): {products_skipped}")
    print("=" * 50)

if __name__ == '__main__':
    load_products()