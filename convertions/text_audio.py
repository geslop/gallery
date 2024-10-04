# Instalar primero pyttsx3 y speechrecognition
import pyttsx3
import speech_recognition as sr



# funcion para que el asistente sea escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

    # Modificar el volumen
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)


    # Selecciona una voz
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)



hablar("texto de prueba")
    