input("Por favor escriba \"go\" para comenzar  ")

pregunta_1 = "¿Simón Bolívar libertó a Colombia?"
pregunta_2 = "¿Camilo Torres fue un guerrillero?"
pregunta_3 = "¿El Binomio de Oro es un grupo de música vallenata?"

a = input(pregunta_1 + " (Si/No)  ")

if a == "Si" or a == "si" or a == "Sí" or a == "sí" or a == "sI" or a == "sÍ" or a == "SÍ" or a == "SI":
    print("Su respuesta es correcta! Felicidades, podra responder la segunda pregunta.")

    b = input(pregunta_2 + " (Si/No)  ")
    if b == "Si" or b == "si" or b == "Sí" or b == "sí" or b == "sI" or b == "sÍ" or b == "SÍ" or b == "SI":
        print("Su respuesta es correcta! Felicidades, podra responder la tercera pregunta.")

        c = input(pregunta_3 + " (Si/No)  ")
        if c == "Si" or c == "si" or c == "Sí" or c == "sí" or c == "sI" or c == "sÍ" or c == "SÍ" or c == "SI":
            print("Su respuesta es correcta! Felicidades, ha respondido todas las preguntas correctamente. Se ha ganado un premio de 1000 dolares.")
        else:
            print("Su respuesta es incorrecta! Fin del juego.")
    else:
        print("Su respuesta es incorrecta! No podra responder la tercera pregunta.")
else:
    print("Su respuesta es incorrecta! No podra responder la segunda pregunta.")