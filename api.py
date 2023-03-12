from flask import Flask, request
from flask_restx import Api, Resource, fields
from apiDao import TodoDAO
from redisDao import RedisDao
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )

ns = api.namespace('chavesUsuarios', description='Usuario operations')

# user_fields = api.model('User', {
#     'id': fields.Integer,
#     'name': fields.String,
# })


chaveUsuario = api.model('Todo', {
    'chave': fields.String(required=True, description='The task unique identifier'),
    'email': fields.String(required=True, description='The task details'),
    'role': fields.String(required=True, description='The task details'),
})

listaKeys = api.model('ListaKeys',{
    'lista': fields.List(fields.String)
})

redisDao = RedisDao()

DAO = TodoDAO(api)
DAO.create({'chave': 'f111', 'email': 'teste@teste.com', 'role': 'admin'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(listaKeys)
    def get(self):
        '''List all tasks'''
        return redisDao.listarTodasKeys()

    @ns.doc('create_todo')
    @ns.expect(chaveUsuario)
    @ns.marshal_with(chaveUsuario, code=201)
    def post(self):
        '''Create a new task'''
        redisDao.inserirKey(api.payload)
        return api.payload, 201


@ns.route('/<string:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(chaveUsuario)
    def get(self, id):
        '''Fetch a given resource'''
        return redisDao.consultarKey(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        redisDao.deletarKey(id)
        return '', 204

    @ns.expect(chaveUsuario)
    @ns.marshal_with(chaveUsuario)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
