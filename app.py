from flask import Flask, request, Response
import pandas as pd
import json

from lib.datasetquery import get_comments_from_dataset

app = Flask(__name__)

df = pd.read_csv('data/comments.csv')

@app.route('/')
def hello_world():
    return dict({'success': True })

@app.get('/comments')
def comments():
    args = request.args.to_dict()
    
    try:
        comments_json = get_comments_from_dataset(df=df, **args)
        return json.loads(comments_json)
    except Exception as e:
        return Response(
            json.dumps({'error': str(e)}),
            mimetype='application/json',
            status=400,
        )

