# 🧬 Protein Secondary Structure Prediction

This project uses an **XGBoost model** to predict the **secondary structure of proteins** (Helix, Strand, Coil) from an amino acid sequence.

The model is trained on protein sequence data and predicts the structure for each residue in the input sequence.

---

## 🚀 Features

* Takes an amino acid sequence (e.g., `"ACDEFGHIKLMNPQRSTVWY"`) as input.
* Predicts **secondary structure labels**:

  * **H** → Helix (α-helix)
  * **E** → Strand (β-sheet)
  * **C** → Coil/loop
* Provides sequence-to-sequence prediction.
* Interactive **Streamlit web app** for testing.

---

## 📂 Project Structure

```
├── data/                  # Dataset                
├── app.py                 # Streamlit app
├── trad.py                # Model training script
└── README.md              # Project documentation
```

---

## ⚙️ Installation

1. Clone this repo:

```bash
git clone https://github.com/1sahmuel/protein-structure-prediction.git
cd protein-structure-prediction
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🎯 Usage

1. Enter an **amino acid sequence** into the Streamlit app input box:

```
ACDEFGHIKLMNPQRSTVWY
```

2. Model Output (example):

```
HHHCCCCCEEEECCCCCHHH
```

Each character in the output corresponds to the **predicted secondary structure** of the respective amino acid.

---

## 🧑‍💻 Model Details

* **Model:** XGBoost Classifier
* **Input features:** Encoded amino acid sequences
* **Output classes:** 3 (Helix, Strand, Coil)
* **Metrics:** Accuracy, F1-score, Confusion Matrix

---

## 📊 Example

**Input sequence:**

<img width="1856" height="1025" alt="image" src="https://github.com/user-attachments/assets/926a203c-2182-4b75-87c1-ba7b095495a7" />


## ✅ Requirements

* Python 3.8+
* XGBoost
* Scikit-learn
* NumPy, Pandas, Matplotlib
* Streamlit

Install them with:

```bash
pip install xgboost scikit-learn numpy pandas matplotlib streamlit
```

---

## 🏗 Future Improvements

* Train with larger datasets (e.g., PDB, UniProt).
* Add **8-class DSSP mapping** for more detailed predictions.
* Deploy online (HuggingFace Spaces / Streamlit Cloud).



