import datetime
import time
import os
from apps.modulIA import*
from apps.donnees import*
from apps.fonction import*
from apps.gptAPI import*

BASE_DIR = os.path.dirname(__file__)
SAVE_TEXTE = os.path.join(BASE_DIR, "Save/note.txt")


def assistant():
    nom_utilisateur = "John"
    Intro = lambda : Salutation() + " " + presenter() + " " + "Que puis-je faire pour vous ?"
    parler(Intro())

    while True:
        commande = ecouter()
        
        if "intro" in commande :
            parler(Intro())

        elif "heure" in commande:
            heure = datetime.datetime.now().strftime("%H:%M")
            parler(f"Il est {heure}.")

        elif "date" in commande or "jour" in commande:
            date = datetime.datetime.now().strftime("%A %d %B %Y")
            parler(f"Aujourd'hui, nous sommes le {date}.")
            
        elif "mon nom est" in commande:
            nom_utilisateur = commande.replace("mon nom est", "").strip()
            parler(f"Enchanté, {nom_utilisateur} !")

        elif "quel est mon nom" in commande:
            if nom_utilisateur:
                parler(f"Vous vous appellez {nom_utilisateur}.")
            else:
                parler("Je ne connais pas encore ton nom.")
                
        elif "ouvre youtube" in commande:
            webbrowser.open("https://www.youtube.com")
            parler("J'ai ouvert YouTube.")

        elif "ouvre google" in commande:
            webbrowser.open("https://www.google.com")
            parler("Google est ouvert.")
        
        elif "logique" in commande or "contradiction" in commande:
            webbrowser.open("https://www.youtube.com/watch?v=RGKZPBS-sac&list=RDRGKZPBS-sac&start_radio=1")
            parler("Playlist Scylla : logique d'une contradiction")

        elif "wikipédia" in commande:
            parler("Que voulez-vous savoir sur Wikipédia ?")
            sujet = ecouter()
            if sujet != "" :
                recherche_wikipédia(sujet)
            
        elif "blague" in commande:
            blague = Blagues()
            parler(blague)

        elif "arrête" in commande or "stop" in commande or "au revoir" in commande or "fin" in commande:
            parler("Au revoir, à bientôt !")
            break
        
        elif "recherche" in commande :
            sujet = commande.lower().replace("recherche", "").replace("", "").strip()
            recherche_google(sujet)
        
        elif "merci" in commande :
            parler("Je vous en prie Commandant")
            
        elif "note" in commande:
            parler("Que dois-je noter ?")
            note = ecouter()
            with open(SAVE_TEXTE, "a", encoding="utf-8") as f:
                f.write(note + "\n")
            parler("C'est noté !")
        
        elif "minuteur" in commande or "alarme" in commande:
            parler("Combien de secondes ?")
            try :
                secondes = int(ecouter())
            except :
                secondes = 5
            parler(f"Minuteur lancé pour {secondes} secondes.")
            time.sleep(secondes)
            parler("Le temps est écoulé.")
        
        elif "gpt" in commande or 'chat' in commande :
            question = commande.replace("gpt", "").replace("chat", "").strip()
            reponse = gpt_reponse(question)
            parler(reponse)
        
        elif "repeat" in commande :
            phrse = commande.replace('repeat', "").strip()
            parler(phrse)

        elif commande != "":
            parler("Je ne connais pas cette commande, désolé.")

# Lancement de l'assistant
assistant()
