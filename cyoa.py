def start_adventure():
    print("Welcome to CYOA. Please make sure you follow instructions carefully. Entering words that are not listed as choices could result in a bad ending for you. Answers are CASE SENSETIVE!")
    print("You enter an abandoned building. To your left you see a door marked 'Administrative Wing' and to your right, a door marked 'Medical Wing'")
    door_picked = input("Do you pick the left door or right door? > ")

    if door_picked == "left":
      print("You picked the Administrative Wing")
      print("As soon as you enter the Administrative Wing, you're plunged into darkness, apart from one emergency light at the end of a long hallway. You hear a long, low moan coming from somewhere in the dark. ")
      adwing_choice = input("Do you continue here or return to the entrance? Type 'continue' or 'return to entrance'>")
      if adwing_choice == "continue":
        print("You chose to continue through the dark towards the flashing light. The moan seems to be coming from behind you now. You stumble upon something in the dark and pick it up. It's a gun.")
        gun_choice = input("As you continue on, you hear the moaning getting louder. Do you turn around and shoot or pick up the pace towards the light? Type 'shoot' or 'faster'>")
        if gun_choice == "shoot":
          print("You turn around and shoot. You hear the sound of a body slumping to the floor. The moaning stops. You reach the emergency light and find a hatch. You open the hatch and climb down a ladder. At the end of the ladder, you're in what appears to be a storage room. The hatch slams shut above you. There are doors on either side of the storage room. One is marked 'Medical Wing Basement'. The other is marked 'Maximum Security Wing Basement")
          storage_choice = input("Whice door do you go through? Type 'max' or 'med'>")
          if storage_choice == "max":
            print("You walk into the maximum security wing and see another hallway, this time lined with cells. There are noises coming from within the cells. You pass the cells and hands try to reach out and grab you. You make it to the end of the wing without being grabbed. but the last cell on the left is open. Now that you have reached the end, you hear a moaning similar to the one before. It's moving and getting closer to you")
            max_choice = input("Do you investigate the open cell or do you shoot at the moaning voice? Type 'investigate' or 'shoot'>")
            if max_choice == "investigate":
              print("You enter the cell and the door shuts behind you. The moaning sound gets closer. It's some sort of monster with the lower half of a human and the upper half of a hyena. There'es a bullet wound in it's chest from where you shot it before. The monster growls, before leaping at the bars, but it's unable to get through. You shoot at it again, but this time you aim for it's head. The monster slumps to the ground. You notice a key around it's neck. You can barely reach it and unlock the cell. You step over the body and run back down the hallway towards the storage room. You wnter the storage room and head into the medical wing basement.")
              print("You enter a room filled with rubble. It is dark, but you can see a rope in front of you. You climb the rope and end up in a hallway of windows, each one peering into a room. At one end of the hallway is a stairwell, and at the other is a room marked 'Operating Room")
              obroom3_choice = input("Do you go down the stairs or enter the Operating Room? Type 'stairs' or 'enter'>")
              if obroom3_choice == "stairs":
                print("You head down the stairs. At the end is a door. You open the door. You see a corridor full of open doors. An alarm is blaring from above, but it sounds like it is running out of power. The voice on the alarm says 'Warning. Power Failure. Patient Rooms may open. Use caution'. You also hear a noise that sounds like the shuffling of feet. You try to head back to the room with the stairs, but the door you came from is locked. At the end of the corridor, you can see a door marked 'to entrance'. You also hear what sounds like shuffling coming from somewhere in the corridor, but you're unsure where the noise is coming from.")
                medwing_choice3 = input("Do you enter one of the open rooms to hide or run to the door? Type 'enter room' or 'run'>")
                if medwing_choice3 == "run":
                  print("You chose to run to the entrance door and but it's locked as well. The shuffling gets louder and louder until you see some sort of monster with the lower half of a human and the upper half of a hyena. The monster growls before leaping to you in one large bound. It eats you. Sorry, you are dead.")
                elif medwing_choice3 == "enter room":
                  print("You enter one of the rooms, but all of the doors in the corridor shut as soon as you enter. You call for help but no one comes. Days, weeks pass. You starve to death.")
                else:
                  print("You decided that it was better to die than continue? You're a coward.")
              elif obroom3_choice == "enter":
                print("You enter the operating room and see the upper half of a body on an operating table, being consumed by some sort of monster with the lower half of a human and the upper half of a hyena. The monster turns around and growls, before leaping to you in one large bound. It eats you. Sorry, you are dead.")
              else:
                print("You decided that it was better to die than continue? You're a coward.")
            elif max_choice == "shoot":
              print("You shoot just like last time, but there's no thump this time. The moaning sound gets closer. It's some sort of monster with the lower half of a human and the upper half of a hyena. There'es a bullet wound in it's chest from where you shot it before, and now one in its head, but it seems unaffected. The monster growls, before leaping to you in one large bound. It eats you. Sorry, you are dead. ")
            else:
              print("You decided that it was better to die than continue? You're a coward.")
          elif storage_choice == "med":
            print("You enter a room filled with rubble. It is dark, but you can see a rope in front of you. You climb the rope and end up in a hallway of windows, each one peering into a room. At one end of the hallway is a stairwell, and at the other is a room marked 'Operating Room")
            obroom2_choice = input("Do you go down the stairs or enter the Operating Room? Type 'stairs' or 'enter'>")
            if obroom2_choice == "stairs":
              print("You head down the stairs. At the end is a door. You open the door. You see a corridor full of open doors. An alarm is blaring from above, but it sounds like it is running out of power. The voice on the alarm says 'Warning. Power Failure. Patient Rooms may open. Use caution'. You also hear a noise that sounds like the shuffling of feet. You try to head back to the room with the stairs, but the door you came from is locked. At the end of the corridor, you can see a door marked 'to entrance'. You also hear what sounds like shuffling coming from somewhere in the corridor, but you're unsure where the noise is coming from.")
              medwing_choice2 = input("Do you enter one of the open rooms to hide or run to the door? Type 'enter room' or 'run'>")
              if medwing_choice2 == "run":
                print("You chose to run to the entrance door and but it's locked as well. The shuffling gets louder and louder until you see some sort of monster with the lower half of a human and the upper half of a hyena. The monster growls before leaping to you in one large bound. It eats you. Sorry, you are dead.")
              elif medwing_choice2 == "enter room":
                print("You enter one of the rooms, but all of the doors in the corridor shut as soon as you enter. You call for help but no one comes. Days, weeks pass. You starve to death.")
              else:
                print("You decided that it was better to die than continue? You're a coward.")
            elif obroom2_choice == "enter":
              print("You enter the operating room and see the upper half of a body on an operating table, being consumed by some sort of monster with the lower half of a human and the upper half of a hyena. The monster turns around and growls, before leaping to you in one large bound. It eats you. Sorry, you are dead.")
            else:
              print("You decided that it was better to die than continue? You're a coward.")
          else:
            print("You decided that it was better to die than continue? You're a coward.") 

        elif gun_choice == "faster":
          print("You tried to run but the moaning caught up with you. You turn around and are greeted by the source of the moan, a man in a lab coat who looks like he was alive at some point, but is no longer. he proceeds to eat you. Sorry, you are dead.")
        else:
          print("You decided that it was better to die than continue? You're a coward.")        
      elif adwing_choice == "return to entrance":
        print("You turn around to leave, but are greeted by the source of the moan, a man in a lab coat who looks like he was alive at some point, but is no longer. he proceeds to eat you. Sorry, you are dead.")
      else:
        print("You decided that it was better to die than continue? You're a coward.")
    elif door_picked == "right":
      print("You picked the Medical Wing")
      print("As soon as you enter the Medical Wing, you see a coridor of open doors. An alarm is blaring from above, but it sounds like it is running out of power. The voice on the alarm says 'Warning. Power Failure. Patient Rooms may open. Use caution'. You also hear a noise that sounds like the shuffling of feet. You try to leave, but the door you came from is locked. At the end of the corridor, you can see a door marked 'observation rooms'.")
      medwing_choice = input("Do you enter one of the open rooms to hide or run to the observation room? Type 'enter room' or 'run'>")
      if medwing_choice == "run":
        print("You chose to run to the observation room door and make it through, just before all of the doors in the coridor shut. As the observation room door closes behind you, the shuffling grows louder and once the door is closed completely, you hear a lound banging on it.")
        print ("You see a stairwell leading up. You head up the stairs and see a long hallway, lined with windows. Each window has a view from the ceiling of each room from the corridor below. You walk along the hallway, and can see that all of the rooms are empty. One of the windows is broken, and you see that someone has tied a rope to descend into the room. The floor of the room has caved in, and you cannot see where the rope ends. As well, at the end of the hallway is a door marked 'Operating Room'.")
        obroom_choice = input("Do you climb down the rope or enter the Operating Room? Type 'climb' or 'enter'>")
        if obroom_choice == "climb":
          print("You start to climb down the rope. Above you, you hear the operating room door open. Something starts to come into view, it's a monster with the lower half of a human and the upper half of a hyena. It attempts to follow you down the rope but loses its grip and falls past you, eventually hitting the ground in the darkness below with a loud crunch. You reach the bottom of the rope and see a door marked 'Storage Room'. You enter the room and see another door marked 'Maximum Security Room'. There is also a ladder leading up.")
          storage_choice2 = input("Do you climb up the ladder or enter maxiumum security? Type 'climb' or 'max'>" )
          if storage_choice2 == "climb":
            print("You climb up the ladder and find a hatch at the top. You open the hatch, but you hear something coming up the ladder behind you. You go through the hatch and find a pitch dark hallway, except for an emergency light at the end over a door that reads 'To Entrance'. You make your way down the hallway but now you hear a low moaning behind you. In the darkness you trip over something. It's a gun. You pick it up.")
            gun_choice2 = input("Do you shoot behind you at the noise or pick up the pace towards the entrance? Type 'shoot' or 'run'>")
            if gun_choice2 == "shoot":
                print("You turn around and shoot. You hear the sound of a body slumping to the floor. The moaning stops. You reach the emergency lit door and try to exit, but it's locked. The moaning starts up again. You shoot just like last time, but there's no thump this time. The moaning sound gets closer. It's some sort of monster with the lower half of a human and the upper half of a hyena. There'es a bullet wound in it's chest from where you shot it before, and now one in its head, but it seems unaffected. The monster growls, before leaping to you in one large bound. It eats you. Sorry, you are dead. ")
            elif gun_choice2 == "run":
                print("You run as fast as you can to the light. You open the door and find yourself in the entranceway where you started. You run out of the building, vowing never to return.")
                print("CONGRATULATIONS! YOU ESCAPED THE BUILDING ALIVE.")
            else:
                print("You decided that it was better to die than continue? You're a coward.")
          elif storage_choice2 == "max":
            print("You walk into the maximum security wing and see another hallway, this time lined with cells. There are noises coming from within the cells. You pass the cells and hands try to reach out and grab you. You make it to the end of the wing without being grabbed. but the last cell on the left is open. Now that you have reached the end, you hear a moaning similar to the one before. It's moving and getting closer to you")
            max_choice2 = input("Do you investigate the open cell or do you shoot at the moaning voice? Type 'investigate' or 'shoot'>")
            if max_choice2 == "investigate":
              print("You enter the cell and the door shuts behind you. The moaning sound gets closer. It's some sort of monster with the lower half of a human and the upper half of a hyena. There'es a bullet wound in it's chest from where you shot it before. The monster growls, before leaping at the bars, but it's unable to get through. You shoot at it again, but this time you aim for it's head. The monster slumps to the ground. You notice a key around it's neck. You can barely reach it and unlock the cell. You step over the body but it grabs at your leg causing you to trip. It gets up again and rips you to shreds. Sorry, you are dead.")
            elif max_choice == "shoot":
              print("You shoot just like last time, but there's no thump this time. The moaning sound gets closer. It's some sort of monster with the lower half of a human and the upper half of a hyena. There'es a bullet wound in it's chest from where you shot it before, and now one in its head, but it seems unaffected. The monster growls, before leaping to you in one large bound. It eats you. Sorry, you are dead. ")
            else:
              print("You decided that it was better to die than continue? You're a coward.")
        elif obroom_choice == "enter":
          print("You enter the operating room and see the upper half of a body on an operating table, being consumed by some sort of monster with the lower half of a human and the upper half of a hyena. The monster turns around and growls, before leaping to you in one large bound. It eats you. Sorry, you are dead.")
        else:
          print("You decided that it was better to die than continue? You're a coward.")
        
      elif medwing_choice == "enter room":
        print("You enter one of the rooms, but all of the doors in the corridor shut as soon as you enter. You call for help but no one comes. Days, weeks pass. You starve to death.")
      else:
        print("You decided that it was better to die than continue? You're a coward.")
    else:
        print("Sorry, it's either 'left' or 'right' as the answer. You're the weakest link, goodbye!")


def main():
   
    player_name =  input("What's your name? >")
    print(f"Your name is {player_name}")

    start_adventure()

if __name__ == '__main__':
    main()
