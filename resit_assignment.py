import sys


def createCommandsList(commandsTXT):
    # Create command list by clearing "\n"
    list_commands = []
    with open(commandsTXT, "r") as commands:
        for line in commands:
            splitted = line.split(" ")
            splitted[-1] = splitted[-1].rstrip("\n")
            list_commands.append(splitted)

    return list_commands


def createFriendships(smnTXT):
    data_dict = {}
    # Create friendship relations by clearing "\n"
    with open(smnTXT, "r") as data:
        for line in data:
            person, friends = line.split(":")
            friend_list = friends.split(" ")
            friend_list[-1] = friend_list[-1].rstrip("\n")
            data_dict[person] = friend_list

    return data_dict


def suggestFriend(sf_dict, name, no, out):
    suggested_two = []
    suggested_three = []
    list_two = []
    list_three = []
    conclusion = "Suggestion List for '{}' (when MD is {}):\n".format(name, no)
    str_two = "'{}' has 2 mutual friends with ".format(name)
    str_three = "'{}' has 3 mutual friends with ".format(name)

    for key, value in sf_dict.items():
        if value == 2:
            list_two.append(key)
            suggested_two.append(key)
        if value == 3:
            list_three.append(key)
            suggested_two.append(key)
            suggested_three.append(key)


    people_two = ",".join(list_two)
    people_three = ",".join(list_three)
    str_two = str_two + people_two + "\n"
    str_three = str_three + people_three + "\n"

    str_suggested_two = ",".join(suggested_two)
    str_suggested_three = ",".join(suggested_three)
    str_suggest = "The suggested friends for '{}':".format(name)

    finalSuggestTwo = str_suggest + str_suggested_two + "\n"
    finalSuggestThree = str_suggest + str_suggested_three + "\n"

    out.write(conclusion)

    if int(no) == 2:
        out.write(str_two)
        out.write(str_three)
        out.write(finalSuggestTwo)
    if int(no) == 3:
        out.write(str_three)
        out.write(finalSuggestThree)


def play(outputTXT, data_dict, list_commands ):
    with open(outputTXT, "w") as out:
        out.write("Welcome to Assignment 3\n")
        out.write("-------------------------------\n")

        for command in list_commands:
            if command[0] == "ANU":
                person = command[1]
                if person in data_dict:
                    out.write("ERROR: Wrong input type! for 'ANU' -- This user already exists!!\n")
                else:
                    data_dict[person] = []
                    out.write(f"User '{person}' has been added to the social network successfully\n")

            elif command[0] == "DEU" or command[0] == "REU":
                person = command[1]
                if person in data_dict:
                    del data_dict[person]

                    for tempPerson in data_dict:
                        if person in data_dict[tempPerson]:
                            data_dict[tempPerson].remove(person)

                    out.write(
                        f"User '{person}' and his/her all relations has been deleted to the social network successfully\n")
                else:
                    out.write(f"ERROR: Wrong input type! for 'DEU' -- There is no named '{person}'!!\n")

            elif command[0] == "ANF":
                source = command[1]
                target = command[2]

                if (source in data_dict) and (target in data_dict):
                    if (source in data_dict[target]) and (target in data_dict[source]):
                        out.write(f"ERROR: A relation between '{source}' and '{target}' already exists!!\n")
                    else:
                        data_dict[target].append(source)
                        data_dict[source].append(target)
                        out.write(f"Relation between '{source}' and '{target}' has been added successfully\n")

                elif (source not in data_dict) and (target in data_dict):
                    out.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{source}' found!!\n")
                elif (source in data_dict) and (target not in data_dict):
                    out.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named '{target}' found!!\n")
                else:
                    out.write(
                        f"ERROR: Wrong input type! for 'ANF'! -- No user named '{source}' and '{target}' found!\n")

            elif command[0] == "DEF":
                source = command[1]
                target = command[2]
                if (source in data_dict) and (target in data_dict):
                    if (source in data_dict[target]) and (target in data_dict[source]):
                        data_dict[source].remove(target)
                        data_dict[target].remove(source)
                        out.write(f"Relation between '{source}' and '{target}' has been deleted succesfully.\n")
                    else:
                        out.write(f"ERROR: No relation between '{source}' and '{target}' found!!\n")
                elif (source not in data_dict) and (target in data_dict):
                    out.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{source}' found!!\n")
                elif (source in data_dict) and (target not in data_dict):
                    out.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{target}' found!!\n")
                else:
                    out.write(
                        f"ERROR: Wrong input type! for 'DEF'! -- No user named '{source}' and '{target}' found!\n")

            elif command[0] == "CF":
                person = command[1]
                if person in data_dict:
                    number = len(data_dict[person])
                    out.write(f"User '{person}' has '{number}' friends.\n")
                else:
                    out.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{person}' found!\n")

            elif command[0] == "FPF":
                person = command[1]
                if person in data_dict:
                    number = int(command[2])
                    if number == 1 or number == 2 or number == 3:
                        listFPF = []

                        for p1 in data_dict[person]:
                            if (p1 == person) or (p1 in listFPF):
                                pass
                            else:
                                listFPF.append(p1)

                            if number == 2:
                                for p2 in data_dict[p1]:
                                    if (p2 == person) or (p2 in listFPF):
                                        pass
                                    else:
                                        listFPF.append(p2)

                                    if number == 3:
                                        for p3 in data_dict[p3]:
                                            if (p3 == person) or (p3 in listFPF):
                                                pass
                                            else:
                                                listFPF.append(p3)
                        listFPF.sort()

                        first_sent = "These possible friends:"
                        sec_sent = ", ".join(str(i) for i in listFPF)

                        out.write(
                            f"User '{person}' has {len(listFPF)} possible friends when maximum distance is {number}\n")
                        out.write(first_sent + "{" + sec_sent + "}\n")
                    else:
                        pass
                else:
                    out.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named '{person}' found!\n")

            else:  # command[0] == "SF"
                person = command[1]
                if person in data_dict:
                    number = int(command[2])
                    if (number == 2) or (number == 3):
                        sf_dict = {}
                        for p1 in data_dict[person]:
                            for p2 in data_dict[p1]:
                                if p2 == person:
                                    pass
                                else:
                                    if p2 in sf_dict:
                                        sf_dict[p2] += 1
                                    else:
                                        sf_dict[p2] = 1

                        suggestFriend(sf_dict, person, number, out)
                    else:
                        out.write("Error: Mutually Degree cannot be less than 1 or greater than 4.\n")
                else:
                    out.write(f"Error: Wrong input type! for 'SF'! -- No user named '{person}' found!!\n")


try:
    smnTXT = sys.argv[1] #"smn.txt"
    commandsTXT = sys.argv[2] #"commands.txt"
    outputTXT = "output.txt"

    if len(sys.argv) != 3:
        raise IndexError

    temp = open(outputTXT, "w")
    temp.close()

    list_commands = createCommandsList(commandsTXT)
    data_dict = createFriendships(smnTXT)
    play(outputTXT, data_dict, list_commands)

    for i in data_dict:
        print(i , " : ", data_dict[i])

except IndexError:
    print("IndexError: number of input files less than expected.")
except IOError as ioe:
    print(f"IOError: cannot open {ioe.filename}")
except Exception:
    print("There is a problem. Program cannot be executed")
