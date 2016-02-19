#https://docs.python.org/2/library/pwd.html

import pwd

username = raw_input("Please provide a username: ")
password = raw_input("Please provide a password: ")
pw_uid = 2


pass_tuple = (username, password, pw_uid)


pwd.getpwnam(username)

