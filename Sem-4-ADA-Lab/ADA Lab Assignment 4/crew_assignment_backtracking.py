flights = [('F1', 8, 10), ('F2', 9, 11), ('F3', 11, 13)]
crew = ['C1', 'C2']

assignment = {}

def is_valid(flight, crew_member):
    for f, c in assignment.items():
        if c == crew_member:
            if not (flight[2] <= f[1] or flight[1] >= f[2]):
                return False
    return True

def backtrack(i):
    if i == len(flights):
        return True
    
    for c in crew:
        if is_valid(flights[i], c):
            assignment[flights[i]] = c
            if backtrack(i+1):
                return True
            del assignment[flights[i]]
    
    return False

backtrack(0)
print("Assignment:", assignment)