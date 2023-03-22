from src import s12p1modulo

# Apartado 5
persona_luis = ClasePersona("Luis Martin", 40)
trabajador_luis = ClaseTrabajador("TRD", 35000)
print(persona_luis.obtener_nombre_y_edad())
print(trabajador_luis.obtener_codigo_y_salario())

# Apartado 6
for departamento in EnumeracionDepartamento:
    print(departamento, departamento.name, departamento.value)

# Apartado 8
empleado_javier = \
    ClaseEmpleado("Javier Moreno", 32, "CEQ", 29500, EnumeracionDepartamento.financiero)
print(empleado_javier.concatenacion())
