def clean_data(df):
    """
    Perform feature trimming, re-encoding, and engineering for demographics
    data
    
    INPUT: Demographics DataFrame
    OUTPUT: Trimmed and cleaned demographics DataFrame
    """
    
    #############################################################
    #Convert missing value codes into NaN's:
    
    #parsing function
    def list_as_str_into_list (st):
        lst = []
        if st == "[]":
            return np.NaN
        else:
            for x in st.strip("[]").split(","):
                try:
                    lst.append(int(x))
                except:   ### if x is not an integer
                    lst.append(x)
            return(lst)   

    missing_values = feat_info.missing_or_unknown
    missing_values = missing_values.apply(lambda x : list_as_str_into_list(x))
    
    #setting up the dictionary
    
    dict_missing = {x:y for x,y in zip(feat_info.attribute, missing_values)}
    #replacing datacodes for missing data with NaN's 
    df = df.replace(dict_missing, np.NaN)
    
    ##############################################################
    #remove the columns with more than 30% of the missing data:  
    
    
    df = df.drop(['AGER_TYP', 'GEBURTSJAHR', 'TITEL_KZ', 'ALTER_HH', 'KK_KUNDENTYP', 'KBA05_BAUMAX'],axis=1)
    
    
    ##############################################################
    # Removing rows that have lots of missing values:
    
    row_nans = df.isnull().sum(axis = 1)
    num_columns = len(df.columns)
    row_nans = row_nans*100/num_columns
    
    #remove the rows with more than 30% of the missing values
    df = df.drop(row_nans[row_nans>30].index,axis=0) 
    
    ##############################################################
    #dropping columns with mixed values as well
    df = df.drop(["CAMEO_DEU_2015","LP_LEBENSPHASE_FEIN", "LP_LEBENSPHASE_GROB", "WOHNLAGE", "PLZ8_BAUMAX","GEBAEUDETYP"],axis = 1)
    
    
    # re-encoding column values:
    
    # encode some of the categorical features
       
#     lst =  ['CJT_GESAMTTYP', 'FINANZTYP', 'GFK_URLAUBERTYP', 'LP_FAMILIE_FEIN','LP_FAMILIE_GROB',\
#             'LP_STATUS_FEIN', 'LP_STATUS_GROB','NATIONALITAET_KZ', 'SHOPPER_TYP',\
#             'ZABEOTYP', 'GEBAEUDETYP','CAMEO_DEUG_2015']
    
       
    
    
    
    
    # OST_WEST_KZ must be binary with int values
    df["OST_WEST_KZ"] = df["OST_WEST_KZ"].apply(lambda x: 1 if x=="O" else 2)
    
    #1 = Mainstream, 2 = Avantgarde
    movement = {1:1,2:2,3:1,4:2,5:1,6:2,7:2,8:1,9:2,10:1,11:2,12:1,13:2,14:1,15:2}
    decade = {1:4,2:4,3:5,4:5,5:6,6:6,7:6,8:7,9:7,10:8,11:8,12:8,13:8,14:9,15:9}

    df["movement"] = df["PRAEGENDE_JUGENDJAHRE"].apply(lambda x: movement.get(x))
    df["decade"] = df["PRAEGENDE_JUGENDJAHRE"].apply(lambda x: decade.get(x))
    
    df["CAMEO_INTL_2015_wealth"] = df["CAMEO_INTL_2015"].apply(lambda x: x[0] if type(x)==str else 0).astype(int)
    df["CAMEO_INTL_2015_life"] = df["CAMEO_INTL_2015"].apply(lambda x: x[:-1] if type(x)==str else 0).astype(int)
    
    df = df.drop(["PRAEGENDE_JUGENDJAHRE","CAMEO_INTL_2015"],axis = 1)
    
    ########## DUMMY VARIABLES
    
    lst =  ['CJT_GESAMTTYP', 'FINANZTYP', 'GFK_URLAUBERTYP', 'LP_FAMILIE_FEIN','LP_FAMILIE_GROB',\
            'LP_STATUS_FEIN', 'LP_STATUS_GROB','NATIONALITAET_KZ', 'SHOPPER_TYP',\
            'ZABEOTYP','CAMEO_DEUG_2015']
    
    df  = pd.get_dummies(df, columns = lst)
    
    
    # Return the cleaned dataframe
    
    return df
  
  
def main():
    print("preprocessing the arvato dataset")
    
if __name__== "__main__":
    main()
