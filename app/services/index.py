from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..factories.factories import feed_basic_options
from ..controllers import IndexController

index = Blueprint('index', __name__)

@index.route('/', methods=GET)
def get_index():
    is_database_up, error = IndexController.test_connection()
    return jsonify({'version': '0.0.2', 'status': 'up' if is_database_up else 'down', 'error': error})

@index.route('/seed_database', methods=GET)
def seed_database():
    feed_basic_options()
    return jsonify({'working': 'hard'})