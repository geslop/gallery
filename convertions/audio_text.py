# Instalar primero pyaudio y speechrecognition
import speech_recognition as sr


# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micrófono
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-co")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print("ups, no entendí")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendió el audio
            print("no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except Exception as e:

            # prueba de que no comprendió el audio
            print("ups, algo ha salido mal", e)

            # devolver error
            return "sigo esperando"

transformar_audio_en_texto()
