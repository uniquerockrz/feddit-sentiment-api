import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data_path = 'data/comments.csv'

from api import get_subfeddits, get_comments

# we first get all the subfeddit IDs
subfeddit_ids = []
subfeddit_names = []

for subfeddit in get_subfeddits()['subfeddits']:
    subfeddit_ids.append(subfeddit['id'])
    subfeddit_names.append(subfeddit['title'])

# now we have to get the comments and store that into a dataframe
def get_all_comments_subfeddit(subfeddit_id):
    start_index = 0
    page_size = 1000
    has_comments = True

    comments_list = []

    while(has_comments):
        comments = get_comments(subfeddit_id=subfeddit_id, skip=start_index, limit=page_size)

        if len(comments['comments']) > 0:
            comments_list = comments_list + comments['comments']
            print(f'Loaded {len(comments_list)} comments in subfeddit id {subfeddit_id}')
            start_index = start_index + page_size
        else:
            has_comments = False
            break

    comment_data_frame = pd.DataFrame(comments_list)
    comment_data_frame['subfeddit_id'] = subfeddit_id
    comment_data_frame['subfeddit_name'] = subfeddit_names[subfeddit_ids.index(subfeddit_id)]

    return comment_data_frame

comment_dataframes = []
for subfeddit_id in subfeddit_ids:
    print(f'Getting Comments for subfeddit id: {subfeddit_id}')
    comment_list_df = get_all_comments_subfeddit(subfeddit_id=subfeddit_id)

    comment_dataframes.append(comment_list_df)

df = pd.concat(comment_dataframes)

print('Running Sentiment Analysis')

def get_comment_sentiment(comment_text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(comment_text)
    sentiment_class = ''
    if scores['compound'] >= 0.05:
        sentiment_class = 'positive'
    elif scores['compound'] > -0.05 and scores['compound'] < 0.05:
        sentiment_class = 'neutral'
    else:
        sentiment_class = 'negative'
    
    return (sentiment_class, scores['compound'])

df[['sentiment_class', 'sentiment_score']] = df['text'].apply(get_comment_sentiment).apply(pd.Series)

df.to_csv(data_path, index=False)