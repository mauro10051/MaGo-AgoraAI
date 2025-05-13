# creazione del progetto 
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os
from pathlib import Path
import os
import ollama
import threading
import time
import shutil
from pathlib import Path
#from mappa import Mappe
from mappa_max import Mappa_max
from mappa_sam import Mappa_sam
from valuta_mappa_max import Valuta_max
from valuta_mappa_sam import Valuta_sam



modello_max='gemma3:12b'
modello_sam='gemma3:12b'
modello_pol='gemma3:12b'



project_path = Path.cwd()

project_dir = Path(project_path) / "progetto" 

root = tk.Tk()
from tkinter import scrolledtext
root.title("AgoraAi  Create your project generate the concept map")
root.geometry("550x850")

style = ttk.Style()
style.configure("Green.TButton", background="#fdf5e6",foreground="red")


# ============================
# DATI
# =============================

esempi = {
    "Fisica e Filosofia - Tempo": ["Tu sei Max, un Fisico esperto in fisica teorica e meccanica quantistica.",
                                   "Tu sei Samanta, una Filosofa esperta in epistemologia e ontologia.",
                                   "Il tempo è una realtà oggettiva o una costruzione della mente?"],
    "Fisica e Filosofia - Conoscenza": ["Tu sei Max, un Fisico esperto in fisica teorica e meccanica quantistica.",
                                        "Tu sei Samanta, una Filosofa esperta in epistemologia e ontologia.",
                                        "Quale è il ruolo dell’osservatore nella conoscenza della realtà?"],
    "Format vuoto": ["", "", ""]
}

MESSAGGIO_CONFERMA = {
    "Italiano": "Creazione del progetto terminata",
    "English": "Project has been successfully created",
    "Español": "Creación del proyecto completada con éxito",
    "Deutsch": "Projekt wurde erfolgreich erstellt"
}

project_path = Path.cwd()

# Cartella che contiene tutte le sottocartelle dei progetti
CARTELLA_PROGETTI = "progetti"

# =============================
# FUNZIONI
# =============================


def carica_progetti():
    # Elenca solo le cartelle (i progetti)
    return [nome for nome in os.listdir(CARTELLA_PROGETTI)
            if os.path.isdir(os.path.join(CARTELLA_PROGETTI, nome))]

def on_scelta(event):
    progetto = combo.get()
    #print(f"Progetto selezionato: {progetto}")
    #print(progetto)

def carica_esempio(event):
    selected = esempio_var.get()
    if selected in esempi:
        esp1_entry.delete("1.0", tk.END)
        esp1_entry.insert(tk.END, esempi[selected][0])

        esp2_entry.delete("1.0", tk.END)
        esp2_entry.insert(tk.END, esempi[selected][1])

        domanda_entry.delete("1.0", tk.END)
        domanda_entry.insert(tk.END, esempi[selected][2])

def aggiorna_combo_progetti():
    progetti = carica_progetti()
    combo['values'] = progetti
    if progetti:
        combo.set(progetti[-1])  # opzionale: seleziona subito l'ultimo salvato
    root.update()

def salva_progetto():
    esp1 = esp1_entry.get("1.0", tk.END).strip()
    esp2 = esp2_entry.get("1.0", tk.END).strip()
    domanda = domanda_entry.get("1.0", tk.END).strip()
    nome = nome_entry.get().strip()
    lingua = lingua_var.get()

    if not nome:
        result_label.config(text="Inserisci un nome per il progetto", foreground="red")
        return

    project_dir = project_path / "progetti" / nome
    project_dir.mkdir(parents=True, exist_ok=True)

    (project_dir / "esp1.txt").write_text(esp1, encoding="utf-8")
    (project_dir / "esp2.txt").write_text(esp2, encoding="utf-8")
    (project_dir / "domanda.txt").write_text(domanda, encoding="utf-8")
    (project_dir / "lingua.txt").write_text(lingua, encoding="utf-8")

    msg = MESSAGGIO_CONFERMA.get(lingua, "Progetto creato")
    aggiorna_combo_progetti()
    result_label.config(text=msg, foreground="green")

def aggiorna_lista_progetti(combo):
    progetti_dir = project_path / "progetti"
    progetti = [p.name for p in progetti_dir.iterdir() if p.is_dir()]
    combo['values'] = progetti
    combo.set('')  # resetta la selezione


def delete_progetto():

    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    shutil.rmtree(project_dir)
    aggiorna_lista_progetti(combo)
    domanda_entry.delete("1.0", tk.END)
    esp1_entry.delete("1.0", tk.END)
    esp2_entry.delete("1.0", tk.END)
    result_label.config(text="Progetto cancellato.", fg="red")

    return
def safe_read(file_path):
    if file_path.exists():
      
        return file_path.read_text(encoding="utf-8")
    else:
        return ""

def on_scelta(event):
    progetto_selezionato = combo.get()
    carica_progetto()  # Passa il nome del progetto selezionato

def carica_progetto():
    progetto = combo.get().strip()
    if not progetto:
        result_label.config(text="Inserisci un nome per il progetto", foreground="red")
        return
    esp1_entry.delete("1.0", tk.END)
    esp2_entry.delete("1.0", tk.END)
    domanda_entry.delete("1.0", tk.END)
    project_dir = project_path / "progetti" / progetto
    project_dir.mkdir(parents=True, exist_ok=True)
 
    esp1 = safe_read(project_dir / "esp1.txt")

    esp2 = safe_read(project_dir / "esp2.txt")
    domanda = safe_read(project_dir / "domanda.txt")
    lingua = safe_read(project_dir / "lingua.txt")
    intervista_max = safe_read(project_dir / "intervista_max.txt")

    file_mappa1 = project_dir / "map1.txt"
    esp1_entry.insert("1.0", esp1)
    esp2_entry.insert("1.0", esp2)
    domanda_entry.insert("1.0", domanda)
    lingua_var.set(lingua)

    map1 = safe_read(project_dir / "map1.txt")  
    map2 = safe_read(project_dir / "map2.txt")  
    valuto_mappa_max = safe_read(project_dir / "valuto_mappa_max.txt")  
    valuto_mappa_sam = safe_read(project_dir / "valuto_mappa_sam.txt")  
    dibattito = safe_read(project_dir / "dibattito.txt")  

    try:
        if len(map1) > 0:
            check1m.config(state="normal")
            check1m.select()
        else:
            check1m.config(state="disabled")
            check1m.deselect()
    except (NameError, TypeError):
        check1m.config(state="disabled")
        check1m.deselect()

    try:
        if len(valuto_mappa_max) > 0: # Solo per verificare se esiste
            check2m.config(state="normal")
            check2m.select()
        else:
            check2m.config(state="disabled")
            check2m.deselect()
    except NameError:
        check2m.config(state="disabled")
        check2m.deselect()

    try:
        if len(map2) > 0:
            check1s.config(state="normal")
            check1s.select()
        else:
            check1s.config(state="disabled")
            check1s.deselect()

    except (NameError, TypeError):
        check1s.config(state="disabled")
        check1s.deselect()

    try:
        if len(valuto_mappa_sam) > 0: # Solo per verificare se esiste
            check2s.config(state="normal")
            check2s.select()
        else:
            check2s.config(state="disabled")
            check2s.deselect()
    except NameError:
        check2s.config(state="disabled")
        check2s.deselect()
    
    try:
        if len(intervista_max) > 0: # Solo per verificare se esiste
            predef_frame.place(x=5, y=700, width=505, height=120)
        else:
            predef_frame.place_forget()
    except NameError:
            predef_frame.place_forget()

  

def genera_mappa_max():
    result_label.config(text="I am working .....", fg="red")
    root.update()
    # Prendi i valori dal form
    esp1 = esp1_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp1
    esp2 = esp2_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp2
    domanda = domanda_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per domanda
    lingua = lingua_var.get()  # Ottieni la lingua selezionata
    progetto = combo.get().strip()  # Ottieni il nome del progett

    # Verifica che tutte le informazioni siano inserite
    if not esp1 or not esp2 or not domanda or not progetto:
        result_label.config(text="Tutti i campi sono obbligatori.", fg="red")
        return

    # Crea l'istanza della classe Mappe senza salvare il progetto
    mappa_max = Mappa_max(esp1, esp2, domanda, lingua, progetto, modello_max, modello_sam, modello_pol,ollama)
    
    # Esegui il metodo per generare le mappe
    map1 = mappa_max.esegui()
    
    # Mostra un risultato nell'interfaccia
    result_label.config(text="Max map successfully generated.", fg="green")



def valuta_mappa_max():
    result_label.config(text="I am working .....", fg="red")
    root.update()
    esp1 = esp1_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp1
    esp2 = esp2_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp2
    domanda = domanda_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per domanda
    lingua = lingua_var.get()  # Ottieni la lingua selezionata
    #progetto = nome_entry.get().strip() # Ottieni il nome del progettonome = nome_entry.get().strip()
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    project_dir.mkdir(parents=True, exist_ok=True)
    map1 = (project_dir / "map1.txt").read_text(encoding="utf-8")
   
    valuta_max = Valuta_max( esp1, domanda, progetto,lingua,map1, modello_max, modello_sam, modello_pol,ollama)
    # Esegui il metodo per generare le mappe
    valuazione_mappa_max = valuta_max.esegui()   
        # Mostra un risultato nell'interfaccia
    result_label.config(text="Max's map evaluation completed.", fg="green")

def genera_mappa_sam():
    result_label.config(text="I am working .....", fg="red")
    root.update()
    esp1 = esp1_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp2
    esp2 = esp2_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp2
    domanda = domanda_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per domanda
    lingua = lingua_var.get()  # Ottieni la lingua selezionata
    progetto = combo.get().strip()  # Ottieni il nome del progetto

    # Verifica che tutte le informazioni siano inserite
    if not esp1 or not esp2 or not domanda or not progetto:
        result_label.config(text="Tutti i campi sono obbligatori.", fg="red")
        return

    # Crea l'istanza della classe Mappe senza salvare il progetto
    mappa_sam = Mappa_sam(esp1,esp2, domanda, lingua, progetto, modello_max, modello_sam, modello_pol,ollama)
    
    # Esegui il metodo per generare le mappe
    map2 = mappa_sam.esegui()
    
    # Mostra un risultato nell'interfaccia
    result_label.config(text="Samanta map successfully generated.", fg="green")

def valuta_mappa_sam():
    result_label.config(text="I am working .....", fg="red")
    root.update()

    esp1 = esp1_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp1
    esp2 = esp2_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per esp2
    domanda = domanda_entry.get("1.0", tk.END).strip()  # Estrarre testo da Text widget per domanda
    lingua = lingua_var.get()  # Ottieni la lingua selezionata
    #progetto = nome_entry.get().strip() # Ottieni il nome del progettonome = nome_entry.get().strip()
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    project_dir.mkdir(parents=True, exist_ok=True)
    map2 = (project_dir / "map2.txt").read_text(encoding="utf-8")
   
    valuta_sam = Valuta_sam(esp2, domanda, progetto,lingua,map2,modello_max, modello_sam, modello_pol,ollama)
    # Esegui il metodo per generare le mappe
    valuazione_mappa_sam = valuta_sam.esegui()   
    result_label.config(text="Samanta's map evaluation completed.", fg="green")

def mostra_map1():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Mappa concettuale di Max")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    map1 = (project_dir / "map1.txt").read_text(encoding="utf-8")
    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, map1)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

def mostra_val1():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Mappa concettuale di Max")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    valuto_mappa_max = (project_dir / "valuto_mappa_max.txt").read_text(encoding="utf-8")
    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, valuto_mappa_max)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

def mostra_val2():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Mappa concettuale di Max")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    valuto_mappa_sam = (project_dir / "valuto_mappa_sam.txt").read_text(encoding="utf-8")
    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, valuto_mappa_sam)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

def mostra_map2():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Mappa concettuale di Samanta")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    try:
        map2 = (project_dir / "map2.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        result_label.config(text="Attenzione: il file non esiste.", fg="red")

    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, map2)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

def mostra_intervista_m():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Lesson and Interview with Max")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    try:
        intervista_max = (project_dir / "intervista_max.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        result_label.config(text="Attenzione: il file non esiste.", fg="red")

    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, intervista_max)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

def mostra_intervista_s():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Lesson and Interview with Samanta ")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    try:
        intervista_sam = (project_dir / "intervista_sam.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        result_label.config(text="Attenzione: il file non esiste.", fg="red")

    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, intervista_sam)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile



def mostra_dibattito():
    finestra = tk.Toplevel()  # Crea una nuova finestra
    finestra.title("Debate Between Max and Samanta, Moderated by Pol")
    progetto = combo.get().strip()
    project_dir = project_path / "progetti" / progetto
    try:
        dibattito = (project_dir / "dibattito.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        result_label.config(text="Attenzione: il file non esiste.", fg="red")

    area_testo = scrolledtext.ScrolledText(finestra, width=80, height=20)
    area_testo.pack(padx=10, pady=10)
    
    area_testo.insert(tk.END, dibattito)  # Inserisce il contenuto di map1
    area_testo.config(state='disabled')  # Rende il testo non modificabile

# Finestra principale


# =============================
# UI
# =============================


style.configure("LeftAlign.TButton", anchor="w")  # "w" = west = sinistra
(style.theme_use('clam'))
#style.configure('TButton', padding=(10, 5))  # (orizzontale, verticale)
style.configure("LeftAlign.TButton", anchor="w",padding=(5, 1))
style.configure("Green.TButton", background="#f8f4e3",foreground="blue", anchor="w",padding=(5, 1))
style.configure("Gre.TButton", background="lightblue",foreground="black", anchor="w",padding=(5, 1))
style.configure("Pinki.TButton", background="#FFD700",foreground="black", anchor="w",padding=(5,1))

# Dropdown esempi
tk.Label(root, text="Project example").place(x=10, y=5, width=100, height=20)
esempio_var = tk.StringVar()
esempio_dropdown = ttk.Combobox(root, textvariable=esempio_var, values=list(esempi.keys()), width=50)
esempio_dropdown.place(x=10, y=25, width=180, height=22)
esempio_dropdown.bind("<<ComboboxSelected>>", carica_esempio)

# Lingua (radio
lingua_var = tk.StringVar(value="English")
lingua_frame = tk.LabelFrame(root, text="Response LANGUAGE")
lingua_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
for i, lang in enumerate(["Italiano", "English", "Español", "Deutsch"]):
    tk.Radiobutton(lingua_frame, text=lang, variable=lingua_var, value=lang).grid(row=0, column=i)

# Esp1
tk.Label(root, text="🤵Max's Expertise").grid(row=2, column=0, padx=10, sticky="w")
esp1_entry = tk.Text(root, height=3, width=60, wrap="word")
esp1_entry.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

# Esp2
tk.Label(root, text="👩‍🔬Samanta's Expertise").grid(row=4, column=0, padx=10, sticky="w")
esp2_entry = tk.Text(root, height=3, width=60, wrap="word")
esp2_entry.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

# Domanda
tk.Label(root, text="🎯Main question").grid(row=6, column=0, padx=10, sticky="w")
domanda_entry = tk.Text(root, height=3, width=60, wrap="word")
domanda_entry.grid(row=7, column=0, padx=10, pady=5, columnspan=2)


pro_frame = tk.LabelFrame(root, text="Fill in expertise and question fields - name your project and SAVE")
pro_frame.place(x=5, y=330, width=500, height=60)  # Dimensioni adatte a contenere i bottoni

# Nome progetto
tk.Label(pro_frame, text="Name new project").place(x=0, y=10, width=100, height=22)
nome_entry = tk.Entry(pro_frame, width=10)
nome_entry.place(x=130, y=10, width=150, height=22)

# Bottone Salva
save_button = ttk.Button(pro_frame, text="Save project",style="LeftAlign.TButton", command=salva_progetto)
save_button.place(x=300, y=10, width=100, height=22)

# Esito
result_label = tk.Label(root, text="",anchor="w", font=("Helvetica", 10))
result_label.place(x=20, y=690, width=300, height=22)



# Bottone cancella progetto
save_button = ttk.Button(root, text="Delete project",style="Gre.TButton", command=delete_progetto)
save_button.place(x=405, y=440, width=100, height=22)  # Imposta posizione e dimensione


tk.Label(root, text="Load project").place(x=5, y=420, width=100, height=20)

progetti = carica_progetti()

combo = ttk.Combobox(root, values=progetti, state="normal")
combo.place(x=5, y=440, width=180, height=25)
combo.bind("<<ComboboxSelected>>", on_scelta)

max_frame = tk.LabelFrame(root, text="Max")
max_frame.place(x=5, y=500, width=240, height=180)  # Dimensioni adatte a contenere i bottoni

# --- Bottoni dentro il frame ---
# Bottone mappa Max
mappa_button_max = ttk.Button(max_frame, text="Generate Max's Map", style="LeftAlign.TButton", command = genera_mappa_max)
mappa_button_max.place(x=5, y=5, width=170, height=25)

var1m = tk.IntVar()
check1m = tk.Checkbutton(max_frame, text="", variable=var1m, state="disabled")
check1m.place(x=190, y=5, width=20, height=25)

bottone_st_map = ttk.Button(max_frame, text="Show concept map", style="Green.TButton", command=mostra_map1)
bottone_st_map.place(x=5, y=35, width=170, height=25)

# Bottone valuta mappa Max
mappa_button_max_v = ttk.Button(max_frame, text="Evaluate Max's Map", style="LeftAlign.TButton", command=valuta_mappa_max)
mappa_button_max_v.place(x=5, y=95, width=170, height=25)

var2m = tk.IntVar()
check2m = tk.Checkbutton(max_frame, text="", variable=var2m, state="disabled")
check2m.place(x=190, y=95, width=20, height=25)

bottone_st_val = ttk.Button(max_frame, text="Pol evaluates Max", style="Green.TButton", command=mostra_val1)
bottone_st_val.place(x=5, y=125, width=170, height=25)


sam_frame = tk.LabelFrame(root, text="Samanta")
sam_frame.place(x=260, y=500, width=245, height=180)  # Cornice giusta

# Bottoni dentro sam_frame (coordinate piccole relative al frame)
mappa_button_sam = ttk.Button(sam_frame, text="Generate Samanta's Map ", style="LeftAlign.TButton", command=genera_mappa_sam)
mappa_button_sam.place(x=5, y=5, width=170, height=25)

var1s = tk.IntVar()
check1s = tk.Checkbutton(sam_frame, text="", variable=var1s, state="disabled")
check1s.place(x=190, y=5, width=20, height=25)

bottone_sa_map = ttk.Button(sam_frame, text="Show concept map", style="Green.TButton", command=mostra_map2)
bottone_sa_map.place(x=5, y=35, width=170, height=25)

mappa_button_sam_v = ttk.Button(sam_frame, text="Evaluate Samanta's Map", style="LeftAlign.TButton", command=valuta_mappa_sam)
mappa_button_sam_v.place(x=5, y=95, width=170, height=25)

var2s = tk.IntVar()
check2s = tk.Checkbutton(sam_frame, text="", variable=var2s, state="disabled")
check2s.place(x=190, y=95, width=20, height=25)

bottone_sa_val = ttk.Button(sam_frame, text="Pol evaluates Samanta", style="Green.TButton", command=mostra_val2)
bottone_sa_val.place(x=5, y=125, width=170, height=25)

predef_frame = tk.LabelFrame(root, text="Predefined and Generated Results (Source Process Not Public at This Time)")
predef_frame.place(x=5, y=700, width=505, height=120)

btn_lezione_1 = ttk.Button(predef_frame, text="Show Pol Interviews 🤵 Max", style="Pinki.TButton", command=mostra_intervista_m)
btn_lezione_1.place(x=5, y=15, width=180, height=25)
btn_lezione_2 = ttk.Button(predef_frame, text="Show Pol Interviews 👩‍🔬 Samanta", style="Pinki.TButton", command=mostra_intervista_s)
btn_lezione_2.place(x=260, y=15, width=185, height=25)
btn_dibattito = ttk.Button(predef_frame, text="Show cooperative dialogue with Pol, Max, and Samanta", style="Pinki.TButton", command=mostra_dibattito)
btn_dibattito.place(x=130, y=65, width=245, height=25)

aggiorna_lista_progetti(combo)



root.mainloop()

