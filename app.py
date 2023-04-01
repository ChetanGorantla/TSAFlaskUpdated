from flask import Flask, redirect, url_for
from views import views

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(views, url_prefix="/views")

@app.route('/')
def index():
    return redirect(url_for('views.index'))


if __name__ == '__main__':
    app.run(debug = True, port = 8000)

