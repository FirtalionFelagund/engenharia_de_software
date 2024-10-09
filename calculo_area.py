class Forma:
    def calcular_area(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14159 * self.raio**2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Utilizando as classes
circulo = Circulo(5)
quadrado = Quadrado(4)
triangulo = Triangulo(6, 8)

print("Área do círculo:", circulo.calcular_area())
print("Área do quadrado:", quadrado.calcular_area())
print("Área do triângulo:", triangulo.calcular_area())