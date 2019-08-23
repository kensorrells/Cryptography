import base64

message = input("What's the message? ")

def encode():
    while True:
        data = base64.b64encode(message.encode())
        if len(message) > 0:
            print(data)
            break
        else:
            print("error")
            break

def decode():
    while True:
        code = input("What is the code? ")
        data = base64.b64decode(code)
        if len(code) > 0:
            print(data)
            break
        else:
            print("error")
            break

encode()
decode()
