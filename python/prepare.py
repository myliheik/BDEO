import os
import pandas as pd

statdir = '/u/58/wittkes3/unix/Documents/bdeo/stats/18'
csvname = '/u/58/wittkes3/unix/Documents/bdeo/s1_VVVH_18.csv'
attributes = '/media/wittkes3/satdat6/bigdataeo_LUKE/original/feb20/reference-zone1-2017.csv'


datelist=[]
fulldf=None

for x in os.listdir(statdir):
    xpa = os.path.join(statdir,x)
    df = pd.read_csv(xpa)
    #print(df.head())
    meandf = df[['parcelID','mean']]
    #mediandf = df[['parcelID','median']]
    year = x.split('_')[2][:4]
    pol = x.split('_')[4]
    meandf.rename(columns={'parcelID':'parcelID','mean':'mean_'+ pol},inplace=True)
    print(meandf.head())
    meandf['parcelID'] = meandf['parcelID'].apply(lambda x: "{}{}{}".format(year,'_', x))
    #print(newdf)
    #datelist.append(date)
    if fulldf is None:
        fulldf = meandf
    else:
        fulldf= pd.merge(fulldf,meandf, on='parcelID')
    
    #sorteddf = fulldf.reindex(sorted(fulldf.columns), axis=1)
    #sorteddf.rename(columns={'0ID':'PlotID'}, inplace=True)
print(fulldf)


dfa = pd.read_csv(attributes)

dfa['parcelID'] = dfa['parcelID'].apply(lambda x: "{}{}{}".format(year,'_', x))

print(dfa)

dfauv = pd.merge(fulldf,dfa, on='parcelID' )

print(dfauv)

dfauv.to_csv(csvname)
