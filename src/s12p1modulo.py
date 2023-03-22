from enum import Enum

# Apartado 2
class EnumeracionDepartamento(Enum):
    direccion = 1
    financiero = 2
    procesos = 3
    RRHH = 4
    tesoreria = 5

# Apartado 3
class ClasePersona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_nombre_y_edad(self):
        return f"{self.nombre} {self.edad}"

# Apartado 4
class ClaseTrabajador:
    def __init__(self, codigo, salario):
        self.codigo = codigo
        self.salario = salario

    def obtener_codigo_y_salario(self):
        return f"{self.codigo} {self.salario}"

# Apartado 7
class ClaseEmpleado(ClasePersona, ClaseTrabajador):
    def __init__(self, nombre, edad, codigo, salario, departamento):
        ClasePersona.__init__(self, nombre, edad)
        ClaseTrabajador.__init__(self, codigo, salario)
        self.departamento = departamento

    def concatenacion(self):
        nombre_y_edad = ClasePersona.obtener_nombre_y_edad(self)
        codigo_y_salario = ClaseTrabajador.obtener_codigo_y_salario(self)
        return f"{nombre_y_edad} {codigo_y_salario} {self.departamento.name} {self.departamento.value}"
