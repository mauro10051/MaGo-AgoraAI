# 📖 # 💬 Progetto di Simulazione Intelligente - README

Benvenuti nel repository dedicato alla simulazione guidata di lezioni e dibattiti tra agenti intelligenti.

Questa soluzione consente di eseguire in locale notebook Python che sfruttano modelli LLM tramite la piattaforma **Ollama**, con un focus su **Gemma3:12b**.  

---

## ✅ Requisiti hardware

- Scheda grafica **NVIDIA RTX serie 4000 o superiore**
- Tutti i notebook sono stati testati con:
  - **GPU:** RTX 4070
  - **RAM:** 32 GB
- **Sistema operativo:** Windows (per ora supportato esclusivamente)

---

## 🧠 Modello LLM

Il progetto utilizza il modello **Gemma3:12b** eseguito tramite [Ollama](https://ollama.com/).  
Assicurati di:

- Avere **installato Ollama**
- Avere **caricato in locale** il modello `gemma3:12b`

> ✨ È possibile usare altri modelli, ma sarà necessario modificare opportunamente il codice.
>
> Gemma3 ha garantito ottime performance grazie alla qualità della rete e alla gestione innovativa degli agenti.

---

## 📁 Notebook disponibili

### 1. `1_install.ipynb`  
Registra il **path di lavoro** dove viene caricato il progetto.  
⚠️ **Funziona solo su Windows.**

### 2. `2_generate_project.ipynb`  
Genera la struttura del progetto e i dati iniziali.  
✅ Se non usi Windows, **puoi partire da qui**, modificando manualmente i percorsi nel codice.

> 🧪 Una versione compatibile con **Google Colab** è in fase di sviluppo.

---

## 📦 Ambiente Python consigliato

Si consiglia l’utilizzo di **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** o **Anaconda** per creare un ambiente dedicato.

### 📚 Librerie richieste

```python
import os
import json
from pathlib import Path
import gradio as gr
import ollama
import threading
import time
import shutil
import subprocess
from time import sleep
