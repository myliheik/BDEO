import sys

attributes = sys.argv[1]
    dfa = pd.read_csv(attributes)
    dfa = dfa.astype({'parcelID': 'str'})
    #each parcelID gets its year added to the parcelID (year_parcelID)
    dfa['parcelID'] = dfa['parcelID'].apply(lambda x: "{}{}{}".format(year,'_', x))
    #print(dfa.columns)
    #print(dfa.head(5))
    dfauv = pd.merge(fulldf,dfa, on='parcelID' )
    #print(dfauv.head(5))