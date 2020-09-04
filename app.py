from flask import (Flask,jsonify,abort)

app = Flask(__name__)

movies = [
    {
        'id':1,
        'title': 'Dil Bechara',
        'review': 'An adaptation of the bestselling novel The Fault in Our Stars, it tells the story of Kizie (Sanghi) and Manny (Rajput), who are young, suffering from cancer, and about to fall in love.'
        },
    {
        'id':2,
        'title': 'Frozen 2',
        'review': 'It tells the story of a fearless princess who sets off on a journey alongside a rugged iceman,his loyal reindeer, and a naive snowman to find her estranged sister, whose icy powers have inadvertently trapped their kingdom in eternal winter.'
    },   
    {
        'id':3,
        'title': 'French Biriyani',
        'review':'The film is about a three day trip between an auto driver from Shivaji Nagar (played by Danish Sait) and a French emigrant (played by Sal Yusuf) during the latters visit to Bengaluru'

        },
    {
        'id':4,
        'title': 'Joker',
        'review':'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime. This path brings him face-to-face with his alter-ego: the Joker.'    
    
    }
    ]
@app.route('/movies',methods=['GET'])
def movies():
    return jsonify({'movies':movies})


@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = [movie for movie in movies if movie['id'] == movie_id]
    if len(movie) == 0:
        abort(404)
    return jsonify({'movie': movie[0]})


if __name__ == '__main__':
    app.run(debug=True)
