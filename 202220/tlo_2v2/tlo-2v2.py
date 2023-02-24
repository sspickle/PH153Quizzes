
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

tlo='TLO-2v2'
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

        while True:
            pfz = random.randint(-5,5)
            if pfz != 0:
                break

        pfz = pfz*1e-24
        p_i = vp.vec(random.randint(15,40)*1e-24,0,0)
        p_f = vp.vec(p_i.x,0,pfz)
        dt = random.randint(1,4)*1e-11
        dp = p_f - p_i
        F = dp/dt
        newData.update(p_i=latex_vec(p_i,"kg.m/s"))
        newData.update(p_f=latex_vec(p_f,"kg.m/s"))
        newData.update(dt=latex_float(dt,"s"))
        newData.update(dp=latex_vec(dp,"kg.m/s"))
        newData.update(F=latex_vec(F,"N"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

