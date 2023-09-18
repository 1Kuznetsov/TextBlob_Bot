from textblob import TextBlob
from textblob import Word
import commands as com
from textblob.classifiers import NaiveBayesClassifier
from googletrans import Translator


translator = Translator()
set_com = [(com.TRANSLATE, com.DETECT_LANG),
           (com.SENTENCES, com.SINGULARIZE, com.PLURALIZE, com.LEMMATIZE),
           (com.SYNSETS, com.DEFINITIONS, com.CORRECT, com.SPELLCHECK),
           (com.COUNT, com.PARSE, com.NGRAMS, com.START_END_INDEX),
           (com.CLASSIFY, com.MAXI, com.PROB, com.ACCURACY),
           (com.TAGS, com.NOUN_PHRASES, com.SENTIMENT, com.WORDS)]


def dialogue(t):
    for k in range(len(set_com[t])):
        print(f"{k+1}: ", set_com[t][k])
    if t == 0:
        return input(com.QUESTION_FIRST)
    elif t == 5:
        return input(com.LAST_SET_COMS)
    else:
        return input(com.QUESTION)


def first_coms(reply):
    text = input(com.TEXT)
    if reply == '1':
        lang = input(com.LANG)
        print(translator.translate(text, dest=lang).text)
    if reply == '2':
        print(translator.detect(text).text)


def second_coms(reply):
    text = TextBlob(input(com.TEXT))
    if reply == '1':
        print(text.sentences)
    if reply == '2':
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            print(text.words[number_word-1].singularize())
        else:
            print(Word(str(text)).singularize())
    if reply == '3':
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            print(text.words[number_word-1].pluralize())
        else:
            print(Word(str(text)).pluralize())
    if reply == '4':
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            w = text.words[number_word-1]
            verb = input(com.VERB)
            if verb.lower() == 'yes':
                print(Word(w).lemmatize('v'))
            else:
                print(Word(w).lemmatize())
        else:
            verb = input(com.VERB)
            if verb.lower() == 'yes':
                print(Word(text).lemmatize('v'))
            else:
                print(Word(text).lemmatize())


def third_coms(reply):
    text = TextBlob(input(com.TEXT))
    if reply == '1':
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            print(text.words[number_word-1].synsets)
        else:
            print(Word(str(text)).synsets)
    if reply == '2':
        transl_def = input(com.TRANSL_DEF)
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            res = text.words[number_word-1].definitions
            print(res)
            if transl_def != '0':
                for item in res:
                    print(translator.translate(item, dest=transl_def).text)
        else:
            res = Word(str(text)).definitions
            print(res)
            if transl_def != '0':
                for item in res:
                    print(translator.translate(item, dest=transl_def).text)
    if reply == '3':
        print(text.correct())
    if reply == '4':
        if len(text.words) > 1:
            number_word = int(input(com.NUM))
            print(text.words[number_word - 1].spellcheck())
        else:
            print(Word(str(text)).spellcheck())


def fourth_coms(reply):
    text = TextBlob(input(com.TEXT))
    if reply == '1':
        word = Word(input(com.WORD))
        sensitivity = input(com.SENSITIVITY)
        if sensitivity.lower() == 'yes':
            print(text.words.count(word, case_sensitive=True))
        else:
            print(text.words.count(word))
    if reply == '2':
        print(text.parse())
    if reply == '3':
        n = int(input(com.AMOUNT))
        print(text.ngrams(n))
    if reply == '4':
        for s in text.sentences:
            print(s)
            print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))


def fifth_coms(reply):
    amount_train_data = int(input(com.AMOUNT_TRAIN_DATA))
    train = []
    for i in range(amount_train_data):
        train.append(input(com.TRAIN).split(','))
    cl = NaiveBayesClassifier(train)
    if reply == '1':
        text = TextBlob(input(com.TEXT))
        if len(text.sentences) > 1:
            for s in text.sentences:
                print(s)
                print(s.classify())
        else:
            print(text)
            print(cl.classify(str(text)))
    if reply == '2':
        text = TextBlob(input(com.TEXT))
        prob_dist = cl.prob_classify(text)
        print(prob_dist.max())
    if reply == '3':
        text = TextBlob(input(com.TEXT))
        mark = input(com.MARK)
        prob_dist = cl.prob_classify(text)
        print(round(prob_dist.prob(mark), 2))
    if reply == '4':
        test = input(com.TEST)
        print(cl.accuracy(test))


def sixth_coms(reply):

    text = TextBlob(input(com.TEXT))
    if reply == '1':
        print(text.tags)
    if reply == '2':
        print(text.noun_phrases)
    if reply == '3':
        print(text.sentiment)
    if reply == '4':
        print(text.words)
