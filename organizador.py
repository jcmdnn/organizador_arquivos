import os

os.chdir(r"")  # Adicionar caminho pasta que deseja organizar os arquivos
lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]
set_extensoes = {tipo.split('.')[-1] for tipo in lista_arquivos}

for tipo in set_extensoes:
    if os.path.exists(tipo):
        pass
    else:
        os.mkdir(tipo)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split('.')[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)
