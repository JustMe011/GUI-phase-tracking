################ PARSER ################

import numexpr as ne
import numpy as np
import re
from scipy import constants as consts
import unicodedata as ud
# x variable is initialized to None (NoneType)
# When I call parse_x I update the value of x to the actual domain array
# After I've evaluated the function I set x again to None in order to
# remember to change the x array for the new function

constDict = {
    #'x1' : None,
    #'x2' : None,
    #'x3' : None,
    'x' : None,
    '^' : '**',
    'pi' : consts.pi,
    'e' : consts.e,
    'phi' : consts.golden,
    'eps_0' : consts.epsilon_0,
    'mu_0' : consts.mu_0,
    'g' : consts.G
}

def parseFuncs(eqList):

    # I'll read x arrays from the dictionary


    func = list()
    for equation in eqList:
        equation = adjustEquation(equation)
        funcToEvaluate = None
        if _isNum(equation):
            funcToEvaluate = [equation for i in range(len(constDict['x']))]
            func.append(funcToEvaluate)
        else:
            funcToEvaluate = equation
            func.append(ne.evaluate(funcToEvaluate,constDict))
    return func

def adjustEquation(eq):

    #future implementations
    # Insert a product sign between a number and a variable (ax -> a*x)
    # NB: for the moment it works for ax, but not for xa)

    clean_eq = re.sub(r"((?:\d+)|(?:[a-zA-Z]\w*\(\w+\)))((?:[a-zA-Z]\w*)|\()", r"\1*\2", eq)

    return clean_eq

def parseX(samplingTimes, samplesNum):
    # It accepts 3 sample times
    samplesNum = int(samplesNum)
    samplingTimes = float(samplingTimes)

    x = np.zeros(samplesNum)
    for i_num in range(samplesNum):
        x[i_num] = float(i_num*samplingTimes)
    constDict['x'] = x
    return x

def _isNum(eqStr):
    try:
        float(eqStr)
        return True
    except ValueError:
        pass

    try:
        ud.numeric(eqStr)
        return True
    except (ValueError, TypeError):
        pass
    return False   
