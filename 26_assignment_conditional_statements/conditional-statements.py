def personalized_message(name, age, hobby):
    if age < 13:
        category = "Kid"
    elif 13 <= age <= 19:
        category = "Teen"
    elif 20 <= age <= 64:
        category = "Adult"
    else:
        category = "Senior"

    message = f"Hey {name} ({category})! Sounds like you're rocking life by loving {hobby}!"
    print(message)

if __name__ == "__main__":
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hobby = input("Enter hobby: ")
    personalized_message(name, age, hobby)
