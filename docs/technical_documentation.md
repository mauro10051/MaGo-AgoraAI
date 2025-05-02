# 📖  Technical Documentation

Welcome to the repository dedicated to the guided simulation of lessons and debates between intelligent agents.

This solution allows you to run Python notebooks **locally** using LLM models through the **Ollama** platform, with a focus on **Gemma3:12b**.

---

## ✅ Hardware Requirements

- **NVIDIA RTX 4000 series or higher** graphics card
- All notebooks have been tested with:
  - **GPU:** RTX 4070
  - **RAM:** 32 GB
- **Operating System:** Windows (currently the only supported OS)

---

## 🧠 LLM Model

This project uses the **Gemma3:12b** model, running locally via [Ollama](https://ollama.com/).  
Make sure you have:

- **Installed Ollama**
- **Downloaded and loaded** the `gemma3:12b` model locally

> ✨ You may test other models, but doing so requires modifying the code accordingly.  
> Gemma3 has shown excellent performance in our demos, likely due to the model's quality and the innovative management of agents.

---

## 📦 Recommended Python Environment

We recommend using **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** or **Anaconda** to create a dedicated Python environment.

### 📚 Required Libraries

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
```

---

## ⚙️ Project Pipeline

To ensure proper execution, follow this step-by-step pipeline:

1. **Register the projects**
2. **Extract the conceptual maps**
3. **Update the profiles of the two agents**
4. **Run the interviews**
5. **Start the debate**

⚠️ Do **not** run the lessons or debate before completing the first three steps.

---

## 📌 Final Notes

- The interface is built using **Tkinter** for interactive usage.
- The system is modular and can be easily adapted to new logic and agent behavior.

---

## 📬 Contact

For feedback, suggestions, or contributions, feel free to open an [Issue](https://github.com/mauro10051/MaGo-AgoraAI/issues) or submit a Pull Request!

---

> **Made with ❤️ for interactive AI learning**
