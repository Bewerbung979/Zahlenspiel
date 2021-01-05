import random 

versuch = "" #Zahl die vom Spieler geraten wird
versuch_anzahl = 0 #Anzahl der Versuche
gesuchte_zahl = random.randint(0, 100) #Zufallszahl die erraten werden soll
erraten = False #Zustand ob die Zahl erraten wurde


print("Bitte raten sie eine Zahl von 0 bis 100: ")
while erraten == False:
    versuch_anzahl += 1 
    versuch = int (input("Versuch: ")) #Benutzereingabe
    
    if versuch == gesuchte_zahl: #Zahl entspricht der gesuchten Zahl
        print("Glückwunsch, du hast die Zahl in {} Versuchen erraten!".format(versuch_anzahl))
        erraten = True #Schleife wird beendet
        break

    elif versuch > gesuchte_zahl:
        print("Versuche es erneut. (Die gesuchte Zahl ist kleiner)")

    else:
        print("Versuche es erneut. (Die gesuchte Zahl ist größer)")
