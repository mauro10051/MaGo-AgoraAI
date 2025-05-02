#versione con max che cambia in base al prompt 

import os
from pathlib import Path
import ollama 
import sys

modello_max='gemma3:12b'
modello_sam='gemma3:12b'
modello_pol='gemma3:12b'

class Valuta_max:         
    def __init__(self, esp1, domanda, progetto,lingua, map1,modello_max, modello_sam, modello_pol,ollama):
        self.esp1 = esp1
        self.domanda = domanda
        self.map1 = map1
        self.lingua = lingua
        self.progetto = progetto
        self.modello_max = modello_max
        self.modello_sam = modello_sam
        self.modello_pol = modello_pol
        
        # Crea la directory del progetto se non esiste
        SCRIPT_DIR = Path(sys.argv[0]).parent
        self.project_dir = SCRIPT_DIR / "progetti" / progetto
        os.makedirs(self.project_dir, exist_ok=True)
        messages = []  # Lista dei messaggi globali



    def valutazione_mappa_max(self,esp1, domanda,map1,lingua):
  
        messages =    [
   {'role': 'system','content': f"Pol sei  un valutatore esterno esperto di grande cultura scientifica."},
 {'role': 'system','content': f"Pol devi valutare questa  mappa concettuale  {map1}  generata da Max un {esp1}  sulla base di una domanda iniziale  {domanda}."},
 {'role': 'system','content': f"Pol tu devi **Motivare brevemente ogni valutazione e **Formulare un suggerimento per migliorare la mappa."},
 {'role': 'system','content': f"Criteri di valutazione (usa una scala da 1 a 5 ):"},
 {'role': 'system','content': f"1 Completezza concettuale: la mappa include i concetti di un esperto in {esp1} rilevanti per rispondere alla domanda {domanda}"},
 {'role': 'system','content': f"2 Chiarezza delle relazioni: le connessioni tra concetti sono corrette, esplicite e ben formulate?"},
 {'role': 'system','content': f"3 Organizzazione logica e gerarchica: la mappa ha una struttura chiara, con concetti principali e secondari ben distinti?"},
 {'role': 'system','content': f"4 Accuratezza scientifica o teorica: i concetti sono usati correttamente secondo la disciplina dell’attore che ha generato la mappa?"},
 {'role': 'system','content': f"5 Gestione della complessità: la mappa riesce a sintetizzare concetti complessi senza semplificare in modo eccessivo?"},
 {'role': 'system','content': f"Pol dopo la valutazione  ** formula un suggerimento per migliorare la mappa."},


]


        return messages

    def genera_valutazione_max(self):
        messages=[]
        esp1=self.esp1
        map1=self.map1
        lingua=self.lingua
        domanda=self.domanda
        messages = self.valutazione_mappa_max(esp1, domanda,map1,lingua)
        messages.append({"role": "user", "content": f"Rispondi sempre in {self.lingua}."})
        
        response = ollama.chat(model=self.modello_max, messages=messages)
        rifletto = f"{self.esp1}\n{response['message']['content']}"
        
        # Salva il profilo su file
        with open(self.project_dir / 'valuto_mappa_max.txt', 'w', encoding="utf-8") as file:
            file.write(rifletto)


    def esegui(self):
        return (
        self.genera_valutazione_max()# les1

  
    )
 
if __name__ == "__main__":
                        
    valuta_max = Valuta_max( esp1, domanda, progetto,lingua, map1,modello_max, modello_sam, modello_pol,ollama)
    valuta_max.esegui()

   
        
    
 
    
