# Introduction

This is the code for the Feddit (fake reddit data) API with the sentiment scores and classification.

## Accessing The API

The API has been deployed on Render and can be accessed using this URL [feddit-sentiment-api.onrender.com](https://feddit-sentiment-api.onrender.com/).

The features supported are as follows:

* Get comments from a certain subfeddit by ID: [feddit-sentiment-api.onrender.com/comments?subfeddit_id=2](http://feddit-sentiment-api.onrender.com/comments?subfeddit_id=2)
* Get comments from a certain subfeddit by subfeddit name: [feddit-sentiment-api.onrender.com/comments?subfeddit_name=Dummy%20Topic%201](http://feddit-sentiment-api.onrender.com/comments?subfeddit_name=Dummy%20Topic%201)
* Filter by start and end date: [feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&start_date=1631270048&end_date=1692930847](http://feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&start_date=1631270048&end_date=1692930847)
* Sort comments by polarity: [feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&sorted_by_polarity=true](http://feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&sorted_by_polarity=true)
* Sort comments by polarity in descending order: [feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&sorted_by_polarity=true&polarity_sort=desc](http://feddit-sentiment-api.onrender.com/comments?subfeddit_id=2&sorted_by_polarity=true&polarity_sort=desc)

## How To Run

* Clone the repo
* Install the requirements `pip3 install -r requirements.txt`
* Run the flask APP `flask run`

## Using Docker

You can also use Docker to run the app. The Dockerfile is already provided

```bash
docker build --tag python-docker .
docker run -d -p 5000:5000 python-docker
```

## Architecture

* The comments from the feddit API is stored in a CSV file inside the `data` folder.
* The flask API reads the file and does the operations as required. 

## Notebook and Docs

You can see the `Notebooks` folder to get an idea of how to use the functions. Docstrings have been provided for each of the functions and modules.

## Testing And Linting

To run unit tests, run

```bash
python3 -m pytest
```

For linting

```bash
python3 -m pylint lib
```

Same has been implemented in the GitHub workflows. 