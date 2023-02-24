
import random
from vpython import vec, mag
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

tlo='TLO-1v3'
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

        dirs = {
            "+x":vec(1,0,0),
            "-x":vec(-1,0,0),
            "+y":vec(0,1,0),
            "-y":vec(0,-1,0),
            "+z":vec(0,0,1),
            "-z":vec(0,0,-1)
        }

        dir = random.choice(list(dirs.keys()))
        pmag = random.randint(8,15)
        F = vec(random.randint(-5,5),random.randint(-5,5),0)
        dt = random.randint(10,20)/100

        newData.update(dir=dir)
        newData.update(pmag=latex_float(pmag,"kg.m/s"))
        newData.update(Ftex = latex_vec(F,"N"), Fvec = F)
        newData.update(dt=latex_float(dt,"sec"))

        p = pmag*dirs[dir]
        dp = F*dt
        pnew = p + dp
        newData.update(p=latex_vec(p))
        newData.update(dp=latex_vec(dp))
        newData.update(pnew=latex_vec(pnew))
        newData.update(pnewx=latex_float(pnew.x,"kg.m/s"))
        newData.update(pnewy=latex_float(pnew.y,"kg.m/s"))
        newData.update(pnewz=latex_float(pnew.z,"kg.m/s"))
        newData.update(pmagnew=latex_float(mag(pnew),"kg.m/s"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

