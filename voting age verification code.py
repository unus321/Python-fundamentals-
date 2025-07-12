user_age = int(input("ENTER YOUR AGE.\n"))
min_age = 18
if 0 <= user_age <=17:
    print("YOU ARE NOT OLD ENOUGH TO SUBMIT YOUR VOTE YET.\n")
    print(f" you have to wait {min_age - user_age} more years to try again.\n")
elif user_age == min_age:
        print("YOU ARE OLD ENOUGH TO SUBMIT YOUR VOTE.\n ")
elif min_age < user_age <= 80:
    print("YOU ARE OLD ENOUGH TO SUBMIT YOUR VOTE.\n")
elif 80 < user_age:
    print(f"🫡 you are {user_age} years old but still doing your dute as a responsible citizen by giving your vote, really appreciated")
else:
    print("error")