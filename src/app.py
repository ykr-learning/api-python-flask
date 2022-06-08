import json
from flask import Flask, jsonify, render_template, request

def create_app():
    app = Flask(__name__)

    stores = [
        {
            'name': 'My wonderful store',
            'items': [
                {
                    'name': 'My Item',
                    'price': 15.99
                }
            ]
        }
    ]

    @app.route('/')
    def home():
        return render_template('index.html'), 200

    @app.route('/store/', methods = ['POST'])
    def create_store():
        request_data = request.get_json()
        new_store = {
            'name': request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store), 201

    @app.route('/store/<string:name>')
    def get_store(name):
        for store in stores:
            if store['name'] == name:
                return jsonify(store), 200
        return jsonify({'message': 'store not found'}), 404

    @app.route('/store')
    def get_stores():
        return jsonify({'stores': stores}), 200

    @app.route('/store/<string:name>/item', methods = ['POST'])
    def create_item_in_store(name):
        request_data = request.get_json()
        for store in stores:
            if store['name'] == name:
                new_item = {
                    'name': request_data['name'],
                    'price': request_data['price']
                }
                store['items'].append(new_item)
                return jsonify(new_item), 201
        return jsonify({'message': 'store not found'}), 404

    @app.route('/store/<string:name>/item')
    def get_items_in_store(name):
        for store in stores:
            if store['name'] == name:
                return jsonify({'items': store['items']}), 200
        return jsonify({'message': 'store not found'}), 404

    return app

def start_app():
    myapp = create_app()
    myapp.run(port=5000)
