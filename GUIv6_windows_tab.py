import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import class_list
from combat import*






class main_menu():
    
    def __init__(self,master):
        units = []
        self.names = tk.Listbox(master, height = 30)
        self.names.grid(row=0,column=1,columnspan=2)
        self.option(master,units, self.names)
        
              

    def option(self,master,units,names):
        add = tk.Button(master, text= "Add Character", command =lambda:add_character(master,units,names))
        view = tk.Button(master, text ="View Character",command= lambda: self.get_name(master,units))
        delete = tk.Button(master, text="Delete Character", command= lambda: self.get_del(master,units,names))
        edit = tk.Button(master, text="Edit Character", command = lambda: self.get_edit(master, units))
        combat = tk.Button(master, text="Combat!", command =lambda:damage_calc(master,units,names))
        
        add.grid(row=1,column=0)
        view.grid(row=1,column=1)
        edit.grid(row=1,column=2)
        delete.grid(row=1, column=3)
        combat.grid(row=2, column=1, ipadx=50,columnspan =2 )
    
    def get_name(self,master, units):
        temp = self.names.curselection() 
        select = self.names.get(temp[0])
        view_character(master,units ,select)
    
    def get_del(self,master,units,names):
        select = self.names.curselection() 
        
        delete_character(master,units ,names,select)
    
    def get_edit(self,master,units):
        temp = self.names.curselection() 
        select = self.names.get(temp[0])
        edit_character(master,units ,select,self.names)

class damage_calc(tk.Tk):
        def __init__(self,master,units,names):
            battle = tk.Toplevel()
            battle.title("Damage Calculator")
            list_names = []
            
            #battle.config(pady=25)
       
            
            self.var1 = tk.StringVar(battle)
            self.var1.set(units[0].name)
            
            self.var2 = tk.StringVar(battle)
            self.var2.set(units[0].name)
            
            self.T = tk.Text(battle, height=10, width=50)
            self.T.grid(row=10,column=1,columnspan=4)
            self.T.insert(tk.END, "Blood for the blood gods!")
     
           
            
            n = len(units)
            for x in range(n):
                list_names.append(units[x].name)
                print(list_names[x])
            
            
            self.char1 = tk.OptionMenu(battle, self.var1, *list_names) 
            self.char2 = tk.OptionMenu(battle, self.var2, *list_names) 
            
            self.labels(battle)
            self.combat(battle,units)
            
            #T.insert(tk.END, combat_calc.player1.name)
            
            
            
            
        def labels(self,battle):
            
            attacker = tk.Label(battle, text = "Attacker")
            defender = tk.Label(battle, text = "Defender")
             
            attacker.grid(row=0, column=1)
            defender.grid(row=0,column=3)
             
            self.char1.grid(row =1, column=1)
            self.char2.grid(row =1, column=3)
            
            
            
        def combat(self,battle,units):
            self.damage = tk.Entry(battle, width= 5)
            damage_label =tk.Label(battle, text = "Damage Rolled:")
            
            self.damage.grid(row=2, column=1)
            damage_label.grid(row=2,column=0)
            
            self.target_var = tk.StringVar(battle)
            self.target_var.set("Skull")
            
            self.target = tk.OptionMenu(battle, self.target_var,"Skull","Torso","Vitals", "Arms", "Legs")
            self.target_label = tk.Label(battle, text= "Where is the attacker aiming?") 
            
            self.target.grid(row=3, column=1)
            self.target_label.grid(row=3,column=0)
            combat_calc = tk.Button(battle, text = "Calculate Damage", command = lambda: self.dam_calc(units,battle)).grid(row=5,column=2)
            
            
        def dam_calc(self,units,battle):
            
            #self.var1.get(), self.var2.get(),self.target_var.get()) 
            p1 = self.var1.get()
            p2 = self.var2.get()
            
            
            index1 = self.player_finder(p1, units)
            index2 = self.player_finder(p2, units)
            
            target = self.target_var.get()
          
            dam = self.damage.get()
            dam = float(dam)
            print(dam)
            
            print(isinstance(dam, float))  
               
            combat_log =combat_calc(units[index1], units[index2], target, dam)
            
            self.T.insert(tk.END,combat_log)
            #T.insert(tk.END, text)

 
     
            
            

            
            
            
        def player_finder(self,name,units):
            n = len(units)
            for x in range(n):
                if name == units[x].name:
                    index = x
                    
            

            return index
            
             
            
                      
    
class edit_character(tk.Tk):
        def __init__(self,master,units,select,names):
            char_edit = tk.Toplevel()
            n = len(units)
            for x in range(n):
                if select == units[x].name:
                    char_edit.title(units[x].name+"'s Edit Screen")
                    self.name = tk.Entry(char_edit)
                    namel = tk.Label(char_edit, text = "Character Name:")
                    self.HP_max = tk.Entry(char_edit)
                    HP_maxl = tk.Label(char_edit, text = "Character Max HP:")
                    self.str = tk.Entry(char_edit)
                    strl = tk.Label(char_edit, text = "Character Strength:")
                    
                    #char Armor
                    self.head = tk.Entry(char_edit)
                    headl = tk.Label(char_edit, text = "Head Armor:")
                    self.torso = tk.Entry(char_edit)
                    torsol = tk.Label(char_edit, text = "Torso Armor:")
                    self.arm = tk.Entry(char_edit)
                    arml = tk.Label(char_edit, text = "Arm Armor:")
                    self.leg = tk.Entry(char_edit)
                    legl = tk.Label(char_edit, text = "Leg Armor:")
                    
                    self.var = tk.StringVar(char_edit)
                    self.var.set(units[x].weapon.weapon_pen)
                    
                    #button
                    #finishb = tk.Button(char_edit, text = "Finish Character", command = lambda: self.entry_field(char_new, units,names)).grid(row=10,column=0)
                    
                    finishb = tk.Button(char_edit, text = "Finish Edit", command = lambda: self.entry_field(char_edit, units,names,x)).grid(row=10,column=0)
                    
                    #char weapon
                    self.wep_name = tk.Entry(char_edit)
                    wep_namel = tk.Label(char_edit, text ="Weapon Name:" )
                    self.wep_pen = tk.OptionMenu(char_edit, self.var,"pi-","pi","pi+","cut","cr","imp","burn","tox","cor")
                    wep_penl = tk.Label(char_edit, text ="Weapon Penetration:" )

                    self.dr = tk.Entry(char_edit)
                    drl = tk.Label(char_edit, text = "Armor Divisor")
                    
                    #defualt entries
                    self.name.insert(0,units[x].name )
                    self.HP_max.insert(0,units[x].HP_max)
                    self.str.insert(0,units[x].STR)
                    self.head.insert(0,units[x].armor.head)
                    self.torso.insert(0,units[x].armor.torso)
                    self.arm.insert(0,units[x].armor.arm)  
                    self.leg.insert(0,units[x].armor.leg)
                    self.wep_name.insert(0,units[x].weapon.name)
           
                    self.dr.insert(0,units[x].weapon.dr)
                    
                    
                    
                    
                    #char stats grid
                    self.name.grid(row =0, column=1)
                    namel.grid(row=0,column=0)
                    self.HP_max.grid(row =1, column=1)
                    HP_maxl.grid(row=1,column=0)
                    self.str.grid(row =2, column=1)
                    strl.grid(row=2,column=0)
                    
                    #char armor  grid
                    self.head.grid(row =3, column=1)
                    headl.grid(row=3,column=0)
                    self.torso.grid(row =4, column=1)
                    torsol.grid(row=4,column=0)
                    self.arm.grid(row =5, column=1)
                    arml.grid(row=5,column=0)
                    self.leg.grid(row =6, column=1)
                    legl.grid(row=6,column=0)
                    
                    #weapon grid
                    self.wep_name.grid(row =7, column=1)
                    wep_namel.grid(row=7,column=0)
                    self.wep_pen.grid(row =8, column=1)
                    wep_penl.grid(row=8,column=0)
                    self.dr.grid(row =9, column=1)
                    drl.grid(row=9,column=0)
     
        def entry_field(self,char_new,units,names, select):
            
    
            player_weapon = class_list.Weapons(self.wep_name.get(), self.var.get(),self.dr.get())
            player_armor = class_list.Armor(self.torso.get(), self.head.get(),self.arm.get(), self.leg.get())
            player = class_list.gen_combat(self.name.get(), self.HP_max.get(),self.str.get(), player_armor, player_weapon)
            units.insert(select,player)
           
            
            #delete_character.remove_list(self, select, names)
            #self.refresh(units,names)
            units[select].print_stats()
            print(select)
            
            self.replace(char_new, units, names, select)
            char_new.destroy()
        
        def replace(self,char_new,units,names, select):
            '''
            if select == 1:
                names.insert(select, units[select].name)
                names.delete(select+1,last = None )
            
            else:
            '''    
            n = len(units)-1
            names.insert(select, units[select].name)
            names.delete(select+1,last = None )
                

            
        
class add_character(tk.Tk):
        def __init__(self,master,units,names):
            char_new = tk.Toplevel()
            char_new.title("Character Creator")
            
            #char stats
            self.name = tk.Entry(char_new)
            namel = tk.Label(char_new, text = "Character Name:")
            self.HP_max = tk.Entry(char_new)
            HP_maxl = tk.Label(char_new, text = "Character Max HP:")
            self.str = tk.Entry(char_new)
            strl = tk.Label(char_new, text = "Character Strength:")
            
            #char Armor
            self.head = tk.Entry(char_new)
            headl = tk.Label(char_new, text = "Head Armor:")
            self.torso = tk.Entry(char_new)
            torsol = tk.Label(char_new, text = "Torso Armor:")
            self.arm = tk.Entry(char_new)
            arml = tk.Label(char_new, text = "Arm Armor:")
            self.leg = tk.Entry(char_new)
            legl = tk.Label(char_new, text = "Leg Armor:")
            
            self.var = tk.StringVar(char_new)
            self.var.set("pi-")
            
            #button
            finishb = tk.Button(char_new, text = "Finish Character", command = lambda: self.entry_field(char_new, units,names)).grid(row=10,column=0)
            
            
            #char weapon
            self.wep_name = tk.Entry(char_new)
            wep_namel = tk.Label(char_new, text ="Weapon Name:" )
            self.wep_pen = tk.OptionMenu(char_new, self.var,"pi-","pi","pi+","cut","cr","imp","burn","tox","cor")
            wep_penl = tk.Label(char_new, text ="Weapon Penetration:" )
            self.dr = tk.Entry(char_new)
            drl = tk.Label(char_new, text = "Armor Divisor")
            
            #char stats grid
            self.name.grid(row =0, column=1)
            namel.grid(row=0,column=0)
            self.HP_max.grid(row =1, column=1)
            HP_maxl.grid(row=1,column=0)
            self.str.grid(row =2, column=1)
            strl.grid(row=2,column=0)
            
            #char armor  grid
            self.head.grid(row =3, column=1)
            headl.grid(row=3,column=0)
            self.torso.grid(row =4, column=1)
            torsol.grid(row=4,column=0)
            self.arm.grid(row =5, column=1)
            arml.grid(row=5,column=0)
            self.leg.grid(row =6, column=1)
            legl.grid(row=6,column=0)
            
            #weapon grid
            self.wep_name.grid(row =7, column=1)
            wep_namel.grid(row=7,column=0)
            self.wep_pen.grid(row =8, column=1)
            wep_penl.grid(row=8,column=0)
            self.dr.grid(row =9, column=1)
            drl.grid(row=9,column=0)
       
    
        def entry_field(self,char_new,units,names):
            
            p_dr = self.dr.get()
            p_tor = self.torso.get()
            p_hel = self.head.get()
            p_arm = self.arm.get()
            p_leg = self.leg.get()
            p_HP = self.HP_max.get()
            STR = self.str.get()
            
            player_weapon = class_list.Weapons(self.wep_name.get(), self.var.get(),float(p_dr))
            player_armor = class_list.Armor(float(p_tor), float(p_hel),float(p_arm), float(p_leg))
            player = class_list.gen_combat(self.name.get(), float(p_HP),float(STR), player_armor, player_weapon)
            units.append(player)
      
            
            self.refresh(units,names)
            char_new.destroy()
            
        def refresh(self,units,names):
            n = len(units)-1
            names.insert(tk.END, units[n].name)
            
            

class delete_character(tk.Tk):
    def __init__(self,master,units,names,select):
        select_name = names.get(select[0])
        print(select_name)
        n = len(units)
        for x in range(n):
            if select_name == units[x].name:
                delBox = tk.messagebox.askquestion("Character Delete", "Are you sure you want to delete "+units[x].name)
        
                if delBox == "yes":
                    units.pop(x)
                    self.remove_list(x,names)
                    
    def remove_list(self,select,names):
        
            names.delete(select, last = None)           
        

class view_character(tk.Tk):
    def __init__(self,master,units,select):
      
        n = len(units)
        for x in range(n):
            if select == units[x].name:
                stats = tk.Toplevel()
                stats.config(padx=10, pady=10)
                stats.title(units[x].name+"'s Stats")
                
                
                #print labels
                #n = "Name: " + units[x].name
                #name = tk.Label(stats,text = n)
                name = tk.Label(stats, text = "Name:" + units[x].name)
                hp = tk.Label(stats , text = "HP: "+ str(units[x].HP_max) + "/" + str(units[x].HP_current))
                str = tk.Label(stats, text = "Strength: " + str(units[x].STR))
                armor = tk.Label(stats, text="Armor= |Head: "+ str(units[x].armor.head)+ " |Torso: "+ str(units[x].armor.torso)+" |Arms: "+str(units[x].armor.arm)+ " |Legs: " +str(units[x].armor.leg))
                wep = tk.Label(stats, text ="Weapon Name: " + units[x].weapon.name + "| Weapon Penetration: " + units[x].weapon.weapon_pen + " |DR: "+str(units[x].weapon.dr))
                
                #print
                
                name.grid(row=0,column=0)
                hp.grid(row=0,column=1)
                str.grid(row=0,column=2)
                armor.grid(row=1,column=0 )
                wep.grid(row=2, column=0)

        
if __name__ == '__main__':
    root = tk.Tk()
    root.config(padx=10, pady=10)
    root.title('GURPS')
    main_menu(root)


    root.mainloop()
    

    
