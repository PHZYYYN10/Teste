class motorista:
    def __init__(self,nome,codigo,telefone,disponivel:bool):
        self.nome=nome
        self.codigo=codigo
        self.telefone=telefone
        self.disponivel=disponivel
    def mostrar_dados(self):
        if self.disponivel is True:
            self.status="disponivel"
        else:
            self.status="Não esta disponivel!"    
        return f"O motorista {self.nome},com o id de {self.codigo},com o numero {self.telefone},esta {self.status}"
        
    def alterar_disponiblidade(self):
        print("Alterar disponiblidade:")
        if self.disponivel is False:
            self.status="O taxi já esta disponivel!"
            self.disponivel=True
        else:
            self.status="O taxi não esta mais disponivell!"
            self.disponivel=True




class passageiro:
    def __init__(self,nome,telefone,codigo):
        super().__init__(nome,telefone,codigo)

    def mostrar_dados(self):
        print("Dados do passageiro")
        return f"O passageiro {self.nome} tem o codigo {self.codigo},e o seu numero é {self.telefone}"
    

class viagem:
    def __init__(self,motorista,passageiro,origem,destino,preco,estado:bool):
        self.motorista=motorista
        self.passageiro=passageiro
        self.origem=origem
        self.destino=destino
        self.preco=preco
        self.estado=estado

    def iniciar_viagem(self):
        if self.estado is True:
            print("Este taxi esta ocupado")
            self.viagem="Ocupado"
            self.
        else:
            self.    






    def concluir_viagem(self):
        pass
    def mostar_dados(self):
        pass


class empresa:
    def __init__(self,nome):
        self.nome=nome
        self.motorista=[]
        self.passageiro=[]
        self.viagens=[]
