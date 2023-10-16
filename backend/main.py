from flask import Flask
import os
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Recipe
from etxs import db


app = Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

api = Api(app, doc="/docs")

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# model (serializer)
recipe_model = api.model("Recipe",{
    "id": fields.Integer(),
    "title": fields.String(),
    "description": fields.String()
}
)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Recipe=Recipe)

if __name__ == '__main__':
    app.run()