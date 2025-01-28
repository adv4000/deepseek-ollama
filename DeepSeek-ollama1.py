# ------------------------------------------------------------------------------
# Request to Ollama API Server with GenAI model via ollama package
#
# Version      Date              Name                 Info
# 1.0          28-January-2025   Denis Astahov        Initial Version
#
# ------------------------------------------------------------------------------
import ollama

client = ollama.Client()

model = "deepseek-r1:8b"
prompt = "Capital city of Canada?"

model_reply = client.generate(model=model, prompt=prompt)

print("Response:")
print(model_reply.response)
