from model import Usuarios, Tarefas

#função para inserir um usuario
def inserir_usuario():
    usuario = Usuarios(nome='Lucas', email='lucas@gmail.com', senha=12345)
    usuario.save()
    # print(tarefa)

def listar_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

def consulta_usuario():
    usuario = Usuarios.query.filter_by(nome='Caroline').first()
    print(usuario.id)

def atualiza_usuario():
    usuario = Usuarios.query.filter_by(id=5).first()
    usuario.nome = "Talita"
    usuario.save()

def remover_usuario():
    usuario = Usuarios.query.filter_by(id=5).first()
    usuario.delete()

#função para inserir uma tarefa
def inserir_tarefa():
    tarefa = Tarefas(titulo='Estudar Java', fk_usuario_id=1)
    tarefa.save()
    print(tarefa)

def listar_tarefas():
    tarefas = Tarefas.query.all()
    print(tarefas)

def consulta_tarefa():
    tarefa = Tarefas.query.filter_by(titulo='Estudar Python').first()
    print(tarefa.id)

def atualiza_tarefa():
    tarefa = Tarefas.query.filter_by(id=1).first()
    tarefa.titulo = "Estudar React"
    tarefa.save()

def remover_tarefa():
    tarefa = Tarefas.query.filter_by(id=1).first()
    tarefa.delete()

if __name__ == '__main__':
    # inserir_usuario()
    # remover_usuario()
    # listar_usuarios()
    # atualiza_usuario()
    # consulta_usuario()
    inserir_tarefa()
    # remover_tarefa()
    # listar_tarefas()
    # atualiza_tarefa()
    # consulta_tarefa()