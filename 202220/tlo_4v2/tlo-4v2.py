
import random
import vpython as vp
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

tlo='TLO-4v2'
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
        
        m1 = random.randint(1,5)*1e32
        m2 = random.randint(4,9)*1e32

        t1 = 1000
        t2 = 9000

        newData.update(t1=latex_float(t1,"s"))
        newData.update(t2=latex_float(t2,"s"))

        while True:
            r1 = vp.vec(random.randint(-5,5),random.randint(-5,5),random.randint(-5,5))*1e10
            r2 = vp.vec(random.randint(-5,5),random.randint(-5,5),random.randint(-5,5))*1e10
            if vp.mag(r1-r2) > 3e10:
                break

        p1 = vp.vec(random.randint(-5,5),random.randint(-5,5),random.randint(-5,5))*1e37
        p2 = vp.vec(random.randint(-5,5),random.randint(-5,5),random.randint(-5,5))*1e37

        r12 = r1-r2
        r12mag = vp.mag(r12)
        r12hat = vp.hat(r12)
        G = 6.67e-11

        Fmag = G*m1*m2/(r12mag**2)
        F = -Fmag*r12hat
        dp = F*(t2-t1)
        p1f = p1 + dp
        r1f = r1 + p1f/m1*t2

        newData.update(G=latex_float(G,"N.m^2/kg^2"))
        newData.update(m1=latex_float(m1,"kg"))
        newData.update(m2=latex_float(m2,"kg"))
        newData.update(p1=latex_vec(p1,"kg.m/s"))
        newData.update(p2=latex_vec(p2,"kg.m/s"))
        newData.update(r1=latex_vec(r1,"m"))
        newData.update(r2=latex_vec(r2,"m"))
        newData.update(r12=latex_vec(r12,"m"))
        newData.update(r12mag=latex_float(r12mag,"m"))
        newData.update(r12hat=latex_vec(r12hat,""))
        newData.update(Fmag=latex_float(Fmag,"N"))
        newData.update(F=latex_vec(F,"N"))
        newData.update(dp=latex_vec(dp,"kg.m/s"))
        newData.update(p1f=latex_vec(p1f,"kg.m/s"))
        newData.update(r1f=latex_vec(r1f,"m"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

