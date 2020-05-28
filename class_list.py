import pickle
import os


class Armor:
    
    def __init__(self, torso, head, leg, arm):
        self.torso = torso
        self.head = head
        self.leg = leg
        self.arm = arm
        
    def print_stats(self):
        print("Head Armor: " + str(self.head))
        print("Torso Armor: " + str(self.torso))
        print("Arm Armor: " + str(self.arm))
        print("Leg Armor: " + str(self.leg))

class Weapons:
    def __init__(self, name, weapon_pen, dr):
        self.name = name
        self.damage = 1
        # self.weapon_bonus_damage = float(input(" Enter Weapon Bonus Damage:  "))
        self.weapon_pen = weapon_pen
        self.dr = dr
        
    def print_stats(self):
  
        print("Weapon Name: " + self.name)
        #print("Weapon Bonus Damage: " + str(self.weapon_bonus_damage))
        print("Weapon Pen: " + self.weapon_pen)
        print("Armor Divsor: " + str(self.dr))
        

class gen_combat:


    def __init__(self,name, HP_max, STR, armor, weapon):
        self.name = name
        self.HP_max = HP_max
        self.HP_current = HP_max
        self.STR = STR
        self.armor = armor
        self.weapon = weapon
        
    def print_stats(self):
        print("\n==========================================")
        print("Name: " + str(self.name))
        print("Max HP/Current HP: " + str(self.HP_max)+ "/" +str(self.HP_current))
        print("Strength: " + self.STR)
        print("==========================================")
        Weapons.print_stats(self.weapon)
        Armor.print_stats(self.armor)
        
    def get_name(self):
        return self.name

def gen_char(master_player_list):
    
    choice = "yes"
    
    while(choice == "yes"):
        
        print_names(master_player_list) 
         
    
        
        choice = input("\n Do you to add a character? (yes/no) ")
        if choice == "no":
            break
   
        
        player = gen_combat()
        master_player_list.append(player)
        
        
        
    return master_player_list
    
def delete_entry(master_player_list):
     
    choice = " yup"
    
    while(choice != "exit"):
        
        print_names(master_player_list)
        choice = input("\n Input the player number of who you like to delete? Or type exit to leave ")
        
        if choice != "exit":
            
            index = int(choice) - 1
            
            master_player_list.pop(int(index))
        

        
    return master_player_list

def print_entry(master_player_list):
    
    index = input("\n Which player would you like to view?")
    
    
    
    
    master_player_list[int(index)].print_stats()
        
    choice = input("\n Do you wish to view more characters? ")
    
    while(choice == "yes"):
        index = input("\n Which player would you like to view?")
        
        
    
        master_player_list[int(index)].print_stats()
        
    
        choice = input("\n Do you wish to view more characters? ")

def edit_entry(master_player_list):
    
    main_menu = "start"
    submenu = ""
    temp = " "
    player = gen_combat
    
    
    
    while main_menu != "exit":
        '''
        n = len(master_player_list) 


        for x in range(n):
            temp = master_player_list[int(x)].get_name()
            print(str(x+1) +". " + temp )
        '''    
                  
        print_names(master_player_list)     
        main_menu = input("\n Which player would you like to edit, type the number next to their name.  Or type Exit to leave ")
        
        if main_menu != "exit":
            
            index = int(main_menu) -1
        
        while submenu != "8" :
            
            submenu = input("\n 1: Change Character Name "
            "\n 2: Change Max HP"
            "\n 3: Change Armor Set"
            "\n 4: Change Current Weapon"
            "\n 5: To exit current menu"
            )
            
            if submenu == "1":
                player.name = input("\n New Player Name: ")
                master_player_list[int(index)].name = player.name
            
            elif submenu == "2":
                player.HP_max = input("\n New Player Max HP: ")
                if float(player.HP_max) < master_player_list[int(index)].HP_current:
                    master_player_list[int(index)].HP_current = player.HP_max
                
                master_player_list[int(index)].HP_max = player.HP_max
             
                
            elif submenu == "3":
                player.armor = Armor()
                master_player_list[int(index)].armor = player.armor
                
            
            elif submenu == "4":
                player.head_armor = input("New Head Armor: ")
                master_player_list[int(index)].head_armor = player.head_armor
            
            elif submenu == "5":
                player.leg_armor = input("New Leg Armor: ")
                master_player_list[int(index)].leg_armor = player.leg_armor
            
            elif submenu == "6":
                player.arm_armor = input("New Arm Armor: ")
                master_player_list[int(index)].arm_armor = player.arm_armor
                
            elif submenu == "7":
                player.weapon = Weapons()
                master_player_list[int(index)].weapon = player.weapon
                
            
        
        
        
        
        
        #while(choice != "8"):

                
                
            
            
            
                
                
            
        
    
 
        
        '''
        player = gen_combat()
        
        master_player_list[int(index)] = player
        
        player.name = input("\n Name?")
           
        master_player_list[int(index)].name = player.name
        '''
    
    return master_player_list
    
def print_names(master_player_list):
    n = len(master_player_list) 

    print("==============Player List==============")
    for x in range(n):
        temp = master_player_list[int(x)].get_name()
        print(str(x+1) +". " + temp )
    
def save(master_player_list):
    
    save = input("Save As: ")
    with open(save, 'wb') as output:
        #save01 = master_player_list[0]
       #pickle.dump(save01, output, pickle.HIGHEST_PROTOCOL)
    
        pickle.dump(master_player_list, output)
        
          
def load(master_player_list):
    load = input("Name of the file to Load: ")
    did_work = os.path.exists(load)
    while did_work == False:
        load = input(load + " does not exist, enter the correct name or exit to leave: ")
        did_work = os.path.exists(load)
    with open(load, 'rb') as dehe:
        
        
       
     
        newList = pickle.load(dehe)
        print("Load Successful!")
    
    #return master_player_list
    return newList
'''    
 def print_charinto():

    print("\n==========================================")
    print("\n Name: " + str(x.name))
    print("\n Max HP: " + str(x.HP_max))
    print("\n Current HP: " + str(x.HP_current))
    print("\n Armor: " + str(x.armor))
    print("\n Weapon: " + str(x.weapon_pen))
    print("\n==========================================")   
'''



''' 
master_player_list = expand_master_list(master_player_list)

print(master_player_list(0))
'''




#master_player_list[0].print_stats()

