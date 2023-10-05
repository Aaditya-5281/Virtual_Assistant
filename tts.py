import requests

# Your API key
api_key = "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"

# API endpoint URL
url = "https://api.openai.com/v1/engines/davinci/completions"

# Input text for the AI model
input_text = "HI"

# Send a request to the OpenAI API
response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "prompt": input_text,
        "max_tokens": 50  # Adjust as needed
    }
)

# Get the AI model's response
if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['text'])
else:
    print("Error:", response.status_code)
