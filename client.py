from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello! Tell me a fun fact."
        }
    ],
    temperature=0.7,
    max_tokens=100
)

print(response.choices[0].message.content)
