
from flask import Flask, render_template_string

app = Flask(__name__)

SITE_NAME = "Fresh Laundry"

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{ name }} — Прачечная</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5f9fc;
                color: #172b4d;
            }
            header {
                padding: 22px 8%;
                background: white;
                font-size: 24px;
                font-weight: bold;
            }
            main {
                text-align: center;
                padding: 90px 20px;
            }
            h1 {
                font-size: 44px;
                margin-bottom: 15px;
            }
            p {
                font-size: 18px;
                color: #526477;
            }
            .button {
                display: inline-block;
                margin-top: 25px;
                padding: 16px 32px;
                background: #1677d2;
                color: white;
                text-decoration: none;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <header>{{ name }}</header>
        <main>
            <h1>Чистые вещи без лишних забот</h1>
            <p>Профессиональная стирка, сушка и глажка одежды.</p>
            <a class="button" href="#services">Наши услуги</a>
        </main>
        <section id="services" style="text-align:center;padding:40px">
            <h2>Наши услуги</h2>
            <p>Стирка · Сушка · Глажка</p>
        </section>
    </body>
    </html>
    """, name=SITE_NAME)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
