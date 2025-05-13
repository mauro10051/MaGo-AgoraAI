# MaGo AgoraAI - Source Code

This folder contains the necessary Python files to run the base version of the MaGo AgoraAI project, limited to generating concept maps from an initial question.

## ✅ Requirements

- Python ≥ 3.10
- [Ollama](https://ollama.com) (to run LLM models locally)
- Recommended virtual environment: **conda**

## ⚙️ Setting Up the Environment (Recommended with Conda)

```bash
conda create -n mago python=3.10
conda activate mago

🧠 Installing Ollama

To install Ollama, follow the official instructions:

👉 Ollama Download

Ensure that the model gemma:12b is downloaded and running:

ollama run gemma:12b

🚀 Running the Project

The main file is main.py:

python main.py

📁 File Structure

    main.py: The project startup file. It prompts for the main question and the essential profiles of Max and Samanta (e.g., Max the Physicist and Samanta the Philosopher) (see examples).

    mappa_max.py: Imported by main.py. Function to generate Max's text-based concept map.

    mappa_sam.py: Imported by main.py. Function to generate Samanta's text-based concept map.

    valuta_mappa_max.py: Imported by main.py. Function where Pol evaluates Max's concept map and suggests improvements.

    valuta_mappa_sam.py: Imported by main.py. Function where Pol evaluates Samanta's concept map and suggests improvements.

    Progetti Folder: Contains some demo projects created by us. You can overwrite these projects or create new ones, which will be saved in this folder.

🧾 Features

    Automatic generation of text-based concept maps based on the question, using Max's and Samanta's academic profiles in natural language.

    Automatic evaluation of the map's quality by the moderator Pol.

    Ability to export the generated maps.

Currently, for the projects developed by us, we provide the original-language, interviews, debates and thesis

