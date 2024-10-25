import math
# This function calculated the bare module cost of a blender.
# The different types that can be selected are: 'kneader', 'ribbon', and 'rotary'
# minSize should be reported in m3 and equal to the volume of the material being blended plus an emptiness factor
# cepciCurrent is the present value of the Chemical Engineering Plant Cost Index (CEPCI)

def blenderCapCost(blenderType, minSize, cepciCurrent):
    config = blenderType                # Sets the blender type equal to the configuration variable
    size = minSize*1.2                  # Adds 20% more volume to the blender minimum volume to account for mixing material
    kneaderMin = 0.14                   # Minimum size for the kneader blender correlation
    kneaderMax = 3                      # Maximum size for the kneader blender correlation
    ribbonMin = 0.7                     # Minimum size for the ribbon and rotary blender correlation
    ribbonMax = 11                      # Maximum size for the ribbon and rotary blender correlation
    cepci2001 = 394                     # CEPCI value in 2001 when the initial capital cost correlation was developed

    # General cost equation = log10(Cost) = k1 + k2*log10(Size) + k3*(log10(Size))^2
    if config == 'kneader':             # Conditional for kneader blender types
        k1 = 5.0141                     # k1 variable for kneader blender type
        k2 = 0.5867                     # k2 variable for kneader blender type
        k3 = 0.3224                     # k3 variable for kneader blender type
        if size > kneaderMax:           # Conditional to determine how many blenders are needed to accommoate full size requirements
            count = math.ceil(size/kneaderMax) 
            avgSize = math.ceil(size/count)
        elif size < kneaderMin:         # Returns error if size of blender is too small for this correlation
             print('The size of this blender is too small for this correlation.')
             raise ValueError
        else:
            count = 1                   # If size requirement is between Min and Max values, only 1 blender is needed
            avgSize = size              # When 1 blender is required, it can be the full size
    elif config == 'ribbon' or config == 'rotary':  # Conditional for ribbon and rotary blender types
            k1 = 4.1366                 # k1 for ribbon and rotary blender types
            k2 = 0.5072                 # k2 for ribbon and rotary blender types
            k3 = 0.0070                 # k3 for ribbon and rotary blender types
            if size > ribbonMax:        # Conditional to determine how many blenders are needed to accommodate full size requirements    
                count = math.ceil(size/ribbonMax)
                avgSize = math.ceil(size/count)
            elif size < ribbonMin:      # Returns error if size of blender is too small for this correlation
             print('The size of this blender is too small for this correlation.')
             raise ValueError
            else:
                count = 1               # If size requirement is between Min and Max values, only 1 blender is needed
                avgSize = size          # When 1 blender is required, it can be the full size
    else:
        raise TypeError
    
    # Initial Cost Equation
    cost = 10**(k1 + k2*math.log10(avgSize) + k3*(math.log10(avgSize))**2)*(cepciCurrent/cepci2001)*count
    # Bare Module Cost Factor for Blenders (kneaders, ribbons, and rotary are all the same value)
    bareModuleFactor = 1.12
    # Caluclate Bare Module Cost
    bareModuleCost = cost*bareModuleFactor

    print(f'This application requires {count} blenders of {round(avgSize,1)} m3, each costing ${round(cost/count,2)}, totalling ${round(cost,2)}')
    # Return count for # of blenders, aggregate equipment cost, and aggregate bare module cost
    return [count, cost, bareModuleCost]