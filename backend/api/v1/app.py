from backend.api.v1.views import app_views
from flask import Flask, make_response, jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger
import asyncio


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': str(error)}), 404)


app.config['SWAGGER'] = {
    'title': 'Moodify API',
    'uiversion': 1
}

Swagger(app)


if __name__ == '__main__':
    asyncio.run(app.run(host='0.0.0.0', port=5000, threaded=True))
