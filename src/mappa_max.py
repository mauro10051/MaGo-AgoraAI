import os
from pathlib import Path
import sys
import ollama
import threading
import time
import shutil
from pathlib import Path

#from mappa import mappe
project_path = Path.cwd()


modello_max='gemma3:12b'
modello_sam='gemma3:12b'
modello_pol='gemma3:12b'


class Mappa_max:
    def __init__(self, esp1, esp2, domanda, lingua, nome, modello_max, modello_sam,modello_pol, ollama):
  
        self.esp1 = esp1
        self.esp2 = esp2
        self.domanda = domanda
        self.lingua = lingua
        self.nome = nome
        self.modello_max = modello_max
        self.modello_sam = modello_sam
        self.ollama = ollama

        SCRIPT_DIR = Path(sys.argv[0]).parent
        self.project_dir = SCRIPT_DIR / "progetti" / nome
        os.makedirs(self.project_dir, exist_ok=True)

        self.messages = []
        self.map1 = ""
        self.map2 = ""

    def inizializza_mappa_max(self,esp1,domanda,lingua):
       
        messages = [ 
    {'role': 'system', 'content': f" Sei Max, esperto in {esp1}. Il tuo compito è analizzare e approfondire la seguente domanda: '{domanda}'."},  
    {'role': 'system', 'content': f"Tu Max parti dal tuo profilo {esp1} per individuare e restituire solo una lista estesa e strutturata degli elementi essenziali per comprendere questa domanda. La lista deve essere articolata nelle seguenti categorie: "},  
    {'role': 'system', 'content': f"- **Concetti fondamentali**:individua i Principi e teorie chiave, formulati esclusivamente nel tuo ambito di competenza '{esp1}' in relazione alla domanda {domanda}   "},
    {'role': 'system', 'content': f"- **Raggruppa i concetti fondamentali in categorie tematiche pertinenti con la '{domanda}'  "},
   {'role': 'system', 'content': f"- **Relazioni tra concetti fondamentali: Connessioni tra idee per individuare strutture logiche "},
    {'role': 'system', 'content': f"- **Evoluzione storica: come i temi espressi nella domanda sono cambiati nel tempo. "},
    {'role': 'system', 'content': f"- **Scuole di pensiero o approcci teorici**: Correnti di pensiero rilevanti all'interno della tua disciplina. "},  
    {'role': 'system', 'content': f"- **Autori e figure chiave**: Studiosi ed esperti che hanno dato contributi significativi nel tuo settore di competenza in relazione alla domanda. "}, 
    {'role': 'system', 'content': f"- **Eventi o esperimenti rilevanti**: Scoperte, test o sviluppi cruciali, esaminati attraverso il tuo punto di vista disciplinare sempre in relazione ai temi contenuti nella domanda. "}, 
    {'role': 'system', 'content': f"- **Dibattiti aperti e controversie: Questioni ancora irrisolte o dibattute. "}, 
    {'role': 'system', 'content': f"- **Ambito interdisciplinare**: Connessioni con altre discipline, interpretate dalla prospettiva del tuo campo disciplinare e in relazione alla domanda.  "}, 
    {'role': 'system', 'content': f"- **Referenze scientifiche estese includendo testi e anche articoli scientifici significativi,bibliografia a scopo didattico e le fonti utilizzate"},
    {'role': 'system', 'content': f" La tua risposta è completamente in lingua {lingua} ed anche i titoli come esempio *concetti fondamentali* sono in lingua {lingua} e deve contenere solo la lista, senza titolo, senza introduzione e senza conclusione. "},    


]  
 

        return messages

    
    
    def genera_mappa_max(self):

        chat_stato_max = []
        esp1=self.esp1
        lingua=self.lingua
        domanda=self.domanda   

         
        messages=self.inizializza_mappa_max(esp1,domanda,lingua)
   
        response = ollama.chat(model=modello_max, messages=messages)
        messages.append({'role': 'assistant', 'content': response['message']['content']})
       
        comp=response['message']['content']
    
         # Costruisci il percorso corretto per il file usando Path
        file_path = self.project_dir / 'map1.txt'

        # Scrivi la risposta di Max su un file di testo
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(comp)
        
        return comp

       # def _scrivi_file(self, nome_file, contenuto):
          #  file_path = self.project_dir / nome_file
           # with open(file_path, 'w', encoding='utf-8') as f:
              #  f.write(contenuto)

    def esegui(self):
        return self.genera_mappa_max()

if __name__ == "__main__":
    mappa_max = Mappa_max(esp1, esp2, domanda, lingua, progetto, modello_max, modello_sam,modello_pol, ollama)

    mappa_max.esegui()