from cgitb import text
from string import punctuation
from turtle import pu
from django.http import Http404
from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,'TextModifier/index.html')


def Analyzer(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    capitalise=request.GET.get('capitalise','off')
    lower=request.GET.get('lower','off')
    newlineremove=request.GET.get('newlineremove','off')
    count=request.GET.get('count','off')
    analyzed=''
    punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc =='on':    
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed +char
        
        context={'purpose' : 'Remove Punctutations' ,'analyzed_text': analyzed}
        return render(request,'TextModifier/Anaylzer.html',context)

    elif capitalise =='on':
        analyzed=djtext.upper() 
        context={'purpose' : 'Convert to Upper Case' ,'analyzed_text': analyzed}
        return render(request,'TextModifier/Anaylzer.html',context)

    elif lower =='on':
        analyzed=djtext.lower() 
        context={'purpose' : 'Convert to Lower Case' ,'analyzed_text': analyzed}
        return render(request,'TextModifier/Anaylzer.html',context) 

    elif newlineremove =='on':
        for char in djtext:
            if char != '\n':
                analyzed=analyzed + char
        context={'purpose' : 'Remove New Line' ,'analyzed_text': analyzed}
        return render(request,'TextModifier/Anaylzer.html',context)


    elif count =='on':
        count=0
        for char in djtext:
            count+=1
        analyzed=count
        context={'purpose' : 'Count Number of Characters' ,'analyzed_text': analyzed}
        return render(request,'TextModifier/Anaylzer.html',context)

    else:
        return HttpResponse('Error')

def About(request):
    return render(request,'TextModifier/About.html')