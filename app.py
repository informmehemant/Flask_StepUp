from flask import Flask, render_template, abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/500')
def error500():
    abort(500)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages/<int:idx>')
def messages(idx):
    app.logger.info('Building the message list...')
    messages = ['message 0', 'message 1', 'message 2', 'message 3']
    try:
        app.logger.debug('Get message with the index:{}'.format(idx))
        return render_template('messages.html', messages=messages[idx])
    except IndexError:
        abort(404)
           