
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

tlo='TLO-mv1'
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

        theta_deg = random.randint(20,40)
        m = random.randint(10,30)/10
        g = 9.8
        cottheta = 1/np.tan(np.radians(theta_deg))
        Fs = m*g*cottheta

        theta_rad = np.radians(theta_deg)
        newData.update(theta_deg=latex_float(theta_deg,"degrees"))
        newData.update(theta_rad=latex_float(theta_rad,"radians"))
        newData.update(m=latex_float(m,"kg"))
        newData.update(g=latex_float(g,"m/s^2"))
        newData.update(cottheta=latex_float(cottheta,""))
        newData.update(Fs=latex_float(Fs,"N"))

        

        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

