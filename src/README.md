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

    main.py: file di avvio del progetto.

    modelli_agenti.py: definizione degli agenti (Pol, Max, Samanta).

    mappa_generator.py: logica di costruzione delle mappe concettuali.

    valutazione.py: autovalutazione della mappa da parte di Pol.

    utils.py: funzioni di supporto (stampa, salvataggio, ecc.).

🧾 Funzionalità

    Generazione autonoma di mappe concettuali in linguaggio naturale.

    Valutazione automatica della qualità della mappa da parte del moderatore Pol.

    Possibilità di stampare o esportare la mappa generata.

Per ulteriori dettagli, torna alla pagina principale del progetto o leggi l’abstract esteso.
