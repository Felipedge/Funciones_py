def  agregar_notas(lista):
    try:
        nota = 0 
        while nota <=0:
            nota= float(input("ingresar una nota"))
        lista.append(nota)
        print("nota agregada correctamente")
    except:
        print("la nota debe ser un valor numerico")