from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import pipeline, AutoTokenizer

app = FastAPI()

# Load model once
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
pipe = pipeline("text-generation", model=model_name, torch_dtype=torch.bfloat16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

class GenerationRequest(BaseModel):
    messages: list[dict[str, str]]
    max_new_tokens: int = 256
    temperature: float = 0.7
    top_k: int = 50
    top_p: float = 0.95

@app.post("/generate")
async def generate(request: GenerationRequest):
    try:
        prompt = tokenizer.apply_chat_template(request.messages, tokenize=False, add_generation_prompt=True)
        outputs = pipe(prompt, max_new_tokens=request.max_new_tokens, do_sample=True,
                       temperature=request.temperature, top_k=request.top_k, top_p=request.top_p)
        return {"generated_text": outputs[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

