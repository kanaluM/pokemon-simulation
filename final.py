# CS 5 Gold
# Filename: poke.py
# Name: Kanalu Monaco
# Problem Description: The final battle!

# of course there's RNG involved
import random 

# List of pokemon types
types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", 
"Ground", "Flying", "Psychic", "Bug","Rock", "Ghost", "Dragon", "Dark", "Steel"]

# type multipliers based on type
# KEY is attacking type
# VALUES are multiplier based on defending type
matchup = {
"Normal": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5], 
"Fire": [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 1],
"Water": [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1],
"Electric": [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1],
"Grass": [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5],
"Ice": [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5],
"Fighting": [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2],
"Poison": [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0],
"Ground": [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2],
"Flying": [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5],
"Psychic": [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5],
"Bug": [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5],
"Rock": [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5],
"Ghost": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5],
"Dragon": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5],
"Dark": [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5],
"Steel": [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5]
}

# dictionary of moves
# KEY is move
# VALUES are type, special/physical, power, accuracy, secondary effect
# no status moves
moves = {
"Strength": ["Normal", "atk", 80, 100, [0, "None"]],
"Hyper Voice": ["Normal", "spatk", 90, 100, [0, "None"]],
"Flamethrower": ["Fire", "spatk", 95, 100, [0.1, "BRN"]],
"Flame Wheel": ["Fire", "atk", 60, 100, [0.1, "BRN"]],
"Surf": ["Water", "spatk", 95, 100, [0, "None"]],
"Waterfall": ["Water", "atk", 80, 100, [0.2, "flinch"]],
"Thunderbolt": ["Electric", "spatk", 95, 100, [0.1, "PRZ"]],
"Spark": ["Electric", "atk", 65, 100, [0.3, "PRZ"]],
"Energy Ball": ["Grass", "spatk", 80, 100, [0.1, "spdef"]],
"Seed Bomb": ["Grass", "atk", 80, 100, [0, "None"]],
"Leaf Blade": ["Grass", "atk", 90, 100, [2, "crit"]],
"Ice Beam": ["Ice", "spatk", 95, 100, [0.1, "FRZ"]],
"Avalanche": ["Ice", "atk", 80, 100, [0, "None"]],
"Aura Sphere": ["Fighting", "spatk", 90, 100, [0, "None"]],
"Brick Break": ["Fighting", "atk", 75, 100, [0, "None"]],
"Sludge Bomb": ["Poison", "spatk", 90, 100, [0.3, "PSN"]],
"Poison Jab": ["Poison", "atk", 90, 100, [0.3, "PSN"]],
"Earthquake": ["Ground", "atk", 100, 100, [0, "None"]],
"Earth Power": ["Ground", "spatk", 90, 100, [10, "spdef"]],
"Air Slash": ["Flying", "spatk", 75, 95, [0.3, "flinch"]],
"Aerial Ace": ["Flying", "atk", 60, 100, [0, "None"]],
"Psychic": ["Psychic", "spatk", 90, 100, [0.1, "spdef"]],
"Psycho Cut": ["Psychic", "atk", 90, 100, [0, "None"]],
"Extrasensory": ["Psychic", "spatk", 80, 100, [0.1, "flinch"]],
"X-scissor": ["Bug", "atk", 80, 100, [0, "None"]],
"Bug Buzz": ["Bug", "spatk", 90, 100, [0.1, "spdef"]],
"Rock Slide": ["Rock", "atk", 75, 90, [0.3, "flinch"]],
"Stone Edge": ["Rock", "atk", 100, 80, [2, "crit"]],
"Power Gem": ["Rock", "spatk", 80, 100, [0, "None"]],
"Shadow Ball": ["Ghost", "spatk", 80, 100, [0.2, "spdef"]],
"Shadow Punch": ["Ghost", "atk", 60, 100, [0, "None"]],
"Dragon Pulse": ["Dragon", "spatk", 90, 100, [0, "None"]],
"Dragon Claw": ["Dragon", "atk", 80, 100, [0, "None"]],
"Dark Pulse": ["Dark", "spatk", 80, 100, [0.2, "flinch"]],
"Night Slash": ["Dark", "atk", 70, 100, [2, "crit"]],
"Crunch": ["Dark", "atk", 80, 100, [0.2, "def"]],
"Iron Head": ["Steel", "atk", 80, 100, [0.3, "flinch"]],
"Flash Cannon": ["Steel", "spatk", 80, 100, [0.1, "spdef"]]
}

# dictionary of Cynthia's pokemon (AI opponent)
# KEY is pokemon
# VALUES are [innoh dex number, [types], [base stats: hp, atk, def, spatk, spdef, spe], [moveset]
# some moves cannot be normally learned by pokemon but I do not care
cynthia = {
"Spiritomb": [108, ["Ghost", "Dark"], [50, 92, 108, 92, 108, 35], ["Dark Pulse", "Shadow Ball", "Bug Buzz", "Psychic"]],
"Lucario": [116, ["Fighting", "Steel"], [70, 110, 70, 115, 70, 90], ["Strength", "Aura Sphere", "Shadow Ball", "Stone Edge"]],
"Togekiss": [175, ["Normal", "Flying"], [85, 50, 95, 120, 115, 80], ["Air Slash", "Aura Sphere", "Surf", "Thunderbolt"]],
"Roserade": [27, ["Grass", "Poison"], [60, 70, 55, 125, 105, 90], ["Energy Ball", "Sludge Bomb", "Extrasensory", "Shadow Ball"]],
"Milotic": [139, ["Water", "None"], [95, 60, 79, 100, 125, 81], ["Surf", "Ice Beam", "Dragon Pulse", "Flamethrower"]],
"Garchomp": [111, ["Dragon", "Ground"], [108, 130, 95, 80, 85, 102], ["Dragon Claw", "Earthquake", "Flamethrower", "Rock Slide"]],
}

# dictionary of player pokemon
# KEY is pokemon
# VALUES are sinnoh dex number, [types], [stats - hp, atk, def, spatk, spdef, spe], [moveset]
# some moves cannot be normally learned by pokemon but I do not care
yourpokemon = {
"Torterra": [3, ["Grass", "Ground"], [95, 109, 105, 75, 85, 56], ["Energy Ball", "Earthquake", "Crunch", "Rock Slide"]],
"Infernape": [6, ["Fire", "Fighting"], [76, 104, 71, 104, 71, 108], ["Flamethrower", "Brick Break", "Aura Sphere", "Poison Jab"]],
"Empoleon": [9, ["Water", "Steel"], [84, 86, 88, 111, 101, 60], ["Surf", "Flash Cannon", "Aerial Ace", "Strength"]],
"Staraptor": [12, ["Normal", "Flying"], [85, 120, 70, 50, 50, 100], ["Strength", "Aerial Ace", "Brick Break", "Leaf Blade"]],
"Bibarel": [14, ["Normal", "Water"], [79, 85, 60, 55, 60, 71], ["Strength", "Waterfall", "Aerial Ace", "Brick Break"]],
"Luxray": [19, ["Electric", "None"], [80, 120, 79, 95, 79, 70], ["Spark", "Crunch", "Brick Break", "Strength"]],
"Alakazam": [22, ["Psychic", "None"], [55, 50, 45, 135, 85, 120], ["Psychic", "Shadow Ball", "Dark Pulse", "Aura Sphere"]],
"Gyarados": [24, ["Water", "Flying"], [95, 125, 79, 60, 100, 81], ["Waterfall", "Aerial Ace", "Earthquake", "Hyper Voice"]],
"Steelix": [35, ["Steel", "Ground"], [75, 85, 200, 55, 65, 30], ["Iron Head", "Earthquake", "Strength", "Stone Edge"]],
"Machamp": [42, ["Fighting", "None"], [90, 130, 80, 65, 85, 55], ["Brick Break", "Rock Slide", "Strength", "Earthquake"]],
"Gastrodon": [61, ["Water", "Ground"], [111, 83, 68, 92, 82, 39], ["Earth Power", "Surf", "Ice Beam", "Sludge Bomb"]],
"Heracross": [62, ["Bug", "Fighting"], [80, 125, 75, 40, 95, 85], ["Brick Break", "X-scissor", "Earthquake", "Night Slash"]],
"Gengar": [71, ["Ghost", "Poison"], [60, 65, 60, 130, 75, 110], ["Shadow Ball", "Sludge Bomb", "Dark Pulse", "Aura Sphere"]],
"Honchkrow": [75, ["Dark", "Flying"], [100, 125, 52, 105, 52, 71], ["Night Slash", "Aerial Ace", "Shadow Ball", "Dark Pulse"]],
"Rapidash": [91, ["Fire", "None"], [65, 100, 70, 80, 80, 105], ["Flame Wheel", "Poison Jab", "Strength", "Iron Head"]],
"Pikachu": [104, ["Electric", "None"], [35, 55, 50, 50, 40, 90], ["Thunderbolt", "Flamethrower", "Surf", "Aura Sphere"]],
"Snorlax": [113, ["Normal", "None"], [160, 110, 65, 65, 110, 30], ["Strength", "Rock Slide", "Crunch", "Earthquake"]],
"Drapion": [128, ["Poison", "Dark"], [70, 90, 110, 60, 75, 95], ["Poison Jab", "Night Slash", "X-scissor", "Earthquake"]],
"Toxicroak": [130, ["Poison", "Fighting"], [83, 106, 65, 86, 65, 85], ["Poison Jab", "Brick Break", "Extrasensory", "Night Slash"]],
"Abomasnow": [143, ["Grass", "Ice"], [90, 92, 75, 92, 85, 60], ["Avalanche", "Seed Bomb", "Ice Beam", "Earthquake"]],
"Weavile": [145, ["Dark", "Ice"], [70, 120, 65, 45, 85, 125], ["Night Slash", "Avalanche", "X-scissor", "Iron Head"]],
"Gardevoir": [159, ["Psychic", "None"], [68, 65, 65, 125, 115, 80], ["Psychic", "Shadow Ball", "Aura Sphere", "Energy Ball"]],
"Gallade": [160, ["Psychic", "Fighting"], [68, 125, 65, 65, 115, 80], ["Leaf Blade", "Psycho Cut", "Brick Break", "Strength"]],
"Altaria": [172, ["Dragon", "Flying"], [75, 70, 90, 70, 105, 80], ["Dragon Pulse", "Dragon Claw", "Aerial Ace", "Ice Beam"]],
"Houndoom": [177, ["Dark", "Fire"], [75, 90, 50, 110, 80, 95], ["Dark Pulse", "Flamethrower", "Energy Ball", "Earth Power"]],
"Magnezone": [180, ["Electric", "Steel"], [70, 70, 115, 130, 90, 60], ["Flash Cannon", "Thunderbolt", "Hyper Voice", "Bug Buzz"]],
"Rhyperior": [188, ["Ground", "Rock"], [115, 140, 130, 55, 55, 40], ["Earthquake", "Stone Edge", "Poison Jab", "Brick Break"]],
"Dusknoir": [191, ["Ghost", "None"], [45, 100, 135, 65, 135, 45], ["Shadow Punch", "Night Slash", "Rock Slide", "Strength"]],
"Porygon-z": [194, ["Normal", "None"], [85, 80, 70, 135, 75, 90], ["Hyper Voice", "Thunderbolt", "Dark Pulse", "Ice Beam"]],
"Scizor": [196, ["Bug", "Steel"], [70, 130, 100, 55, 80, 65], ["Iron Head", "X-scissor", "Strength", "Night Slash"]],
"Electivire": [199, ["Electric", "None"], [75, 123, 67, 95, 85, 95], ["Spark", "Earthquake", "Iron Head", "Rock Slide"]],
"Magmortar": [202, ["Fire", "None"], [75, 95, 67, 125, 95, 83], ["Flamethrower", "Dark Pulse", "Thunderbolt", "Psychic"]],
"Mamoswine": [205, ["Ice", "Ground"], [110, 130, 80, 70, 60, 80], ["Avalanche", "Earthquake", "Strength", "Stone Edge"]],
"Froslass": [208, ["Ice", "Ghost"], [70, 80, 70, 80, 70, 110], ["Shadow Ball", "Ice Beam", "Thunderbolt", "Psychic"]]
} 


# type multiplier function
def typematch(m, t1, t2):
    """Takes the type of the attacking player's move (m) and the defending
    player's type (t1 and t2) and calculates a damage multiplier"""

    t0 = moves.get(m)[0]   # move type
    deftype1 = types.index(t1)   # defending type 1 number
    tmult1 = matchup.get(t0)[deftype1]   # matchup against defending type 1

    if t2 == "None":   # no type 2
        tmult2 = 1
    else:
        deftype2 = types.index(t2)   # defending type 2 number
        tmult2 = matchup.get(t0)[deftype2]   # matchup against defending type 2

    tmult = tmult1 * tmult2   # matchup against defending pokemon (multipliers multiplied)

    return tmult


# hp calculator
def hpstat(base, level):
    """Takes a pokemon's base hp stat and level and turns it into its effective hp"""

    IV = random.choice(range(20, 32))   # random decent IV
    EV = random.choice(range(100, 253))   # random decent EV - EV total will be >510 but I do not care 

    HP = (((2*base) + IV + EV//4)*level)//100 + level + 10

    return HP


# other stat calculator
def otherstat(base, level):
    """"Takes a pokemon's base stat and level and turns it into its effective stat"""

    IV = random.choice(range(20, 32))   # random decent IV
    EV = random.choice(range(100, 253))   # random decent EV - EV total will be >510 but I do not care 

    stat = 5 + (((2*base) + IV + EV//4)*level)//100

    return stat


# applies stat modifier when hit by a move - current moves are only opponent defense drops
def statmod(player, move):
    """calculates and applies a stat modifier to a target pokemon if necessary"""

    # stat modifiers moves only
    if moves.get(move)[4][1] in ["def", "spdef"]:
        pass
    else:
        return

    # does a modifier occur?
    probability = moves.get(move)[4][0]   # probability of secondary modifier effect
    threshold = random.random()   # generate a random number from 0 to 1
    if threshold <= probability:   # continue if yes
        pass
    else:
        return

    # stat modifier
    if moves.get(move)[4][1] == "def":
        player.stats[1] += 1
        print("{}'s defense was lowered!".format(player))
    elif moves.get(move)[4][1] == "spdef":
        player.stats[3] += 1
        print("{}'s special defense was lowered!".format(player))

    # the multipliers (decrease only)
    atkmult = 2/(2+player.stats[0])
    defmult = 2/(2+player.stats[1])
    spatkmult = 2/(2+player.stats[2])
    spdefmult = 2/(2+player.stats[3])
    spemult = 2/(2+player.stats[4])

    player.stats = [0, 0, 0, 0, 0]   # reset stat drops so calculation stops

    # apply the modifiers
    player.atk *= atkmult
    player.defs *= defmult
    player.spatk *= spatkmult 
    player.spdef *= spdefmult
    player.spe *= spemult


# turn order
def turnorder(player, opp):
    """Accepts battling mons and determines turn order
    True if you outspeed Cynthia, False if you get outsped"""
    
    if player.spe > opp.spe:   # player goes first
        return True
    else:
        return False   # opponent goes first
    

# applies status when hit by a move
def applystatus(target, move):
    """calculates and applies a status condition to a target/user pokemon if necessary"""

    status = ["flinch", "PSN", "FRZ", "BRN", "PRZ"]   # status list

    prob = moves.get(move)[4][0]   # probability of status occuring
    effect = moves.get(move)[4][1]   # the status that could occur
    threshold = random.random()   # randomly generated threshold

    # is there a secondary effect?
    if effect in status:   # yes
        pass
    else:
        return   # no

    # does secondary effect happen?
    if threshold <= prob:   # yes
        pass
    else: 
        return   # no

    # is there already a non-volatile status condition?
    if effect in status[1:]:
        for x in status[1:]:
            if x in target.status:   # yes
                return

    # apply status to a target    
    target.status += [effect]
    if effect == "PSN":
        print(target, "was poisoned!")
    elif effect == "BRN":
        print(target, "was burned!")
    elif effect == "FRZ":
        print(target, "was frozen solid!")
    elif effect == "PRZ":
        print(target, "was paralyzed")
    

# status effect
def statuseffect(player):
    """determines effect of status on a pokemon turn capability. Returns True if a pokemon
    can still attack, returns False if not"""

    status = ["flinch", "BRN", "FRZ", "PRZ", "NVPRZ"]   # cannot attack status list
    
    for x in player.status:
        if x == "FRZ":
            if random.random() <= 0.2:
                print(player, "thawed out!")
                player.status = []
                return True
            else:
                return False
            return False
        elif x == "PRZ":
            player.status = ["NVPRZ"]
            player.spe *= 0.25
            if random.random() <= 0.25:
                return False
            else:
                return True
        elif x == "NVPRZ":
            if random.random() <= 0.25:
                return False
            else:
                return True
        elif x == "BRN":
            player.status = ["NVBRN"]
            player.atk *= 0.5
            return True
        elif x == "flinch":
            return False

    return True


# prints status message if you cannot attack due to status
def statusmsg(player):
    """prints the message corresponding to a status condition that prevents attacking"""

    status = ["flinch", "FRZ", "PRZ", "NVPRZ"]   # cannot attack status list
    
    for x in player.status:
        if x == "FRZ":
            print(player, "is frozen solid")
        elif x == "PRZ":
            print(player, "is paralyzed and can't move")
        elif x == "NVPRZ":
            print(player, "is paralyzed and can't move")
        elif x == "flinch":
            print(player, "flinched!")
         

# damage multiplier calculator
def damagemult(player, opp, move):
    """returns damage multiplier"""

    if moves.get(move)[4][1] == "crit":
        critmult = random.choice([1, 1, 1, 1, 1, 1, 1, 2])   # 1/8 chance to crit for a high-crit move
    else:
        critmult = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])   # 1/16 chance to crit for 2x damage

    rngmult = random.uniform(0.85, 1.0)   # high/low roll
    
    if player.type1 == moves.get(move)[0]:   # type 1
        STAB = 1.5
    elif player.type2 == moves.get(move)[0]:   # type 2
        STAB = 1.5
    else:   # no stab   :(
        STAB = 1

    typemult = typematch(move, opp.type1, opp.type2)   # type multiplier helper function 

    # status mult in progress

    totmult = critmult*rngmult**STAB*typemult   # total damage multiplier

    return [totmult, critmult]
    

# accuracy check
def acccheck(move):
    """accuracy check for a move. Returns Trus if hit, False if miss"""

    acc = (moves.get(move)[3])/100
    threshold = random.random()

    if threshold <= acc:
        return True
    else:
        return False


# Defining individual pokemon - consider modifying to make Cynthia stronger
class indpoke:
    """An individual pokemon class"""

    # constructor
    def __init__(self, mon):
        """constructs a pokemon (accepted as a string) with types, stats, and moves"""

        if mon in list(yourpokemon.keys()):   # pokemon you use
            self.name = mon
            self.level = random.randrange(52, 61)   # random level between 52 and 60
            self.type1 = yourpokemon.get(mon)[1][0]   # type 1 from yourpokemon dictionary
            self.type2 = yourpokemon.get(mon)[1][1]   # type 2 from yourpokemon dictionary if exists
            self.hp = hpstat(yourpokemon.get(mon)[2][0], self.level)   # effective hp stat
            self.atk = otherstat(yourpokemon.get(mon)[2][1], self.level)   # effective attack stat
            self.defs = otherstat(yourpokemon.get(mon)[2][2], self.level)   # effective defense stat
            self.spatk = otherstat(yourpokemon.get(mon)[2][3], self.level)   # effective special attack stat
            self.spdef = otherstat(yourpokemon.get(mon)[2][4], self.level)   # effective special defense stat
            self.spe = otherstat(yourpokemon.get(mon)[2][5], self.level)   # effective speed stat
            self.moves = [ yourpokemon.get(mon)[3][x] for x in [0, 1, 2, 3] ]  # list of moves
            self.status = []   # start with no status condition
            self.stats = [0, 0, 0, 0, 0]   # start with no stat modifiers - atk, def, spatk, spdef, spe

        elif mon in list(cynthia.keys()):   # pokemon for cynthia
            self.name = mon
            self.level = 60   # random level between 52 and 60
            self.type1 = cynthia.get(mon)[1][0]   # type 1 from yourpokemon dictionary
            self.type2 = cynthia.get(mon)[1][1]   # type 2 from yourpokemon dictionary if exists
            self.hp = hpstat(cynthia.get(mon)[2][0], self.level)   # effective hp stat
            self.atk = otherstat(cynthia.get(mon)[2][1], self.level)   # effective attack stat
            self.defs = otherstat(cynthia.get(mon)[2][2], self.level)   # effective defense stat
            self.spatk = otherstat(cynthia.get(mon)[2][3], self.level)   # effective special attack stat
            self.spdef = otherstat(cynthia.get(mon)[2][4], self.level)   # effective special defense stat
            self.spe = otherstat(cynthia.get(mon)[2][5], self.level)   # effective speed stat
            self.moves = [ cynthia.get(mon)[3][x] for x in [0, 1, 2, 3] ]  # list of moves
            self.status = []   # start with no status condition
            self.stats = [0, 0, 0, 0, 0]   # start with no stat modifiers - atk, def, spatk, spdef, spe


    # represents as a string (name)
    def __repr__(self):
        """indpoke objects are represented by their name as a string"""

        return self.name


# Main user menu
def mainmenu():
    """A function that simply prints the main menu"""
    print()
    print("(1) Battle!")   # battle cynthia
    print("(2) View your team")   # view your pre-set randomized team
    print("(3) Re-randomize your team")   # re-randomize your pre-set team
    print("(4) Build a team")   # build a team
    print("(5) Rules")   # see some basic not helpful rules
    print("(6) Quit")   # quit program

    print()


# Battle menu
def battlemenu(team):
    """the battle menu - fight, switch, bag, forfeit"""

    global player 

    while True:
        print()
        print("(1) Fight")   # choose a move
        print("(2) Pokemon")   # switch and view your team
        print("(3) Bag")   # view items (you do not have any)
        print("(4) Run")   # forfeit
        print()
        inpt = input("What will you do (#)? ")   # choose an option

        try:
            inpt = int(inpt)   # hopefully the input was an integer

            if int(inpt) not in range(1, 5):   # hopefully the input was a correct integer...
                print()
                print("That's not an option... Continuing...")
                print()
                continue
            else:
                pass

        except:
            print("I didn't understand your input! Continuing...")
            continue

        if inpt == 1:
            return True

        elif inpt == 2:
            while True:
                print()
                fteam = [ x for x in team if x != player and "fainted" not in x.status ]   # do not send out your current pokemon
                for i in range(1, len(fteam)+1):
                    if fteam[i-1].type2 == "None":
                        print("({})".format(i), fteam[i-1].name, '({})'.format(fteam[i-1].type1))   # display list of team (one type)
                    else:
                        print("({})".format(i), fteam[i-1].name, '({}, {})'.format(fteam[i-1].type1, fteam[i-1].type2))   # display list of team (two types)
                print()
                print("Press 0 to go back")
                choice = input("Who will you send out next (#)? ")
                    
                try:
                    if int(choice) in range(0, len(team)+1): 
                        if int(choice) == 0:   # go back
                            return "back"
                        else:
                            player = fteam[int(choice)-1]
                            print()
                            print("You sent out", player)   # you send out a new mon
                            return False

                except:
                    print()
                    print("Type a number corresponding to the pokemon you would like to send out: ") 
                    continue

        elif inpt == 3:
            print()
            print("The bag is EMPTY! Suffer!!!")
            continue

        elif inpt == 4:
            print()
            print("You forfeited and lost to Cynthia")
            return "forfeit"


# Fight menu
def movemenu(mon):
    """Accepts the string name of a pokemon and returns its move menu"""
    print()
    print("(1) {}".format(mon.moves[0]))   # move 1
    print("(2) {}".format(mon.moves[1]))   # move 2
    print("(3) {}".format(mon.moves[2]))   # move 3
    print("(4) {}".format(mon.moves[3]))   # move 4
    print()
    print("Press 0 to go back")

    while True:
        move = input("Which move will you use (#)? ")

        try:
            move = int(move)   # hopefully the input was an integer

            if int(move) not in range(5):   # hopefully the input was a correct integer...
                print()
                print("That's not an option... Continuing...")
                print()
                continue
            
            else:
                if int(move) == 0:
                    return False   # go back to battle menu
                else:
                    return int(move)   # returns move number

        except:
            print("I didn't understand your input! Continuing...")
            continue


# damage calculator
def damagecalc(player, opp, move):
    """calculates damage done by a move"""

    if moves.get(move)[1] == "atk":   # physical move
        A = player.atk
        D = opp.defs
    elif moves.get(move)[1] == "spatk":   # special move
        A = player.spatk
        D = opp.spdef

    L = player.level   # attacker's level
    P = moves.get(move)[2]    # move power
    MOD = damagemult(player, opp, move)   # damage multiplier - [total, crit]

    if acccheck(move) == True:
        if MOD[1] == 1:   
            damage = ((((2*L/5)+2)*P*(A/D)/50)+2)*MOD[0]   # no crit
            return [damage, False]
        elif MOD[1] == 2:
            damage = ((((2*L/5)+2)*P*(A/D)/50)+2)*MOD[0]   # yes crit
            return [damage, True]

    else:
        return [0, False]   # no damage and no crit because why not


# the turn function for player
def turn(player, opp, move):
    """A single turn for you.
    Returns True if target is still alive
    Returns False if you just won
    Returns new opponent if target faints"""
    
    while True:
        if statuseffect(player) == True:   # player can attack
            print()
            print(player, "used", move)
            D = damagecalc(player, opp, move)   # damage dealt - list (crit)
            if D[0] == 0:
                print(player, "missed!")   # unfortunate miss
                return True
            else:
                if D[1] == True:
                    print("A critical hit!")   # crit

                if typematch(move, opp.type1, opp.type2)  >=2:   # super effective move used
                    print("It's super effective!")
                    opp.hp = int(opp.hp - D[0])
                elif typematch(move, opp.type1, opp.type2) < 1:   # not very effective move used
                    opp.hp = int(opp.hp - D[0])
                    print("It's not very effective")
                else:
                    opp.hp = int(opp.hp - D[0])   # lose health anyway

            if opp.hp <= 0:
                print()
                print(opp, "fainted!")   # if opponent faints
                opp.status += ["fainted"]   # pokemon is fainted
                global cteam
                cteam = [ x for x in cteam if "fainted" not in x.status ]   # delete pokemon from team
                if cteam == []:
                    return False   # you just won bro
                newopp = random.choice(cteam)   # cynthia chooses a random new pokemon
                print("Cynthia sent out", newopp)   
                return newopp

            else:
                statmod(opp, move)   # lower stats?
                applystatus(opp, move)   # apply a status?
                print()
                if "BRN" in opp.status:
                    print(opp, "was hurt by burn")   # hurt by burn
                    opp.hp -= 8
                elif "NVBRN" in opp.status:
                    print(opp, "was hurt by burn")   # hurt by burn
                    opp.hp -= 8
                elif "PSN" in opp.status:
                    print(opp, "was hurt by poison")   # hurt by burn
                    opp.hp -= 16

                if opp.hp <= 0:
                    print()
                    print(opp, "fainted!")   # if opponent faints
                    opp.status += ["fainted"]   # pokemon is fainted
                    cteam = [ x for x in cteam if "fainted" not in x.status ]   # delete pokemon from team
                    if cteam == []:
                        return False   # you just won bro
                    newopp = random.choice(cteam)   # cynthia chooses a random new pokemon
                    print("Cynthia sent out", newopp)   
                    return newopp

                else:
                    print(opp, "has", opp.hp, "HP left")
                    return True

        elif turnorder(player, opp) == True:   # cannot attack
            print()
            statusmsg(player)
            return True


# a turn for cynthia
def cturn(player, opp):
    """A single turn for cynthia
    Return True if target is still alive
    Returns False if you just lost
    Returns new pokemon if yours faints"""

    while True:
        if statuseffect(opp) == True:   # cynthia can attack
            whichmove = []
            for x in opp.moves:
                D = damagecalc(opp, player, x)   # calculate damage for each possible move - [damage, T/F] for crit
                whichmove += [D]
            oppmovenum = whichmove.index(max(whichmove))   # strongest move index
            oppmove = opp.moves[oppmovenum]   # strongest move
            oppmoved = whichmove[oppmovenum][0]   # damage from strongest move
            print()
            print(opp, "used {}".format(oppmove))

            if whichmove[oppmovenum][1] == True:   # crit
                print("A critical hit!")
                    
            if typematch(oppmove, player.type1, player.type2)  >=2:   # super effective move used
                print("It's super effective!")
                player.hp = int(player.hp - oppmoved)
            elif typematch(oppmove, player.type1, player.type2) < 1:   # not very effective move used
                player.hp = int(player.hp - oppmoved)
                print("It's not very effective")
            else:
                player.hp = int(player.hp - oppmoved)   # always subtract health regardless

            if player.hp <= 0:
                print()
                print(player, "fainted!")   # if your pokemon faints
                print()
                player.status += ["fainted"]   # pokemon is fainted
                global team
                team = [ x for x in team if "fainted" not in x.status ]   # delete pokemon from team
                if team == []:
                    return False   # you just lost bro
                for i in range(1, len(team)+1):
                    if team[i-1].type2 == "None":
                        print("({})".format(i), team[i-1].name, '({})'.format(team[i-1].type1))   # display list of team (one type)
                    else:
                        print("({})".format(i), team[i-1].name, '({}, {})'.format(team[i-1].type1, team[i-1].type2))   # display list of team (two types)
                
                while True:
                    print()
                    choice = input("Who will you send out next (#)? ")
                    
                    try:
                        if int(choice) in range(1, len(team)+1): 
                            player = team[int(choice)-1]
                            print("You sent out", player)   # you send out a new mon
                            return player

                    except:
                        print()
                        print("Type a number corresponding to the pokemon you would like to send out: ") 
                        continue   

            else:
                statmod(player, oppmove)   # lower stats?
                applystatus(player, oppmove)   # apply a status?
                print()
                if "BRN" in player.status:
                    print(player, "was hurt by burn")   # hurt by burn
                    player.hp -= 8
                elif "NVBRN" in player.status:
                    print(player, "was hurt by burn")   # hurt by burn
                    player.hp -= 8
                if "PSN" in player.status:
                    print(player, "was hurt by poison")   # hurt by burn
                    player.hp -= 16

                if player.hp <= 0:
                    print()
                    print(player, "fainted!")   # if your pokemon faints
                    print()
                    player.status += ["fainted"]   # pokemon is fainted
                    team = [ x for x in team if "fainted" not in x.status ]   # delete pokemon from team
                    if team == []:
                        return False   # you just lost bro
                    
                    for i in range(1, len(team)+1):
                        if team[i-1].type2 == "None":
                            print("({})".format(i), team[i-1].name, '({})'.format(team[i-1].type1))   # display list of team (one type)
                        else:
                            print("({})".format(i), team[i-1].name, '({}, {})'.format(team[i-1].type1, team[i-1].type2))   # display list of team (two types)
                
                    while True:
                        print()
                        choice = input("Who will you send out next (#)? ")
                        
                        try:
                            if int(choice) in range(1, len(team)+1): 
                                player = team[int(choice)-1]
                                print("You sent out", player)   # you send out a new mon
                                return player

                        except:
                            print()
                            print("Type a number corresponding to the pokemon you would like to send out: ") 
                            continue   
                else:
                    print(player, "has", player.hp, "HP left")
                    return True
        
        elif statuseffect(opp) == False:
            print()
            statusmsg(opp)
            return True
            break


# All the menu selection stuff - ideally returns the move you choose...
def sturn(team, cteam):
    """selection time... returns your move choice if necessary"""

    global player 
    global opp 

    while True:
        x = battlemenu(team)

        if x == "forfeit":   # forfeit
            return "forfeit"

        elif x == "back":   # go back...
            continue
        
        elif x == False:   # if you switch, your turn is over
            return True

        elif x == True:   # no switch, go to move selection
            
            y = movemenu(player)   # hopefully y = the move index number

            if y == False:
                continue

            else:
                move = player.moves[y-1]
                return move   # return move name ideally


# THE FULL BATTLE
def battle(team, cteam):
    """The full battle function in all its glory"""

    global player
    player = team[0]
    global opp
    opp = cteam[0]

    while True:   # everyone has pokemon left

        player.status = [x for x in player.status if x != "flinch"]   # flinches only apply if you move second
        opp.status = [x for x in opp.status if x != "flinch"]   # therefore get rid of flinch status at start of turns

        a = sturn(team, cteam)   # ideally it's your choice of attack

        if a == "forfeit":   # you forfeit and the message was already displayed in battlemenu()
            return

        elif a == True:   # turn is over because you switched
            d = cturn(player, opp)   # cynthia attacks
            if d == True:   # you survive, turn ends
                continue
            elif d == False:   # you just lost bro
                return "lose"
            else:
                player = d   # you faint and your new pokemon is set
                continue

        else:   # you chose a move and we can finally fight
            b = turnorder(player, opp)   # True if you go first, False if you go second

            if b == True:   # you attack first
                
                c = turn(player, opp, a)   # returns True if cynthia's pokemon survives, otherwise returns new pokemon

                if c == True:   # you switched
                    d = cturn(player, opp)   # cynthia attacks
                    if d == True:   # you survive, turn ends
                        continue
                    elif d == False:   # you just lost bro
                        return "lose"
                    else:
                        player = d   # you faint and your new pokemon is set
                        continue
                
                elif c == False:   # you just won bro
                    return "win"
                
                else:
                    opp = c    # cynthia's pokemon fainted and now a new turn against the next pokemon
                    continue
    
            else:   # you attack second

                d = cturn(player, opp)   # cynthia attacks first

                if d == True:   # you survived
                    c = turn(player, opp, a)   # you attack
                    if c == True:
                        continue   # cynthia's pokemon survived and new turn
                    elif c == False:   # you just won bro
                        return "win"
                    else:
                        opp = c   # cynthia's pokemon fainted and now a new turn
                        continue
                
                elif d == False:   # you just lost bro
                    return "lose"
                
                else:
                    player = d   # your pokemon fainted and now a new turn
                    continue
    

# prints a message based on the outcome of the battle
def outcome(wl):
    """prints a statement depending on whether you won or lost"""

    W = ["That was excellent. Truly, an outstanding battle. You gave the support your Pokémon needed to maximize their power. And you guided them with certainty to secure victory. You have both passion and calculating coolness. Together, you and your Pokémon can overcome any challenge that may come your way. Those are the impressions I got from our battle. I'm glad I got to take part in the crowning of Sinnoh's new Champion! Come with me. We'll take the lift."]   # win messages
    L = ["Smell ya later!", "Better luck next time", "Keep training", "Time to soft-reset", "You whited out...", "Come back when you're stronger", "Do or do not...there is no try", "Looks like you're blasting off again"]   # lose messages

    if wl == "lose":
        print("You lost to Cynthia...")   # you run out of pokemon first - you lose in the tie
        print(random.choice(L))
        return

    elif wl == "win":
        print("You defeated Cynthia!")   # Cynthia runs out of pokemon first
        print(random.choice(W))
        return

        
# The main user interface loop
def main():
    """The main user-interaction loop"""

    monlist = list(yourpokemon.keys())   # list of pokemon from yourpokemon dictionary 
    teamlist = random.sample(monlist, 6)   # randomized team of 6 (list of strings)
    global team
    team = []
    for x in teamlist:
        newmon = indpoke(x)   # turns strings into class indpoke
        team += [newmon]   # adds string name to list

    global cteam
    cteam = []
    for x in list(cynthia.keys()):
        mon = indpoke(x)
        mon.level = 60
        cteam += [mon]

    while True:
        mainmenu()
        choice = input("Choose an option (#): ")

        try:
            choice = int(choice)   # hopefully the input was an integer

            if int(choice) not in range(1, 7):   # hopefully the input was a correct integer...
                print()
                print("That's not an option... Continuing...")
                print()
                continue
            else:
                pass

        except:
            print("I didn't understand your input! Continuing...")
            continue

        if choice == 1:   # battle time
            print()
            global opp
            opp = cteam[0]
            print("Cynthia sent out", opp)
            print()
            global player
            player = team[0]
            print("You sent out", player)
            bato = battle(team, cteam)   # battle function
            outcome(bato)   # print a message depending on outcome of battle
            print()
            return

        elif choice == 2:   # view team
            print()
            print("Here's your team...")
            print()
            for x in team:
                if x.type2 == "None":
                    print(x.name, '({})'.format(x.type1))   # display list of team (one type)
                else:
                    print(x.name, '({}, {})'.format(x.type1, x.type2))   # display list of team (two types)
            print()

        elif choice == 3:   # re-randomize team
            monlist = list(yourpokemon.keys())   # list of pokemon from yourpokemon dictionary 
            teamlist = random.sample(monlist, 6)   # randomized team of 6 (list of strings)
            team = []
            for x in teamlist:
                newmon = indpoke(x)   # turns strings into class indpoke
                team += [newmon]   # adds string name to list
            print()
            print("You have a new team!")
            print("Press 2 to view your team")
            print()

        elif choice == 4:   # customize team members
            monlist = list(yourpokemon.keys())   # list of pokemon from yourpokemon dictionary reset if necessary
            team = []
            print()
            print("Here's a list of pokemon you can use")
            print("The stats are randomized, but don't worry - they have good moves")
            print()
            while len(team) < 6:   # add 6 members
                print("[{0}]".format(', '.join(map(str, monlist))))   # idk how this works but it prints the list without the quotations
                print()
                print("Press 4 to quit")
                choice = input("Pick a pokemon to add to your team: ")   # pick a mon from the list

                try:
                    if int(choice) == 4:   # quit if they want
                        team = []   # reset team selections
                        for x in teamlist:   # make a random new team
                            newmon = indpoke(x)   # turns strings into class indpoke
                            team += [newmon]   # adds string name to list
                        break
                except:
                    pass   # otherwise check if they input a name

                choice = choice.lower()   # make everything lower case
                choice = chr(ord(choice[0]) - 32) + choice[1:]   # make the first letter uppercase

                try:
                    if choice not in monlist: 
                        print()
                        print("Oops! That's not in the list... Try again")
                        print()
                        continue
                    
                    else:
                        monlist.remove(choice)
                        team += [indpoke(choice)]
                        print()
                    
                except:
                    print("Hmm I don't understand")
                
            print()
            print("Your team is ready!")
            print("Press 2 to view your team")

        elif choice == 5:   # rules
            print()
            print("Welcome to the world of pokemon")
            print("You must become the champion of Sinnoh by defeating Cynthia in a slightly unfair battle")
            print("All pokemon will have randomized stats")
            print("The first trainer to run out of pokemon loses the battle")
            print("A world of dreams and adventures with Pokémon awaits!")
            continue

        elif choice == 6:   # quit
            break
