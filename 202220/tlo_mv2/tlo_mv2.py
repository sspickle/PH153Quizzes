
import random
from vpython import vec
import numpy as np
from genlatex import latex_float, latex_vec, TeXData

"""
naming convention. 

tlo: this is the prefix to all the templates, and to the .tex outputs

e.g., if you're working on TLO-3 and this is the third quiz you've
given, you might say "tlo = 'TLO-3v3' and then the template would
be 'TLO-3v1-template.txt' and the .tex files would be:

'TLO-3v1-XX.tex' and
'TLO-3v1-soln-XX.tex' 

where 'XX' would be a quiz version number based on the random numbers
used to create the problem/solution pairs.

"""

tlo='TLO-mv2'
templateFile = tlo + '-template.text' # tex template
quizFilenameTemplate = tlo + '-{:}.tex'
quizSolnFilenameTemplate = tlo + '-soln-{:}.tex'

def getTemplateValues(numSamples, seeds, extra=0):

    answers = []
    data = []

    for i in range(numSamples):
    
        random.seed(seeds[i]) # make these reproducible, but randomish

        newData = {}
        data.append(newData)
        
        newData.update(vnum= str(seeds[i]).zfill(2))
        newData.update(tlo=tlo)

        newAns = dict(dummy='dummy')
        answers.append(newAns)

        l0 = random.randint(10,20)/100
        l2 = random.randint(5,10)/100 + l0
        l1 = random.randint(10,20)/100 + l2

        m = random.randint(40,80)/100
        k = random.randint(80,120)/10
        g = 9.8

        #print(m*g, k*(l1-l0))

        Fs1 = k*(l1-l0)
        Fs2 = k*(l2-l0)
        Fg = m*g
        Fhx = Fs2
        Fhy = m*g - Fs1

        newData.update(m=latex_float(m,"kg"))
        newData.update(g=latex_float(g,"m/s^2"))
        newData.update(l0=latex_float(l0,"m"))
        newData.update(l1=latex_float(l1,"m"))
        newData.update(l2=latex_float(l2,"m"))
        newData.update(k=latex_float(k,"N/m"))
        newData.update(Fs1=latex_float(Fs1,"N"))
        newData.update(Fs2=latex_float(Fs2,"N"))
        newData.update(Fg=latex_float(Fg,"N"))
        newData.update(Fhx=latex_float(Fhx,"N"))
        newData.update(Fhy=latex_float(Fhy,"N"))


        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

