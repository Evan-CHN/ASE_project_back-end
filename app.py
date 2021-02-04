from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from routes.user import UserRoute

app = Flask(__name__)
api = Api(app)

# solve cross-origin resource sharing
cors = CORS(app, resources={r"/routes/*": {"origins": "*"}})

# test code
api.add_resource(UserRoute, '/')

if __name__ == '__main__':
    app.run(debug=True)
