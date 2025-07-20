# + ---------------------------------------------------- +
# |                                                      |
# |     This is a simple video downloader prototype      |
# |                                                      |
# + ---------------------------------------------------- +

# Busy days due to work and college starting at the same time... will update the work soon
# most of the stuff are in testing phase and might also include config files incase I couldnt solve the laying issue.
# Found a guide on creating the gui using python as I donot have much knowledge in python
# However, the first version of this app will be in CLI-CMD mode while working on gui in seperate file which will only be uploaded once finished and functions as desired.
# The github is just for placeholder rn... will be working locally before publishing a working version independent of my own device
# Sadly this app is only gonna be for windows as I donot own any mac-devices. My apologies for all the macOS users.


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