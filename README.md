# Ollama - Run Large Language Models - DeepSeek

1. Download `ollama` CLI https://github.com/ollama/ollama/releases
2. In One CLI window start server: `ollama serve`
3. In Another CLI window:
4. Download model: `ollama pull deepseek-r1:8b`
5. Run model: `ollama run deepseek-r1:8b`
6. Chat with model.


## CURL
```
curl http://127.0.0.1:11434/api/tags
curl http://127.0.0.1:11434/api/generate -d '{"model": "deepseek-r1:8b", "stream": false, "prompt": "1+1?" }'
```

## Models
* DeepSeek Models: https://ollama.com/library/deepseek-r1
