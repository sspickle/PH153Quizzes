
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

tlo='TLO-mv4'
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

        g=9.8
        newData.update(g=latex_float(g,'N/kg'))

        M = random.randint(15,30)
        newData.update(M=latex_float(M,'kg'))

        R = random.randint(6,12)
        newData.update(R=latex_float(R,'m'))

        frac = random.uniform(0.3,0.7)
        v = round(np.sqrt(frac*g*R),2)

        newData.update(v=latex_float(v,'m/s'))

        Fnet = M*v**2/R
        Fg = M*g
        Fs = Fg - Fnet

        newData.update(Fnet=latex_float(Fnet,'N'))
        newData.update(Fg=latex_float(Fg,'N'))
        newData.update(Fs=latex_float(Fs,'N'))

    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

