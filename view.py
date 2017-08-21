#!/usr/bin/env python
#coding: utf-8
from Tkinter import *
from model import *

class ViewTk(object):
	def inserir_registro(self):
		print("Novo")
	def alterar_registro(self):		
		print("Alterar")
	def excluir_registro(self):
		print("Excluir")
    
	def mostrar_historico(self, conta):
		height = 1
		width = 0
			
		Label(self.root, text="ID", borderwidth=2, relief=SUNKEN).grid(row=0, column=0, sticky="nsew")		
		Label(self.root, text="Data", borderwidth=2, relief=SUNKEN).grid(row=0, column=1, sticky="nsew")
		Label(self.root, text="Descrição", borderwidth=2, relief=SUNKEN).grid(row=0, column=2, sticky="nsew")
		Label(self.root, text="Valor", borderwidth=2, relief=SUNKEN).grid(row=0, column=3, sticky="nsew")
		Label(self.root, text="Pago Em", borderwidth=2, relief=SUNKEN).grid(row=0, column=4, sticky="nsew")		
		
		for hist in conta.get_historico():
			Label(self.root, text=hist.id, borderwidth=2, relief=SUNKEN).grid(row=height, column=0, sticky="nsew")
			Label(self.root, text=hist.criado_em, borderwidth=2, relief=SUNKEN).grid(row=height, column=1, sticky="nsew")
			Label(self.root, text=hist.descricao, borderwidth=2, relief=SUNKEN).grid(row=height, column=2, sticky="nsew")
			Label(self.root, text=hist.valor, borderwidth=2, relief=SUNKEN).grid(row=height, column=3, sticky="nsew")
			Label(self.root, text=hist.pago_em, borderwidth=2, relief=SUNKEN).grid(row=height, column=4, sticky="nsew")			
			height += 1

		Label(self.root, text="TOTAL ENTRADAS: ").grid(row=height, column=0, sticky="nsew")
		Label(self.root, text=conta.total_entradas).grid(row=height, column=1, sticky="nsew")
		height += 1
		Label(self.root, text="TOTAL SAIDAS: ").grid(row=height, column=0, sticky="nsew")
		Label(self.root, text=conta.total_saidas).grid(row=height, column=1, sticky="nsew")
		height += 1
		Label(self.root, text="TOTAL SALDO: ").grid(row=height, column=0, sticky="nsew")
		Label(self.root, text=conta.total_entradas + conta.total_saidas).grid(row=height, column=1, sticky="nsew")
		
	def mostrar_menu(self):
	
		menu = Menu(self.root)		
		self.root.config(menu=menu)		
		menu_registros = Menu(menu)		
		menu_registros.add_command(label="Novo", command=self.inserir_registro)
		menu_registros.add_command(label="Alterar", command=self.alterar_registro)
		menu_registros.add_command(label="Excluir", command=self.excluir_registro)
		menu_registros.add_separator()
		menu_registros.add_command(label="Exit", command=self.root.quit)		
		menu.add_cascade(label="Ações", menu=menu_registros)
		
		
	def __init__(self):
		self.root = Tk()
		self.mostrar_menu()
		self.mostrar_historico(Conta('Teste'))
				
	def start(self):
		self.root.mainloop()

class ViewTerminal(object):
	def start(self):
		print("Bem vindo ao gerenciador de Contas \n")
		return self.menu()

	def menu(self):

		print("")
		print("1 - Inserir registro")
		print("2 - Listar registros")
		print("3 - Excluir registro")
		print("4 - Alterar registro")
		print("0 - Sair")

		return int(input("\nDigite a opcao: "))

	def get_registro(self):
		print("\nDigite os valores do novo registro")
		descricao = raw_input("Descricao: ")
		valor = float(input("Valor: "))
		pago_em = raw_input("Digite a data do pagamento: ")
		return pago_em, descricao, valor

	def mostrar_historico(self, conta):

		print("")
		print(("-"*31)+"Historico da conta"+("-"*31))
		print("|  ID  |    Data    |           Descricao           |    Valor    |  Pago  em  |")
		print("-"*80)
		for hist in conta.get_historico():
			print("|{: <6}|{: <12}|{: <31}|{: <13}|{: <12}|".format(hist.id, hist.criado_em, hist.descricao, hist.valor, hist.pago_em))
			print("-"*80)
		print("TOTAL ENTRADA:{}".format(conta.total_entradas))
		print("TOTAL SAIDA:{}".format(conta.total_saidas))
		print("TOTAL SALDO:{}".format(conta.total_entradas + conta.total_saidas))

	def get_id_registro(self):		
		return input("Informe o ID do registro: ")
		
	def finalizar(self):
		print("Programa finalizado!")
		