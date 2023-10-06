class carros:
    def __init__(self, marca, modelo, ano, cor, km,) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.km = km

    def dirigir(self, distancia):
        self.km += distancia
            
    
    def mostar_km(self):
        print("A Quilometragem do {} {}: {} km".format(self.marca, self.modelo, self.km))


carro1 = carros("Toyota", "Corolla", 2022, "Prata", 0)
carro2 = carros("Honda", "Civic", 2021, "Preto", 0)
carro3 = carros("Fiat", "Uno", 2012, "Prata", 0)
carro4 = carros("Hiunday", "Hb20", 2015, "Vermelho", 0)

carro1.dirigir(100)
carro2.dirigir(50)

print ("Carro 1:", carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
carro1.mostar_km()
print ("Carro 1:", carro2.marca, carro2.modelo, carro2.ano, carro2.cor)
carro2.mostar_km()
