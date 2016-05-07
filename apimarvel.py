# coding=utf-8


import requests #libreria para hacer peticions http api​

url = "http://gateway.marvel.com/v1/public/" #La base de url de marvel api
apikey = "5aae412d99cd1bd950ddd08a961df6c8" #la llave publica de nuestro usuario en marvel developer
ts = 1 #Aquí siempre pondremos uno
hash = "07c0d55387452ea51303d55422edb584" #md5 formado por ts + private key + api key de marvel developer​

params = {'apikey' : apikey, 'ts': ts, 'hash': hash} #la autenticación que solicita la api de marvel

def getHistories (id) : #Te da las historias del supereroe con el id ingresado
    response = requests.get(url + "characters/" + str(id), params= params) #Guarda la respuesta
    diccionario = response.json() #La convierte en json
    items = diccionario['data']['results'] #Se ingresa al vector results
    for uri in items: #Iterar uri en results
        print('tiene esta uri ' + uri['series']['collectionURI']) # imprime cada collection uri por cada serie en results

def getCharacters () : #función que me devuelve una lista con nombres y urls de los personajes
    response = requests.get(url + "characters", params=params) #Guarda en una variable la respuesta del API
    diccionario = response.json() #guarda en una variable la respuesta en json
    items = diccionario['data']['results'] #Guarda en una variable el vector de 'results' del api
    for personaje in items: #Itera cada personaje dentro 'results'
        nombre = personaje['name'] #guarda en una variable el nombre del personaje que existe en esa ubicación
        urls = personaje['urls'] #guarda en una variable las urls de un personaje
        getHistories(personaje['id']) #llama a la funcion getHistories y le pasa como parametro el id del personaje
        for anUrl in urls: #itera por cada url del personaje y obtiene la url de dicho personaje
            print("y tiene la siguente url " + anUrl['url'])
        print(nombre + ' aparece en ')

getCharacters()