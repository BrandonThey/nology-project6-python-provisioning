from csv import writer
class Game:
    def __init__(self, marine_count):
        self._marine_count = marine_count
    
    @property
    def marine_count(self):
        return self._marine_count

    @marine_count.setter
    def marine_count(self, new_count):
        self._marine_count = new_count

#so far worst path you lose 23 marines
#best path you lose 9 marines
def difficulty_select(log_file_name,user_choice=""):
    print()
    print("                                                      Welcome to this Warhammer 40k text adventure!"                                                          )
    print("                         Please choose a difficulty to play! Your choice will determine how many marines('lives') you have during the game"                   )
    print("                                             Initiate:25 Marines      Astartes:20 Marines     Custodes: 15 Marines"                                           )
    print()
    while(True):
        if(not user_choice):
            user_choice = input("Initiate, Astartes, Custodes: ")
        if(user_choice.lower() == "initiate"):
            game_instance = Game(25)
            log_message(log_file_name, game_instance, "New Game Started, none")
            log_message(log_file_name,game_instance, "Difficulty Chosen, Initiate")
            break
        elif(user_choice.lower() == "astartes"):
            game_instance = Game(20)
            log_message(log_file_name, game_instance, "New Game Started, none")
            log_message(log_file_name,game_instance, "Difficulty Chosen, Astartes")
            break
        elif(user_choice.lower() == "custodes"):
            game_instance = Game(15)
            log_message(log_file_name, game_instance, "New Game Started, none")
            log_message(log_file_name,game_instance, "Difficulty Chosen, Custodes")
            break
    
    return game_instance

#each segment of the story should be it's own functions, maybe set up a counter to count the number of squad members are left and if reaches 0 you lose
def intro(game_instance,log_file_name,user_choice=""):
    print()
    print("                             You play as Gabriel Angelos, captain of an elite group of infantry known as the Space Marines"                                   )
    print(f"                       Your goal as their captain is to get as many of your {game_instance.marine_count} men out alive as possible"                          )
    print("                          Your Chapter, The Blood Ravens, are in deep combat with the forces of evil on the recruiting world of Aurelia"                      )
    print("                      Here we see Gabriel Angelos, his squad, and their base besieged by waves and waves of Tyranids, hideous insectoid aliens"               )
    print("                                                     And here you are met with your first decision..."                                                        )
    print(" As the captain will you order your men to lob grenades at the aliens in hopes to stem their assault or will you risk a danger close airstrike on the aliens?")
    print()

    while(True):
        if(not user_choice):
            user_choice = input("Grenades or airstrike? ")
        if(user_choice.lower() == "grenades"):
            log_message(log_file_name,game_instance, "Decision Made, Lob Grenades")
            lob_grenades(game_instance,log_file_name)
            break
        elif(user_choice.lower() == "airstrike"):
            log_message(log_file_name,game_instance, "Decision Made, Call Airstrike")
            call_airstrike(game_instance,log_file_name)
            break

    return

def lob_grenades(game_instance,log_file_name, user_choice=""):
    print()
    print("                 Not wanting to risk the chance of friendly fire from a airstrike, you instead order your marines to lob grenades at the Tyranids"            )
    print("                 Your marines lob their grenades and after a few seconds you hear their explosions followed by the screams of pain of the aliens"             )
    print("                             However the aliens don't relent and continue to attack your squad and rip into your men"                                         )
    print("                     Their assualt was only broken with a second barrage of grenades, after which the aliens start retreating"                                )
    print("                 After the battle you take a tally of your men and realize that half of your men were killed by the ferocity of the Tyranids"                 )
    print("                       But now is not the time to grieve your lost brethren, as the aliens scurry away you must make a new decision"                          )
    print("      Will you order your men to set up more defense in anticipation of the next wave or will you push forward and press your attack on the tyranids?"        )
    game_instance.marine_count -= 10
    print(f"                                                         You have {game_instance.marine_count} space marines remaining"                                      )
    print()
    while(True):
        if(not user_choice):
            user_choice = input("Defend or attack? ")
        if(user_choice.lower() == "defend"):
            log_message(log_file_name,game_instance, "Decision Made, Defend Base")
            defend(game_instance,log_file_name)
            break
        elif(user_choice.lower() == "attack"):
            log_message(log_file_name,game_instance, "Decision Made, Push Forward")
            push_forward(game_instance,log_file_name)
            break
    return

def call_airstrike(game_instance,log_file_name, user_choice=""):
    print()
    print("               Thinking that grenades won't quell the Tyranids' thirst, you decide to call in an airstrike to wipe all the aliens out"                        )
    print("                            You can hear the roar of the mighty Thunderhawk strike crafts as they start their bombing run"                                    )
    print("        As their bombs land you see the Tyranid forces getting wiped out and they start retreating, and the stench of their blood lingers in the air"         )
    print("            However in the chaos of battle, 3 of your men were caught in the bombing run, they die honorable deaths in the name of the Emperor"               )
    print("                       But now is not the time to grieve your lost brethren, as the aliens scurry away you must make a new decision"                          )
    print("      Will you order your men to set up more defense in anticipation of the next wave or will you push forward and press your attack on the tyranids?"        )
    game_instance.marine_count -= 3
    print(f"                                                         You have {game_instance.marine_count} space marines remaining"                                                    )
    print()
    while(True):
        if(not user_choice):
            user_choice = input("Defend or attack? ")
        if(user_choice.lower() == "defend"):
            log_message(log_file_name,game_instance, "Decision Made, Defend Base")
            defend(game_instance,log_file_name)
            break
        elif(user_choice.lower() == "attack"):
            log_message(log_file_name,game_instance, "Decision Made, Push Forward")
            push_forward(game_instance,log_file_name)
            break
    return

def defend(game_instance,log_file_name):
    print()
    print("                              You decide that an offensive would be unwise and order your men to set reinforce the defenses around the base"                                )
    print("                             The marines set up heavy boltor machine guns around the base and plant cluster mines around the base's perimeter"                              )
    print("                                                 Come night time, the alarm sounds indicating that there is an attack imminent"                                             )
    print("                     The Tyranids return and do so in greater force. Your scouts estimate that the renewed alien force may be twice or even three times as large"           )
    print("                             As the Tyranids charge your base, you can hear the explosions of your mines and you can smell the gunpowder in the air"                        )
    print(" Your base defensive cuts down the aliens in droves and yet they continue to press onwards, eventually your landmines all but exhuasted and your machine guns overwhelmed"  )
    print("                 By the time the battle finishes your men are exhausted, beaten down, and bloody. The base holds but not without the sacrifice of 7 of your brothers"       )
    game_instance.marine_count -= 7
    if(game_instance.marine_count <= 0):
        log_message(log_file_name,game_instance, "Ending Decided, Bad Ending")
        bad_ending()
    else:
        print()
        print("                               Seeing the suffered losses thus far your marines become frustrated with the lack of action against the aliens"                               )
        print("                                             They decide to push the fight to the aliens rather than weathering the constant assualts."                                     )
        print("                                            The marines move out to find and attack the alien base and you have no choice but to follow"                                    )
        print(f"                                                            You have {game_instance.marine_count} space marines remaining"                                                 )
        print()

        log_message(log_file_name,game_instance, "Game Event, Counter Attack")
        counter_attack(game_instance,log_file_name)
    return

def push_forward(game_instance,log_file_name):
    print()
    print("                                         You decide that the best defense is a strong offense and order your men to persue the aliens"                                      )
    print("                                  You and your men follow the aliens in a proper formation slowly eliminating the stragglers as you move forward"                           )
    print("         At one point in the persuit a organized group of grunt and ranged aliens managed to catch your squad off guard and manage to claim the lives of 3 of your men"     )
    game_instance.marine_count -= 3
    print(f"                                                         You have {game_instance.marine_count} space marines remaining"                                                    )
    print()

    log_message(log_file_name,game_instance, "Game Event, Counter Attack")
    counter_attack(game_instance,log_file_name)
    return

def counter_attack(game_instance,log_file_name, user_choice=""):
    print()
    print("                  Eventually your marines manage to find the Tyranid's hive base. You send your scouts to recon the base and determine the strength of the hive"            )
    print("                     They return with the report. The hive has been severly weakened from the losses they incurred during their battles with the Blood Ravens"              )
    print("                    However they still field some heavy units, specifically a couple of Carnifex, massive creatures that acts as the Tyranid's battle tank"                )
    print("             Your scouts also report the presence of a Hive Tyrant, a large flying beast that serves as the Tyranid's commander, issuing commands via psychic waves"        )
    print("                     The formation of a kill squad of your most elite marines was unanimously agreed upon, but the target of the kill squad was hotly debated"              )
    print("                           Some of your marines argue that the Carnifex's ability to absorb massive amounts of damage and deal it back was a higher priority"               )
    print("                              Your other marines argue that the Hive Tyrant was a bigger priority as it is able to organize and control the whole hive"                     )
    print("                                                                In the end it all boils down to your decision"                                                              )
    print()

    while(True):
        if(not user_choice):
            user_choice = input("Tyrant or Carnifex? ")
        if(user_choice.lower() == "tyrant"):
            log_message(log_file_name,game_instance, "Decision Made, Eliminate Carnifex")
            eliminate_tyrant(game_instance,log_file_name)
            break
        elif(user_choice.lower() == "carnifex"):
            log_message(log_file_name,game_instance, "Decision Made, Eliminate Carnifex")
            eliminate_carnifex(game_instance,log_file_name)
            break
    return

def eliminate_tyrant(game_instance,log_file_name):
    print()
    print("      You decide that the Tyrant commander is a much larger priority. Your thinking being that without the commander the Tyrannid hordes will be uncoordinated and weakened")
    print("                             Your thinking was correct. After your kill squad eliminated the Tyrant there is a noticeable breakdown in the hive."                           )
    print("              Minor annoyances between the creatures lead to full out in-fighting. The smaller hormogaunts start attacking each other and even attacking the Carnifex"      )
    print("                                 After all is said and done the hive cluster just about halved in size from their already weakened state"                                   )
    print("                                             You then order your squads to move in and clean up the surviving aliens"                                                       )
    print("               While the rest of the squad cleans up the rest of the aliens, you and a few of your elite marines face off against the remaining weakened Carnifex"          )
    print("             You manage to get some good hits in with your chainsword but the Carnifex will not concede easily, it attacks back slicing two of your marines in half"        )
    print("                                  You then use your jetpack to launch yourself onto the back of the monster to slice it up some more."                                      )
    print("                                         In an angry rage it fires off its bio-plasma guns melting down another marine"                                                     )
    print("                          After a few more swings of your chainsword the beast finally falls and the rest of hive has been eliminated"                                      )
    print()
    game_instance.marine_count -=3
    if(game_instance.marine_count <= 0):
        print("                           You have defeated the hive... but have taken damage yourself and the rest of your squad is in critical condition"                                )
        log_message(log_file_name,game_instance, "Ending Achieved, Bad Ending")
        bad_ending()
    elif(game_instance.marine_count < 6):
        log_message(log_file_name,game_instance, "Ending Achieved, Standard Ending")
        standard_ending()
    else:
        log_message(log_file_name,game_instance, "Ending Achieved, Good Ending")
        good_ending()
    return

def eliminate_carnifex(game_instance, log_file_name):
    print()
    print("                   You decide that the firepower and strength of the two Carnifex must be eliminated in order to stand a chance against the hive cluster"                   )
    print("              You send the kill squad off to kill off the Carnifex and they set off later in the night, thinking that these beasts must sleep at some point"                )
    print("                        Your squad slowly approach the Carnifex as they're sleeping, and start laying down packed explosives to ensure their deaths"                        )
    print("       But during their mission, the men notice the beasts starting to wake, at this rate the whole squad will be killed by the time they're done planting explosives"      )
    print("                     Two men of the squad decide to take the sacrifice and stay behind to finish planting explosives while the rest leaves before things get bad"           )
    print("                         As the rest of the squad runs away from the situation they can hear the screams of their brothers and a loud explosion afterwards"                 )
    print("                    The kill squad has succeeded in blowing up the two Carnifex at the lost of a couple men, but there still remains the Hive Tyrant commander."            )
    print("                                 In the morning after, you and the men have formed a plan to overtake the hive base and destroy any last alien"                             )
    print("                        As the battle begins you can tell that the dead Carnifex is a definite help as your men slowly but surely cleans out the hive"                      )
    print("                         However as the aliens start to crumble underneath you, the Tyrant starts to rally the aliens to form new coordinated attacks"                      )
    print("                             These coordinated attacks managed to catch some of your men off guard, killing four men in total throughout the attacks"                       )
    print("                                                 You realize that in order to succeed in your mission you must kill off the Tyrant"                                         )
    print("          You order your men to focus their fire at the Tyrant flying overhead the battlefield. As it is weakly armored, it falls dead quickly after the barrage of bullets")
    print("                            With the Hive Tyrant dead and the alien heavy units gone, your men sweep up the rest of the base, and the hive has now been eliminated"         )
    print()
    game_instance.marine_count -=6

    if(game_instance.marine_count <= 0):
        print("                           You have defeated the hive... but have taken heavy damage yourself and the rest of your squad is in critical condition"                                )
        log_message(log_file_name,game_instance, "Ending Achieved, Bad Ending")
        bad_ending()
    elif(game_instance.marine_count < 6):
        log_message(log_file_name,game_instance, "Ending Achieved, Standard Ending")
        standard_ending()
    else:
        log_message(log_file_name,game_instance, "Ending Achieved, Good Ending")
        good_ending()
    return

def bad_ending():
    print()
    print("                              As you lay dying, you look around you and see the corpses of all your brothers and think to yourself what could you have done better?"        )
    print("                                  You have regrets with your dying breath, regrets from failing your brothers, failing your Empire, and failing your Emperor"               )
    print("                            There is no room for regrets now Captain, your death will hopefully inspire the future chapters, but for now take some much needed rest"        )
    print("                                                                   End of Story, you have achieved the Bad Ending"                                                          )
    print()
    return

def standard_ending():
    print("      After the battles you and your brothers have acheived victory over the Tyranid scum. You have crushed the hive base and its inhabitants and survived another day"     )
    print("                                    But as you bask in the blood of your enemies, you realize that the blood of your brothers is also on your hands."                       )
    print("                                             You have prevented the Tyrannids from infesting the world today, but at what cost?"                                            )
    print("                                 And yet the forces of evil still lurk among the cities and ruins of Aurelia, and the space marines never rest"                             )
    print("                                                             End of Story, you have achieved the Standard Ending"                                                           )
    print()
    return

def good_ending():
    print("      After the battles you and your brothers have acheived victory over the Tyranid scum. You have crushed the hive base and its inhabitants and survived another day"     )
    print("        You have lost respected brothers along the way, but this is war and casualties are a given. At least you've done as much as you can to keep your Chapter alive"     )
    print("             However there is no time to celebrate Captain, the forces of evil still lurk among the cities and ruins of Aurelia, and the space marines never rest"          )
    print("                                                                 End of Story, you have achieved the Good Ending"                                                           )
    print()
    return

def log_message(log_file_name,game_instance, message):
    with open(log_file_name, "a", newline="") as log_file:
        log_file.writelines(f"{message}, {game_instance.marine_count} \n")
    log_file.close()

# log_message(log_file_name,game_instance, "Ending Achieved, Good Ending")
def main():
    log_file_name = "game-decisions.txt"
    game_instance = difficulty_select(log_file_name)
    intro(game_instance,log_file_name)
    return 0

# main()