import json
with open ("game_data.json","r")as file:
    game_data = json.load(file)


inventory = []


rooms = game_data["rooms"]
intro = game_data["intro"]
current_room = game_data["start"]

home = current_room

while True:
    print(f"You appear to be in the {current_room}")
   
    if "Item" in rooms [current_room].keys():
        print (f"There is a {rooms[current_room]['Item']} in the room")
    else:
        print("The room is empty")
        
    if len(inventory)> 0:
        print (f"You have {len(inventory)} items")
        print (inventory)
    else:   
        print("You have no items!")
           
    user_input = input("Enter command\n")
    commands = user_input.split(" ")
    

    action = commands[0].title()
    #item = commands[1].title()
    item = " ".join(commands[1:]).title() if len(commands) > 1 else ""

    
    #print (action)
    direction = ""
    msg=""
    
    if len(commands) >1:
        direction= commands[1:]
        direction= " ".join(direction).title()
        
        #print (direction)
        
        if action =="Exit":
            break
        
        
        elif action == "Go" and direction in ["North","South","East","West","Up","Down","Out","In"]:
            try:
                current_room = rooms[current_room][direction]
                msg=f"You moved {direction}"
                print (rooms[current_room]["Desc"])
                
            except:
                msg= "You cant go that way."
                
        elif action == "Give":
            print (rooms[current_room]["Desc"])
        
        elif action == "Passcode 8915" and current_room == "Library":
            print("Lock unlocked!")
                
        elif action == "Get":
            print("Getting from Room: ",rooms[current_room])
            
                   
            try:
                if item == rooms[current_room]["Item"]:
                    print(rooms[current_room]["Item"])
                    if item not in inventory:
                        inventory.append(rooms[current_room]["Item"])
                        
                        rooms[current_room].pop("Item")
                        msg = f"{item} retrieved!"
                        
                    else:
                        msg = f"You already have the {item}"
                        
                else:
                    msg = f"Can't find {item}"
                    
            except:
               msg = f"Can't find {item}"


    print(msg)         
            
    







