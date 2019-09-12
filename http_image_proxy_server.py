from flask import Flask
from flask import g
from flask import jsonify
from flask import render_template
from flask import request
from flask import send_file

from db import update_db, query_db
from image_processing import image_processing

app = Flask(__name__)


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
    query = 'UPDATE apicounter SET count = count + 1 WHERE api_name = ?'
    args = ('proxy',)
    update_db(query, args)

    if 'url' not in request.args:
        return render_template('empty.html'), 200

    url = request.args.get('url')

    img_io, message, message_code = image_processing(url)

    if message_code is False:
        return render_template('empty.html'), 200

    return send_file(img_io, mimetype='image/png', as_attachment=False)


@app.route('/admin', methods=['GET'])
def admin():
    query = 'SELECT count FROM apicounter WHERE api_name = ?'
    args = ('proxy',)
    proxy_query_count = query_db(query, args, one=True)

    return jsonify({
        'query_count': proxy_query_count
    })


if __name__ == '__main__':
    app.run(processes=3, threaded=False)
