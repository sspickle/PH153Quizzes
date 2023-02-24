
import random
import vpython as vp
import numpy as np
from genlatex import latex_float, latex_vec, TeXData
import mendeleev as md

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

tlo='TLO-6v1'
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

        elements = [md.Al, md.Au, md.Ag, md.Cu, md.Pt, md.Pd, md.Pb, md.Sn, md.Zn,
            md.Na, md.Mg, md.K, md.Be, md.Mn, md.Fe, md.Ni, md.Ti]

        element = elements[i%len(elements)]

        dens_gpcc=element.density
        dens_kgm3=dens_gpcc*1000
        atomic_wt=element.atomic_weight
        NA = 6.022e23
        ma = atomic_wt/(1000*NA)

        newData.update(element=element.name)
        newData.update(density_gpcc=latex_float(dens_gpcc,"g/cm^3"))
        newData.update(density_kgm3=latex_float(dens_kgm3,"kg/m^3"))
        newData.update(mpermole=latex_float(atomic_wt,"g/mol"))
        newData.update(NA=latex_float(NA))
        newData.update(ma=latex_float(ma,"kg/atom"))
        d = (ma/dens_kgm3)**(1/3)
        newData.update(d=latex_float(d,"m"))
        r = d/2
        newData.update(r=latex_float(r,"m"))
        
    promptData = {'data': data}
    promptDataSet = TeXData('prompt', quizFilenameTemplate, promptData )
    answerData = {'data':data, 'ans':answers}
    answerDataSet = TeXData('answers', quizSolnFilenameTemplate, answerData)
    
    return dict( templateFile = templateFile,
                       dataSets = [promptDataSet, answerDataSet])

