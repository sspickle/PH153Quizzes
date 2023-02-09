
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

tlo='TLO-4v1'
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
        
        mp = random.randint(1,5)*1e24
        ms = random.randint(3,9)*1e30

        while True:
            rp = vp.vec(random.randint(-5,5),random.randint(-5,5),0)*1e11
            rs = vp.vec(random.randint(-5,5),random.randint(-5,5),0)*1e11
            if vp.mag(rp-rs) > 3e11:
                break

        rsp = rp-rs
        rspmag = vp.mag(rsp)
        rsphat = vp.hat(rsp)
        G = 6.67e-11

        Fmag = G*mp*ms/(rspmag**2)
        F = -Fmag*rsphat

        newData.update(G=latex_float(G,"N m^2/kg^2"))
        newData.update(mp=latex_float(mp,"kg"))
        newData.update(ms=latex_float(ms,"kg"))
        newData.update(rp=latex_vec(rp,"m"))
        newData.update(rs=latex_vec(rs,"m"))
        newData.update(rsp=latex_vec(rsp,"m"))
        newData.update(rspmag=latex_float(rspmag,"m"))
        newData.update(rsphat=latex_vec(rsphat,""))
        newData.update(Fmag=latex_float(Fmag,"N"))
        newData.update(F=latex_vec(F,"N"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

