wedSeats = 30  # Some hardcode
satSeats = 30
noAdult = 0
noChild = 0
noSenior = 0
date = ""
while True:
    try:
        print("Ticket system")  # print all the ticket info here
        command = input("Please select system operations\n(n: new transaction, e: edit info, f: finish transaction, p: print vacancy, q: quit): ")
        if command.lower() == "n":
            while True:
                try:
                    while True:
                        noAdult = int(input("No. of adult: "))
                        if noAdult >= 0:
                            break
                        else:
                            print("Please enter 0 or positive integer")
                    while True:
                        noChild = int(input("No. of child: "))
                        if noChild >= 0:
                            break
                        else:
                            print("Please enter 0 or positive integer")
                    while True:
                        noSenior = int(input("No. of senior: "))
                        if noSenior >= 0:
                            break
                        else:
                            print("Please enter 0 or positive integer")
                    while True:
                        date = int(input("Date of the show (0: Sat, 1: Wed): "))
                        if date == 0 or date == 1:
                            break
                        else:
                            print("Please enter 0 or 1")
                    totalNo = noAdult + noChild + noSenior
                    if totalNo <= wedSeats or totalNo <= satSeats:
                        break
                    else:
                        print("No. of tickets exceed current available tickets, please enter again.")
                except ValueError:
                    print("Please enter a valid number")
        elif command.lower() == "e":
            print(
                "Current number is shown in the (). Key in the new value to edit it or just press Enter to ignore editing it.")
            while noAdult != "" or noChild != "" or noSenior != "" or date != "":
                while True:
                    noAdult = int(input("No. of adult (" + str(noAdult) + "): "))
                    if noAdult >= 0:
                        break
                    else:
                        print("Please enter 0 or positive integer")
                while True:
                    noChild = int(input("No. of child (" + str(noChild) + "): "))
                    if noChild >= 0:
                        break
                    else:
                        print("Please enter 0 or positive integer")
                while True:
                    noSenior = int(input("No. of senior (" + str(noSenior) + "): "))
                    if noSenior >= 0:
                        break
                    else:
                        print("Please enter 0 or positive integer")
                while True:
                    date = int(input("Date of the show (0: Sat, 1: Wed): "))
                    if date == 0 or date == 1:
                        break
                    else:
                        print("Please enter 0 or 1")
                totalNo = noAdult + noChild + noSenior
                if totalNo <= wedSeats or totalNo <= satSeats:
                    break
                else:
                    print("No. of tickets exceed current available tickets, please enter again.")
        elif command.lower() == "f":
            while satSeats>0 or wedSeats>0:
                combo = 0
                adultTicket = 0
                seniorTicket = 0
                childTicket = 0
                discount = 0
                totalTicket = 0
                gst = 0
                totalNo = noAdult + noChild + noSenior
                if date == 1:
                    while noAdult >= 2 and noChild >= 2:  # wile loops number of child and adult adding to combo for every 2 and subtracting 2
                        noAdult -= 2
                        noChild -= 2
                        combo += 192
                    adultTicket = noAdult * 50
                    childTicket = noChild * 70
                    seniorTicket = noSenior * 30
                    totalTicket = combo + adultTicket + childTicket + seniorTicket  # total cost excluding gst
                    discount = round(totalTicket * 0.1, 2)
                    totalTicket -= discount
                    gst = round(totalTicket * 0.07, 2)
                else:
                    while noAdult > 2 and noChild > 2:
                        noAdult -= 2
                        noChild -= 2
                        combo += 192
                    adultTicket = noAdult * 50
                    childTicket = noChild * 70
                    seniorTicket = noSenior * 30
                    totalTicket = combo + adultTicket + childTicket + seniorTicket
                    gst = round(totalTicket * 0.07, 2)
                print("Receipt")
                print("combo: " + str(combo))
                print("adult: " + str(adultTicket))
                print("senior: " + str(seniorTicket))
                print("child: " + str(childTicket))
                print("discount: -" + str(discount))
                print("total: " + str(totalTicket))
                print("gst incl: " + str(gst))
                print("no. tickets: " + str(totalNo))
                if date == 0 and totalNo<=satSeats:
                    satSeats -= totalNo  # subtract no. of tickets bought and updates var satSeats
                    break  # Break ensures while loop breaks instead of infinite loop
                elif date == 1 and totalNo<=wedSeats:
                    wedSeats -= totalNo
                    break
                else:
                    print("You tried finishing transaction without ordering tickets")
                    break
            else:
                print("No tickets ordered")
        elif command.lower() == "p":
            print("wednesday:"+str(wedSeats))
            print("saturday:" + str(satSeats))
        elif command.lower() == "q":
            print("Exited with q")
            break
        else:
            print("Please enter valid input")
    except ValueError:
        if noAdult == "" or noChild == "" or noSenior == "" or date == "":
            print("Skipped with enter")
        else:
            print("Please enter valid input")
