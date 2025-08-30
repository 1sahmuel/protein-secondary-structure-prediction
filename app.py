import streamlit as st
import numpy as np
import joblib

# ---------------------------
# Load the trained model
# ---------------------------
model = joblib.load("protein_ss_xgb_model.pkl")

# Amino acids and mappings
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
aa_dict = {aa: i for i, aa in enumerate(amino_acids)}
label_map = {0: 'H', 1: 'E', 2: 'C'}

# Preprocessing function for a single sequence
def preprocess_input(seq, window_size=17):
    half_window = window_size // 2
    padded_seq = 'X' * half_window + seq + 'X' * half_window
    X = []
    
    for i in range(len(seq)):
        window = padded_seq[i:i+window_size]
        window_vec = []
        for aa in window:
            vec = np.zeros(20)
            if aa in aa_dict:
                vec[aa_dict[aa]] = 1
            # else: leave as zero vector for unknowns/padding
            window_vec.extend(vec)  # Flatten for XGBoost
        X.append(window_vec)
    return np.array(X)

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("Protein Secondary Structure Predictor (XGBoost)")

st.write("""
This app predicts the **secondary structure** (H=Helix, E=Sheet, C=Coil) of proteins 
using a **traditional machine learning model (XGBoost)** trained on sliding-window features.
""")

user_seq = st.text_area("Enter your amino acid sequence (e.g., ACDEFG...)", "")

if st.button("Predict"):
    seq = user_seq.strip().upper()
    
    if len(seq) < 17:
        st.error("Sequence too short! Please enter at least 17 amino acids.")
    else:
        X_input = preprocess_input(seq)
        preds = model.predict(X_input)
        predicted_ss = ''.join([label_map[p] for p in preds])
        
        st.subheader("Predicted Secondary Structure:")
        st.text(predicted_ss)

        # Optional: color-coded output
        colored_output = "".join(
            [f":red[{c}]" if c == "H" else f":blue[{c}]" if c == "E" else f":green[{c}]" for c in predicted_ss]
        )

        st.caption("Legend: 🟥 H=Helix | 🟦 E=Sheet | 🟩 C=Coil")
        st.markdown(colored_output)
