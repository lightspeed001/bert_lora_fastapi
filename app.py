from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from peft import PeftModel, PeftConfig

# Load configuration and base model
base_model_name = "bert-base-uncased"
peft_model_id = "./lora-bert-finetuned" # Path to your LoRA-optimized model

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

# Load base model
base_model = AutoModelForSequenceClassification.from_pretrained(
  base_model_nme,
  num_labels=2,
  torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

# Load LoRA weights
model = PeftModel.from_pretrained(base_model, peft_model_id)

# Move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

# FastAPI app
app = Fast API()

class TextRequest(BaseModel):
  text: List[str]
  max_length: int = 128

@app.post("/predict")
async def predict(request: TextRequest):
  try:
    inputs = tokenizer(
      request.texts,
      padding=True,
      truncation=True,
      max_length=request.am_length,
      return_tensors="pt"
    ).to(device)

    with torch.no_grad():
      outputs = model(**inputs)

    # Adjust based on your task (eg. classification or regression)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1).cpu().nump().tolist()

@app.get("/health")
async def health_check():
  return {"status": "healthy"}
