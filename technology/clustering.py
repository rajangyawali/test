import re
from string import punctuation
import nltk


from .models import TechNews, TelcoNews, GadgetNews, GlobalNews

def minhash(input_question, compare_question):
    score = 0.0
    shingles = lambda s: set(s[i:i+3] for i in range(len(s)-2))
    jaccard_distance = lambda seta, setb: len(seta & setb)/float(len(seta | setb))
    try:
        score = jaccard_distance(shingles(input_question), shingles(compare_question))
    except ZeroDivisionError:
        print('ZeroDivisionError')

    return score

def cluster(newsclass):
    if newsclass == 'technews':
        news = TechNews.objects.all()
    if newsclass == 'telconews':
        news = TelcoNews.objects.all()
    if newsclass == 'gadgetnews':
        news = GadgetNews.objects.all()
    if newsclass == 'globalnews':
        news = GlobalNews.objects.all()
    headlines = []
    headlines_cleaned = []

    for n in news:
        headlines.append(n.title)

    text_lower = [text.lower() for text in headlines]
    text_letters = [''.join(c for c in s if c not in punctuation) for s in text_lower]
    text_final = [re.sub(r'[^A-Za-z0-9]+', ' ', x) for x in text_letters]

    for text in text_final:
        headlines_cleaned.append(text)
    
    
    stop_words = {'whom', 'some', 'shouldn', 'will', 'why', 'other', 'doesn', "it's", 'until', 'has', 'any', 'wasn', 'mightn', 'do', 'don', 'off', "aren't", 'its', "that'll", 'further', 're', 'during', 'ma', 'up', 'ourselves', 'now', 'then', "hasn't", "mightn't", 't', "haven't", "mustn't", 'those', 'was', 'before', 'couldn', "don't", 'i', "weren't", "won't", 'itself', 'having', 'can', 'between', 'be', 'both', "wasn't", 'being', 'him', "you've", 'mustn', "should've", 'been', 'when', 'only', 'under', 'these', 'on', "you'll", 'me', 'too', "couldn't", 'his', 'because', 'their', 'below', "doesn't", 'or', 'theirs', 'o', 'that', "shouldn't", 'you', "she's", 'such', 'yours', 'more', 'over', 'd', 'for', 'so', 'haven', 'we', 'above', 'this', 'from', 'own', 'your', 'y', "hadn't", "isn't", 'while', 'and', 'weren', 'doing', 'her', 'once', "shan't", 'but', 'wouldn', 'didn', 'by', 'it', 'same', 'she', 's', 'he', 'through', 'aren', 'hadn', 'did', 'most', 'my', 'few', 'does', 'where', 'am', "you're", 'isn', "wouldn't", 'than', 'who', 'should', 'needn', 'an', 'of', 'about', 'after', 'our', 've', 'have', 'yourselves', 'had', 'were', 'again', 'against', 'no', 'out', 'himself', 'in', 'm', 'very', 'just', "didn't", 'if', 'with', 'herself', 'as', 'into', 'is', "needn't", 'hers', 'are', 'down', 'there', 'the', 'a', 'nor', 'themselves', 'here', 'they', 'how', 'll', 'ain', 'myself', 'shan', 'which', 'at', 'ours', "you'd", 'all', 'each', 'won', 'not', 'yourself', 'hasn', 'what', 'to', 'them'}
    custom_words = ['nepal', 'officially', 'smartphones', 'mobiles', 'internet', 'launched', 'announced', 'camera', 'battery', 'mp', 'gb', 'mah', 'setup', 'price', 'rs', 'updated']
    for i in custom_words:
        stop_words.add(i)
    headlines_cleaned = [' '.join([word for word in x.split() if word not in stop_words]) for x in headlines_cleaned]

    final_headlines = []
    
    for i in range(len(headlines)):
        clustered_headlines = []
        clustered_headlines.append(headlines[i])
        for j in range(len(headlines)):
            if i == j:
                continue
            score = minhash(headlines_cleaned[i], headlines_cleaned[j])
            if score > 0.2:
                clustered_headlines.append(headlines[j])
        final_headlines.append(clustered_headlines)
    return final_headlines

    

