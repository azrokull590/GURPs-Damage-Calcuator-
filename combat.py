
import math



def attack(list):
    n = len(list) - 1
    
    attacker = input("\n What player is attacking?" )
    defender = input("\n Who is defending? ")
    target = input("\n What part are you aiming at: Skull, Vitals, Torso, Arms, Legs ?")
    
    
    combat_calc(list[int(attacker)], list[int(defender)], target)
     
    
def combat_calc(player1, player2, target):
    
    armor_round = armor_rating(player2.armor, target)
    pen_calc = weapon_pen(player1.weapon)
    damage_multi = 0
    
    print(target)
    
    if target != "torso":
        damage_multi = attacker_aiming(target, player1.weapon)
        
    else:
        damage_multi = pen_calc
        
    print(damage_multi)
 
     
    player1.weapon.damage = float(input("Damage dealt this turn?[3D+x] : "))
    
    
    if (player1.weapon.dr == 0): #error checking to avoid dividing by zero
        player1.weapon.dr = 1        
    
    armor_round =   armor_round / player1.weapon.dr    #placeholder to calc the armor
                                                #reduction from weapon
    
    current_damage =  math.floor(player1.weapon.damage - armor_round)
    if(current_damage <= 0):
        current_damage = 0
    
    
    
    player2.HP_current = player2.HP_current - math.floor(damage_multi*(current_damage))
    
    print("\n" + player1.name + " shot " + player2.name + " for " + str(math.floor((damage_multi*(player1.weapon.damage - armor_round)))) + " points of damage!")
    print("\n"+ player2.name + "'s armor absorbed " + str(math.floor(armor_round)) + " points of damage!")
    print("\n" + player2.name + " has " + str(player2.HP_current) + " hit points left!")
 

def weapon_pen(weapon_info):
    pen_bonus = 1.0
    
    if weapon_info.weapon_pen == "pi-":
        pen_bonus = 0.5
        return pen_bonus
    
    elif weapon_info.weapon_pen == "cut" or weapon_info.weapon_pen == "pi+":
        pen_bonus = 1.5
        return pen_bonus
    
    elif weapon_info.weapon_pen == "imp" or weapon_info.weapon_pen == "pi++":
        pen_bonus = 2.0
        return pen_bonus
    
    else:
        return pen_bonus


def attacker_aiming(body_parts, pen):
    bonus_damage = 1.0
    
    if body_parts == "vitals":
        if pen.weapon_pen == "pi-" or pen.weapon_pen == "pi++" or pen.weapon_pen == "pi" or pen.weapon_pen == "pi+" or pen.weapon_pen == "imp":
            bonus_damage = 3.0
            return bonus_damage
        
        elif pen.weapon_pen == "burn":
            bonus_damage = 2.0
            return bonus_damage
        
    elif body_parts == "skull":
        bonus_damage = 4.0
        return bonus_damage
    
    elif body_parts == "arms" or body_parts == "legs":
        if pen.weapon_pen == "pi++" or pen.weapon_pen == "pi+" or pen.weapon_pen == "imp":
            bonus_damage = 1.0
            return bonus_damage
    else:
        return bonus_damage
          
    
def armor_rating(player, target): 
    armor = player.torso
    
    if(target == "skull"):
        armor = player.head + 2
        return armor
    
    elif target == "arms":
        armor = player.arm
        return armor
     
    elif target == "legs":
        armor = player.leg
        return armor
    
    else:
        return armor
    
    
