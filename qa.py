from transformers import pipeline
import os

# prompt for question
q = input("What is your question? ")

# Load the model
model = pipeline('question-answering')
# Load the data
data = ""
with open("data/_all_data.txt", "r") as f:
    data = f.read()
    f.close()

next_q = True
while next_q:
    # Get the answer
    answer = model(question=q, context=data)
    print(f"Question: {q}")
    print(f"Answer: '{answer['answer']}' with score {answer['score']}")
    # Prompt for another question
    next_q = input("Do you have another question? (y/n) ")
    if next_q == "y":
        q = input("What is your question? ")
    else:
        next_q = False
        print("Goodbye!")
