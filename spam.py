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

# Try to import WhatsApp related libraries
try:
    import pywhatkit
    WHATSAPP_AVAILABLE = True
except ImportError:
    print(Fore.YELLOW + "Warning: pywhatkit not available. Install with: pip install pywhatkit" + Style.RESET_ALL)
    WHATSAPP_AVAILABLE = False

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
except ImportError:
    print(Fore.YELLOW + "Warning: selenium not available. Install with: pip install selenium" + Style.RESET_ALL)
    SELENIUM_AVAILABLE = False

# Initialize colorama
init()

# Try to import pyautogui with error handling
try:
    import pyautogui
    PYTHON_GUI_AVAILABLE = True
except Exception as e:
    print(Fore.YELLOW + "Warning: PyAutoGUI not available. GUI functions will be disabled." + Style.RESET_ALL)
    PYTHON_GUI_AVAILABLE = False

# WhatsApp configuration
WHATSAPP_CONFIG = {
    'method': 'pywhatkit',  # 'pywhatkit', 'selenium', or 'twilio'
    'country_code': '62',   # Indonesia country code
}

def send_whatsapp_message(phone_number, message):
    """
    Send WhatsApp message using selected method
    """
    # Format phone number
    if not phone_number.startswith('+'):
        if phone_number.startswith('0'):
            phone_number = WHATSAPP_CONFIG['country_code'] + phone_number[1:]
        else:
            phone_number = WHATSAPP_CONFIG['country_code'] + phone_number
    
    print(Fore.CYAN + f"\nAttempting to send message to: {phone_number}" + Style.RESET_ALL)
    print(Fore.CYAN + f"Message: {message}" + Style.RESET_ALL)
    
    if WHATSAPP_CONFIG['method'] == 'pywhatkit' and WHATSAPP_AVAILABLE:
        return send_whatsapp_pywhatkit(phone_number, message)
    elif WHATSAPP_CONFIG['method'] == 'selenium' and SELENIUM_AVAILABLE:
        return send_whatsapp_selenium(phone_number, message)
    else:
        print(Fore.RED + "WhatsApp messaging not available. Please install required libraries." + Style.RESET_ALL)
        return False

def send_whatsapp_pywhatkit(phone_number, message):
    """
    Send WhatsApp message using pywhatkit
    """
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, 15, True, 5)
        print(Fore.GREEN + "Message sent successfully via pywhatkit!" + Style.RESET_ALL)
        return True
    except Exception as e:
        print(Fore.RED + f"Error sending message via pywhatkit: {e}" + Style.RESET_ALL)
        return False

def send_whatsapp_selenium(phone_number, message):
    """
    Send WhatsApp message using Selenium
    """
    try:
        # Setup Chrome driver
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./whatsapp_profile')
        options.add_argument('--profile-directory=Default')
        
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
        
        # Wait for page to load (you need to scan QR code first time)
        print(Fore.YELLOW + "Waiting for WhatsApp Web to load..." + Style.RESET_ALL)
        time.sleep(20)
        
        # Find message box and send message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message + Keys.ENTER)
        
        time.sleep(5)
        driver.quit()
        print(Fore.GREEN + "Message sent successfully via Selenium!" + Style.RESET_ALL)
        return True
    except Exception as e:
        print(Fore.RED + f"Error sending message via Selenium: {e}" + Style.RESET_ALL)
        return False

def setup_whatsapp_config():
    """
    Setup WhatsApp configuration
    """
    print(Fore.CYAN + "\n=== WhatsApp Configuration ===" + Style.RESET_ALL)
    print("Select WhatsApp sending method:")
    print("[1] pywhatkit (Recommended - requires internet)")
    print("[2] Selenium (requires Chrome and manual QR scan)")
    
    choice = input(Fore.GREEN + "[+] Select method (1 or 2): " + Style.RESET_ALL)
    
    if choice == "1":
        WHATSAPP_CONFIG['method'] = 'pywhatkit'
        print(Fore.GREEN + "Using pywhatkit method" + Style.RESET_ALL)
    elif choice == "2":
        WHATSAPP_CONFIG['method'] = 'selenium'
        print(Fore.GREEN + "Using Selenium method" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice, using pywhatkit" + Style.RESET_ALL)
        WHATSAPP_CONFIG['method'] = 'pywhatkit'
    
    # Set country code
    country = input(Fore.GREEN + "[+] Enter country code (default: 62 for Indonesia): " + Style.RESET_ALL)
    if country.strip():
        WHATSAPP_CONFIG['country_code'] = country.strip()
    
    print(Fore.GREEN + "WhatsApp configuration completed!" + Style.RESET_ALL)
    return True

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
        - WhatsApp Direct:""" + Style.RESET_ALL + Fore.BLUE + """ Send messages directly to WhatsApp numbers.""" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Message with Counting:""" + Style.RESET_ALL + Fore.BLUE + """ Sends sequentially numbered messages. """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Random Message Generator:""" + Style.RESET_ALL + Fore.BLUE + """ Sends messages with random words or sentences. """ + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + """
            - Meaningless Message Generator:""" + Style.RESET_ALL + Fore.BLUE + """ Sends messages with random, nonsensical content.
        """ + Style.RESET_ALL + Fore.RED + """
          
Help Section """ + Style.RESET_ALL + Fore.GREEN + """

Main Menu """ + Style.RESET_ALL + Fore.BLUE + """
            Choose an option from the following:
            - [1] User Typed Message
            - [2] Auto Typed Message
            - [3] WhatsApp Direct
            - [4] Help
            - [5] Setup WhatsApp
            - [0] Quit
            - Enter Option -> """ + Style.RESET_ALL)
    spammer()

def whatsapp_direct():
    """
    Send messages directly to WhatsApp numbers
    """
    print(Fore.LIGHTMAGENTA_EX + "\n[*] WhatsApp Direct" + Style.RESET_ALL + Fore.RED + "\t\t<SELECTED>" + Style.RESET_ALL)
    
    if not WHATSAPP_AVAILABLE and not SELENIUM_AVAILABLE:
        print(Fore.RED + "WhatsApp features not available. Please install required libraries." + Style.RESET_ALL)
        print(Fore.YELLOW + "Run: pip install pywhatkit selenium" + Style.RESET_ALL)
        spammer()
        return
    
    # Get phone number
    print("\n[N] Enter WhatsApp phone number")
    print("    Format: 08123456789 (without country code)")
    print("    Or: +628123456789 (with country code)")
    phone_number = input(Fore.GREEN + "[+] Enter phone number: " + Style.RESET_ALL)
    
    if not phone_number.strip():
        print(Fore.RED + "Phone number cannot be empty!" + Style.RESET_ALL)
        whatsapp_direct()
        return
    
    # Get message type
    print("\n[N] Select message type:")
    print("[1] Single message")
    print("[2] Multiple messages")
    print("[3] Message with counting")
    message_type = input(Fore.GREEN + "[+] Select option: " + Style.RESET_ALL)
    
    if message_type == "1":
        # Single message
        message = input(Fore.GREEN + "[+] Enter your message: " + Style.RESET_ALL)
        if message.strip():
            send_whatsapp_message(phone_number, message)
        else:
            print(Fore.RED + "Message cannot be empty!" + Style.RESET_ALL)
    
    elif message_type == "2":
        # Multiple messages
        num_messages = input(Fore.GREEN + "[+] How many different messages: " + Style.RESET_ALL)
        try:
            num_messages = int(num_messages)
            messages = []
            for i in range(num_messages):
                msg = input(Fore.GREEN + f"[+] Message {i+1}: " + Style.RESET_ALL)
                if msg.strip():
                    messages.append(msg.strip())
            
            repeat = input(Fore.GREEN + "[+] How many times to repeat: " + Style.RESET_ALL)
            repeat = int(repeat) if repeat.strip() else 1
            
            for r in range(repeat):
                for msg in messages:
                    send_whatsapp_message(phone_number, msg)
                    time.sleep(2)  # Delay between messages
        
        except ValueError:
            print(Fore.RED + "Invalid number!" + Style.RESET_ALL)
    
    elif message_type == "3":
        # Message with counting
        base_message = input(Fore.GREEN + "[+] Enter base message: " + Style.RESET_ALL)
        count = input(Fore.GREEN + "[+] How many messages to send: " + Style.RESET_ALL)
        try:
            count = int(count)
            for i in range(count):
                message = f"{base_message} {i+1}"
                send_whatsapp_message(phone_number, message)
                time.sleep(2)  # Delay between messages
        except ValueError:
            print(Fore.RED + "Invalid number!" + Style.RESET_ALL)
    
    else:
        print(Fore.RED + "Invalid option!" + Style.RESET_ALL)
    
    print(Fore.GREEN + "\nWhatsApp sending completed!" + Style.RESET_ALL)
    spammer()

# [Keep all your existing functions like user_typed_message, message_with_counting, etc.]
# [Just add the new menu option in spammer() function]

def spammer(): 
    # Print options for the user to choose from
    print(Fore.YELLOW + "\nChoose an option from the following:" + Style.RESET_ALL)
    print("[1] User typed message")
    print("[2] Auto typed message")
    print("[3] WhatsApp Direct")
    print("[4] Help")
    print("[5] Setup WhatsApp")
    print("[0] Quit")

    # Handle any errors if occur
    try:
        # Get user input and convert it to an integer
        message_type = input(Fore.GREEN + Style.BRIGHT + "[+] Enter Option -> "+ Style.RESET_ALL)
        # Add validation for user input
        if message_type == "1":
            user_typed_message()
        elif message_type == "2":
            auto_typed_message()
        elif message_type == "3":
            whatsapp_direct()
        elif message_type == "4":
            tool_help()
        elif message_type == "5":
            setup_whatsapp_config()
            spammer()
        elif message_type == "0":
            # Call the exit function
            exit_from_tool()
        else:
            print(Fore.RED + "Invalid option. Please choose 1, 2, 3, 4, 5 or 0.\r" + Style.RESET_ALL)
            time.sleep(1.5)
            spammer()
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        time.sleep(1.5)
        spammer()

# [Keep all your other existing functions...]

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
    name_of_tool = pyfiglet.figlet_format("WA-Spam Pro")

    # List of colors
    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "bold red", "light_green", "blue", "bold yellow", "bold cyan", "bold magenta"]

    # Choose a random color
    random_color = random.choice(colors)

    # Name of Tool and Code Developer
    name_of_tool_color = Console()

    name_of_tool_color.print(name_of_tool, style=random_color, end="\t\t\t\t\t-")
    print(Fore.GREEN + Style.BRIGHT + 'sh1vam-03'+ Style.RESET_ALL)
    
    print(Fore.CYAN + "WhatsApp Spammer Pro - Direct WhatsApp Integration" + Style.RESET_ALL)
    
    # Check if WhatsApp libraries are available
    if not WHATSAPP_AVAILABLE and not SELENIUM_AVAILABLE:
        print(Fore.YELLOW + "Note: Install WhatsApp libraries for full features:" + Style.RESET_ALL)
        print(Fore.YELLOW + "pip install pywhatkit selenium" + Style.RESET_ALL)

    # Start tool
    spammer()
