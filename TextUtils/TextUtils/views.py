from typing import Dict, Any

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def about(request):
    return HttpResponse("about Saimu")


def analyzetext(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    capital = request.POST.get('capital', 'off')
    newline_remover = request.POST.get('newline_remover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    character_count = request.POST.get('character_count', 'off')
    operation = ""
    if removepunc == "on":
        analyzed_text = ""
        punctuation = '''!.:,;'!-/(){}[]@#$%^&*<>?"\,'''
        for i in djtext:
            if i not in punctuation:
                analyzed_text = analyzed_text + i
        djtext = analyzed_text
        operation += " Remove Punctuation +"
        #params = {'operation': 'Remove Punctuation', 'analyzed_text': djtext}
        #return render(request, 'output2.html', params)
    if capital == "on":
        djtext = djtext.upper()
        operation += " Upper Case +"
        #params = {'operation': 'Capitalize text', 'analyzed_text': djtext}
        #return render(request, 'output2.html', params)
    if newline_remover == "on":
        analyzed_text =''
        for i in djtext:
            if i != '\n' and i!= '\r':
                analyzed_text = analyzed_text + i
                print(analyzed_text)
            else:
                analyzed_text = analyzed_text + " "
        djtext = analyzed_text
        operation += " newline remover +"
        #params = {'operation': 'Newline remover', 'analyzed_text': djtext}
        #return render(request, 'output2.html', params)
    if extra_space_remover == "on":
        analyzed_text = ""
        for index, i in enumerate(djtext):
            if index < len(djtext) - 1 and not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed_text = analyzed_text + i
                print(analyzed_text)
        djtext = analyzed_text
        operation += " extra space remover +"
        #params = {'operation': 'Extra space remover', 'analyzed_text': djtext}
        #return render(request, 'output2.html', params)
    if character_count == "on":
        length = len(djtext)
        operation += " Character Count "
        djtext += str(length)
        #params = {'operation': 'Character Count', 'analyzed_text': str(length)}
        #eturn render(request, 'output2.html', params)
    params = {'operation': operation,'analyzed_text': djtext}
    return render(request, 'output2.html', params)
    #else:
        #return HttpResponse(djtext)
