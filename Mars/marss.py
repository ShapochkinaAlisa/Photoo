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


@app.route('/carousel')
def carol():
    return '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Пейзажи Марса</title>
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha512-Dop/vW3iOtayerlYAqCgkVr2aTr2ErwwTYOvRFUpzl2VhCMJyjQF0Q9TjUXIo6JhuM/3i0vVEt2e/7QQmnHQqw==" crossorigin="anonymous">
  <!-- Дополнительные стили Bootstrap (не обязательно) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha512-iy8EXLW01a00b26BaqJWaCmk9fJ4PsMdgNRqV96KwMPSH+blO82OHzisF/zQbRIIi8m0PiO10dpS0QxrcXsisw==" crossorigin="anonymous">
  <!-- jQuery (необходим для Bootstrap JS) -->
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
  <!-- Bootstrap JS -->
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.4.1/js/bootstrap.min.js" integrity="sha512-oBTprMeNEKCnqfuqKd6sbvFzmFQtlXS3e0C/RGFV0hD6QzhHV+ODfaQbAlmY6/q0ubbwlAM/nCJjkrgA3waLzg==" crossorigin="anonymous"></script>
</head>
<body>
  <div class="container text-center">
    <h1 class="h3" style="margin-top: 20px; margin-bottom: 5px;">Пейзажи Марса</h1>

    <div id="carousel" class="carousel slide" data-ride="carousel" style="display: inline-block;">
        <div class="carousel-inner">
            <div class="item active">
                <img src="static/img/1.png" alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="item">
                <img src="static/img/2.png" alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="item">
                <img src="static/img/3.png" alt="здесь должна была быть картинка, но не нашлась">
            </div>
        </div>
        <!-- Элементы управления -->
        <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Предыдущий</span>
        </a>
        <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Следующий</span>
        </a>
    </div>
</div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
