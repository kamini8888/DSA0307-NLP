from transformers import MarianMTModel, MarianTokenizer

# Load English to French translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Translate English text to French
english_text = "Hello, how are you?"
input_ids = tokenizer.encode(english_text, return_tensors="pt")
output_ids = model.generate(input_ids)
french_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print(f"English: {english_text}")
print(f"French: {french_text}")
