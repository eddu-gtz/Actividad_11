from particula import Particula
import json

class Administradora:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        #join recibe n cantidad de elementos para meter a ese string
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def guardar(self,ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista,archivo, indent=5)
            return 1
        except:
            return 0
    
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                #Los dos asteriscos los comvierte los datos json a parametros
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0
    
    def __len__(self):
        return len(self.__particulas)
    
    #Crear un iterador
    def __iter__(self):
        #retorna el contador
        self.cont = 0
        return self

    def __next__(self):
        #siguiente elemento
        if self.cont < len(self.__particulas):
            #se guarda el elemento en la posicion que indique el contador
            particula = self.__particulas[self.cont]
            #antes de retornar se incrementa el contador
            self.cont += 1
            return particula
        else:
            #deja de continuar con el ciclo
            raise StopIteration
        