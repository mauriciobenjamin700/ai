from ollama import ChatResponse, chat


order = '''
'''

input = '''
'''

response: ChatResponse = chat(
    model='qwen:110b',
    messages=[
        {
            'role': 'user',
            'content': order + input
        }
    ],
    keep_alive='30m', # Mantém o modelo na memória por 30 minutos
    think=True
)

text = response.message.content

with open('output2.txt', 'w') as f:
    f.write(text)