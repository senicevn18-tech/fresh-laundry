
from flask import Flask, render_template_string

app = Flask(__name__)

# Основные настройки сайта
SITE_NAME = "Fresh Laundry"
CITY = "Кострома"
ADDRESS = "ул. Ерохова, 3А"
PHONE = "+7 920 380-20-97"
PHONE_LINK = "+79203802097"
WORK_HOURS = "9:00–18:00"
START_YEAR = "2016"

SERVICES = [
    {
        "number": "01",
        "name": "Стирка одежды",
        "description": (
            "Стирка повседневной одежды. "
            "Подробности обработки вещей и "
            "стоимость уточняйте по телефону."
        ),
        "icon": "✦"
    },
    {
        "number": "02",
        "name": "Сушка белья",
        "description": (
            "Услуга сушки белья после стирки. "
            "Условия и сроки выполнения "
            "уточняются при обращении."
        ),
        "icon": "◌"
    },
    {
        "number": "03",
        "name": "Постельное бельё",
        "description": (
            "Стирка постельного белья "
            "для частных клиентов, "
            "гостиниц и отелей."
        ),
        "icon": "▧"
    },
    {
        "number": "04",
        "name": "Глажка",
        "description": (
            "Услуги глажки белья и одежды. "
            "Возможность обработки конкретных "
            "вещей уточняйте заранее."
        ),
        "icon": "◇"
    }
]

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1">

<meta name="description"
      content="Fresh Laundry — прачечная в Костроме.
      Стирка, сушка и глажка белья.
      Работаем с 2016 года.">

<title>{{ name }} — Прачечная в Костроме</title>

<style>
:root {
    --navy: #142b43;
    --blue: #2876c7;
    --light: #f2f7fc;
    --white: #ffffff;
    --muted: #65778b;
    --border: #e2eaf2;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    color: var(--navy);
    background: var(--white);
}

a {
    text-decoration: none;
}

.container {
    max-width: 1200px;
    margin: auto;
    padding: 0 24px;
}

header {
    background: white;
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
}

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 85px;
    gap: 20px;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--navy);
}

.logo span {
    color: var(--blue);
}

nav {
    display: flex;
    align-items: center;
    gap: 25px;
}

nav a {
    color: var(--navy);
    font-size: 14px;
    font-weight: 500;
}

nav a:hover {
    color: var(--blue);
}

.nav-phone {
    color: var(--blue);
    font-weight: bold;
}

.hero {
    background: linear-gradient(
        115deg,
        #eaf4ff 0%,
        #f6faff 55%,
        #ffffff 100%
    );
    padding: 110px 0;
}

.hero-content {
    max-width: 760px;
}

.eyebrow {
    display: inline-block;
    color: var(--blue);
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

h1 {
    font-size: clamp(40px, 6vw, 70px);
    letter-spacing: -2.5px;
    line-height: 1.08;
    margin: 0 0 25px;
}

.hero p {
    font-size: 19px;
    color: var(--muted);
    line-height: 1.8;
    max-width: 590px;
}

.buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-top: 35px;
}

.btn {
    display: inline-block;
    padding: 17px 28px;
    border-radius: 9px;
    font-weight: 700;
    font-size: 15px;
    transition: 0.2s;
}

.btn-primary {
    background: var(--blue);
    color: white;
}

.btn-primary:hover {
    background: #175da5;
}

.btn-outline {
    border: 1px solid var(--blue);
    color: var(--blue);
}

.btn-outline:hover {
    background: #e5f1ff;
}

.hero-info {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin-top: 65px;
    color: var(--muted);
    font-size: 14px;
}

.hero-info strong {
    display: block;
    font-size: 22px;
    color: var(--navy);
    margin-bottom: 6px;
}

section {
    padding: 95px 0;
}

.section-head {
    max-width: 700px;
    margin-bottom: 45px;
}

.section-title {
    font-size: clamp(30px, 4vw, 44px);
    letter-spacing: -1.5px;
    margin: 0 0 18px;
}

.section-desc {
    color: var(--muted);
    font-size: 17px;
    line-height: 1.8;
}

.services-grid {
    display: grid;
    grid-template-columns:
        repeat(2, minmax(0, 1fr));
    gap: 22px;
}

.service-card {
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 35px;
    transition: 0.2s;
}

.service-card:hover {
    border-color: #a9cbea;
    transform: translateY(-3px);
}

.service-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 35px;
}

.service-number {
    font-size: 13px;
    color: var(--muted);
}

.service-icon {
    font-size: 34px;
    color: var(--blue);
}

.service-card h3 {
    font-size: 25px;
    margin: 0 0 15px;
}

.service-card p {
    color: var(--muted);
    line-height: 1.8;
    min-height: 75px;
}

.service-price {
    color: var(--blue);
    font-weight: bold;
    font-size: 15px;
    margin-top: 20px;
}

.about {
    background: var(--light);
}

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.about-box {
    background: var(--navy);
    color: white;
    padding: 60px;
    border-radius: 20px;
}

.about-box .big-year {
    font-size: 90px;
    font-weight: 800;
    letter-spacing: -5px;
}

.about-box p {
    color: #d4e2ef;
    line-height: 1.8;
}

.about-text p {
    color: var(--muted);
    line-height: 1.9;
    font-size: 17px;
}

.features {
    display: grid;
    grid-template-columns:
        repeat(3, minmax(0, 1fr));
    gap: 25px;
}

.feature {
    padding: 30px;
    border-radius: 15px;
    background: var(--light);
}

.feature h3 {
    font-size: 20px;
}

.feature p {
    color: var(--muted);
    line-height: 1.8;
}

.business {
    background: var(--navy);
    color: white;
}

.business .section-desc {
    color: #c8d6e5;
}

.business-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
}

.business-card {
    background: #203e5c;
    padding: 35px;
    border-radius: 18px;
}

.business-card p {
    color: #d4e2ef;
    line-height: 1.8;
}

.steps {
    display: grid;
    grid-template-columns:
        repeat(3, minmax(0, 1fr));
    gap: 30px;
}

.step {
    padding: 25px 0;
    border-top: 2px solid var(--blue);
}

.step-number {
    font-size: 35px;
    color: var(--blue);
    font-weight: bold;
}

.step h3 {
    font-size: 21px;
}

.step p {
    color: var(--muted);
    line-height: 1.8;
}

.faq {
    background: var(--light);
}

.faq-item {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 14px;
    padding: 22px 26px;
}

.faq-item summary {
    font-weight: bold;
    font-size: 17px;
    cursor: pointer;
}

.faq-item p {
    color: var(--muted);
    line-height: 1.8;
}

.contacts-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
}

.contact-item {
    margin-bottom: 30px;
}

.contact-label {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 8px;
}

.contact-value {
    font-size: 21px;
    font-weight: bold;
}

.contact-value a {
    color: var(--navy);
}

.map-link {
    display: inline-block;
    color: var(--blue);
    margin-top: 12px;
    font-weight: bold;
}

.contact-panel {
    background: var(--light);
    border-radius: 18px;
    padding: 40px;
}

.contact-panel p {
    color: var(--muted);
    line-height: 1.8;
}

footer {
    background: #0e2033;
    color: #b8c8d8;
    padding: 45px 0;
}

.footer-content {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
}

footer .logo {
    color: white;
}

footer p {
    font-size: 14px;
    line-height: 1.7;
}

@media (max-width: 850px) {
    .navbar {
        flex-wrap: wrap;
        padding: 20px 0;
    }

    nav {
        flex-wrap: wrap;
        gap: 15px;
    }

    .about-grid,
    .business-grid,
    .contacts-grid {
        grid-template-columns: 1fr;
    }

    .features,
    .steps {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 75px 0;
    }
}

@media (max-width: 600px) {
    .services-grid {
        grid-template-columns: 1fr;
    }

    section {
        padding: 65px 0;
    }

    .service-card {
        padding: 25px;
    }

    .about-box {
        padding: 35px;
    }

    .about-box .big-year {
        font-size: 65px;
    }

    .contact-panel {
        padding: 25px;
    }

    h1 {
        letter-spacing: -1.5px;
    }

    .hero-info {
        gap: 20px;
    }
}
</style>
</head>

<body>

<header>
    <div class="container navbar">
        <a href="/" class="logo">
            Fresh<span> Laundry</span>
        </a>

        <nav>
            <a href="#services">Услуги</a>
            <a href="#about">О нас</a>
            <a href="#delivery">Доставка</a>
            <a href="#business">Для бизнеса</a>
            <a href="#contacts">Контакты</a>
        </nav>

        <a class="nav-phone"
           href="tel:{{ phone_link }}">
            {{ phone }}
        </a>
    </div>
</header>

<main>

<div class="hero">
    <div class="container">
        <div class="hero-content">
            <span class="eyebrow">
                Прачечная в Костроме
            </span>

            <h1>
                Чистота вещей —
                наша работа.
            </h1>

            <p>
                Стирка, сушка и глажка белья
                для дома, гостиниц и отелей.
                Работаем в Костроме с 2016 года.
            </p>

            <div class="buttons">
                <a href="tel:{{ phone_link }}"
                   class="btn btn-primary">
                    Связаться с нами
                </a>

                <a href="#services"
                   class="btn btn-outline">
                    Наши услуги
                </a>
            </div>

            <div class="hero-info">
                <div>
                    <strong>С 2016 года</strong>
                    Работаем для вас
                </div>

                <div>
                    <strong>4 услуги</strong>
                    Стирка, сушка и глажка
                </div>

                <div>
                    <strong>Кострома</strong>
                    ул. Ерохова, 3А
                </div>
            </div>
        </div>
    </div>
</div>

<section id="services">
    <div class="container">

        <div class="section-head">
            <span class="eyebrow">Что мы предлагаем</span>
            <h2 class="section-title">Наши услуги</h2>

            <p class="section-desc">
                Услуги прачечной для частных
                клиентов и организаций.
                Условия и стоимость уточняются
                индивидуально.
            </p>
        </div>

        <div class="services-grid">
            {% for service in services %}
            <div class="service-card">

                <div class="service-top">
                    <span class="service-number">
                        {{ service.number }}
                    </span>

                    <span class="service-icon">
                        {{ service.icon }}
                    </span>
                </div>

                <h3>{{ service.name }}</h3>
                <p>{{ service.description }}</p>

                <div class="service-price">
                    Стоимость по запросу
                </div>

            </div>
            {% endfor %}
        </div>

    </div>
</section>

<section class="about" id="about">
    <div class="container about-grid">

        <div class="about-box">
            <div class="big-year">2016</div>
            <h2>Работаем с 2016 года</h2>

            <p>
                Прачечная Fresh Laundry
                находится в городе Костроме.
                Мы оказываем услуги
                стирки, сушки и глажки белья.
            </p>
        </div>

        <div class="about-text">
            <span class="eyebrow">О прачечной</span>

            <h2 class="section-title">
                Уход за бельём
                без лишних хлопот
            </h2>

            <p>
                Fresh Laundry — прачечная
                в Костроме, работающая
                с 2016 года.
            </p>

            <p>
                Мы принимаем заказы от
                частных клиентов, гостиниц
                и отелей.
            </p>

            <p>
                У нас можно заказать стирку
                одежды и постельного белья,
                сушку и глажку.
                Также доступна доставка.
            </p>

            <a href="#contacts"
               class="btn btn-primary">
                Наши контакты
            </a>
        </div>

    </div>
</section>

<section id="delivery">
    <div class="container">

        <div class="section-head">
            <span class="eyebrow">Удобство для клиентов</span>

            <h2 class="section-title">
                Доставка белья
            </h2>

            <p class="section-desc">
                Необязательно самостоятельно
                организовывать перевозку белья.
                В нашей прачечной доступна
                услуга доставки.
            </p>
        </div>

        <div class="features">
            <div class="feature">
                <h3>Забор белья</h3>
                <p>
                    Возможность забора вещей
                    уточняйте при обращении.
                </p>
            </div>

            <div class="feature">
                <h3>Стирка и обработка</h3>
                <p>
                    Выберите необходимые услуги:
                    стирку, сушку или глажку.
                </p>
            </div>

            <div class="feature">
                <h3>Возврат заказа</h3>
                <p>
                    Условия, стоимость и время
                    доставки согласовываются
                    по телефону.
                </p>
            </div>
        </div>

    </div>
</section>

<section class="business" id="business">
    <div class="container business-grid">

        <div>
            <span class="eyebrow">
                Для организаций
            </span>

            <h2 class="section-title">
                Услуги для гостиниц
                и отелей
            </h2>

            <p class="section-desc">
                Fresh Laundry работает
                не только с частными клиентами,
                но и с гостиницами и отелями.
            </p>

            <p class="section-desc">
                Для уточнения условий
                обслуживания, объёмов белья,
                сроков и стоимости
                свяжитесь с нами.
            </p>

            <a href="tel:{{ phone_link }}"
               class="btn btn-primary">
                Обсудить сотрудничество
            </a>
        </div>

        <div class="business-card">
            <h3>Услуги для бизнеса</h3>

            <p>Стирка постельного белья</p>
            <p>Сушка белья</p>
            <p>Глажка</p>
            <p>Доставка по согласованию</p>

            <p>
                Стоимость и условия
                обслуживания уточняются
                индивидуально.
            </p>
        </div>

    </div>
</section>

<section id="how">
    <div class="container">

        <div class="section-head">
            <span class="eyebrow">Порядок обращения</span>

            <h2 class="section-title">
                Как заказать услуги
            </h2>

            <p class="section-desc">
                Связаться с прачечной просто.
            </p>
        </div>

        <div class="steps">
            <div class="step">
                <div class="step-number">01</div>
                <h3>Позвоните нам</h3>

                <p>
                    Расскажите, какие вещи
                    необходимо постирать,
                    высушить или погладить.
                </p>
            </div>

            <div class="step">
                <div class="step-number">02</div>
                <h3>Уточните условия</h3>

                <p>
                    Согласуйте стоимость,
                    сроки и необходимость
                    доставки белья.
                </p>
            </div>

            <div class="step">
                <div class="step-number">03</div>
                <h3>Передайте бельё</h3>

                <p>
                    Уточните удобный способ
                    передачи белья и
                    дальнейшего получения заказа.
                </p>
            </div>
        </div>

    </div>
</section>

<section class="faq" id="faq">
    <div class="container">

        <div class="section-head">
            <span class="eyebrow">Полезная информация</span>

            <h2 class="section-title">
                Частые вопросы
            </h2>
        </div>

        <details class="faq-item">
            <summary>
                Сколько стоит стирка?
            </summary>

            <p>
                Стоимость зависит от услуги.
                Актуальные цены уточняйте
                по телефону {{ phone }}.
            </p>
        </details>

        <details class="faq-item">
            <summary>
                Есть ли доставка?
            </summary>

            <p>
                Да, услуга доставки доступна.
                Стоимость, территория
                обслуживания и условия
                согласовываются по телефону.
            </p>
        </details>

        <details class="faq-item">
            <summary>
                Работаете ли вы с гостиницами?
            </summary>

            <p>
                Да, прачечная принимает
                обращения от гостиниц и отелей.
            </p>
        </details>

        <details class="faq-item">
            <summary>
                Сколько времени занимает стирка?
            </summary>

            <p>
                Срок выполнения заказа
                необходимо уточнить при обращении.
            </p>
        </details>

        <details class="faq-item">
            <summary>
                Где находится прачечная?
            </summary>

            <p>
                Кострома, улица Ерохова, 3А.
            </p>
        </details>

    </div>
</section>

<section id="contacts">
    <div class="container">

        <div class="section-head">
            <span class="eyebrow">Связаться с нами</span>

            <h2 class="section-title">
                Контакты
            </h2>
        </div>

        <div class="contacts-grid">

            <div>
                <div class="contact-item">
                    <div class="contact-label">
                        Телефон
                    </div>

                    <div class="contact-value">
                        <a href="tel:{{ phone_link }}">
                            {{ phone }}
                        </a>
                    </div>
                </div>

                <div class="contact-item">
                    <div class="contact-label">
                        Адрес
                    </div>

                    <div class="contact-value">
                        {{ city }}, {{ address }}
                    </div>

                    <a class="map-link"
                       target="_blank"
                       rel="noopener noreferrer"
                       href="https://yandex.ru/maps/?text=Кострома%20Ерохова%203А">
                        Посмотреть на карте
                    </a>
                </div>

                <div class="contact-item">
                    <div class="contact-label">
                        Время работы
                    </div>

                    <div class="contact-value">
                        {{ hours }}
                    </div>

                    <p style="color:var(--muted)">
                        Дни работы уточняйте
                        по телефону.
                    </p>
                </div>
            </div>

            <div class="contact-panel">
                <h3>Остались вопросы?</h3>

                <p>
                    Позвоните нам, чтобы узнать
                    стоимость услуг, сроки
                    выполнения заказа
                    и условия доставки.
                </p>

                <a href="tel:{{ phone_link }}"
                   class="btn btn-primary">
                    Позвонить
                </a>

                <p>
                    {{ city }}, {{ address }}
                </p>
            </div>

        </div>

    </div>
</section>

</main>

<footer>
    <div class="container footer-content">

        <div>
            <div class="logo">
                Fresh<span> Laundry</span>
            </div>

            <p>
                Прачечная в Костроме.
                Работаем с 2016 года.
            </p>
        </div>

        <div>
            <p>{{ city }}, {{ address }}</p>
            <p>{{ phone }}</p>
            <p>Время работы: {{ hours }}</p>
        </div>

        <div>
            <p>© {{ name }}</p>
            <p>Информация о ценах уточняется.</p>
        </div>

    </div>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        name=SITE_NAME,
        city=CITY,
        address=ADDRESS,
        phone=PHONE,
        phone_link=PHONE_LINK,
        hours=WORK_HOURS,
        services=SERVICES
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
