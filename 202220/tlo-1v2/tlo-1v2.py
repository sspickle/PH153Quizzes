
import random
import vpython as vp
import numpy as np
from genlatex import latex_float, latex_vec, TeXData
import tikz

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

tlo='TLO-1v2'
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
        
        m = random.randint(3,8)/10
        newData.update(m=latex_float(m,"kg"))
        
        p = vp.vec(random.randint(1,5),random.randint(6,12),random.randint(3,9))
        
        newData.update(p=latex_vec(p,"kg.m/s"))
        Fx = random.choice(range(-80,85,5))
        Fy = random.choice(range(-80,85,5))
        Fz = random.choice(range(-80,85,5))
        
        
        
        F = vp.vec(Fx,Fy,Fz)
        newData.update(F=latex_vec(F,"N"))
        
        t_ms = random.randint(2,7)
        t = t_ms/1000
        
        newData.update(t_ms=latex_float(t_ms,"ms"))
        newData.update(t=latex_float(t,"s"))
        
        dp = F*t
        pf = p + dp
        newData.update(dp=latex_vec(dp,"kg.m/s"))
        newData.update(pf=latex_vec(pf,"kg.m/s"))

        
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

