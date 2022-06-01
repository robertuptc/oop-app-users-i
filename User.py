class User:
    def __init__(self, name, age, phone, email):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

    def contact_info(self):
        return f"you can reach me at {self.phone}, and my email is {self.email}"

charlie = User("Charlie", 18, "123-321-11", "robert@random.com")
print(charlie)
print(charlie.contact_info())

