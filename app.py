
from flask import Flask, render_template_string

app = Flask(__name__)

SITE_NAME = "Fresh Laundry"
PHONE = "+7 920 380-20-97"
PHONE_LINK = "+79203802097"

SERVICES = [
    ("Стирка одежды", "Стирка повседневной одежды.", "🧺"),
    ("Сушка белья", "Сушка белья. Сроки уточняются.", "☁️"),
    ("Постельное бельё", "Стирка белья для дома и гостиниц.", "🛏️"),
    ("Глажка", "Глажка одежды и белья.", "👔")
]

IMAGES = [
    "https://images.unsplash.com/photo-1517677208171-0bc6725a3e60?w=800",
    "https://images.unsplash.com/photo-1545173168-9f1947eebb7f?w=800",
    "https://images.unsplash.com/photo-1489274495757-95c7c837b101?w=800",
    "https://images.unsplash.com/photo-1521656693074-0ef32e80a5d5?w=800"
]

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ name }} — Прачечная в Костроме</title>

<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
:root {
    --blue: #236db5;
    --dark: #13283e;
    --light: #edf6fd;
    --gray: #607184;
}
* {box-sizing:border-box}
html {scroll-behavior:smooth}
body {
    margin:0;
    font-family:Manrope,Arial,sans-serif;
    color:var(--dark);
}
a {text-decoration:none;color:inherit}
.container {
    max-width:1200px;
    margin:auto;
    padding:0 24px;
}
header {
    position:sticky;
    top:0;
    z-index:100;
    background:white;
    border-bottom:1px solid #e2eaf0;
}
.navbar {
    min-height:80px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:20px;
}
.logo {
    font-size:24px;
    font-weight:800;
}
.logo span {color:var(--blue)}
nav {display:flex;gap:22px}
nav a {font-size:14px;font-weight:600}
nav a:hover {color:var(--blue)}
.menu-button {display:none}
.hero {
    background:var(--light);
    padding:80px 0;
}
.hero-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:50px;
    align-items:center;
}
.tag {
    color:var(--blue);
    font-size:13px;
    font-weight:800;
    letter-spacing:2px;
    text-transform:uppercase;
}
h1 {
    font-size:clamp(40px,5vw,68px);
    letter-spacing:-2px;
    line-height:1.1;
}
h2 {
    font-size:clamp(30px,4vw,44px);
    letter-spacing:-1px;
}
p {line-height:1.8}
.muted {color:var(--gray)}
.hero p {font-size:18px}
.hero img {
    width:100%;
    height:450px;
    object-fit:cover;
    border-radius:22px;
    box-shadow:0 20px 50px #12345622;
}
.btn {
    display:inline-block;
    padding:16px 26px;
    background:var(--blue);
    color:white;
    border-radius:10px;
    font-weight:700;
    margin-top:20px;
    transition:.25s;
}
.btn:hover {
    transform:translateY(-4px);
    background:#185995;
}
.btn-outline {
    background:white;
    color:var(--blue);
    border:1px solid var(--blue);
    margin-left:10px;
}
.btn-outline:hover {background:#e0efff}
section {padding:85px 0}
.cards {
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    margin-top:35px;
}
.card {
    border:1px solid #e2eaf0;
    border-radius:16px;
    overflow:hidden;
    transition:.3s;
}
.card:hover {
    transform:translateY(-8px);
    box-shadow:0 15px 40px #12345618;
}
.card img {
    width:100%;
    height:180px;
    object-fit:cover;
}
.card-content {padding:22px}
.card h3 {font-size:19px}
.card p {font-size:14px;color:var(--gray)}
.price {color:var(--blue);font-weight:800}
.about {background:#f3f8fc}
.split {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:55px;
    align-items:center;
}
.split img {
    width:100%;
    height:380px;
    object-fit:cover;
    border-radius:20px;
}
.business {
    background:#142b43;
    color:white;
}
.business p {color:#c5d5e4}
.steps {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:25px;
    margin-top:40px;
}
.step {
    border-top:2px solid #73b3eb;
    padding-top:20px;
}
.step b {font-size:30px;color:#82c0f5}
.faq {background:#f3f8fc}
details {
    padding:20px;
    margin:12px 0;
    border:1px solid #e2eaf0;
    border-radius:12px;
    background:white;
}
summary {cursor:pointer;font-weight:700}
.contacts {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
}
.panel {
    background:var(--light);
    border-radius:16px;
    padding:35px;
}
footer {
    background:#0c2033;
    color:#c4d3e0;
    padding:40px 0;
}
.reveal {
    opacity:0;
    transform:translateY(30px);
    transition:opacity .7s,transform .7s;
}
.reveal.visible {
    opacity:1;
    transform:none;
}
@media(prefers-reduced-motion:reduce) {
    .reveal {opacity:1;transform:none;transition:none}
}
@media(max-width:900px) {
    .hero-grid,.split {grid-template-columns:1fr}
    .cards {grid-template-columns:repeat(2,1fr)}
}
@media(max-width:650px) {
    .cards,.steps,.contacts {grid-template-columns:1fr}
    .menu-button {
        display:block;
        background:white;
        border:1px solid #ddd;
        border-radius:8px;
        padding:10px;
        font-size:20px;
    }
    nav {
        display:none;
        position:absolute;
        top:80px;
        left:0;
        right:0;
        padding:25px;
        background:white;
        flex-direction:column;
    }
    nav.open {display:flex}
    .hero img {height:280px}
    section {padding:60px 0}
    .btn-outline {margin-left:0}
}
</style>
</head>

<body>
<header>
<div class="container navbar">
    <a href="#" class="logo">Fresh<span> Laundry</span></a>
    <button class="menu-button" id="menuButton"
            aria-label="Открыть меню"
            aria-expanded="false">☰</button>
    <nav id="nav">
        <a href="#services">Услуги</a>
        <a href="#about">О нас</a>
        <a href="#delivery">Доставка</a>
        <a href="#business">Для гостиниц</a>
        <a href="#contacts">Контакты</a>
    </nav>
</div>
</header>

<main>
<div class="hero">
<div class="container hero-grid">
    <div>
        <span class="tag">Прачечная в Костроме</span>
        <h1>Чистые вещи.<br>Больше времени для себя.</h1>
        <p class="muted">
            Стирка, сушка и глажка белья для частных
            клиентов, гостиниц и отелей.
            Работаем с 2016 года.
        </p>
        <a class="btn" href="tel:{{ phone_link }}">
            Связаться с нами
        </a>
        <a class="btn btn-outline" href="#services">
            Наши услуги
        </a>
    </div>
    <img src="https://images.unsplash.com/photo-1545173168-9f1947eebb7f?w=1200"
         alt="Иллюстративное фото прачечной">
</div>
</div>

<section id="services">
<div class="container">
    <span class="tag">Наши услуги</span>
    <h2>Уход за вашими вещами</h2>
    <p class="muted">Стоимость и сроки уточняйте по телефону.</p>
    <div class="cards">
        {% for service in services %}
        <div class="card reveal">
            <img src="{{ images[loop.index0] }}"
                 alt="Иллюстрация услуги">
            <div class="card-content">
                <h3>{{ service[2] }} {{ service[0] }}</h3>
                <p>{{ service[1] }}</p>
                <div class="price">Цена по запросу</div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
</section>

<section class="about" id="about">
<div class="container split">
    <img class="reveal"
         src="https://images.unsplash.com/photo-1517677208171-0bc6725a3e60?w=1200"
         alt="Иллюстративное фото белья">
    <div class="reveal">
        <span class="tag">О прачечной</span>
        <h2>Работаем с 2016 года</h2>
        <p class="muted">
            Fresh Laundry — прачечная в Костроме
            по адресу улица Ерохова, 3А.
        </p>
        <p class="muted">
            Оказываем услуги стирки одежды,
            постельного белья, сушки и глажки.
            Работаем с частными клиентами,
            гостиницами и отелями.
        </p>
    </div>
</div>
</section>

<section id="delivery">
<div class="container split">
    <div class="reveal">
        <span class="tag">Доставка</span>
        <h2>Доставка белья</h2>
        <p class="muted">
            В прачечной доступна доставка.
            Условия, стоимость и возможность
            забора и возврата вещей уточняйте
            по телефону.
        </p>
        <a class="btn" href="tel:{{ phone_link }}">
            Уточнить доставку
        </a>
    </div>
    <img class="reveal"
         src="https://images.unsplash.com/photo-1489274495757-95c7c837b101?w=1200"
         alt="Иллюстративное фото чистого белья">
</div>
</section>

<section class="business" id="business">
<div class="container">
    <span class="tag">Для бизнеса</span>
    <h2>Стирка белья для гостиниц и отелей</h2>
    <p>
        Принимаем обращения от гостиниц и отелей.
        Объёмы, сроки, стоимость и условия доставки
        обсуждаются индивидуально.
    </p>
    <a class="btn" href="tel:{{ phone_link }}">
        Обсудить сотрудничество
    </a>
    <div class="steps">
        <div class="step reveal">
            <b>01</b>
            <h3>Свяжитесь с нами</h3>
            <p>Расскажите, какие услуги вам нужны.</p>
        </div>
        <div class="step reveal">
            <b>02</b>
            <h3>Уточните условия</h3>
            <p>Согласуйте стоимость и сроки.</p>
        </div>
        <div class="step reveal">
            <b>03</b>
            <h3>Передайте бельё</h3>
            <p>Договоритесь о передаче заказа.</p>
        </div>
    </div>
</div>
</section>

<section class="faq">
<div class="container">
    <h2>Частые вопросы</h2>
    <details>
        <summary>Сколько стоит стирка?</summary>
        <p>Актуальные цены уточняйте по телефону.</p>
    </details>
    <details>
        <summary>Есть ли доставка?</summary>
        <p>Да, условия доставки уточняются при обращении.</p>
    </details>
    <details>
        <summary>Сколько времени занимает заказ?</summary>
        <p>Срок выполнения зависит от заказа.</p>
    </details>
    <details>
        <summary>Работаете с гостиницами?</summary>
        <p>Да, принимаем обращения от гостиниц и отелей.</p>
    </details>
</div>
</section>

<section id="contacts">
<div class="container">
    <span class="tag">Контакты</span>
    <h2>Мы в Костроме</h2>
    <div class="contacts">
        <div class="panel reveal">
            <h3>Наш адрес</h3>
            <p>Кострома, улица Ерохова, 3А</p>
            <h3>Время работы</h3>
            <p>9:00–18:00 (дни уточняются)</p>
            <h3>Телефон</h3>
            <p>{{ phone }}</p>
            <a class="btn" href="tel:{{ phone_link }}">
                Позвонить
            </a>
        </div>
        <div class="panel reveal">
            <h3>Как нас найти</h3>
            <p>Откройте адрес в Яндекс Картах.</p>
            <a class="btn" target="_blank"
               rel="noopener noreferrer"
               href="https://yandex.ru/maps/?text=Кострома%20Ерохова%203А">
                Открыть карту
            </a>
        </div>
    </div>
</div>
</section>
</main>

<footer>
<div class="container">
    <h3>{{ name }}</h3>
    <p>Прачечная в Костроме. Работаем с 2016 года.</p>
    <p>ул. Ерохова, 3А · {{ phone }}</p>
    <p>Фотографии на сайте иллюстративные.</p>
</div>
</footer>

<script>
const btn = document.getElementById("menuButton");
const nav = document.getElementById("nav");

btn.addEventListener("click", () => {
    const opened = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", String(opened));
    btn.textContent = opened ? "✕" : "☰";
});

nav.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
        btn.textContent = "☰";
    });
});

const elements = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {threshold: 0.08});

    elements.forEach(el => observer.observe(el));
} else {
    elements.forEach(el => el.classList.add("visible"));
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        name=SITE_NAME,
        phone=PHONE,
        phone_link=PHONE_LINK,
        services=SERVICES,
        images=IMAGES
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
