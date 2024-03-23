"""Define a function accept_login(**users, username, password) with three parameters.
users a dictionary of username keys and password values
username a string containing login name
password a string containing password
The function should return True if the user exists and the password is correct; otherwise returns False. 
Consider following two dictionaries and call above function as experimented follows.
dict1 = {“user1” : “password1”, “user2” : “password2”, “user3” : “password3”}
dict2 = {“user4” : “password4”, “user5” : “password5”, “user6” : “password6”}
Calling statements:
accept_login(dict1, “user2”, “password2”)
accept_login(dict1, “user11”, “password11”)
accept_login(dict2, “user2”, “password2”)
accept_login(dict2, “user11”, “password11”)
accept_login(dict1, “user1”, “123”)
"""
dict1 = {"user1" : "password1", "user2" : "password2", "user3" : "password3"}
dict2 = {"user4" : "password4", "user5" : "password5", "user6" : "password6"}

def accept_login(username,password,**users):
    d1=list(users.keys())
    d2=list(users.values())
    if username in d1 and password in d2:
        return True
    else:
        return False
a=accept_login("user2","password2",**dict1)
b=accept_login("user11", "password11",**dict1)
c=accept_login("user2", "password2",**dict2)
d=accept_login("user11", "password11",**dict2)
e=accept_login("user1", "123",**dict1)
print(a)
print(b)
print(c)
print(d)
print(e)