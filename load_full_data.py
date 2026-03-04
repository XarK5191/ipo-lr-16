import os
import django
import sys
import random

# Добавляем текущую папку в путь поиска
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Указываем правильный файл настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yogadoeba.settings')

# Инициализируем Django
django.setup()

# Теперь импортируем модели
from django.contrib.auth.models import User
from YogaShop.models import Category, Manufacturer, Product, Cart, CartItem

# ============================================
# 1. ИСПОЛЬЗУЕМ ВАШИХ ПРОИЗВОДИТЕЛЕЙ (5 шт)
# ============================================
# Получаем созданных вами производителей из БД
def get_manufacturers():
    manufacturers = list(Manufacturer.objects.all())
    if len(manufacturers) < 5:
        print("⚠️ Найдено меньше 5 производителей. Создаю недостающих...")
        # Создаем, если их меньше 5
        manufacturers_data = [
            {'name': 'Max', 'country': 'Беларусь'},
            {'name': 'MegaYog', 'country': 'Russia'},
            {'name': 'RoboPasha', 'country': 'Poland'},
            {'name': 'FitShapes', 'country': 'USA'},
            {'name': 'RoboPetya', 'country': 'Poland'},
        ]
        for m in manufacturers_data:
            man, created = Manufacturer.objects.get_or_create(
                name=m['name'],
                defaults={
                    'country': m['country'],
                    'description': f'Производитель {m["name"]}'
                }
            )
            if created:
                print(f"✅ Создан производитель: {man.name} ({man.country})")
        manufacturers = list(Manufacturer.objects.all())
    
    return manufacturers

# ============================================
# 2. КАТЕГОРИИ (10 шт)
# ============================================
categories_data = [
    {'name': 'Коврики для йоги', 'description': 'Профессиональные коврики для практики йоги различных толщин и материалов'},
    {'name': 'Одежда для йоги', 'description': 'Удобная и дышащая одежда для занятий йогой'},
    {'name': 'Аксессуары', 'description': 'Блоки, ремни, валики и другие полезные аксессуары для йоги'},
    {'name': 'Сумки и чехлы', 'description': 'Сумки и чехлы для переноски и хранения ковриков'},
    {'name': 'Коврики для путешествий', 'description': 'Легкие и компактные коврики для йоги в путешествиях'},
    {'name': 'Мячи для массажа', 'description': 'Массажные мячи для расслабления мышц и миофасциального релиза'},
    {'name': 'Книги по йоге', 'description': 'Книги по философии йоги, асанам и медитации'},
    {'name': 'Ароматерапия', 'description': 'Эфирные масла, свечи и диффузоры для создания атмосферы'},
    {'name': 'Подушки для медитации', 'description': 'Подушки и коврики для комфортной медитации'},
    {'name': 'Коврики для йоги (ковровое покрытие)', 'description': 'Мягкое покрытие для ковриков для дополнительного комфорта'}
]

# ============================================
# 3. ТОВАРЫ (34 шт) - распределяем по вашим производителям
# ============================================
# Функция для случайного выбора производителя из ваших
def get_random_manufacturer(manufacturers):
    return random.choice(manufacturers)

products_data = [
    # Коврики для йоги (6 шт)
    {
        'name': 'Коврик для йоги Премиум 6мм',
        'description': 'Профессиональный коврик для йоги. Отличное сцепление, плотный и устойчивый.',
        'price': 8990.00,
        'stock_quantity': 15,
        'category': 'Коврики для йоги',
    },
    {
        'name': 'Коврик эко 5мм',
        'description': 'Экологичный коврик из натурального каучука. Биоразлагаемый.',
        'price': 6990.00,
        'stock_quantity': 12,
        'category': 'Коврики для йоги',
    },
    {
        'name': 'Коврик Harmony 5мм',
        'description': 'Популярный коврик с отличной амортизацией.',
        'price': 6490.00,
        'stock_quantity': 20,
        'category': 'Коврики для йоги',
    },
    {
        'name': 'Коврик с разметкой',
        'description': 'Инновационный коврик с разметкой для правильной постановки рук и ног.',
        'price': 9990.00,
        'stock_quantity': 8,
        'category': 'Коврики для йоги',
    },
    {
        'name': 'Коврик для начинающих 6мм',
        'description': 'Качественный коврик для начинающих. Хорошее соотношение цены и качества.',
        'price': 3490.00,
        'stock_quantity': 30,
        'category': 'Коврики для йоги',
    },
    {
        'name': 'Коврик для путешествий 2мм',
        'description': 'Тонкий коврик для путешествий. Легко складывается.',
        'price': 4490.00,
        'stock_quantity': 18,
        'category': 'Коврики для путешествий',
    },
    
    # Одежда для йоги (8 шт)
    {
        'name': 'Леггинсы для йоги',
        'description': 'Мягкие леггинсы с высокой талией. Ощущение "второй кожи".',
        'price': 4990.00,
        'stock_quantity': 22,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Топ для йоги',
        'description': 'Спортивный топ со встроенным бюстгальтером.',
        'price': 3990.00,
        'stock_quantity': 18,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Шорты для йоги',
        'description': 'Свободные шорты из хлопка для горячей йоги.',
        'price': 2490.00,
        'stock_quantity': 25,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Штаны для йоги',
        'description': 'Широкие штаны из мягкого трикотажа для медитации.',
        'price': 3990.00,
        'stock_quantity': 12,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Футболка для йоги Ом',
        'description': 'Свободная футболка из органического хлопка с принтом Ом.',
        'price': 1990.00,
        'stock_quantity': 30,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Топ на широких бретелях',
        'description': 'Элегантный топ из переработанных материалов.',
        'price': 3290.00,
        'stock_quantity': 15,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Носки для йоги',
        'description': 'Носки с силиконовыми вставками против скольжения.',
        'price': 890.00,
        'stock_quantity': 40,
        'category': 'Одежда для йоги',
    },
    {
        'name': 'Толстовка после йоги',
        'description': 'Мягкая толстовка из флиса для расслабления после практики.',
        'price': 4490.00,
        'stock_quantity': 10,
        'category': 'Одежда для йоги',
    },
    
    # Аксессуары (8 шт)
    {
        'name': 'Блоки для йоги (2 шт)',
        'description': 'Легкие и прочные блоки из пеноматериала.',
        'price': 990.00,
        'stock_quantity': 45,
        'category': 'Аксессуары',
    },
    {
        'name': 'Ремень для йоги 2.5м',
        'description': 'Хлопковый ремень с металлической пряжкой.',
        'price': 790.00,
        'stock_quantity': 35,
        'category': 'Аксессуары',
    },
    {
        'name': 'Валик для йоги',
        'description': 'Мягкий валик для восстановительных практик.',
        'price': 2290.00,
        'stock_quantity': 12,
        'category': 'Аксессуары',
    },
    {
        'name': 'Полотенце для йоги',
        'description': 'Микрофибровое полотенце с силиконовыми вставками.',
        'price': 1490.00,
        'stock_quantity': 28,
        'category': 'Аксессуары',
    },
    {
        'name': 'Колесо для йоги',
        'description': 'Помогает раскрыть грудной отдел и улучшить гибкость спины.',
        'price': 1890.00,
        'stock_quantity': 15,
        'category': 'Аксессуары',
    },
    {
        'name': 'Эспандер для йоги',
        'description': 'Резиновый эспандер для усиления растяжки.',
        'price': 690.00,
        'stock_quantity': 40,
        'category': 'Аксессуары',
    },
    {
        'name': 'Глазной мешочек с лавандой',
        'description': 'Мешочек с лавандой для расслабления в шавасане.',
        'price': 590.00,
        'stock_quantity': 25,
        'category': 'Аксессуары',
    },
    {
        'name': 'Ковровое покрытие для коврика',
        'description': 'Мягкое покрытие, впитывает пот и предотвращает скольжение.',
        'price': 2490.00,
        'stock_quantity': 18,
        'category': 'Коврики для йоги (ковровое покрытие)',
    },
    
    # Сумки и чехлы (5 шт)
    {
        'name': 'Сумка для коврика базовая',
        'description': 'Простая сумка из натурального хлопка.',
        'price': 1290.00,
        'stock_quantity': 25,
        'category': 'Сумки и чехлы',
    },
    {
        'name': 'Сумка для коврика с карманами',
        'description': 'Сумка с карманами для телефона, ключей и бутылки.',
        'price': 2490.00,
        'stock_quantity': 18,
        'category': 'Сумки и чехлы',
    },
    {
        'name': 'Чехол для коврика',
        'description': 'Защитный чехол из плотного нейлона.',
        'price': 1590.00,
        'stock_quantity': 20,
        'category': 'Сумки и чехлы',
    },
    {
        'name': 'Рюкзак для йоги',
        'description': 'Рюкзак с отделением для коврика и ноутбука.',
        'price': 4990.00,
        'stock_quantity': 8,
        'category': 'Сумки и чехлы',
    },
    {
        'name': 'Сумка через плечо',
        'description': 'Небольшая сумка для аксессуаров.',
        'price': 1890.00,
        'stock_quantity': 15,
        'category': 'Сумки и чехлы',
    },
    
    # Книги и ароматерапия (5 шт)
    {
        'name': 'Йога-сутры Патанджали',
        'description': 'Классический текст по философии йоги.',
        'price': 590.00,
        'stock_quantity': 20,
        'category': 'Книги по йоге',
    },
    {
        'name': 'Свеча для медитации',
        'description': 'Натуральная соевая свеча с ароматом ладана.',
        'price': 890.00,
        'stock_quantity': 25,
        'category': 'Ароматерапия',
    },
    {
        'name': 'Эфирное масло лаванды',
        'description': '100% натуральное масло для релаксации.',
        'price': 490.00,
        'stock_quantity': 30,
        'category': 'Ароматерапия',
    },
    {
        'name': 'Диффузор',
        'description': 'Ультразвуковой диффузор для ароматерапии.',
        'price': 1990.00,
        'stock_quantity': 10,
        'category': 'Ароматерапия',
    },
    {
        'name': 'Подушка для медитации',
        'description': 'Подушка из гречихи для медитации.',
        'price': 2490.00,
        'stock_quantity': 12,
        'category': 'Подушки для медитации',
    },
    
    # Еще 2 товара до 34
    {
        'name': 'Массажный мяч двойной',
        'description': 'Двойной массажный мяч для спины и шеи.',
        'price': 890.00,
        'stock_quantity': 20,
        'category': 'Мячи для массажа',
    },
    {
        'name': 'Набор для йоги (блоки + ремень)',
        'description': 'Набор для начинающих: 2 блока и ремень.',
        'price': 1790.00,
        'stock_quantity': 15,
        'category': 'Аксессуары',
    }
]

# ============================================
# 4. ПОЛЬЗОВАТЕЛИ (5 шт) с корзинами
# ============================================
users_data = [
    {'username': 'Makson', 'email': 'maksik@example.com', 'password': 'yoga12345'},
    {'username': 'VladosChipinkos', 'email': 'vladosik@example.com', 'password': 'yoga12345'},
    {'username': 'Savchikrut', 'email': 'savchik@example.com', 'password': 'yoga12345'},
    {'username': 'Petyashara', 'email': 'petik@example.com', 'password': 'yoga12345'},
    {'username': 'Pavelin', 'email': 'pashik@example.com', 'password': 'yoga12345'},
]

# ============================================
# ФУНКЦИЯ ЗАГРУЗКИ ВСЕХ ДАННЫХ
# ============================================
def load_all_data():
    print("🚀 НАЧИНАЕМ ЗАГРУЗКУ ДАННЫХ ДЛЯ ЙОГА-МАГАЗИНА")
    print("=" * 60)
    
    # Получаем ваших производителей
    manufacturers = get_manufacturers()
    print(f"\n📋 ИСПОЛЬЗУЕМ ПРОИЗВОДИТЕЛЕЙ:")
    for m in manufacturers:
        print(f"   • {m.name} ({m.country})")
    
    # 2. СОЗДАЕМ КАТЕГОРИИ
    print("\n📁 СОЗДАЕМ КАТЕГОРИИ (10 шт)...")
    categories_created = 0
    for cat_data in categories_data:
        cat, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            categories_created += 1
            print(f"   ✅ {cat.name}")
        else:
            print(f"   ⚠️ Уже существует: {cat.name}")
    
    print(f"   📊 Итого: создано {categories_created} новых категорий")
    
    # 3. СОЗДАЕМ ТОВАРЫ (34 шт)
    print("\n🏷️ СОЗДАЕМ ТОВАРЫ (34 шт)...")
    products_created = 0
    products_skipped = 0
    
    for prod_data in products_data:
        try:
            # Получаем категорию
            category = Category.objects.get(name=prod_data['category'])
            
            # Случайно выбираем производителя из ваших
            manufacturer = random.choice(manufacturers)
            
            # Создаем товар
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock_quantity': prod_data['stock_quantity'],
                    'category': category,
                    'manufacturer': manufacturer,
                    'image': f"products/{prod_data['name'].lower().replace(' ', '_')}.jpg"
                }
            )
            
            if created:
                products_created += 1
                print(f"   ✅ {product.name} - {product.price}₽ (произв: {manufacturer.name})")
            else:
                products_skipped += 1
                print(f"   ⚠️ Уже существует: {prod_data['name']}")
                
        except Category.DoesNotExist:
            print(f"   ❌ Категория не найдена: {prod_data['category']}")
        except Exception as e:
            print(f"   ❌ Ошибка: {str(e)}")
    
    print(f"   📊 Итого: создано {products_created} товаров, пропущено {products_skipped}")
    
    # 4. СОЗДАЕМ ПОЛЬЗОВАТЕЛЕЙ И КОРЗИНЫ
    print("\n👥 СОЗДАЕМ ПОЛЬЗОВАТЕЛЕЙ (5 шт) И КОРЗИНЫ...")
    users_created = 0
    
    # Получаем все товары для корзин
    all_products = list(Product.objects.all())
    
    for user_data in users_data:
        # Создаем пользователя
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'is_active': True
            }
        )
        
        if created:
            user.set_password(user_data['password'])
            user.save()
            users_created += 1
            print(f"   ✅ Создан пользователь: {user.username}")
            
            # Создаем корзину для пользователя
            cart, cart_created = Cart.objects.get_or_create(user=user)
            
            if cart_created:
                # Добавляем случайные товары в корзину (2-4 позиции)
                num_items = random.randint(2, 4)
                selected_products = random.sample(all_products, min(num_items, len(all_products)))
                
                for product in selected_products:
                    quantity = random.randint(1, 3)
                    # Проверяем, что товара достаточно на складе
                    if quantity <= product.stock_quantity:
                        cart_item, item_created = CartItem.objects.get_or_create(
                            cart=cart,
                            product=product,
                            defaults={'quantity': quantity}
                        )
                        if item_created:
                            print(f"      🛒 Добавлен в корзину: {product.name} - {quantity} шт.")
        else:
            print(f"   ⚠️ Пользователь уже существует: {user.username}")
    
    print(f"   📊 Итого: создано {users_created} новых пользователей")
    
    print("\n" + "=" * 60)
    print("✅ ЗАГРУЗКА ЗАВЕРШЕНА!")
    print("=" * 60)
    
    # Итоговая статистика
    print("\n📊 ИТОГОВАЯ СТАТИСТИКА:")
    print(f"   Производители: {Manufacturer.objects.count()}")
    print(f"   Категории: {Category.objects.count()}")
    print(f"   Товары: {Product.objects.count()}")
    print(f"   Пользователи: {User.objects.count()}")
    print(f"   Корзины: {Cart.objects.count()}")
    print(f"   Позиции в корзинах: {CartItem.objects.count()}")

if __name__ == '__main__':
    load_all_data()