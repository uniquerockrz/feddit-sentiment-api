"""This module contains the function needed for the working of the REST API"""

#pylint: disable=too-many-arguments
class NoSubfeddit(Exception):
    """The No SUbfeeddit Exception Class"""

def get_comments_from_dataset(df, subfeddit_id=None, subfeddit_name=None, limit=25,
        start_date=None, end_date=None, sorted_by_polarity=False,
        polarity_sort='asc'):
    """Function for querying comments from the dataset"""
    if (subfeddit_id is None) and (subfeddit_name is None):
        raise NoSubfeddit('No Subfeddit Provided')
    if subfeddit_name is not None:
        df = df[df['subfeddit_name'] == subfeddit_name]
    else:
        df = df[df['subfeddit_id'] == int(subfeddit_id)]

    if (((start_date is None) and (end_date is not None))
        or ((start_date is not None) and (end_date is None))):
        raise NoSubfeddit('Please provide both start and end date for filtering')

    if (start_date is not None) and (end_date is not None):
        # find comments in that date range
        df = df[(df['created_at'] >= int(start_date)) & (df['created_at'] <= int(end_date))]

    if sorted_by_polarity is False:
        # return the most recent comments by default, with a skip and limit
        return df.sort_values(by=['created_at'], ascending=False)[:limit][['id', 'text',
                'sentiment_class', 'sentiment_score']].to_json(orient='records')

    if polarity_sort == 'asc':
        return df.sort_values(by=['sentiment_score'], ascending=True)[:limit][['id', 'text',
            'sentiment_class', 'sentiment_score']].to_json(orient='records')

    return df.sort_values(by=['sentiment_score'], ascending=False)[:limit][['id', 'text',
        'sentiment_class', 'sentiment_score']].to_json(orient='records')
