import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def names(data):
    for i in range(len(data)):
        print(data[i]["name"]["english"])
# Add a language choice feature and print the pokemons name based on the user input
def language(data):
    lang=input("Language")
    y=lang.lower()
    if y=="japanese":
        for i in range(len(data)):
            print(data[i]["name"]["japanese"])
    elif y=="english":
        for i in range(len(data)):
            print(data[i]["name"]["english"])
    elif y=="french":
        for i in range(len(data)):
            print(data[i]["name"]["french"])
    elif y=="chinese":
        for i in range(len(data)):
            print(data[i]["name"]["chinese"]) 
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def type(data):
    g=input("type")
    for i in range(len(data)):
            if data[i]["type"][0]==g:
                print(data[i]["name"])
            if len(data[i]["type"])==2:
                if data[i]["type"][1]==g or data[i]["type"][0]==g:
                    print(data[i]["name"])
              
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def search(data):
    search=input("search")
    numfound=0
    for i in range(len(data)):
        if search in data[i]["name"]["english"]:
            print(data[i]["name"])
            numfound+=1
    if numfound==0: 
        print("No pokemon has been found")
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type
movetyp=open("./moves.json", encoding="utf8")
movetype=json.load(movetyp)
def moves(data):
    pokemon=input("pokemon")
    lis=[]
    for i in range(len(data)):
        if data[i]["name"]["english"]==pokemon:
            types=(data[i]["type"])
            for i in range(len(movetype)):
                if movetype[i]["type"] in types:
                    print(movetype[i]["ename"])
moves(data)