from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

no_of_visit = int(input("Number of History: "))
print("Enter URLs to visit")
for i in range(no_of_visit):
    url = input("url: ")
    print(f"visiting {url}")
    if current_page:
        backward_history.put(current_page)
    current_page = url

print(f"current page: {current_page}")

while input("Do you want to go back? (yes/no): ").lower() == "yes":
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"going back to {current_page}")
    else:
        print("no previous page available")
        break

while input("Do you want to go forward? (yes/no): ").lower() == "yes":
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"going forward to {current_page}")
    else:
        print("no forward page available")
        break
