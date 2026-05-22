def main():
    names = {"Mario", "Luigi", "Daisy"}
    for name in names:
        print(send_letter(name, "Princess Peach"))

def send_letter(reciever, sender):
    return f""" 
+===================================+
          
Dear {reciever},

    You are invited to the royal ball. 
    Please arrive at 7:00PM.
          
          Your friend,
          {sender}"""
main()