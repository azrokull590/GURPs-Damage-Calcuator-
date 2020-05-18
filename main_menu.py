'''
Created on May 15, 2020

@author: Alberto Alvarez
'''
import random
import class_list
import combat
import sys


def main_menu():
    master_player_list =  [] 
    
    master_choice = 0
    while master_choice != "8":
        print("==== Main Menu ====")
        print("1. Add Characters")
        print("2. Edit Characters")
        print("3. Delete Characters")
        print("4. View Characters")
        print("5. Damage Calculator")
        print("6. Save Characters")
        print("7. Load Characters")
        print("8. Exit Program")
        
        master_choice = input(" ")
        
        if master_choice == "1":
            class_list.gen_char(master_player_list)
        
        elif master_choice == "2":
            class_list.edit_entry(master_player_list)
        
        elif master_choice == "3":
            class_list.delete_entry(master_player_list)
        
        elif master_choice == "4":
            class_list.print_entry(master_player_list)
            
        elif master_choice == "5":
            combat.attack(master_player_list)
        
        elif master_choice == "6":
            class_list.save(master_player_list)
            
        elif master_choice == "7":
           master_player_list = class_list.load(master_player_list)
            
        elif master_choice == "8":
            print("Farwell!")
            sys.exit()
    
    
    
def welcome_msg():
        print("############  #          #  ###########    ############  ############ ")
        print("#             #          #  #          #   #          #  #            ")
        print("#             #          #  #          #   #          #  #            ")
        print("#             #          #  #          #   #          #  #            ")
        print("#    #######  #          #  ###########    ############  ############ ")
        print("#          #  #          #  #          #   #                        # ")
        print("#          #  #          #  #           #  #                        # ")
        print("#          #  #          #  #           #  #                        # ")
        print("############  ############  #           #  #             ############ ")
        print("======================== DAMAGE CALCULATOR ===========================")
        
        intro_msg = ["BLOOD FOR THE BLOOD GOD, SKULLS FOR THE SKULL THORNE!",
        "Never forgive, never forgot!", "Cry 'Havoc!', and let slip the dogs of war",
        "Walk softly and carry a big gun", "WAAAGHHHH!!!! ", "Ride now, ride now, ride! Ride for ruin and the world's ending",
        "No friend ever served me, and no enemy ever wronged me, whom I have not repaid in full",
         "The die is cast", "Come and get them!", "The real hero is the man who fights even though he is scared."
         ,"You two take turns kicking each other's asses!  "]
        
        msg = intro_msg[random.randint(0,10)]
        
        print("\n \n ")
        print("( " + msg + " )" )
        print("\n \n ")
        
    