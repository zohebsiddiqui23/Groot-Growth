import os
import shutil
import glob

# ──────── CLEAN UP ANY STALE LOCKS ────────────────────────────────────────
for path in glob.glob("/cache/**/*.lock", recursive=True):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    except Exception:
        pass

# ─── Make sure all HF/Transformers caches go to /cache ───────────────────────
os.environ.setdefault("HF_HOME", "/cache")
os.environ.setdefault("TRANSFORMERS_CACHE", "/cache")
os.environ.setdefault("HF_DATASETS_CACHE", "/cache")
os.environ.setdefault("HF_METRICS_CACHE", "/cache")

import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ─── Streamlit page config ────────────────────────────────────────────────
st.set_page_config(page_title="Groot Growth – Financial Companion")
st.title("🌱 Groot Growth – Your AI Financial Guide")

# ─── Load your training corpus ─────────────────────────────────────────────
with open("training.txt", "r") as f:
    training_corpus = f.read()

# ─── Initialize the generator (cached) ────────────────────────────────────
@st.cache_resource(show_spinner=False)
def init_generator():
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-Coder-1.3B-base")
    model     = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-Coder-1.3B-base")
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

# ─── Lazily load the model into session_state ─────────────────────────────
if "generator" not in st.session_state:
    with st.spinner("Loading Groot’s brain… this may take a minute"):
        st.session_state.generator = init_generator()

# ─── User input ────────────────────────────────────────────────────────────
user_prompt = st.text_area("💬 Ask Groot about finances (saving, credit, investing):")

# ─── On-click generation ───────────────────────────────────────────────────
if st.button("Grow with Groot 🌳"):
    if not user_prompt.strip():
        st.warning("Please enter a question for Groot!")
    else:
        with st.spinner("Groot is thinking… 🌿"):
            # 1) System instruction + corpus
            system_preface = (
                "Groot is an expert AI financial guide. "
                "He answers clearly, concisely, and in full sentences.\n"
            )
            full_prompt = (
                system_preface
                + training_corpus
                + f"\nUser: {user_prompt}\nGroot:"
            )

            # 2) Generate with greedy decoding for consistency
            result = st.session_state.generator(
                full_prompt,
                max_new_tokens=100,
                do_sample=False,
                temperature=0.0,
            )

        # 3) Strip out only Groot’s reply
        raw = result[0]["generated_text"]
        answer = raw.split("Groot:")[-1].split("User:")[0].strip()

        st.markdown("### 🌿 Groot Says:")
        st.write(answer)
