# Лабораторная работа №2
## Веб-сервис "Лотерея" (вариант 20)

### Описание
RESTful веб-сервис для управления лотерейными билетами с автоматической документацией Swagger.

### Функциональность
- CRUD операции с билетами
- Сортировка по полям (price, number, status)
- Статистика (мин, макс, среднее)
- Документация Swagger по адресу /docs

### Запуск
```bash
pip install -r requirements.txt
python main.py

### Документация API
После запуска перейти по адресу: http://127.0.0.1:5000/docs

### Доступные эндпоинты
Метод	Эндпоинт	Описание
GET	/api/lottery/tickets	Все билеты
POST	/api/lottery/tickets	Создать билет
GET	/api/lottery/tickets/{id}	Билет по ID
PUT	/api/lottery/tickets/{id}	Обновить билет
DELETE	/api/lottery/tickets/{id}	Удалить билет
GET	/api/lottery/stats	Статистика
GET	/api/lottery/tickets/sort/{field}	Сортировка (возр.)
GET	/api/lottery/tickets/sort/{field}/desc	Сортировка (убыв.)

### Структура проекта
lab2-lottery/
├── part/
│   ├── lottery.py
│   └── models.py
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
└── README.md
