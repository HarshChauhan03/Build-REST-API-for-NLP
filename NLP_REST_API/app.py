from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load models once
sentiment_model = pipeline("sentiment-analysis")
summarizer_model = pipeline("summarization")
generator_model = pipeline("text-generation", model="gpt2")

class TextRequest(BaseModel):
    text: str

@app.post("/sentiment")
def sentiment_analysis(request: TextRequest):
    result = sentiment_model(request.text)[0]
    return {
        "label": result["label"],
        "confidence": round(result["score"], 3)
    }

@app.post("/summarize")
def summarize_text(request: TextRequest):
    summary = summarizer_model(request.text, max_length=60, min_length=20, do_sample=False)
    return {
        "summary": summary[0]["summary_text"]
    }

@app.post("/generate")
def generate_text(request: TextRequest):
    generated = generator_model(request.text, max_length=100)
    return {
        "generated_text": generated[0]["generated_text"]
    }
