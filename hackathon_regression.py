# Hackathon 
# Openness, Consciensciousness,  Extraversion, Agreeableness, Neuroticisim
#           O    C      E      A      N
# Input data as list of percentages
rahul = [-6, 5, -8, -4, -1]

#function ocean score + f(x) ==> score(Socially active, Mentally active, Mental health, physical health)

#min (score) ==> to intervene category

#SA = (E * (0.35 + 0.12 + 0.39 + 0.18 + 0.17 + 0.21 + 0.2 + 0.47) + A * (0.16 + 0.17 + 0.28) + N * (-0.13 - 0.23 - 0.18)) / 14
#MA = (O * (0.35 + 0.16 + 0.43) + E * (0.39 + 0.2) +  A * (0.09 )) / 6
#MH = (O * (-0.2) + C * (-0.08 + 0.25) + E * (0.39 + 0.19 + 0.37 + 0.13 + 0.21) + N * (-0.54 - 0.63 -0.24 -0.31  - 0.31 - 0.19 -0.09 -0.1 -0.18 -0.32)) / 18
#PH = (O * (-0.02) + C * (0.08 + 0.06) + (A * (0.04))) / 4
    




def ocean_to_intervention(ocean_list):
    
    """ Takes input in the form of list of integers of OCEAN values and predicts scores for Social Activity (SA), Mental Activity (MA), Mental Health (MH), Physical Health (PH). """
    
    O = ocean_list[0]
    C = ocean_list[1]
    E = ocean_list[2]
    A = ocean_list[3]
    N = ocean_list[4]
    
    SA = (O * 0      + C * 0      + E * (2.09) + A * (0.61)  + N * (-0.54)) / 14
    MA = (O * (0.94) + C * 0      + E * (0.59) + A * (0.09 ) + N * 0)  / 6
    MH = (O * (-0.2) + C * (0.17) + E * (1.29) + A * 0       + N * (-2.91)) / 18
    PH = (O * (-0.02)+ C * (0.14) + E * 0      + A * (0.04) +  N * 0) / 4
    
    traits = [SA, MA, MH, PH]
    temp = min(traits)
    aes = [round(n, 3) for n in traits]
    
    for i in range(len(traits)):
        if traits[i] == temp:
            to_correct = ["SA", "MA", "MH", "PH"][i]
    
    return((to_correct, aes))


ocean_to_intervention(rahul)