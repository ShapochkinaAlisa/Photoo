from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def first():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/marss.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 style="color: red"> Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='img/marss.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из дерева.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаеи обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1')
