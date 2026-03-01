from flask import render_template
from flask import Flask
from flask_restx import Api
from part.lottery import api as lottery_api

app = Flask(__name__)

# API с документацией Swagger
api = Api(
    app,
    version='1.0',
    title='Лотерейный сервис API',
    description='Веб-сервис для управления лотерейными билетами (вариант 20)',
    doc='/docs'  # Документация будет доступна по адресу /docs
)

# namespace лотереи
api.add_namespace(lottery_api, path='/api/lottery')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
