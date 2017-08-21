from model import Conta
from view import ViewTerminal

class CtrlTerminal(object):
    def start(self):
		opcao = self.view.start()

		while opcao != 0:
			if opcao == 1:				
				pago_em, descricao, valor = self.view.get_registro()
				self.model.novo_registro(pago_em, descricao, valor)
			elif opcao == 2:								
				self.model.carregar_historico()				
				self.view.mostrar_historico(self.model)
			elif opcao == 3:
				self.model.remover_registro(self.view.get_id_registro())
			elif opcao == 4:				
				pago_em, descricao, valor = self.view.get_registro()
				self.model.atualizar_registro(pago_em, descricao, valor, self.view.get_id_registro())
				
			opcao = self.view.menu()

		self.view.finalizar()
    
    def __init__(self):
		self.model = Conta("teste")
		self.view = ViewTerminal()
	
class CtrlTk(object):
    def start(self):
		self.view.start()
		
    def __init__(self):
		self.model = Conta("teste")
		self.view = ViewTk()