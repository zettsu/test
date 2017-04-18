# auth.py

from flask import Blueprint
from flask import request, url_for, redirect, make_response

# extensions and tools

from flask import json, jsonify
from flask.ext.responses import json_response, xml_response, auto_response

# models

#from models.User_model import Users

from helpers.errors import InvalidUsage

# Blueprints 

apiBlueprint = Blueprint("API", __name__)

@apiBlueprint.route("/<int:id>",methods=['GET'])
def test(id):
	
	actions = { 
		'system': { 
			'tickets': { 
				'add': True, 
				'remove' : True, 
				'modify' : True, 
				'list': True 
			} 
		}
	}

	userdata = {
		'permissions' : 777,
		'role' : 'admin',
		'username' : 'test',
		'actions' : actions
	}

	data = { 'id': id }

	return jsonify(response = data, status_code=200)


@apiBlueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@apiBlueprint.app_errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'No se ha encontrado el metodo.'}), 404)

@apiBlueprint.app_errorhandler(500)
def internalError(error):
    return make_response(jsonify({'error': 'Se ha producido un erorr en el servidor, intente nuevamente.'}), 500)