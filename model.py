#!/usr/bin/env python
#coding: utf-8
import os.path
import sqlite3
from time import gmtime, strftime

class Conta(object):
	def __init__(self, codigo):
	
		self.historico = []
		self.total_entradas = 0
		self.total_saidas = 0
		
		if not os.path.isfile(codigo + '.db'):
			self.conn = sqlite3.connect(codigo + '.db')		
			self.cria_estrutura()
		else:
			self.conn = sqlite3.connect(codigo + '.db')		
		
		self.carregar_historico()
		
	def cria_estrutura(self):
		cursor = self.conn.cursor()		
		cursor.execute("CREATE TABLE historico (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,criado_em DATE NOT NULL,pago_em DATE NOT NULL,descricao TEXT NOT NULL,valor DECIMAL);")
	
	def	carregar_historico(self):
		cursor = self.conn.cursor()	
		cursor.execute("SELECT id FROM historico;")		
		
		self.historico = []
		self.total_entradas = 0
		self.total_saidas = 0
		
		for linha in cursor.fetchall():
			reg = Registro(self, linha[0])
			self.historico.append(reg)
			
			if reg.valor > 0:
				self.total_entradas += reg.valor
			else:
				self.total_saidas += reg.valor
			
	def	get_historico(self):		
		return self.historico
	
	def novo_registro(self, pago_em, descricao, valor):
		reg = Registro(self)
		reg.set_valores(pago_em, descricao, valor)
		reg.salvar()
		self.carregar_historico()
		return
		
	def remover_registro(self, id):
		for reg in self.historico:
			if (reg.id == id):
				reg.excluir()
		self.carregar_historico()
		
	def atualizar_registro(self,pago_em, descricao, valor, id):
		for reg in self.historico:
			if (reg.id == id):
				reg.set_valores(pago_em, descricao, valor)
				reg.atualizar()
				
		self.carregar_historico()
				
class Registro(object):
	def __init__(self, conta, id = 0):
		self.conta = conta
		if id != 0:
			self.id = id
			self.get_valores()
		return
		
	def set_valores(self, pago_em, descricao, valor):
		self.criado_em = strftime("%Y-%m-%d", gmtime())
		self.pago_em = pago_em
		self.descricao = descricao
		self.valor = valor
		return
	
	def get_valores(self):
		cursor = self.conta.conn.cursor()	
		cursor.execute("SELECT id, criado_em, pago_em, descricao, valor FROM historico WHERE id = {0};\n".format(self.id))	
		
		for linha in cursor.fetchall():			
			self.id = linha[0]
			self.criado_em = linha[1]
			self.pago_em = linha[2]
			self.descricao = linha[3]
			self.valor = float(linha[4])
	
	def salvar(self):		
		cursor = self.conta.conn.cursor()		
		cursor.execute("INSERT INTO historico (criado_em, pago_em, descricao, valor) VALUES ('{0}', '{1}', '{2}', {3})".format(self.criado_em, self.pago_em, self.descricao, self.valor))
		self.conta.conn.commit()
	
	def excluir(self):
		cursor = self.conta.conn.cursor()		
		cursor.execute("DELETE FROM historico WHERE id = {}".format(self.id))
		self.conta.conn.commit()
		
	def atualizar(self):
		cursor = self.conta.conn.cursor()		
		cursor.execute("UPDATE historico SET criado_em = '{}', pago_em = '{}', descricao = '{}', valor = {} WHERE id = {}".format(self.criado_em, self.pago_em, self.descricao, self.valor, self.id))
		self.conta.conn.commit()
		