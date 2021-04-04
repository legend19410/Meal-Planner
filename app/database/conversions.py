
def cup_to_ml(cup):
    return cup * 237

def gill_to_ml(gill):
    return gill * 118

def teaspoon_to_ml(teaspoon):
    return teaspoon * 4.9

def tablespoon_to_ml(tablespoon):
    return tablespoon * 14.7868

def pint_to_ml(pint):
    return pint * 473.176

def quart_to_ml(quart):
    return quart * 946.353

def gallon_to_ml(gallon):
    return gallon * 3785.41

def ml_to_ml(ml):
    return ml

def litre_to_ml(litre):
    return litre * 1000

def ounce_to_g(ounce):
    return ounce * 28.3495

def lb_to_g(lb):
    return lb * 453.592

def g_to_g(g):
    return g
def mg_to_g(mg):
    return mg * 0.001

def dl_to_ml(dl):
    return dl * 100

def convert(units,quantity,cal_ml, cal_g):

    if units == 'cup':
        return cal_ml * cup_to_ml(quantity)
    if units == 'gill':
        return cal_ml * gill_to_ml(quantity)
    if units == 'teaspoon':
        return cal_ml * teaspoon_to_ml(quantity)
    if units == 'tablespoon':
        return cal_ml * tablespoon_to_ml(quantity)
    if units == 'ounce':
        return cal_g * ounce_to_g(quantity)
    if units == 'pint':
        return cal_ml * pint_to_ml(quantity)
    if units == 'quart':
        return cal_ml * quart_to_ml(quantity)
    if units == 'cup':
        return cal_ml * cup_to_ml(quantity)
    if units == 'gallon':
        return cal_ml * gallon_to_ml(quantity)
    if units == 'ml':
        return cal_ml * ml_to_ml(quantity)
    if units == 'litre':
        return cal_ml * litre_to_ml(quantity)
    if units == 'lb':
        return cal_g * lb_to_g(quantity)
    if units == 'mg':
        return cal_g * mg_to_g(quantity)
    if units == 'g':
        return cal_g * g_to_g(quantity)
    if units == 'dl':
        return cal_g * dl_to_ml(quantity)
