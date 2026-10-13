
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"o {self.tipo} atacou usando {ataque}")


herois = [

    Heroi("Luna", 25, "ninja"),
    Heroi("Thor", 30, "guerreiro"),
    Heroi("Buda", 60, "monge"),
    Heroi("Merlin", 100, "mago")
]

for heroi in herois:
    heroi.atacar()