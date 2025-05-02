# MaGo AgoraAI - Codice Sorgente

Questa cartella contiene i file Python necessari per eseguire la versione base del progetto MaGo AgoraAI, limitata alla generazione di mappe concettuali a partire da una domanda iniziale.

## ✅ Requisiti

- Python ≥ 3.10
- [Ollama](https://ollama.com) (per eseguire modelli LLM localmente)
- Ambiente virtuale consigliato: **conda**

## ⚙️ Setup ambiente (consigliato con Conda)

```bash
conda create -n mago python=3.10
conda activate mago
pip install -r requirements.txt

    Se il file requirements.txt non è presente, puoi aggiungerlo o elencare manualmente le librerie necessarie (es. requests, pyyaml, ecc.).

🧠 Installazione di Ollama

Per installare Ollama, segui le istruzioni ufficiali:

👉 https://ollama.com/download

Assicurati che il modello gemma:12b sia scaricato e attivo:

ollama run gemma:12b

🚀 Esecuzione del progetto

Il file principale è main.py (puoi rinominare progetto.py in main.py per convenzione):

python main.py

📁 Struttura dei file

    main.py: file di avvio del progetto vengono inserite la domanda e i profili essenziali di Max e di Samnta esempio:Max Fisico  e Samnta filosofo                (vedi esempi) 

    mappa_max.py: importato da main.py funzione per generare la mappa concettuale testuale di Max 

    mappa_sam.py: importato da main.py funzione per generare la mappa concettuale testuale di Samanta 

    valuta_mappa_max.py: importato da main.py. Funzione dove Pol valuta la mappa concettuale di Max e suggerisce miglioramenti.

    valuta_mappa_sam.py: importato da main.py. Funzione dove Pol valuta la mappa concettuale di Samanta e suggerisce miglioramenti

🧾 Funzionalità

    Generazione autonoma di mappe concettuali testuali sulla domanda in base al profilo disciplinare  di Max e di Samanta  in linguaggio naturale .

    Valutazione automatica della qualità della mappa da parte del moderatore Pol.

    Possibilità di esportare le mappa generate.

# Al momento solo per i progetti già sviluppati da noi forniamo le interviste e il dibattito in lingua originale 

Per ulteriori dettagli, torna alla pagina principale del progetto o leggi l’abstract esteso.
