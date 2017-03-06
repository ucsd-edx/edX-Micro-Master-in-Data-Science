from math import log10,ceil
import re
import pandas as pd
import os.path
from glob import glob
from time import ctime

def combineLogs(t_start,t_end,log_dir='/private/tmp', Summary_file='/private/tmp/log.csv'):

    ## Find common digits to t_start,t_end
    for i in range(100):
        if int(t_start/(10**i))==int(t_end/(10**i)):
            time_pref = str(int(t_start/(10**i)))
            break

    file_list=glob(log_dir+'/*'+str(time_pref)+'*.csv')

    # Extract file contact into a dict of dataframes
    pattern=re.compile(log_dir+r'/.*\d+\.(.+)\.csv')
    df={}
    for filename in file_list:
        match=pattern.match(filename)
        if match:
            feature_name=match.group(1)
            df_tmp=pd.read_csv(filename,index_col='t')
            # remove rows with times outside the range
            df[feature_name]=df_tmp[(df_tmp.index>=t_start) & (df_tmp.index<=t_end)]

    ## prepend the name of the table to name of each column
    for key in df.keys():
        newcol=[key+"."+col for col in df[key].columns]
        df[key].columns=newcol

    ## join all of the DFs using time as key.
    combined_df=df[df.keys()[0]]
    for key in df.keys()[1:]:
        combined_df=combined_df.join(df[key])
    columns=sorted(combined_df.columns)
    combined_df=combined_df[columns]

    return combined_df
