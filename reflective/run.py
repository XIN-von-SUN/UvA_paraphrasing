from reflective_listening import ReflectiveListening

input_text = "why don't you go outside and do some exercies" #"Today is a bad day, I'm feeling lonely"

reflector = ReflectiveListening()
rephrase = reflector.get_response(input_text)

print('\nOriginal text is: ', input_text, '\n')
for i in rephrase:
    print('Paraphrase is: ', i, '\n')

