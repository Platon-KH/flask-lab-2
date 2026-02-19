from flask_restx import fields

# Модель для одного билета лотереи
ticket_model = {
    'id': fields.String(required=True, description='Уникальный номер билета'),
    'number': fields.Integer(required=True, description='Номер билета (1-1000)'),
    'price': fields.Float(required=True, description='Цена билета'),
    'status': fields.String(required=True, description='Статус (продан/не продан/выигрышный)'),
    'purchase_date': fields.String(description='Дата покупки'),
    'owner_name': fields.String(description='Имя владельца'),
    'prize_amount': fields.Float(description='Сумма выигрыша')
}

# Модель для статистики лотереи
stats_model = {
    'total_tickets': fields.Integer(description='Всего билетов'),
    'sold_tickets': fields.Integer(description='Продано билетов'),
    'winning_tickets': fields.Integer(description='Выигрышных билетов'),
    'total_revenue': fields.Float(description='Общая выручка'),
    'total_prizes': fields.Float(description='Общая сумма выигрышей'),
    'min_price': fields.Float(description='Минимальная цена'),
    'max_price': fields.Float(description='Максимальная цена'),
    'avg_price': fields.Float(description='Средняя цена')
}

# Модель для сортировки
sort_model = {
    'field': fields.String(description='Поле для сортировки'),
    'order': fields.String(description='Порядок (asc/desc)')
}
