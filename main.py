try:
    username = input("Enter Username: ")
    age = int(input("Enter Age: ")) 

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")
    
    print("\n--- Saved Users ---")
    with open("users.txt", "r") as file:
        print(file.read().strip())

except ValueError:
    print("Error: Age must be a valid whole number.")
except FileNotFoundError:
    print("Error: The file could not be found.")
finally:
    print("\nSystem complete.")