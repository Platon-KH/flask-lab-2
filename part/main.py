from flask import Flask
from flask_restx import Api
from part.lottery import api as lottery_api

app = Flask(__name__)

# Создаем API с документацией Swagger
api = Api(
    app,
    version='1.0',
    title='Лотерейный сервис API',
    description='Веб-сервис для управления лотерейными билетами (вариант 20)',
    doc='/docs'  # Документация будет доступна по адресу /docs
)

# Добавляем namespace лотереи
api.add_namespace(lottery_api, path='/api/lottery')

@app.route('/')
def index():
    return {
        'message': 'Лабораторная работа №2 - Лотерея (вариант 20)',
        'documentation': '/docs',
        'api': '/api/lottery/'
    }

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
