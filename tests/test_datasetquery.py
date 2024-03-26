import pandas as pd
import os
import sys
import pytest
import json

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from lib.datasetquery import get_comments_from_dataset

df = pd.read_csv('tests/dataset_sample.csv')

def test_without_subfeddit_id():
    with pytest.raises(Exception) as e:
        get_comments_from_dataset(df)
    assert str(e.value) == 'No Subfeddit Provided'

def test_without_subfeddit_name():
    with pytest.raises(Exception) as e:
        get_comments_from_dataset(df)
    assert str(e.value) == 'No Subfeddit Provided'

resp_json_subfeddit_id = '[{"id":1118,"text":"Thumbs up. Good work. Love it.","sentiment_class":"positive","sentiment_score":0.7964},{"id":1407,"text":"Good work. Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.872},{"id":4166,"text":"Love it. Well done! Proud of you. Love it.","sentiment_class":"positive","sentiment_score":0.9312},{"id":5145,"text":"Love it. Proud of you. Like it a lot! Good work.","sentiment_class":"positive","sentiment_score":0.9184},{"id":6361,"text":"Awesome. Like it a lot! Love it. It looks great!","sentiment_class":"positive","sentiment_score":0.9476},{"id":6960,"text":"Awesome. Enjoy! Awesome. Enjoy!","sentiment_class":"positive","sentiment_score":0.9449},{"id":7466,"text":"Well done! Awesome. Luckily you did it. Love it.","sentiment_class":"positive","sentiment_score":0.9324},{"id":9154,"text":"Looks decent. Awesome. What you did was right. Luckily you did it.","sentiment_class":"positive","sentiment_score":0.8126},{"id":9401,"text":"Looks decent. Looks decent. Awesome. Looks decent.","sentiment_class":"positive","sentiment_score":0.6249},{"id":10417,"text":"Looks decent. Enjoy! Well done! It looks great!","sentiment_class":"positive","sentiment_score":0.8827},{"id":11752,"text":"What you did was right. Good work. Thumbs up. Well done!","sentiment_class":"positive","sentiment_score":0.6476},{"id":12863,"text":"Thumbs up. Looks decent. Awesome. Proud of you.","sentiment_class":"positive","sentiment_score":0.802},{"id":13163,"text":"Thumbs up. Thumbs up. Well done! Proud of you.","sentiment_class":"positive","sentiment_score":0.6696},{"id":14985,"text":"Like it a lot! Thumbs up. Enjoy! Good work.","sentiment_class":"positive","sentiment_score":0.8475},{"id":15087,"text":"Like it a lot! Like it a lot! Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.9115},{"id":15580,"text":"Like it a lot! Enjoy! Love it. Well done!","sentiment_class":"positive","sentiment_score":0.9165},{"id":17910,"text":"Luckily you did it. Well done! Well done! What you did was right.","sentiment_class":"positive","sentiment_score":0.7955},{"id":19766,"text":"Proud of you. Looks decent. Awesome. Love it.","sentiment_class":"positive","sentiment_score":0.9081},{"id":21836,"text":"Enjoy! Thumbs up. Thumbs up. Like it a lot!","sentiment_class":"positive","sentiment_score":0.7418},{"id":22273,"text":"Enjoy! Luckily you did it. Like it a lot! It looks great!","sentiment_class":"positive","sentiment_score":0.9322},{"id":23450,"text":"I don\'t like it at all. Don\'t do it. Hate it!","sentiment_class":"positive","sentiment_score":0.2914},{"id":24201,"text":"You have done it in a wrong way. Come on dude. I don\'t like it at all. You have done it in a wrong way.","sentiment_class":"negative","sentiment_score":-0.8079},{"id":24256,"text":"You have done it in a wrong way. Why are you doing this? Leave it alone. Why are you doing this?","sentiment_class":"negative","sentiment_score":-0.6917},{"id":24695,"text":"You have done it in a wrong way. Hate it! Are you insane? Come on dude.","sentiment_class":"negative","sentiment_score":-0.8687},{"id":28224,"text":"Come on dude. Come on dude. Hate it! Walk away!","sentiment_class":"negative","sentiment_score":-0.6467}]'

def test_with_subfeddit_id():
    resp_json = get_comments_from_dataset(df, subfeddit_id=1)
    assert resp_json == resp_json_subfeddit_id

def test_with_subfeddit_name():
    resp_json = get_comments_from_dataset(df, subfeddit_name='Dummy Topic 1')
    assert resp_json == resp_json_subfeddit_id

def test_check_limit_25():
    resp_json = get_comments_from_dataset(df, subfeddit_name='Dummy Topic 1')
    assert len(json.loads(resp_json)) == 25

resp_json_date_filter = '[{"id":5145,"text":"Love it. Proud of you. Like it a lot! Good work.","sentiment_class":"positive","sentiment_score":0.9184},{"id":6361,"text":"Awesome. Like it a lot! Love it. It looks great!","sentiment_class":"positive","sentiment_score":0.9476},{"id":6960,"text":"Awesome. Enjoy! Awesome. Enjoy!","sentiment_class":"positive","sentiment_score":0.9449},{"id":7466,"text":"Well done! Awesome. Luckily you did it. Love it.","sentiment_class":"positive","sentiment_score":0.9324},{"id":9154,"text":"Looks decent. Awesome. What you did was right. Luckily you did it.","sentiment_class":"positive","sentiment_score":0.8126},{"id":9401,"text":"Looks decent. Looks decent. Awesome. Looks decent.","sentiment_class":"positive","sentiment_score":0.6249},{"id":10417,"text":"Looks decent. Enjoy! Well done! It looks great!","sentiment_class":"positive","sentiment_score":0.8827},{"id":11752,"text":"What you did was right. Good work. Thumbs up. Well done!","sentiment_class":"positive","sentiment_score":0.6476},{"id":12863,"text":"Thumbs up. Looks decent. Awesome. Proud of you.","sentiment_class":"positive","sentiment_score":0.802},{"id":13163,"text":"Thumbs up. Thumbs up. Well done! Proud of you.","sentiment_class":"positive","sentiment_score":0.6696},{"id":14985,"text":"Like it a lot! Thumbs up. Enjoy! Good work.","sentiment_class":"positive","sentiment_score":0.8475},{"id":15087,"text":"Like it a lot! Like it a lot! Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.9115},{"id":15580,"text":"Like it a lot! Enjoy! Love it. Well done!","sentiment_class":"positive","sentiment_score":0.9165},{"id":17910,"text":"Luckily you did it. Well done! Well done! What you did was right.","sentiment_class":"positive","sentiment_score":0.7955},{"id":19766,"text":"Proud of you. Looks decent. Awesome. Love it.","sentiment_class":"positive","sentiment_score":0.9081},{"id":21836,"text":"Enjoy! Thumbs up. Thumbs up. Like it a lot!","sentiment_class":"positive","sentiment_score":0.7418},{"id":22273,"text":"Enjoy! Luckily you did it. Like it a lot! It looks great!","sentiment_class":"positive","sentiment_score":0.9322}]'

def test_date_filter():
    resp_json = get_comments_from_dataset(df, subfeddit_id=1, start_date=1631270048, end_date=1692930847)
    assert resp_json == resp_json_date_filter

resp_polarity_sort_asc = '[{"id":24695,"text":"You have done it in a wrong way. Hate it! Are you insane? Come on dude.","sentiment_class":"negative","sentiment_score":-0.8687},{"id":24201,"text":"You have done it in a wrong way. Come on dude. I don\'t like it at all. You have done it in a wrong way.","sentiment_class":"negative","sentiment_score":-0.8079},{"id":32620,"text":"Nooooooo! Nooooooo! Nooooooo! Hate it!","sentiment_class":"negative","sentiment_score":-0.7067},{"id":31561,"text":"I don\'t like it at all. Nooooooo! Walk away! You have done it in a wrong way.","sentiment_class":"negative","sentiment_score":-0.6998},{"id":24256,"text":"You have done it in a wrong way. Why are you doing this? Leave it alone. Why are you doing this?","sentiment_class":"negative","sentiment_score":-0.6917},{"id":28224,"text":"Come on dude. Come on dude. Hate it! Walk away!","sentiment_class":"negative","sentiment_score":-0.6467},{"id":31566,"text":"I don\'t like it at all. Nooooooo! Walk away! Why are you doing this?","sentiment_class":"negative","sentiment_score":-0.4007},{"id":28514,"text":"Come on dude. I don\'t like it at all. Nooooooo! Walk away!","sentiment_class":"negative","sentiment_score":-0.4007},{"id":23450,"text":"I don\'t like it at all. Don\'t do it. Hate it!","sentiment_class":"positive","sentiment_score":0.2914},{"id":9401,"text":"Looks decent. Looks decent. Awesome. Looks decent.","sentiment_class":"positive","sentiment_score":0.6249},{"id":11752,"text":"What you did was right. Good work. Thumbs up. Well done!","sentiment_class":"positive","sentiment_score":0.6476},{"id":13163,"text":"Thumbs up. Thumbs up. Well done! Proud of you.","sentiment_class":"positive","sentiment_score":0.6696},{"id":21836,"text":"Enjoy! Thumbs up. Thumbs up. Like it a lot!","sentiment_class":"positive","sentiment_score":0.7418},{"id":17910,"text":"Luckily you did it. Well done! Well done! What you did was right.","sentiment_class":"positive","sentiment_score":0.7955},{"id":1118,"text":"Thumbs up. Good work. Love it.","sentiment_class":"positive","sentiment_score":0.7964},{"id":12863,"text":"Thumbs up. Looks decent. Awesome. Proud of you.","sentiment_class":"positive","sentiment_score":0.802},{"id":9154,"text":"Looks decent. Awesome. What you did was right. Luckily you did it.","sentiment_class":"positive","sentiment_score":0.8126},{"id":14985,"text":"Like it a lot! Thumbs up. Enjoy! Good work.","sentiment_class":"positive","sentiment_score":0.8475},{"id":1407,"text":"Good work. Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.872},{"id":10417,"text":"Looks decent. Enjoy! Well done! It looks great!","sentiment_class":"positive","sentiment_score":0.8827},{"id":19766,"text":"Proud of you. Looks decent. Awesome. Love it.","sentiment_class":"positive","sentiment_score":0.9081},{"id":15087,"text":"Like it a lot! Like it a lot! Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.9115},{"id":15580,"text":"Like it a lot! Enjoy! Love it. Well done!","sentiment_class":"positive","sentiment_score":0.9165},{"id":5145,"text":"Love it. Proud of you. Like it a lot! Good work.","sentiment_class":"positive","sentiment_score":0.9184},{"id":4166,"text":"Love it. Well done! Proud of you. Love it.","sentiment_class":"positive","sentiment_score":0.9312}]'

def test_polarity_sort_asc():
    resp_json = get_comments_from_dataset(df, subfeddit_id=1, sorted_by_polarity=True)
    assert resp_json == resp_polarity_sort_asc

resp_polarity_sort_desc = '[{"id":6361,"text":"Awesome. Like it a lot! Love it. It looks great!","sentiment_class":"positive","sentiment_score":0.9476},{"id":6960,"text":"Awesome. Enjoy! Awesome. Enjoy!","sentiment_class":"positive","sentiment_score":0.9449},{"id":7466,"text":"Well done! Awesome. Luckily you did it. Love it.","sentiment_class":"positive","sentiment_score":0.9324},{"id":22273,"text":"Enjoy! Luckily you did it. Like it a lot! It looks great!","sentiment_class":"positive","sentiment_score":0.9322},{"id":4166,"text":"Love it. Well done! Proud of you. Love it.","sentiment_class":"positive","sentiment_score":0.9312},{"id":5145,"text":"Love it. Proud of you. Like it a lot! Good work.","sentiment_class":"positive","sentiment_score":0.9184},{"id":15580,"text":"Like it a lot! Enjoy! Love it. Well done!","sentiment_class":"positive","sentiment_score":0.9165},{"id":15087,"text":"Like it a lot! Like it a lot! Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.9115},{"id":19766,"text":"Proud of you. Looks decent. Awesome. Love it.","sentiment_class":"positive","sentiment_score":0.9081},{"id":10417,"text":"Looks decent. Enjoy! Well done! It looks great!","sentiment_class":"positive","sentiment_score":0.8827},{"id":1407,"text":"Good work. Good work. Awesome.","sentiment_class":"positive","sentiment_score":0.872},{"id":14985,"text":"Like it a lot! Thumbs up. Enjoy! Good work.","sentiment_class":"positive","sentiment_score":0.8475},{"id":9154,"text":"Looks decent. Awesome. What you did was right. Luckily you did it.","sentiment_class":"positive","sentiment_score":0.8126},{"id":12863,"text":"Thumbs up. Looks decent. Awesome. Proud of you.","sentiment_class":"positive","sentiment_score":0.802},{"id":1118,"text":"Thumbs up. Good work. Love it.","sentiment_class":"positive","sentiment_score":0.7964},{"id":17910,"text":"Luckily you did it. Well done! Well done! What you did was right.","sentiment_class":"positive","sentiment_score":0.7955},{"id":21836,"text":"Enjoy! Thumbs up. Thumbs up. Like it a lot!","sentiment_class":"positive","sentiment_score":0.7418},{"id":13163,"text":"Thumbs up. Thumbs up. Well done! Proud of you.","sentiment_class":"positive","sentiment_score":0.6696},{"id":11752,"text":"What you did was right. Good work. Thumbs up. Well done!","sentiment_class":"positive","sentiment_score":0.6476},{"id":9401,"text":"Looks decent. Looks decent. Awesome. Looks decent.","sentiment_class":"positive","sentiment_score":0.6249},{"id":23450,"text":"I don\'t like it at all. Don\'t do it. Hate it!","sentiment_class":"positive","sentiment_score":0.2914},{"id":28514,"text":"Come on dude. I don\'t like it at all. Nooooooo! Walk away!","sentiment_class":"negative","sentiment_score":-0.4007},{"id":31566,"text":"I don\'t like it at all. Nooooooo! Walk away! Why are you doing this?","sentiment_class":"negative","sentiment_score":-0.4007},{"id":28224,"text":"Come on dude. Come on dude. Hate it! Walk away!","sentiment_class":"negative","sentiment_score":-0.6467},{"id":24256,"text":"You have done it in a wrong way. Why are you doing this? Leave it alone. Why are you doing this?","sentiment_class":"negative","sentiment_score":-0.6917}]'

def test_polarity_sort_asc():
    resp_json = get_comments_from_dataset(df, subfeddit_id=1, sorted_by_polarity=True, polarity_sort='desc')
    assert resp_json == resp_polarity_sort_desc