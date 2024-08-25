from itertools import cycle
import os
import shutil
import time
from colorama import Fore
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
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
  0000000000000000000004                                                                                   6000000000000000000000  
  0000000000000000000000000004                                                                      74000000000000000000000000000  
  50000000000000000000000000000009                                                              780000000000000000000000000000003  
   00000000000000000000000000000000001                                                       30000000000000000000000000000000008   
    0000000000000000000000000000000000003                                                 2000000000000000000000000000000000000    
     800000000000000000000000000000000000003                                           200000000000000000000000000000000000009     
      6000000000000000000000000000000000000000                                       0000000000000000000000000000000000000005      
        00000000000000000000000000000000000000003                                 50000000000000000000000000000000000000000        
         300000000000000000000000000000000000000009                             000000000000000000000000000000000000000001         
           300000000000000000000000000000000000000000                        1000000000000000000000000000000000000000007           
             10000000000000000000000000000000000000092                       2800000000000000000000000000000000000000              
                30000000000000000000000000000002                                   50000000000000000000000000000001                
                    5000000000000000000082                                               2000000000000000000002                    
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                           50     20       9003      00   000000009       000       000000001       000                            
                           50     20      50500      00   00     60      00306             09      80208                           
                           500000000      09  09     00   00 300009     40   03     466666905     50   04                          
                           50     50     0062 205    00   00     00    70051 00     0044000       0053 903                         
                           50     20    000    001   00   00     90    00     00    06   308     00     00                         
                           50     20   505      00   00   000000002   00      70    04     00   00       08                        
                                                                                                                                   
                                                                LITE                                                                              
''')

def show_menu():
    print("                                                  ")
    print(Fore.LIGHTYELLOW_EX + "BY A125141")
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

    modified_code = code.replace('massagetitle', ip_address).replace('massagecontent', str(port))

    vbs_file_path = os.path.join('output', 'FILES', os.path.basename(file_path).replace('.txt', '.vbs'))
    os.makedirs(os.path.dirname(vbs_file_path), exist_ok=True)

    with open(vbs_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_code)

    print(Fore.LIGHTGREEN_EX + f"File '{os.path.basename(file_path)}' has been modified and saved as '{os.path.basename(vbs_file_path)}' successfully.")

def copy_and_save_as_vbs(file_path):
    vbs_file_path = os.path.join('output', 'FILES', os.path.basename(file_path).replace('.txt', '.vbs'))
    os.makedirs(os.path.dirname(vbs_file_path), exist_ok=True)

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

            client_code_path = os.path.join('FILES', 'popup.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'popup.vbs')

            try:
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "popup has been created and saved as popup.vbs successfully.")
            print() 


            ########################################################################################## GHOST #######################################################################################################################

        elif choice == '2':
            ip_address = input(Fore.LIGHTMAGENTA_EX + "Enter the Massage Title: ")
            port = input(Fore.LIGHTGREEN_EX + "Enter the Massage: ")

            print(Fore.YELLOW + "We prepare everything for you, relax...")
            time.sleep(5)

            client_code_path = os.path.join('FILES', 'ghost.txt')
            modify_code_and_save_as_vbs(client_code_path, ip_address, port)

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

            client_code_path = os.path.join('FILES', 'Restro.txt')
            vbs_code_path = os.path.join('output', 'FILES', 'Restro.vbs')

            try:
                shutil.copy(client_code_path, vbs_code_path)
                print(Fore.GREEN + "TXT File has been copied and saved as VBS successfully.")
            except Exception as e:
                print(Fore.RED + "Failed to copy TXT file as VBS:", str(e))

        
            print(Fore.GREEN + "VBS File has been created and saved successfully.") 
            print(Fore.LIGHTGREEN_EX + "virus Created Successfully")
            print() 


##############################################################################################################################################################################################################################################


        elif choice == 'h':
            print(Fore.LIGHTBLUE_EX + "HELP:")
            print(Fore.LIGHTWHITE_EX + "-----")
            print(Fore.LIGHTRED_EX + "This program is designed for educational purposes only.")
            print()
            print(Fore.LIGHTMAGENTA_EX + "Instructions:")
            print(Fore.GREEN + "1. Select the desired option by entering the corresponding number.")
            print(Fore.LIGHTCYAN_EX + "2. Follow the prompts to provide necessary information for the virus.")
            print(Fore.LIGHTGREEN_EX + "3. Wait for the program to prepare the virus.")
            print(Fore.CYAN + "4. The generated virus will be saved in the 'output' folder.")
            print(Fore.LIGHTRED_EX + "5. Use the generated viruses responsibly and only in controlled environments.")
            print(Fore.YELLOW + "6. The program will keep running until you choose to exit (option 0).")
            print()


        elif choice == 'c':
            print(Fore.MAGENTA + "-------------------------------------------------")
            print(Fore.YELLOW + "Contact US for a problem at [a125141contact@gmail.com]")
            print(Fore.MAGENTA + "-------------------------------------------------")


        elif choice == '0':
         break
        

        else:
            print(Fore.RED + "Invalid choice. Please select again.")

            

    print(Fore.BLUE + "@",Fore.LIGHTWHITE_EX + "Haibara will miss you :(",Fore.BLUE + "@" , Fore.LIGHTGREEN_EX + " Haibara©" , Fore.LIGHTYELLOW_EX + "Created by A125141"  )
    print(Fore.BLUE + "_________________________")
    print("                     ")
    print(Fore.YELLOW + "hAcK tHe WoRLd ")
    print("                     ")
    print()

if __name__ == "__main__":
    main()
    time.sleep(3)
