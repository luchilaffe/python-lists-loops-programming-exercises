
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_function(aWord):
    return aWord[0] == "R"

resulting_names = list(filter(filter_function, all_names))

print(resulting_names)




