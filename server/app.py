from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
api = Api(app)

db.init_app(app)

class messages(Resource):
    def get(self):
        messages = [message.to_dict() for message in Message.query.all()]
        return make_response(messages,200)

    def post(self):
        params = request.json
        new_message = Message(body=params['body'],username=params['username'])
        db.session.add(new_message)
        db.session.commit()
        return make_response(new_message.to_dict(),201)
api.add_resource(messages,'/messages')

# @app.route('/messages',)
# def messages():
#     return ''

class messages_by_id(Resource):
    def get(self,id):
        message = Messages.query.get(id)
        if not message:
            return make_response({'error':'message not found'},404)
        return make_response(message.to_dict(),200)
    def patch(self,id):
        message = Message.query.get(id)
        if not message:
            return make_response({'error':'message not found'},404)
        params = request.json
        for attr in params:
            setattr(message,attr,params[attr])
        db.session.commit()
        return make_response(message.to_dict(),200)
    def delete(self,id):
        message = Message.query.get(id)
        if not message:
            return make_response({'error':'message not found'},404)
        db.session.delete(message)
        db.session.commit()
        return make_response('',204)


api.add_resource(messages_by_id,'/messages/<id>')



# @app.route('/messages/<int:id>')
# def messages_by_id(id):
#     return ''

if __name__ == '__main__':
    app.run(port=5555)
