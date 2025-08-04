from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI(title="Laurixy AI", version="1.0")

model_id = "openchat/openchat-3.5-0106"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: PromptRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=300)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": f"{response.strip()}"}