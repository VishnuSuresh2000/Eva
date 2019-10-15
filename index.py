la=[]
import nltk
sen="light. youtube"

tok=nltk.word_tokenize(sen)
print(tok)
print(nltk.pos_tag(tokens=tok))

try:
    from googlesearch import search
except ImportError:
    print("error")

for j in search(sen,tld='co.in',num=10,stop=10):
    la.append(j)
print(la)