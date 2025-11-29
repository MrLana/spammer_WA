# Import some module for style and gui
from rich.console import Console
from colorama import Fore, Style, init
import pyfiglet

# Import modules for interacting with the display and GUI
import urllib.request
import time
import random
import string
import os
import sys

# Initialize colorama
init()

# Try to import pyautogui with error handling
try:
    import pyautogui
    PYTHON_GUI_AVAILABLE = True
except Exception as e:
    print(Fore.YELLOW + "Warning: PyAutoGUI not available. GUI functions will be disabled." + Style.RESET_ALL)
    print(Fore.YELLOW + f"Error: {e}" + Style.RESET_ALL)
    PYTHON_GUI_AVAILABLE = False

# Help section for new users
def tool_help():
    print(Fore.RED + """
    _  _ ____ _    ___     ____ ____ ____ ___ _ ____ _  _    
    |__| |___ |    |__]    [__  |___ |     |  | |  | |- |    
    |  | |___ |___ |       ___] |___ |___  |  | |__| | -|    
                                                         
""" + Style.RESET_ALL + Fore.GREEN + """
             
Features """ + Style.RESET_ALL + Fore.MAGENTA + """
        - User-Typed Message:""" + Style.RESET_ALL + Fore.BLUE + """ Manually type and send messages repeatedly. """ + Style.RESET_ALL + Fore.MAGENTA + """
        - Auto-Typed Message:""" + Style.RESET_ALL + Fore.BLUE + """ Automated message-sending options: """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Message with Counting:""" + Style.RESET_ALL + Fore.BLUE + """ Sends sequentially numbered messages. """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Random Message Generator:""" + Style.RESET_ALL + Fore.BLUE + """ Sends messages with random words or sentences. """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Meaningless Message Generator:""" + Style.RESET_ALL + Fore.BLUE + """ Sends messages with random, nonsensical content.
        """ + Style.RESET_ALL + Fore.RED + """
          
Help Section """ + Style.RESET_ALL + Fore.GREEN + """

Main Menu """ + Style.RESET_ALL + Fore.BLUE + """
            Choose an option from the following:
            - [1] User Typed Message
            - [2] Auto Typed Message
            - [4] Help
            - [0] Quit
            - Enter Option -> """ + Style.RESET_ALL + Fore.MAGENTA + """



[1] User Typed Message (Option 1) """ + Style.RESET_ALL + Fore.BLUE + """
    - Selecting this option allows you to manually input messages that will be sent repeatedly.
            You will be prompted with:
            - [*] User typed message <SELECTED>
            - [N] How many messages do you have?
            - [0] Enter 0 to quit and exit tool.
            - [+] Enter Number of Messages (Default: 1) -> 
            Enter the number of messages you want to send. The default is 1. Enter 0 to quit.

            Next, you will be asked to enter your message:
            - [+] Enter your message here (default [ERROR!]) -> 


            Specify how many times you want the message to be sent:
            - [N] How many times would you like to send these messages?
            - [0] Enter 0 to quit and exit tool.
            - [+] Enter Number of Times (Default: 1) -> 


    - After inputting the required details, move your cursor to the message box in WhatsApp and prepare to send the messages.

    - You will receive a final prompt:
        - [ALERT!!!] Now you have only 10 seconds to move the cursor on message box tab.

    - After 10 second messages will be sent, and you will see:
        - Message Sent...
        - The given task has been completed.

Then you will be returned to the main menu to choose the next task or quit.
""" + Style.RESET_ALL + Fore.MAGENTA + """


[2] Auto Typed Message (Option 2) """ + Style.RESET_ALL + Fore.BLUE + """

        Select this option for automated message-sending functionalities:
            - [*] Auto typed message <SELECTED>
            - Choose an option from the following:
            - [1] Message with Counting
            - [2] Random Message Generator
            - [3] Meaningless Message Generator
            - [0] Quit
            - [+] Enter Option -> """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """


        [1] Message with Counting (Sub-option 1) """ + Style.RESET_ALL + Fore.BLUE + """
            - Enter the number of messages to send:
                - [N] How many messages do you want to send?
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Number of Messages (Default: 1) ->
          

            - Input the message to be sent with counting:
                - [N] Enter the message you want to send with counting
                    -The message looks like [Message 1]
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Your Message (Default: ERROR) -> 
Prepare to send messages as per the instructions provided. """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """


        [2] Random Message Generator (Sub-option 2) """ + Style.RESET_ALL + Fore.BLUE + """
            - Enter the number of messages:
                - [N] How many messages do you want to send?
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Number of Messages (Default: 1) -> 

            - Specify the number of words per message:
                - [N] How many words can each message contain?
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Length of Message (Default: 1 Word) -> """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """

        [3] Meaningless Message Generator (Sub-option 3) """ + Style.RESET_ALL + Fore.BLUE + """
            - Enter the number of messages:
                - [N] How many messages do you want to send?
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Number of Messages (Default: 1) -> 

            - Specify the number of words per message:
                - [N] How many words can each message contain?
                - [0] Enter 0 to quit and exit tool.
                - [+] Enter Length of Message (Default: 1 Word) -> 
For all auto-typed options, you will be prompted to prepare WhatsApp for sending messages, with a 10-second alert.


""" + Style.RESET_ALL)
    spammer()

def check_gui_available():
    """Check if GUI operations are available"""
    if not PYTHON_GUI_AVAILABLE:
        print(Fore.RED + "\n[ERROR] GUI operations are not available in this environment." + Style.RESET_ALL)
        print(Fore.YELLOW + "Please run this program in a graphical environment to use messaging features." + Style.RESET_ALL)
        return False
    return True

def simulate_message_sending(message):
    """Simulate message sending with or without GUI"""
    if PYTHON_GUI_AVAILABLE:
        pyautogui.write(message)
        pyautogui.press('enter')
    else:
        print(Fore.CYAN + f"[SIMULATED] Would send: {message}" + Style.RESET_ALL)
        time.sleep(0.5)  # Simulate delay

# User is able to type a message and send what they want
def user_typed_message():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] User typed message" + Style.RESET_ALL + Fore.RED + "\t\t<SELECTED>" + Style.RESET_ALL)
    
    # Check if GUI is available
    if not check_gui_available():
        print(Fore.YELLOW + "Continuing in simulation mode..." + Style.RESET_ALL)
    
    # Ask the user how many messages are available to send
    print("[N] How many messages do you have?\n[0] Enter 0 to quit and exit tool.")
    available_smg = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Number of Messages (Default 1 Message) ->  " + Style.RESET_ALL)

    # Check if the input is empty and set default to 1
    if available_smg.strip() == "":
        available_smg = 1
    elif available_smg == "0":
        exit_from_tool()
    else:
        try:
            # Try to convert the input to an integer
            available_smg = int(available_smg)
        except ValueError:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL, end="")
            time.sleep(1.5)
            user_typed_message()

    # Store messages in list
    num_of_smg = 0
    list_of_smg = []
    print()
    while num_of_smg < available_smg:
        smg = input(Fore.GREEN + "[+] Enter your message here (default [ERROR!]) -> " + Style.RESET_ALL)
        if smg.strip() == "":
            list_of_smg.append("ERROR!")
        else:
            list_of_smg.append(smg)
        num_of_smg += 1
    
    # How many times would you like to send these messages repeatedly?
    print("\n[N] How many times would you like to send these messages?\n[0] Enter 0 to quit and exit tool.")
    number_of_smg = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Number of Time (Default 1 Time) -> "+ Style.RESET_ALL)
    if number_of_smg.strip() == "":
        number_of_smg = 1
    elif number_of_smg == "0":
        exit_from_tool()
    else:
        try:
            # Try to convert the input to an integer
            number_of_smg = int(number_of_smg)
        except ValueError:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL, end="")
            time.sleep(1.5)
            user_typed_message()
    
    # Show warning only if GUI is available
    if PYTHON_GUI_AVAILABLE:
        print(Fore.RED + "\nNow open the WhatsApp tab and move the cursor to the message box where you can type your message.\n" + Style.RESET_ALL, end="")
        # Check user is ready
        print("Are you ready? If you are ready...\n[1] Press Enter or 1 to continue\n[0] Enter 0 to quit and exit tool.")
        user_is_ready = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL)
        if user_is_ready.strip() == "" or user_is_ready.strip() == "1":
            # Warn to user, code is running now
            print(Fore.RED + "[ALERT!!!] Now you have only 10 seconds to move the cursor on message box tab.\n" + Style.RESET_ALL, end="")
            # Wait for 10 second to move message box tab
            time.sleep(10)
        elif user_is_ready == "0":
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            user_typed_message()
    else:
        print(Fore.YELLOW + "\n[INFO] Running in simulation mode - no actual messages will be sent." + Style.RESET_ALL)
        print("Press Enter to continue with simulation...")
        input()
    
    start_smg = 0
    while start_smg < number_of_smg:
        start_smg += 1
        for message in list_of_smg:
            # write and send messages
            simulate_message_sending(message)
            print("Message Sent...")
    # Show message after Task is completed and Ask What is next task
    print(Fore.GREEN + Style.BRIGHT + "The given task has been completed.\n\n"+ Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "What is the next task?\nIf there are no more tasks, you can quit or exit the tool by using '0'."+ Style.RESET_ALL)
    spammer()

# This function can allow to user send messages with counting
def message_with_counting():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Message with counting" + Style.RESET_ALL + Fore.RED + "\t<SELECTED>" + Style.RESET_ALL)
    
    # Check if GUI is available
    if not check_gui_available():
        print(Fore.YELLOW + "Continuing in simulation mode..." + Style.RESET_ALL)
    
    # Set how many time user want to send a messages
    print("[N] How many messages do you want to send?\n[0] Enter 0 to quit and exit tool.")
    no_of_messages = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Number of Message (Default 1 Message) ->  " + Style.RESET_ALL)

    # Set default number of Message
    if no_of_messages.strip() == "":
        no_of_messages = 1
    elif no_of_messages == "0":
        exit_from_tool() # exit from code
    else:
        try :
            no_of_messages = int(no_of_messages)
        except:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL, end="")
            time.sleep(1.5)
            # Recall random_message_generator if user enter wrong value
            message_with_counting()

    # Set a message that you want use with counting
    print("\n[N] Enter the message you want to send with counting\n\t-The message looks like [Message 1]\n[0] Enter 0 to quit and exit tool.")
    message = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Your Message (Default ERROR) ->  " + Style.RESET_ALL)

    # Set a default value of Message
    if message.strip() == "":
        message = "ERROR"
    elif message == "0":
        exit_from_tool() # exit from code

    # Show warning only if GUI is available
    if PYTHON_GUI_AVAILABLE:
        print(Fore.RED + "\nNow open the WhatsApp tab and move the cursor to the message box where you can type your message.\n" + Style.RESET_ALL, end="")
        # Check user is ready
        print("Are you ready? If you are ready...\n[1] Press Enter or 1 to continue\n[0] Enter 0 to quit and exit tool.")
        user_is_ready = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL)
        if user_is_ready.strip() == "" or user_is_ready.strip() == "1":
            # Warn to user, code is running now
            print(Fore.RED + "[ALERT!!!] Now you have only 10 seconds to move the cursor on message box tab.\n" + Style.RESET_ALL, end="")
            # Wait for 10 second to move message box tab
            time.sleep(10)
        elif user_is_ready == "0":
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            message_with_counting()
    else:
        print(Fore.YELLOW + "\n[INFO] Running in simulation mode - no actual messages will be sent." + Style.RESET_ALL)
        print("Press Enter to continue with simulation...")
        input()

    for no_of_message in range(no_of_messages):
        no_of_message += 1
        # write and send messages
        full_message = f"{message} {no_of_message}"
        simulate_message_sending(full_message)
        print("Message Sent...")
    # Show message after Task is completed and Ask What is next task
    print(Fore.GREEN + Style.BRIGHT + "The given task has been completed.\n\n"+ Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "What is the next task?\nIf there are no more tasks, you can quit or exit the tool by using '0'."+ Style.RESET_ALL)
    spammer()

# This function can allow to user send random messages with random words
def random_message_generator():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Random Message Generator" + Style.RESET_ALL + Fore.RED + "\t<SELECTED>" + Style.RESET_ALL)
    
    # Check if GUI is available
    if not check_gui_available():
        print(Fore.YELLOW + "Continuing in simulation mode..." + Style.RESET_ALL)
    
    # URL of the word list
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    # Fetch the word list from the URL once
    try:
        response = urllib.request.urlopen(url)
        word_list = response.read().decode().splitlines()
    except Exception as e:
        if isinstance(e, urllib.error.URLError):
            print(Fore.YELLOW + "\nInternet connection error. Using fallback word list." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"Something went wrong: {e}. Using fallback word list." + Style.RESET_ALL)
        # Fallback word list
        word_list = ["hello", "world", "python", "test", "message", "random", "word", "example"]

    # Set how many time user want to send a messages
    print("[N] How many messages do you want to send?\n[0] Enter 0 to quit and exit tool.")
    no_of_message = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Number of Message (Default 1 Message) ->  " + Style.RESET_ALL)

    # Set default number of Message
    if no_of_message.strip() == "":
        no_of_message = 1
    elif no_of_message == "0":
        exit_from_tool() # exit from code
    else:
        try :
            no_of_message = int(no_of_message)
        except:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL, end="")
            time.sleep(1.5)
            # Recall random_message_generator if user enter wrong value
            random_message_generator()

    # Set a lenght of words in message 
    print("[N] How many words can contain every message?\n[0] Enter 0 to quit and exit tool.")
    message_length = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Length of Message (Default 1 Word) ->  " + Style.RESET_ALL)

    # Set default lenght of Message
    if message_length.strip() == "":
        message_length = 1
    elif message_length == "0":
        exit_from_tool() # exit from code
    else:
        try :
            message_length = int(message_length)
        except:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL, end="")
            time.sleep(1.5)
            # Recall random_message_generator if user enter wrong value
            random_message_generator()

    # Show warning only if GUI is available
    if PYTHON_GUI_AVAILABLE:
        print(Fore.RED + "\nNow open the WhatsApp tab and move the cursor to the message box where you can type your message.\n" + Style.RESET_ALL, end="")
        # Check user is ready
        print("Are you ready? If you are ready...\n[1] Press Enter or 1 to continue\n[0] Enter 0 to quit and exit tool.")
        user_is_ready = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL)
        if user_is_ready.strip() == "" or user_is_ready.strip() == "1":
            # Warn to user, code is running now
            print(Fore.RED + "[ALERT!!!] Now you have only 10 seconds to move the cursor on message box tab.\n" + Style.RESET_ALL, end="")
            # Wait for 10 second to move message box tab
            time.sleep(10)
        elif user_is_ready == "0":
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            random_message_generator()
    else:
        print(Fore.YELLOW + "\n[INFO] Running in simulation mode - no actual messages will be sent." + Style.RESET_ALL)
        print("Press Enter to continue with simulation...")
        input()

    for _ in range(no_of_message):
        # Initialize sentence for add random words and create a sentence
        sentence = ""
        # punctuation marks for add to the end of sentence
        punctuation_marks = [".", "?", "!", "...", ";"]
        # Generate the message
        for _ in range(message_length):
            if word_list:  # Check if the word_list is not empty
                    sentence += random.choice(word_list) + " "
            else:
                sentence += "ERROR "
        # Create a finnal meassage
        message = sentence + random.choice(punctuation_marks)
        # write and send messages
        simulate_message_sending(message)
        print("Message Sent...")
    # Show message after Task is completed and Ask What is next task
    print(Fore.GREEN + Style.BRIGHT + "The given task has been completed.\n\n"+ Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "What is the next task?\nIf there are no more tasks, you can quit or exit the tool by using '0'."+ Style.RESET_ALL)
    spammer()

# This function can allow to user send messages with meaningless words, that words contains charecter, number and symble. 
def meaningless_message_generator():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Meaningless Message Generator" + Style.RESET_ALL + Fore.RED + "\t<SELECTED>" + Style.RESET_ALL)
    
    # Check if GUI is available
    if not check_gui_available():
        print(Fore.YELLOW + "Continuing in simulation mode..." + Style.RESET_ALL)
    
    # Set how many time user want to send a messages
    print("[N] How many messages do you want to send?\n[0] Enter 0 to quit and exit tool.")
    no_of_message = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Number of Message (Default 1 Message) ->  " + Style.RESET_ALL)

    # Set default number of Message
    if no_of_message.strip() == "":
        no_of_message = 1
    elif no_of_message == "0":
        exit_from_tool() # exit from code
    else:
        try :
            no_of_message = int(no_of_message)
        except:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            # Recall meaningless_message_generator if user enter wrong value
            meaningless_message_generator()

    # Set a lenght of words in message 
    print("[N] How many words can contain every message?\n[0] Enter 0 to quit and exit tool.")
    message_length = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Length of Message (Default 1 Word) ->  " + Style.RESET_ALL)

    # Set default lenght of Message
    if message_length.strip() == "":
        message_length = 1
    elif message_length == "0":
        exit_from_tool() # exit from code
    else:
        try :
            message_length = int(message_length)
        except:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            # Recall meaningless_message_generator if user enter wrong value
            meaningless_message_generator()

    # Show warning only if GUI is available
    if PYTHON_GUI_AVAILABLE:
        print(Fore.RED + "\nNow open the WhatsApp tab and move the cursor to the message box where you can type your message.\n" + Style.RESET_ALL, end="")
        # Check user is ready
        print("Are you ready? If you are ready...\n[1] Press Enter or 1 to continue\n[0] Enter 0 to quit and exit tool.")
        user_is_ready = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL)
        if user_is_ready.strip() == "" or user_is_ready.strip() == "1":
            # Warn to user, code is running now
            print(Fore.RED + "[ALERT!!!] Now you have only 10 seconds to move the cursor on message box tab.\n" + Style.RESET_ALL, end="")
            # Wait for 10 second to move message box tab
            time.sleep(10)
        elif user_is_ready == "0":
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid value entered. Please choose a valid number.\n" + Style.RESET_ALL)
            time.sleep(1.5)
            meaningless_message_generator()
    else:
        print(Fore.YELLOW + "\n[INFO] Running in simulation mode - no actual messages will be sent." + Style.RESET_ALL)
        print("Press Enter to continue with simulation...")
        input()

    for _ in range(no_of_message):
        # Initialize sentence for add random words and create a sentence
        sentence = ""
        # punctuation marks for add to the end of sentence
        punctuation_marks = [".", "?", "!", "...", ";"]
        # Generate the message
        for _ in range(message_length):
            characters = string.ascii_uppercase + string.ascii_lowercase
            lenght_of_word = random.randint(3,10)
            sentence += ''.join(random.choice(characters) for _ in range(lenght_of_word)) + " "

        # Create a finnal meassage
        message = sentence + random.choice(punctuation_marks)
        # write and send messages
        simulate_message_sending(message)
        print("Message Sent...")
    # Show message after Task is completed and Ask What is next task
    print(Fore.GREEN + Style.BRIGHT + "The given task has been completed.\n\n"+ Style.RESET_ALL)
    print(Fore.BLUE + Style.BRIGHT + "What is the next task?\nIf there are no more tasks, you can quit or exit the tool by using '0'."+ Style.RESET_ALL)
    spammer() 

# User is not able to type a message; the tool will create random text using characters and numbers and send it
def auto_typed_message():
    print(Fore.LIGHTMAGENTA_EX + "\n[*] Auto typed message" + Style.RESET_ALL + Fore.RED + "\t\t<SELECTED>" + Style.RESET_ALL)
    # Print options for the user to choose from
    print(Fore.YELLOW + "Choose an option from the following:" + Style.RESET_ALL)
    print("[1] Message with counting")
    print("[2] Random Message Generator")
    print("[3] Meaningless Message Generator")
    print("[0] Quit")

    # Handle any errors if occur
    try:
        # Get user input and convert it to an integer
        message_type = int(input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL))
        # Add validation for user input
        if message_type == 1:
            message_with_counting()
        elif message_type == 2:
            random_message_generator()
        elif message_type == 3:
            meaningless_message_generator()
        elif message_type == 0:
            # Call the exit function
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid option. Please choose 1, 2 or 3.\r" + Style.RESET_ALL)
            time.sleep(1.5)
            auto_typed_message()
    except:
        print(Fore.RED + "Invalid option. Please choose 1, 2 or 3.\r" + Style.RESET_ALL)
        time.sleep(1.5)
        auto_typed_message()

# Starting function of the tool
def spammer(): 
    # Print options for the user to choose from
    print(Fore.YELLOW + "Choose an option from the following:" + Style.RESET_ALL)
    print("[1] User typed message")
    print("[2] Auto typed message")
    print("[4] Help")
    print("[0] Quit")

    # Handle any errors if occur
    try:
        # Get user input and convert it to an integer
        message_type = int(input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL))
        # Add validation for user input
        if message_type == 1:
            user_typed_message()
        elif message_type == 2:
            auto_typed_message()
        elif message_type == 4:
            tool_help()
        elif message_type == 0:
            # Call the exit function
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid option. Please choose 1 or 2.\r" + Style.RESET_ALL,end="")
            time.sleep(1.5)
            spammer()
    except:
        print(Fore.RED + "Invalid option. Please choose 1 or 2.\r" + Style.RESET_ALL,end="")
        time.sleep(1.5)
        spammer()

# Exit function for exit from tool
def exit_from_tool():
# Simple Exit Loading Bar
    start = 0
    end = 50
    load = (Fore.GREEN + Style.BRIGHT + '='+ Style.RESET_ALL)
    unload = (Fore.RED + '_'+ Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + "\nPlease wait while we are exiting the tool" + Style.RESET_ALL)
    while start <= 50:
        print("\r"+load*start+">"+unload*end,end="")
        print("\r\t\t\t",start*2,"\r",end="")
        time.sleep(0.05)
        start += 1
        end -= 1
    print("\n\n")
    sys.exit(0)

# Main execution
if __name__ == "__main__":
    # Tool name design
    name_of_tool = pyfiglet.figlet_format("WA-Spam")

    # List of colors
    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "bold red", "light_green", "blue", "bold yellow", "bold cyan", "bold magenta"]

    # Choose a random color
    random_color = random.choice(colors)

    # Name of Tool and Code Developer
    name_of_tool_color = Console()

    name_of_tool_color.print(name_of_tool, style=random_color, end="\t\t\t\t\t-")
    print(Fore.GREEN + Style.BRIGHT + 'sh1vam-03'+ Style.RESET_ALL)

    # Start tool
    spammer()