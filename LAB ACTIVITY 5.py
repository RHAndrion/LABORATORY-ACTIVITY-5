#LAB ACTIVITY 5
def classify_age(age):
    if age < 0:
        print("Wag mo akong niloloko, walang age na may negative.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")

#Test Runs
classify_age(78)  
classify_age(2)  
classify_age(100)   
classify_age(10)   
classify_age(-190)
classify_age(19)   