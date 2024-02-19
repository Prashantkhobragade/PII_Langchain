# PII_Langchain

steps:

### 1. Clone this repository to your local machine using:
```bash
git https://github.com/Prashantkhobragade/PII_Langchain.git
```
### 2. Create a conda environment after opening the repository:
```bash
conda create -p venv python=3.10 -y
```
```bash
conda activate venv/
```
### 3. Install the requirements:
```bash
pip install -r requirements.txt
```
download model
```bash
python -m spacy download en_core_web_lg 
```

### run stremlit app
```bash
streamlit run anonymizer/anonymizer.py
```