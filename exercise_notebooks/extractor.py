def extractor_species (file):
    """""
    This takes in the test.fa file and extracts either the first and second fields of species name
    """""
    speciesm = [] #Having,it in a list variable
    with open('../Data/test.fa','r') as testa_o:
        oscar = testa_o.readlines()
        for lines in oscar:
                #print(lines)
                #Extracting lines with only ">"
            if lines.startswith(">"):
                #print(lines)
                    sp_l = lines.split()
                    #print(sp_l)
                    #Extracting  the fields,and getting the spicies name
                    if sp_l[1] == "PREDICTED:":

                        fields = [sp_l [2] , sp_l [3]]
                    else:
                        fields = [sp_l [1] , sp_l [2]]
                    #print(fields)
                    species = fields
                    specie = ' '
                    specie = specie.join(species)
                    #print(specie)
                    #Appending in to a list variable
                    speciesm.append(specie)
        #print(speciesm)
        return(speciesm)
