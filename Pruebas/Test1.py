import openai
openai.api_key = "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"
while True:
    prompt = input("\nIntroduce una pregunta: ")
    if prompt == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003", prompt= prompt, max_tokens= 2048)
    print(completion.choices[0].text)