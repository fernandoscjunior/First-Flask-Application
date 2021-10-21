import os
from gamelist import app

def recupera_imagem(id):
    for nome_arquivos in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivos:
            return nome_arquivos


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))