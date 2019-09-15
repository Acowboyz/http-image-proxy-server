import os

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import send_file
from flask_sqlalchemy import SQLAlchemy
from flask import g

from db import update_db, query_db
from image_processing import image_processing

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'data.db'
DEBUG = False

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# create app

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)

import models


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.errorhandler(404)
def page_not_found(e):
    """
    error handler for web app (flask, sanic)
    :return: Not found
    """

    return render_template('404.html'), 404


@app.route('/proxy', methods=['GET'])
def proxy():
    db.session.query(models.APICounter.count).filter_by(api_name='proxy').update({'count': models.APICounter.count + 1})

    db.session.commit()
    # query = 'UPDATE apicounter SET count = count + 1 WHERE api_name = ?'
    # args = ('proxy',)
    # update_db(query, args)

    if 'url' not in request.args:
        return render_template('empty.html'), 200

    url = request.args.get('url')

    img_io, message, message_code = image_processing(url)

    if message_code is False:
        return render_template('empty.html'), 200

    return send_file(img_io, mimetype='image/png', as_attachment=False)


@app.route('/admin', methods=['GET'])
def admin():
    count = db.session.query(models.APICounter.count).filter_by(api_name='proxy').first()
    # query = 'SELECT count FROM apicounter WHERE api_name = ?'
    # args = ('proxy',)
    # proxy_query_count = query_db(query, args, one=True)

    return jsonify({
        'query_count': count
    })


if __name__ == '__main__':
    app.run()
