from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wordcount(request):
    fulltext = request.GET['fulltext']
    worldlist = fulltext.split()
    word_dict = {}
    
    for word in worldlist:
        if word in word_dict:
            #increase
            word_dict[word] += 1
        else:
            #add to dict
            word_dict[word] = 1
    # სორტირებას აკეთებს რიცხვების და იწყებს დიდიდან პატარისკენ
    sorted_words = sorted(word_dict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext': fulltext, 'count':len(worldlist), 'sorted_words': sorted_words})

    