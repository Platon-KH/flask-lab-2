from flask_restx import Namespace, Resource, fields
from .models import ticket_model, stats_model
import random
from datetime import datetime

# Создаем namespace для лотереи
api = Namespace('lottery', description='Операции с лотерейными билетами')

# Определяем модели для Swagger
ticket = api.model('Ticket', ticket_model)
stats = api.model('Stats', stats_model)

# Хранилище данных (в памяти)
tickets = [
    {
        'id': 'T001',
        'number': 1,
        'price': 100.0,
        'status': 'sold',
        'purchase_date': '2025-12-20',
        'owner_name': 'Иван Петров',
        'prize_amount': 0.0
    },
    {
        'id': 'T002',
        'number': 2,
        'price': 100.0,
        'status': 'winning',
        'purchase_date': '2025-12-21',
        'owner_name': 'Мария Сидорова',
        'prize_amount': 5000.0
    },
    {
        'id': 'T003',
        'number': 3,
        'price': 100.0,
        'status': 'available',
        'purchase_date': None,
        'owner_name': None,
        'prize_amount': 0.0
    }
]

@api.route('/tickets')
class TicketList(Resource):
    @api.doc('list_tickets')
    @api.marshal_list_with(ticket)
    def get(self):
        """Получить список всех билетов"""
        return tickets
    
    @api.doc('create_ticket')
    @api.expect(ticket)
    @api.marshal_with(ticket, code=201)
    def post(self):
        """Создать новый билет"""
        new_ticket = api.payload
        new_ticket['id'] = f"T{len(tickets)+1:03d}"
        tickets.append(new_ticket)
        return new_ticket, 201

@api.route('/tickets/<string:id>')
@api.response(404, 'Билет не найден')
@api.param('id', 'Идентификатор билета')
class TicketResource(Resource):
    @api.doc('get_ticket')
    @api.marshal_with(ticket)
    def get(self, id):
        """Получить билет по ID"""
        for ticket in tickets:
            if ticket['id'] == id:
                return ticket
        api.abort(404, f"Билет {id} не найден")
    
    @api.doc('update_ticket')
    @api.expect(ticket)
    @api.marshal_with(ticket)
    def put(self, id):
        """Обновить билет"""
        for i, ticket in enumerate(tickets):
            if ticket['id'] == id:
                updated = api.payload
                updated['id'] = id
                tickets[i] = updated
                return updated
        api.abort(404, f"Билет {id} не найден")
    
    @api.doc('delete_ticket')
    @api.response(204, 'Билет удален')
    def delete(self, id):
        """Удалить билет"""
        global tickets
        tickets = [t for t in tickets if t['id'] != id]
        return '', 204

@api.route('/stats')
class TicketStats(Resource):
    @api.doc('get_stats')
    @api.marshal_with(stats)
    def get(self):
        """Получить статистику по лотерее"""
        total = len(tickets)
        sold = sum(1 for t in tickets if t['status'] == 'sold')
        winning = sum(1 for t in tickets if t['status'] == 'winning')
        revenue = sum(t['price'] for t in tickets if t['status'] in ['sold', 'winning'])
        prizes = sum(t['prize_amount'] for t in tickets)
        prices = [t['price'] for t in tickets]
        
        return {
            'total_tickets': total,
            'sold_tickets': sold,
            'winning_tickets': winning,
            'total_revenue': revenue,
            'total_prizes': prizes,
            'min_price': min(prices) if prices else 0,
            'max_price': max(prices) if prices else 0,
            'avg_price': sum(prices)/len(prices) if prices else 0
        }

@api.route('/tickets/sort/<string:field>')
@api.param('field', 'Поле для сортировки (price, number, status)')
@api.param('order', 'Порядок сортировки (asc/desc)')
class TicketSort(Resource):
    @api.doc('sort_tickets')
    @api.marshal_list_with(ticket)
    def get(self, field):
        """Сортировать билеты по указанному полю"""
        order = api.payload.get('order', 'asc') if api.payload else 'asc'
        
        valid_fields = ['price', 'number', 'status']
        if field not in valid_fields:
            api.abort(400, f"Поле должно быть одним из: {valid_fields}")
        
        sorted_tickets = sorted(tickets, 
                               key=lambda x: x.get(field, ''),
                               reverse=(order == 'desc'))
        return sorted_tickets
