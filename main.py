# + ---------------------------------------------------- +
# |                                                      |
# |     This is a simple video downloader prototype      |
# |                                                      |
# + ---------------------------------------------------- +

# import .config
import sys
import json
import yt_dlp

# demo main()
def main():
    print("Welcome to lucky Devil!")
    
    name = input("What is your name?: ")
    print(f"Hello, {name}! Nice to meet you...")

    while True:
        choice = input("Enter 'quit' to exit, or anything else to continue: ")
        if choice.lower() == 'quit' or choice.lower() =='exit':
            break
        print("You chose to continue.")

    print("Exiting the application. Goodbye!")


# sys.req-2-exc
if __name__ == "__main__":
    main()