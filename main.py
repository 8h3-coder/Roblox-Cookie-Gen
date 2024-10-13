import random
import threading
import time
from colorama import init, Fore

init(autoreset=True)

def logo():
    print(Fore.RED + f"""

  ______    ______    ______   __    __  ______  ________         ______   ________  __    __ 
 /      \  /      \  /      \ |  \  /  \|      \|        \       /      \ |        \|  \  |  \
|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$ /  $$ \$$$$$$| $$$$$$$$      |  $$$$$$\| $$$$$$$$| $$\ | $$
| $$   \$$| $$  | $$| $$  | $$| $$/  $$   | $$  | $$__          | $$ __\$$| $$__    | $$$\| $$
| $$      | $$  | $$| $$  | $$| $$  $$    | $$  | $$  \         | $$|    \| $$  \   | $$$$\ $$
| $$   __ | $$  | $$| $$  | $$| $$$$$\    | $$  | $$$$$         | $$ \$$$$| $$$$$   | $$\$$ $$
| $$__/  \| $$__/ $$| $$__/ $$| $$ \$$\  _| $$_ | $$_____       | $$__| $$| $$_____ | $$ \$$$$
 \$$    $$ \$$    $$ \$$    $$| $$  \$$\|   $$ \| $$     \       \$$    $$| $$     \| $$  \$$$
  \$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$ \$$$$$$$$        \$$$$$$  \$$$$$$$$ \$$   \$$
                                                                                              
                                                                                              
                                                                                              

    """)

def generate_cookie():
    """Generate a random Roblox cookie."""
    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    rancookie = ''.join(random.choice(valid_letters) for _ in range(1356))
    return "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

def worker(total_cookies, progress_lock, file_lock):
    """Worker thread for generating cookies."""
    with open("generated.txt", "a") as f:
        for i in range(total_cookies):
            cookie = generate_cookie()
            with file_lock:
                f.write(cookie + "\n")
                print(Fore.GREEN + f"[COOKIE GENERATED] (hidden) [{i + 1}/{total_cookies}]")
            time.sleep(0.1)  # Feel free to adjust this value if needed for performance

def main():
    logo()
    try:
        total_cookies = int(input("How many cookies do you want to create? "))
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")
        return

    progress_lock = threading.Lock()
    file_lock = threading.Lock()
    
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker, args=(total_cookies // 10, progress_lock, file_lock))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(Fore.BLUE + "All cookies generated and saved to generated.txt successfully!")

if __name__ == "__main__":
    main()
