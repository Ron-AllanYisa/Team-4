
def dictionary_of_metrics(items):
    """This function returns the metrics as a dictionary. The metrics include:
    mean, median, maximum, minimum, standard deviation, variance

    Parameters:
        items(list):list of intergers used to create a dictionary of metrics

    Returns:
        dictionary of metrics rounded to two decimal place
    
    """


    mean=np.mean(items)
    median=np.median(items)
    items.sort()
    small=min(items)
    big=max(items)
    s=[]
    for i in items:
        s.append((i-mean)**2)
    var=sum(s)/(len(items)-1)
    deviate=(var)**(1/2)
    
    dictionary={'mean':round(mean,2),
               'median':round(median,2),
               'var': round(var,2),
               'std': round(deviate,2),
               'min': round(small,2),
               'max':round(big,2)}
    return dictionary

def five_num_summary(items):
    """This function returns the five number summary as a dictionary. The five number summary includes:
    , median, maximum, minimum, quartile 1 and 3
    
    Parameters:
        items(list):list of intergers used to create a dictionary of five number summary
    
    Returns:
        returns a dictionary of five number summary rounded to two decimal place
    """

    median=np.median(items)
    small=min(items)
    big=max(items)
    list2=sorted(items)
    firstquart= np.quantile(list2,0.25)
    lastquart= np.quantile(list2,0.75)
    
    dictionary={'max':round(big,2),
               'median':round(median,2),
               'min': round(small,2),
               'q1':round(firstquart,2),
               'q3':round(lastquart,2)}
        
    return dictionary


def date_parser(dates):
    """The function takes in the date in one format and converts it to another format
    
    Parameters:
        dates(list):The list to be parsed
    
    Returns:
    The list of the parsed dates
    
    """

    truth=[]
    for i in dates:
        prince=i.split(' ')
        truth.append(prince[0])
    return truth

def extract_municipality_hashtags(df):
    """Returns a dataframe with an added column of extracted hashtags from each tweet and an added column
    of the municipality mentioned in each tweet
    
    Parameters:
        df(DataFrame):DataFrame which contains the hashtags and municipalities to be identified
    
    Returns: 
        The DataFrame with added columns of the identified hashtags and municipalities
    
    """

    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane'}
    
    
    df["municipality"] = df["Tweets"].apply(lambda df: ','.join([municipality_dict[key] for key in df.split() if key in municipality_dict.keys()]))
    df["hashtags"] = df["Tweets"].apply(lambda df: [x.lower() for x in df.split() if x[0]=='#'])
    df['hashtags'] = df['hashtags'].apply(lambda x: np.nan if x == [] else x)
    df['municipality']=df['municipality'].apply(lambda x: np.nan if x == '' else x)
  
    return df

def number_of_tweets_per_day(df):
    """The function counts the number of tweets for a specific date in the dataframe 
    
    Parameters:
        df(DataFrame): The DataFrame which contains the tweets(and the dates) to be counted
    
    Returns:
        DataFrame with the column of dates as well as the number of the tweets on that date
    
    """

   #checking the no. of tweets a day
    df['Date']=df['Date'].apply(lambda x : x.split(' ')[0])
    nasty=df.drop(columns=['Date'],axis=1)
    bass=nasty.groupby(df['Date']).count()
    
    return bass

    

def stop_words_remover(df):
    
    """ The function removes stop words from tweets and returns those tweets as a list without the stop words
    
    Parameters:
        df(DataFrame): The Dataframe of tweets which will have it's stop words removed
        
    Returns:
        df(DataFrame): Returns a DataFrame with an added column of a list of tweets with the stop words removed
    
    """
def stop_words_remover(df):
    
    df['Without Stop Words'] = df['Tweets'].apply(str.split)
    for i in range(len(df)):
        df['Without Stop Words'][i] = [item.lower() for item in df['Without Stop Words'][i] 
                                       if item.lower() not in stop_words_dict['stopwords']]
    return df