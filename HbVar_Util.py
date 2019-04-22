import sys

def clasifyThalasemia(inputFile , knowledgeFile , outputFile):
    phenotypeDB = {}
    firstLine_Flag = True
    result = []

    # Read knowledge File and create knowledge Dictionary
    with open(knowledgeFile) as knowledge:
        for line in knowledge:
            info = line.split()
            HbVar = info[0]
            HGVS = info[1]
            Common_name = info[2]
            Phenotype = info[3]

            if firstLine_Flag == True:  #Skip header
                info_header = info
                firstLine_Flag=False
                continue

            value = (Phenotype,Common_name,HGVS)
            phenotypeDB.update({HbVar: value})
    knowledge.close()

    # Read input File and map to knowledge dictionary (phenotype mapping)
    with open(inputFile) as input:
        for line in input:

            if line[0]=="#":    # Skip header
                continue

            info = line.split()
            svID = info[0]
            chr = info[1]
            pos = info[2]
            consequence = info[3]
            HbVarID = info[4]

            if HbVarID in phenotypeDB:  #check key exist
                hit = phenotypeDB.get(HbVarID)
                result.append(hit)
    input.close()


    output = open(outputFile,'w')
    firstColumn_Flag=True

    output.write("Phenotype\tCommonName\tHGVS\n")
    for data in result:
        outputFormat = ""
        for subData in data:

            if firstColumn_Flag==True:
                outputFormat = subData
                firstColumn_Flag = False
            else:
                outputFormat = outputFormat + "\t" + subData

        output.write(outputFormat + "\n")
        firstColumn_Flag=True

    output.close()














