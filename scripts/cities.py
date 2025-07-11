from ollama import chat, ChatResponse


order = 'Transforme em json com cada campo configurado dos endereços abaixo:'

output = '''
endereço = {
    numero: ""
    endereço: ""
    bairro
....
}
'''

input = '''
'''

response: ChatResponse = chat(
    model='qwen:110b',
    messages=[
        {
            'role': 'user',
            'content': order + input + output
        }
    ]
)

text = response.message.content

with open('output.txt', 'w') as f:
    f.write(text)