#Task 67

def cordinator(x,y):
    return (x,y)

my_cordinate = cordinator(5,6)
print(my_cordinate)

#Task 68

my_coordinates = {}
def coordinator(x,y):
    return (x,y)

my_coordinates[coordinator(0,0)] = "Home"
my_coordinates[coordinator(1,1)] = "Work"
my_coordinates[coordinator(-1,-1)] = "School"

for k,v in my_coordinates.items():
    print(f"position: {k} name: {v}")
