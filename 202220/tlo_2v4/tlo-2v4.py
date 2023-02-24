
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

tlo='TLO-2v4'
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
        
        v_i = vp.vec(random.randint(20,40)/10,-random.randint(40,80)/10,0)
        m = random.randint(25,40)/100
        v_f = vp.vec(v_i.x, -v_i.y, v_i.z)
        p_i = m*v_i
        p_f = m*v_f
        dt = random.randint(15,25)/10000
        dp = p_f - p_i

        newData.update(v_i=latex_vec(v_i,"m/s"))
        newData.update(v_f=latex_vec(v_f,"m/s"))
        newData.update(m=latex_float(m,"kg"))
        newData.update(p_i=latex_vec(p_i,"kg.m/s"))
        newData.update(p_f=latex_vec(p_f,"kg.m/s"))
        newData.update(dt=latex_float(dt,"s"))

        F = dp/dt
        newData.update(dp=latex_vec(dp,"kg.m/s"))
        newData.update(F=latex_vec(F,"N"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

