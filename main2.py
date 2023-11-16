import random
def cold():
    print("氷")

def hot():
    print("熱")

def wind():
    print("風")

magic = [cold,hot,wind]
magic[random.randint(0,2)]()