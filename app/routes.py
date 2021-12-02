from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ильфат Половинкин'}
    posts = [
        {
            'author': {'username': 'lebedev'},
            'body': 'Дизайн говно! Поиграй со шрифтами'
        },
        {
            'author': {'username': 'durov'},
            'body': 'я продал телеграм и все равно ввел рекламу }:]!'
        },
        {
            'author': {'username': 'anonymous'},
            'body': 'Я бы рассказал вам пасту про карпа, но ищите сами в архивах /b/'
        }
    ]
    return render_template('index.html', title='ЗАГОЛОВОК', user=user, posts=posts)