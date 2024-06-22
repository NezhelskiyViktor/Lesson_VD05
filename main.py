from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    parameters = {
        'for_name_page': 'Главная страница',
        'for_content': ['Добро пожаловать на главную страницу!',
                        'Здесь вы можете найти информацию о нашем сайте.',
                        'Но вы можете перейти на другую страницу.'],
        'for_link': 'Ссылка на страницу "О нас"',
        'link_url': '/about'
    }
    return render_template('home.html', **parameters)


@app.route('/about')
def about():
    parameters = {
        'for_name_page': 'О нас',
        'for_content': ['Мы - команда разработчиков,',
                        'создающая удивительные веб-приложения',
                        'с использованием '],
        'for_link': 'Ссылка на страницу "Главная"',
        'link_url': '/'
    }
    return render_template('about.html', **parameters)


if __name__ == "__main__":
    app.run(debug=True)
