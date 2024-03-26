import pandas as pd

class NoSubfeddit(Exception):
    pass

def get_comments_from_dataset(df, subfeddit_id=None, subfeddit_name=None, limit=25, start_date=None, end_date=None, sorted_by_polarity=False, polarity_sort='asc'):
    if (subfeddit_id == None) and (subfeddit_name == None):
        raise NoSubfeddit('No Subfeddit Provided')
    elif subfeddit_name != None:
        df = df[df['subfeddit_name'] == subfeddit_name] 
    else:
        df = df[df['subfeddit_id'] == int(subfeddit_id)]

    if (((start_date == None) and (end_date != None)) or ((start_date != None) and (end_date == None))):
        raise NoSubfeddit('Please provide both start and end date for filtering')

    if (start_date != None) and (end_date != None):
        # find comments in that date range
        df = df[(df['created_at'] >= int(start_date)) & (df['created_at'] <= int(end_date))]
    
    if sorted_by_polarity == False:
        # return the most recent comments by default, with a skip and limit
        return df.sort_values(by=['created_at'], ascending=False)[:limit][['id', 'text', 'sentiment_class', 'sentiment_score']].to_json(orient='records')
    else:
        if polarity_sort == 'asc':
            return df.sort_values(by=['sentiment_score'], ascending=True)[:limit][['id', 'text', 'sentiment_class', 'sentiment_score']].to_json(orient='records')
        else:
            return df.sort_values(by=['sentiment_score'], ascending=False)[:limit][['id', 'text', 'sentiment_class', 'sentiment_score']].to_json(orient='records')