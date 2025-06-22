# agents/summarize_agent.py

from transformers import pipeline, PegasusTokenizer, PegasusForConditionalGeneration
import torch

print("[summarize_agent] Loading Pegasus model and tokenizer...")
model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def summarize_text(text):
    print("[summarize_agent] Summarizing using free Pegasus model...")

    try:
        # Tokenize and truncate to max_length
        inputs = tokenizer(
            text,
            truncation=True,
            padding="longest",
            max_length=512,
            return_tensors="pt"
        ).to(device)

        summary_ids = model.generate(inputs["input_ids"], max_length=100, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary

    except Exception as e:
        print(f"[summarize_agent] ❌ Error during summarization: {e}")
        return text[:300] + "..." if len(text) > 300 else text
