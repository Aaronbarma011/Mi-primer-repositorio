import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso, League Of Legends (Un videojuego) ",
            "XD":  "Una cara riendose, se suele utilizar cuando te cuentan algo inesperado",
            
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
time.sleep(3)
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ('Lo sentimos, no disponemos la informacion de esa palabra, mejor buscalo en Google :)')
