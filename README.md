````
Groot Growth – Your AI Financial Companion
===========================================

Groot Growth is a human-centric web app that delivers personalized financial guidance in natural language.  
Powered by a fine-tuned causal language model and served via Streamlit, Groot Growth helps you make smart money decisions without the jargon.

Overview
--------

- Conversational UI: ask any question about saving, credit, investing, or taxes  
- Deterministic Advice: greedy decoding (do_sample=False, temperature=0.0) for consistent recommendations  
- Custom Knowledge Base: your training.txt corpus steers Groot’s expertise  
- Fast & Scalable: model caching + Docker containerization minimize latency and simplify deployment  

Features
--------

- Natural-language Q&A via a Transformers pipeline  
- In-session caching of tokenizer & model for sub-second responses  
- Clean lock-file handling and isolated `/cache` directory  
- One-click deployment via Hugging Face Spaces CI/CD  

Getting Started
---------------

Prerequisites:

- Python 3.9+  
- Docker (for container builds)  
- A Hugging Face account (for Spaces deployment)  

Installation:

1. Clone this repo  
   ```bash
   git clone https://github.com/<your-username>/groot-growth.git
   cd groot-growth
````

2. Install dependencies

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Edit `training.txt` to customize Groot’s domain knowledge

## Usage

Local:

```bash
streamlit run app.py --server.port 8501
```

Open `http://localhost:8501`, enter a question, click "Grow with Groot 🌳".

Docker:

```bash
docker build -t groot-growth .
docker run -p 8501:8501 groot-growth
```

Visit `http://localhost:8501`

## Deployment

Push to `main` on this repo—Spaces CI/CD will build your Docker image and deploy automatically.
Live at `https://huggingface.co/spaces/<your-username>/groot-growth`

## Project Structure

```
groot-growth/
├── app.py
├── Dockerfile
├── requirements.txt
├── training.txt
└── README.md
```

## Contributing

Contributions welcome via issues or pull requests!

## License

MIT License

