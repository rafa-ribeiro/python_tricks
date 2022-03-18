


class Indenter:

	def __init__(self):
		self.level = -1

	def __enter__(self):
		self.level += 1
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.level -= 1

	def print(self, message):
		tab = self.level * 4 * " "
		print(f'{tab}{message}')



if __name__ == '__main__':
	
	with Indenter() as indent:
		indent.print('Olá')
		with indent:
			indent.print('Tudo bem?')
			with indent:
				indent.print('Turo bom e você?')
		with indent:
			indent.print('Eu tô bem tbm = )')

	with Indenter() as indent:
		indent.print('Acabou o assunto')