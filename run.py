import os
import pickle
import random
import subprocess

import settings
import tools

if __name__ == "__main__":
    if not os.path.exists("../Messages/{}/Pretty/complete-pretty.json".format(settings.user_id)):
        subprocess.call("python ../FBMessageScraper/dumper.py {} 2000".format(settings.user_id).split())
        tools.get_conversation_history("Messages/{}/complete.json".format(settings.user_id), "../DATA/raw_data.txt")
        tools.clean_input_text("../DATA/raw_data.txt", "../DATA/clean_data.txt")
        tools.generate_corpus("../DATA/clean_data.txt", "../DATA/corpus.p", settings.markov_length)

    corpus = pickle.load(open("../DATA/corpus.p", 'rb'))

    #get text from conversation
    text = "Waterloo is a good school with software and food and sleep."

    keywords = tools.get_keywords(text)
    keyword = tools.get_start_word(keywords, corpus)

    print tools.generate_markov_message(corpus, start_word=keyword, max_length=random.randrange(0, 30))
