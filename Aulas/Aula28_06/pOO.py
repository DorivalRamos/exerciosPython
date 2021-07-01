class Pessoa:
    # está dentro de uma Class é um Método, inicializador de atributos
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome  # nomePessoa é um atributo
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self, calorias):
        if self.idadePessoa >= 30:
            self.pesoPessoa += (calorias * 2)
        else:
            self.pesoPessoa += calorias

    def malhar(self, calorias):
        if self.idadePessoa < 30:
            self.pesoPessoa -= (calorias * 2)
        else:
            self.pesoPessoa -= calorias

    def mostrarDado(self):
        return f'''
      Nome : {self.nomePessoa}
      Idade: {self.idadePessoa}
      Peso: {self.pesoPessoa}
      '''


# pessoa1 = Pessoa('Dorival', 34, 53)
# pessoa2 = Pessoa('Evelyn', 27, 45)
# pessoa2.malhar(5)
# print(pessoa2.mostrarDado())


pessoa1 = Pessoa(
    str(input('Informe o nome da pessoa 1: ').strip().capitalize()),
    int(input('Informe a idade da pessoa 1: ')),
    int(input('Informe o peso da pessoa 1: ')))

pessoa1.malhar(5)
print(pessoa1.mostrarDado())
