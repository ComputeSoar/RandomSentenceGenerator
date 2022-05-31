question = str(input("For En 1, For De 0: "))

if question == "1":

    exec(open("RandomSentenceEn.py").read())

if question == "0":

    exec(open("RandomSentenceDe.py").read())
