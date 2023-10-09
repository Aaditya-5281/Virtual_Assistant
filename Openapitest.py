import openai
from api_secrets import API_KEY
openai.api_key= "ncTWQkShOcAFVU8LADejT3BlbkFJdiie8AOg6T8SU6PZEeDe"

prompt="what is graphql"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=64
)

print(response)