import random
import torch
import json
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Medix"

def get_response(msg): #Application implementation
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()] #Decides the input tag with prediction

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
        
    
    return "I don't understand, sorry."



# print("Ask me any First Aid questions! type 'quit' to exit")

# while True:
    # sentence = input('\n You: ')
    # if sentence.lower() == "quit":
    #     break

    # sentence = tokenize(sentence)
    # X = bag_of_words(sentence, all_words)
    # X = X.reshape(1, X.shape[0])
    # X = torch.from_numpy(X)

    # output = model(X)
    # _, predicted = torch.max(output, dim=1)
    # tag = tags[predicted.item()] #Decides the input tag with prediction

    # probs = torch.softmax(output, dim=1)
    # prob = probs[0][predicted.item()]

    # if prob.item() > 0.75:
    #     for intent in intents["intents"]:
    #         if tag == intent["tag"]:
    #             print(f"\n {bot_name}: {random.choice(intent['responses'])}")
        
    # else:
    #     print(f"\n {bot_name}: I don't understand")

