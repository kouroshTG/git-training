def login(username, password):
    return username == "admin" and password == "1234"


print(login("admin", "1234"))