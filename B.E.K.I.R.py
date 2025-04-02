import time
import wetter_api
import zeit

cmd = {"Wetter": "12°",
       "motiviere mich": "Ich Handle, Ich denke nicht - ICH HANDLE"}

print("""Hallo ich bin B.E.K.I.R. (Built Efficiently for Knowledge, Intelligence & Resilience)
Ich helfe dir bei deinen alltäglichen aufgaben. Du kannst mit befehlen wie Wetter, Zeit, motiviere mich
diese dinge bei mir erfragen und ich werde dir eine dementsprechende antwort geben. gib dein ersten befehl ein. """)

while True:
    befehl = input().lower()
    if befehl == "wetter":
        print(wetter_api.wetter())
        continue
    elif befehl == "zeit":
        zeit.now()
        continue
    elif befehl == "motiviere mich":
        print(cmd["motiviere mich"])
        continue
    elif befehl == "beenden":
        print(f"Hat mich gefreut! Ich Explodiere jetzt in T-5")
        for i in range(5, 0, -1):
            time.sleep(1)
            print(i)
        print("BOOOOOMM!!")
        break
    else:
        print(f"""Diesen Befehl kenne ich nicht! Hilf mir mal auf die Sprünge :-)
    Ich kenne momentan die Befehle:
    Wetter
    Zeit
    Motiviere mich
    Beenden""")
        continue
