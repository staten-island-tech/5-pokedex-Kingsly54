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
lang=input("Language")
y=lang.lower()
def language(data):
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
    if y=="grass":
        for i in range(len(data)):
            if data[i]["type"][0]=="Grass":
                language(data)
              
type(data)
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

