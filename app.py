from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    # Default port is 5000
    # app.config['LIVESERVER_PORT'] = 8943
    # Default timeout is 5 seconds
    app.config['LIVESERVER_TIMEOUT'] = 10

    @app.route('/')
    def hello():
        return render_template('index.html')

    return app
