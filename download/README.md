# 🎯Gestione dei Download del Progetto

Questo repository contiene i file necessari per eseguire il progetto sia in locale che su Google Colab. I file sono organizzati nelle seguenti cartelle:

## gestione_locale/

La cartella `gestione_locale` contiene i notebook da eseguire in ambiente locale. I notebook dovranno essere lanciati secondo un preciso ordine:

1. [`1_install.ipynb`](gestione_locale/1_install.ipynb): Questo notebook crea e registra il path di lavoro dove posizionare i tuoi notebook e la cartella con tutti i progetti che andrai a costruire.
2. [`2_generate_project.ipynb`](gestione_locale/2_generate_project.ipynb): In questo notebook devi dare un nome a un nuovo progetto, indicare il tema di studio (che avrà la struttura di una domanda) e la disciplina di base degli Agenti. Ad esempio: Max è un Fisico teorico, Samanta è una filosofa, e la domanda potrebbe essere: "Il tempo è reale o una costruzione della mente?"
3. ['3_textual_map.ipynb'](gestione_locale/3_textual_map.ipynb): Dopo aver registrato il progetto, con questo notebook devi generare la mappa concettuale testuale di Max e di Samanta, in relazione al tema della domanda.
4. ['4_profile.ipynb'](gestione_locale/4_profile.ipynb): Questo notebook predispone due strumenti fondamentali: i nuovi profili di Max e di Samanta e le tracce che utilizzerai successivamente per la gestione delle lezioni e del dibattito.
5. ['5_lessons.ipynb'](gestione_locale/5_lessons.ipynb): L'output di questo notebook è una lezione strutturata come intervista tra un Agente (che impersona il ruolo di moderatore) e Max e/o Samanta. Un esempio di testo scientifico con finalità divulgative.
6. ['06_debate.ipynb'](gestione_locale/6_debate.ipynb): Il risultato finale di questa pipeline è un dibattito tra Max e Samanta, moderato da Pol.

## gestione_colab/

La cartella `gestione_colab` contiene i notebook da eseguire su Google Colab:

- **01_presentazione_colab.ipynb**: Introduzione al progetto e configurazione per l'esecuzione su Google Colab.

## Come usare

- **Per ambiente locale**: Segui le istruzioni nel file `01_install.ipynb`, e poi esegui i file in ordine dalla cartella `gestione_locale/` come indicato sopra.
- **Per ambiente Colab**: Apri il file `01_presentazione_colab.ipynb` direttamente su Google Colab e segui le istruzioni per avviare il progetto.
