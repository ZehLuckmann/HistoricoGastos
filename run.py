from controller import CtrlTerminal 
from view import ViewTk

if __name__ == "__main__":	
	print("Selecione sua opcao:")
	print("[1] - Terminal")
	print("[2] - Janelas (WIP)")
	opc = input("Opcao: ")
	
	if opc == 1:
		main = CtrlTerminal()	
	elif opc == 2:
		main = ViewTk()
	else:
		print("Opcao invalida")
	
main.start()
