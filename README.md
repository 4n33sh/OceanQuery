<div align="center">

# OceanQuery 🌊 
## AI-Powered ChatBot for ARGO Ocean Data Discovery and Visualization

<img src="https://img.shields.io/badge/License_-GPL%203.0-orange"> 
<img src="https://img.shields.io/badge/python_->=%203.1-blue"> 
<img src="https://img.shields.io/badge/Version-v0.7.3-yellow">

---

**OceanQuery is an AI-powered chatbot that helps you in finding out the optimal solution for your oceanographic needs by taking in your query as input and generating an solution that matches your query by processing it in through our RAG-modal.**

### [Video Demo](https://youtu.be/HLMw5QCKNGE) | [Source Code](https://github.com/4n33sh/OceanQuery/blob/main/main.py)

</div>

---

# Our Tech Approach towards building the Tool

During initial conception we set some fundamental **constraints** before proceeding forward:

1. The tool must be able to take in and process the user's query through either **plain text or netCDF file(s) or both**.

2. Use of **RAG** (paired with an netCDF parser alongside BeRT) alongside an **LLM** (we chose toeither implement either **LLAmarine or OceanGPT** since these models were trained specially for oceanographic/marine purposes) to properly **map individual queries to their respective vectorestore DB** (with MCP). This helps us in implementing the best from each of the tech stack.

3. Display the **generated output** (alongside their **references/proofs**) for the user to review. If he/she isi'nt satisfied with the output, we'll take another **feedback query** and **repeat the process until his/her satisfaction**.

Based on above constraints, the following technical approach was devised.

<img width="1814" height="1109" alt="final" src="https://github.com/user-attachments/assets/0e6f8217-b5c4-49c8-99b8-40fd02427a3e" />

**Entity recognition** is achieved through **spaCy's NLP** (through it's large dataset) and ML Training based with **BeRT** was implemented through **TensorFlow and HF transformers**.

---

# Installation & Running

* (optional) **Create & activate** new python **virtual (.venv) environment** and update pip configs :  ``` python3 -m venv ~/your/preffered/path && source ~/your/preffered/path/bin/activate && pip install --upgrade pip setuptools wheel ```

* Install required **external packages/modules** (~250-300mb) : ``` pip install chroma pgvector langchain flask ```

* **Clone** the repo into your preferred directory : ``` git clone https://github.com/4n33sh/OceanQuery.git ```

* Change directory **(cd)** into OceanQuery and install the requirements : ``` cd OceanQuery && pip install -r requirements.txt ```

* Install spaCy NLP (large) **dataset** (~540mb) : ``` python3 -m spacy download en_core_web_lg ```

* Alter **permissions** of **main.py** file and **run** it : ``` chmod u+x main.py && python3 main.py ```

---

# Update Log

- **[19-09-2025]** : Implemented crude version of the RAG-modal. Combo of LLAmarine + Claude (token-based retrieval) was used as base LLM and spaCy as NLP for tokenizing the duplicate query. Basic understanding formed and encoder work in progress.
 
- **[24-09-2025]** : Vectorstore implemented (PostgreSQL used to store duplicate query) with chroma. Encoder setup and Feedback loop properly implemented.

- **[29-09-2025]** : UI/UX work in progress but usable for the final demo (btw some issues still persist with encoder still). Also multilingual support added with (m)BeRT (enables tokenization in ~100 languages but no final context-based textual translation).
