def validar_mayuscula(nombre):
    return nombre[0].isupper()

def saludo_adaptado(nombre, sexo):
    if sexo.lower() == "m":
        return f"¡Bienvenido, {nombre}!"
    elif sexo.lower() == "f":
        return f"¡Bienvenida, {nombre}!"
    
def obtener_opciones(region):
    opciones = {
        "Venezuela": ["arepa", "empanada", "chicha"],
        "Italia": ['pasta', 'pizza', 'gelato'],
        "Japon": ['sushi', 'samuráis', 'anime']
    }
    return opciones.get(region, [])

def perfil_usuario():
    try:
        nombre = input("Ingrese su nombre: ")
        if not validar_mayuscula(nombre):
            raise ValueError("El nombre debe comenzar con mayuscula")
        
        sexo = input("Ingrese su sexo (M/F): ").strip().lower()
        if sexo not in ["m", "f"]:
            raise ValueError("Sexo no valido. Saliendo del programa.")
        
        saludo = saludo_adaptado(nombre, sexo)
        print(saludo)

        regiones = ["Venezuela", "Italia", "Japon"]
        print("Regiones disponibles Venezuela, Italia, Japon")
        region = input("Ingrese su region: ")
        if region not in regiones:
            raise ValueError("Region no valida. Saliendo del programa")
        
        opciones_favoritas = obtener_opciones(region)
        print(f"Cosas favoritas en {region}: {', '.join(opciones_favoritas)}")
        cosa_favorita = input("¿cual es tu cosa favorita de esta region?: ")
        if cosa_favorita not in opciones_favoritas:
            raise ValueError("Opcion no completada. Saliendo del programa.")
        
        print(f"Gracias, {nombre}. Tu perfil ha sido creado con exito.")
        print(f"Sexo: {sexo.upper()}, Region: {region}, Cosa favorita: {cosa_favorita}")
    except ValueError as ve:
        print(ve)
        exit()

perfil_usuario()
