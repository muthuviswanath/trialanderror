import threading
def display(name):
    for n in name:
        print(f"Welcome to the worst day {n}")

myth = threading.Thread(target=display, args=(["Muthu","Shreeya","Ravi","Sandesh"],))
myth.start()

print ("Patience is the key muthu")
print("Hi")