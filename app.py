from flask import Flask
from database import get_news,get_idrow

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/api/v1/news", methods=["GET"])
def news():
    
    data_news = get_news()

    return data_news

@app.route("/api/v1/news/<id>")
def get_idnews(id):
    
    data_news = get_idrow(id)

    return data_news


if __name__=="__main__":
    app.run(debug=True)



