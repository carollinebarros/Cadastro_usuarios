from flask import Flask
from flask_restful import Resource, Api
from model import Usuarios

app = Flask(__name__)
api = Api(app)

class Usuario(Resource):
    def get(self, id):
        try:
            usuario = Usuarios.query.filter_by(id=id).first()
            response = {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email,
                'senha': usuario.senha
            }
            return response
        except:
            return {'ERROR': 'Usuario inexistente!'}

class Listar_usuarios(Resource):
   # def get(self):
   # usuarios = Usuarios.query.all()
   # return usuarios
   def post(self):
       usuario = Usuarios(nome='Carol', email='teste@gmail.com', senha=654321)
       usuario.save()


api.add_resource(Usuario, '/usuarios/<int:id>')
api.add_resource(Listar_usuarios, '/usuarios')

if __name__ == '__main__':
    app.run(debug=True)

