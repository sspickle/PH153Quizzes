
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

tlo='TLO-mv5'
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

        m = random.choice([1.67,3.34,4*1.67,7*1.67,12*1.67])*1e-27
        newData.update(m=latex_float(m,"kg"))

        d = random.randint(5,20)/10
        newData.update(d=latex_float(d,"m"))

        c=3e8
        newData.update(c=latex_float(c,"m/s"))

        vfc = random.randint(70,85)/100
        vic = random.randint(86,97)/100
        vi = vic*c
        vf = vfc*c

        newData.update(vi=latex_float(vi,"m/s"))
        newData.update(vf=latex_float(vf,"m/s"))
        newData.update(vic=latex_float(vic))
        newData.update(vfc=latex_float(vfc))

        gamma_i = 1/np.sqrt(1-vic**2)
        gamma_f = 1/np.sqrt(1-vfc**2)
        newData.update(gamma_i=latex_float(gamma_i))
        newData.update(gamma_f=latex_float(gamma_f))

        deltake = (gamma_f-gamma_i)*m*c**2
        newData.update(deltake=latex_float(deltake,"J"))

        FE = -deltake/d
        newData.update(FE=latex_float(FE,"N"))

    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

