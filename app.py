from flask import *
from urls import URLS
from db import db
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3197@localhost/bh_sh'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()


@app.route('/createAlias', methods=['POST'])
def createAlias():
    if request.method == 'POST':
        body = request.form
        if body.get('alias'):
            alias = body.get('alias')
            url = body.get('url')
            if URLS.findURL(alias):
                return jsonify({
                    'msg': 'this short url exists',
                    'final_url': 'http://localhost:5000/{}'.format(URLS.findURL(alias).alias),
                    'url': URLS.findURL(alias).originalURL
                })
            new_alias = URLS(alias, url)
            new_alias.createAlias()
            return jsonify({
                'alias': alias,
                'final_url': 'http://localhost:5000/{}'.format(URLS.findURL(alias).alias),
                'url': URLS.findURL(alias).originalURL,
            })
        else:
            alias = str(uuid.uuid4())[:5]
            url = body.get('url')
            if URLS.findURL(alias):
                return jsonify({
                    'msg': 'this short url exists',
                    'final_url': 'http://localhost:5000/{}'.format(URLS.findURL(alias).alias),
                    'url': URLS.findURL(alias).originalURL
                })
            new_alias = URLS(alias, url)
            new_alias.createAlias()
            return jsonify({
                'alias': alias,
                'final_url': 'http://localhost:5000/{}'.format(URLS.findURL(alias).alias),
                'url': URLS.findURL(alias).originalURL,
            })


@app.route('/<alias>')
def enter_url(alias):
    if URLS.findURL(alias):
        get_url = URLS.findURL(alias).originalURL
        return redirect(get_url)
    else:
        return redirect('http://localhost:5000/home')


@app.route('/home')
def home():
    return 'hi. this is the best url shortener in the world'


if __name__ == '__main__':
    app.run()
