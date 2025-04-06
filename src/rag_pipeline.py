from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# Initialisieren des Tokenizers und Modells
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

# Beispiel-Frage
question = "What is the capital of France?"

# Tokenisieren der Frage
inputs = tokenizer(question, return_tensors="pt")

# Generieren der Antwort
generated_ids = model.generate(inputs["input_ids"])
answer = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(f"Question: {question}")
print(f"Answer: {answer}")