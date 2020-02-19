import pandas as pd
import numpy as np

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}


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