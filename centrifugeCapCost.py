import math
# This function calculated the bare module cost of a centrifuge.
# The different types that can be selected are: 'auto batch separator', 'centrifugal separator', 'oscillating screen' and 'bowl with motor'
# minDia should be reported in m and equal to the minimum diameter of the centrifuge
# cepciCurrent is the present value of the Chemical Engineering Plant Cost Index (CEPCI)

def centrifugeCapCost(centerfugeType, minDia, cepciCurrent):
    config = centerfugeType
    cepci2001 = 294

    # Size Requirements
    autoBatchMin = 0.5
    autoBatchMax = 1.7
    centrifugalMin = 0.5
    centrifugalMax = 1
    oscillatingScreenMin = 0.5
    oscillatingScreenMax = 1.1
    bowlMotorMin = 0.5
    bowlMotorMax = 2

    if config == 'auto batch separator':
        k1 = 4.7681
        k2 = 0.9740
        k3 = 0.0240
        bareModuleFactor = 1.57
        if minDia > autoBatchMax:
            if centrifugalMax > autoBatchMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a centrifugal configuration.')
            elif oscillatingScreenMax > autoBatchMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an oscillating screen configuration.')
            elif bowlMotorMax > autoBatchMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a bowl and motor configuration.')
            else:
               print('The size of this centrifuge is too big for this correlation.') 
        if minDia < autoBatchMin:
            print('The size of this centrifuge is too small for this correlation.')
    elif config == 'centrifugal separator':
        k1 = 4.3612
        k2 = 0.8764
        k3 = -0.0049
        bareModuleFactor = 1.57
        if minDia > centrifugalMax:
            if autoBatchMax > centrifugalMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an auto batch separator configuration.')
            elif oscillatingScreenMax > centrifugalMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an oscillating screen configuration.')
            elif bowlMotorMax > centrifugalMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a bowl and motor configuration.')
            else:
               print('The size of this centrifuge is too big for this correlation.')
        if minDia < centrifugalMin:
            print('The size of this centrifuge is too small for this correlation.')
    elif config == 'oscillating screen':
        k1 = 4.8600
        k2 = 0.3340
        k3 = 0.1063
        bareModuleFactor = 1.57
        if minDia > oscillatingScreenMax:
            if autoBatchMax > oscillatingScreenMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an auto batch separator configuration.')
            elif centrifugalMax > oscillatingScreenMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a centrifugal configuration.')
            elif bowlMotorMax > oscillatingScreenMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a bowl and motor configuration.')
            else:
               print('The size of this centrifuge is too big for this correlation.')
        if minDia < oscillatingScreenMin:
            print('The size of this centrifuge is too small for this correlation.')
    elif config == 'bowl with motor':
        k1 = 4.9697
        k2 = 1.1689
        k3 = 0.0038
        bareModuleFactor = 1.27
        if minDia > bowlMotorMax:
            if autoBatchMax > bowlMotorMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an auto batch separator configuration.')
            elif centrifugalMax > bowlMotorMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using a centrifugal configuration.')
            elif oscillatingScreenMax > bowlMotorMax:
                print('The size of this centrifuge is too large for an auto batch separator correlation, try using an oscillating screen configuration.')
            else:
               print('The size of this centrifuge is too big for this correlation.')
        if minDia < bowlMotorMin:
            print('The size of this centrifuge is too small for this correlation.')
    else:
        raise TypeError
    
    # Initial Cost Equation
    cost = 10**(k1 + k2*math.log10(minDia) + k3*(math.log10(minDia))**2)*(cepciCurrent/cepci2001)
    # Caluclate Bare Module Cost
    bareModuleCost = cost*bareModuleFactor

    print(f'The equipment cost of the {config} centrifuge with a diameter of {minDia} m is ${round(cost,2)}, and has a bare module cost of ${round(bareModuleCost,2)}')

    return bareModuleCost