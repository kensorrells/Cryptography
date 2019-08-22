message = input("Enter Message: ")

def translate():
    t = ""
    i = len(message) - 1
    if i <= 0:
        print("Error")
    else:
        while i >= 0:
            t += message[i]
            i -= 1
        print(t)



translate()