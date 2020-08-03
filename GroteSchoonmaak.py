import random

# Initialize persons and teams
persons = ['Guus', 'Floor', 'Elias', 'Mirjam', 'Fiep', 'Nora', 'Paul', 'Jill', 'Luna', 'Carsten', 'Koen', 'Stijn',
            'Kasper', 'Veerle', 'Ann', 'Max', 'Kelly', 'Steven', 'Tijn', 'Floris']
teams = [['Keuken wasmachine', 5], ['Keuken koelkast', 5], ['Woonkamer', 4], ['Gang', 4], ['Wegbrengen', 2]]

asgmt = []
for t in teams:                         # Loop over the different teams
    for p in range(t[1]):               # Repeat the loop depending on team size
        person = random.choice(persons) # Pick a random person
        asgmt.append([person, t[0]])    # Assign it to the team
        persons.remove(person)          # Do not pick the picked person again

# Create function to find index in the assignment
def find(name):
    return [(ind, asgmt[ind].index(name)) for ind in range(len(asgmt)) if name in asgmt[ind]][0][0]

a = find('Veerle')      # Find index where Veerle is assigned
b = find('Wegbrengen')  # Find index where Veerle should be
asgmt[a][0], asgmt[b][0] = asgmt[b][0], asgmt[a][0] # Swap Veerle and the person on Veerle's place

for i in asgmt:
    print(i)
