import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth


app = Flask(__name__)
setup_db(app)
CORS(app)


'''
#TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

# ROUTES

# get Drinks No Auth needed.


@app.route('/drinks')
def get_drinks():
    return jsonify({
        'success': True,
        'drinks': list(map(Drink.short, Drink.query.all()))
    }), 200


'''
#Get Drinks details
'''


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')  # permission
def get_drinks_details(token):
    return jsonify({
        'success': True,
        'drinks': list(map(Drink.long, Drink.query.all()))
    }), 200


'''
#Add a drink
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(token):
    if request.data:
        body = request.get_json()
        title = body.get('title', None)
        recipe = body.get('recipe', None)
        drink = Drink(title=title, recipe=json.dumps(recipe))
        Drink.insert(drink)
        new_drink = Drink.query.filter_by(id=drink.id).first()
        return jsonify({
            'success': True,
            'drinks': [new_drink.long()]
        })
    else:
        abort(422)


'''
Edit a drink
'''


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drink(token, drink_id):
    data = request.get_json()
    title = data.get('title', None)
    recipe = data.get('recipe', None)
    try:
        drink = Drink.query.filter_by(id=drink_id).one_or_none()
        if drink is None:
            abort(404)
        if recipe is not None:
            drink.recipe = json.dumps(recipe)
        if title is None:
            abort(400)
        else:
            drink.title = title

        drink.update()
        patched_drink = Drink.query.filter_by(id=drink_id).first()
        return jsonify({
            'success': True,
            'drinks': [patched_drink.long()]
        })
    except Exception:
        abort(422)


'''
Delete a drink
'''


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(token, drink_id):
    try:
        drink = Drink.query.filter_by(id=drink_id).one_or_none()
        if drink is None:
            abort(404)
        drink.delete()
        return jsonify({
            'success': True,
            'deleted': drink_id
        })
    except Exception:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
error handler should conform to general task above
'''


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
    }, 401)
