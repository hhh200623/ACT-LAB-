def classify_age(age):
    if age < 0:
        print("Invalid age entered.")
    else:
        category = ["Child", "Teen", "Adult", "Senior"][(age > 12) + (age > 19) + (age > 64)]
        print(f"You are a {category}.")
