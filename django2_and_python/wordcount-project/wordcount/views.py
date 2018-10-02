import operator

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    context = {'fulltext': fulltext, 'count': len(wordlist), 'sorted_words': sorted_words}
    return render(request, 'count.html', context)


def about(request):
    return render(request, 'about.html')
