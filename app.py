
from flask import Flask, render_template_string

app = Flask(__name__)

SITE_NAME = "Fresh Laundry"

SERVICES = [
    {"icon": "🧺", "name": "Стирка одежды",
     "description": "Бережная стирка повседневных вещей",
     "price": "350 ₽ / кг"},
    {"icon": "☁️", "name": "Сушка белья",
     "description": "Аккуратная сушка ваших вещей",
     "price": "150 ₽ / кг"},
    {"icon": "👔", "name": "Глажка",
     "description": "Опрятные вещи без лишних хлопот",
     "price": "250 ₽ / кг"},
    {"icon": "🛏️", "name": "Постельное бельё",
     "description": "Стирка комплектов постельного белья",
     "price": "450 ₽ / комплект"},
]

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1">
    <title>{{ site_name }} — Прачечная</title>
    <style>
        :root {
            --blue: #2563eb;
            --dark: #14243b;
            --muted: #64748b;
            --light: #f3f7fc;
        }

        * { box-sizing: border-box; }

        html { scroll-behavior: smooth; }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            color: var(--dark);
            background: white;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 22px 8%;
            background: white;
            border-bottom: 1px solid #edf0f5;
        }

        .logo {
            font-size: 23px;
            font-weight: 800;
            letter-spacing: -1px;
        }

        nav a {
            margin-left: 25px;
            text-decoration: none;
            color: var(--dark);
            font-size: 14px;
        }

        .hero {
            padding: 110px 8%;
            background: linear-gradient(
                120deg, #eef6ff, #ffffff
            );
        }

        .hero-content { max-width: 680px; }

        .tag {
            color: var(--blue);
            font-weight: bold;
            font-size: 14px;
        }

        h1 {
            font-size: clamp(38px, 6vw, 68px);
            letter-spacing: -2px;
            line-height: 1.1;
            margin: 20px 0;
        }

        .hero p {
            color: var(--muted);
            font-size: 18px;
            line-height: 1.7;
        }

        .btn {
            display: inline-block;
            background: var(--blue);
            color: white;
            padding: 16px 28px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 20px;
        }

        section { padding: 85px 8%; }

        .section-title {
            font-size: 36px;
            letter-spacing: -1px;
            margin-bottom: 12px;
        }

        .subtitle {
            color: var(--muted);
            margin-bottom: 35px;
        }

        .services {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
        }

        .service {
            border: 1px solid #e7edf5;
            border-radius: 16px;
            padding: 30px;
            background: white;
        }

        .service-icon { font-size: 35px; }

        .service h3 { margin-top: 24px; }

        .service p {
            color: var(--muted);
            line-height: 1.6;
            min-height: 52px;
        }

        .price {
            color: var(--blue);
            font-size: 21px;
            font-weight: bold;
            margin-top: 25px;
        }

        .advantages { background: var(--light); }

        .advantages-grid {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(200px, 1fr));
            gap: 25px;
        }

        .advantage {
            background: white;
            padding: 25px;
            border-radius: 14px;
        }

        .advantage p {
            color: var(--muted);
            line-height: 1.6;
        }

        .order {
            text-align: center;
            background: #14243b;
            color: white;
        }

        .order p { color: #cbd5e1; }

        footer {
            padding: 30px 8%;
            color: var(--muted);
            text-align: center;
            font-size: 14px;
        }

        @media (max-width: 600px) {
            header { padding: 20px 6%; }
            nav a { margin-left: 12px; }
            .hero { padding: 75px 6%; }
            section { padding: 65px 6%; }
            .section-title { font-size: 30px; }
        }
    </style>
</head>
<body>

<header>
    <div class="logo">{{ site_name }}</div>
    <nav>
        <a href="#services">Услуги</a>
        <a href="#advantages">О нас</a>
        <a href="#order">Заказ</a>
    </nav>
</header>

<div class="hero">
    <div class="hero-content">
        <div class="tag">ПРАЧЕЧНАЯ НОВОГО ФОРМАТА</div>
        <h1>Чистые вещи.<br>Больше свободного времени.</h1>
        <p>
            Доверьте нам стирку, сушку и глажку.
            Мы позаботимся о ваших вещах,
            пока вы занимаетесь важным.
        </p>
        <a href="#order" class="btn">Оформить заказ</a>
    </div>
</div>

<section id="services">
    <h2 class="section-title">Наши услуги</h2>
    <p class="subtitle">
        Простой и понятный уход за вашими вещами
    </p>

    <div class="services">
        {% for service in services %}
        <div class="service">
            <div class="service-icon">
                {{ service.icon }}
            </div>
            <h3>{{ service.name }}</h3>
            <p>{{ service.description }}</p>
            <div class="price">{{ service.price }}</div>
        </div>
        {% endfor %}
    </div>
</section>

<section class="advantages" id="advantages">
    <h2 class="section-title">Почему выбирают нас</h2>
    <p class="subtitle">
        Забота о вещах без лишних сложностей
    </p>

    <div class="advantages-grid">
        <div class="advantage">
            <h3>Бережный уход</h3>
            <p>Подбираем подходящий режим стирки.</p>
        </div>
        <div class="advantage">
            <h3>Удобный сервис</h3>
            <p>Простое оформление заказа онлайн.</p>
        </div>
        <div class="advantage">
            <h3>Понятные цены</h3>
            <p>Стоимость услуг известна заранее.</p>
        </div>
    </div>
</section>

<section class="order" id="order">
    <h2 class="section-title">Готовы освободить время?</h2>
    <p>
        Скоро здесь появится удобная форма заказа.
    </p>
    <a href="#services" class="btn">
        Посмотреть услуги
    </a>
</section>

<footer>
    © {{ site_name }}. Прачечная.
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        site_name=SITE_NAME,
        services=SERVICES
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
