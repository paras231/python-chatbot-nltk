print("running python in wsl")
import nltk
from nltk.chat.util import Chat, reflections
from pairs import pairs


def chat():
    print("Hi! I am a chatbot created by Paras Sharma for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()