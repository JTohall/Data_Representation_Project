
from flask import Flask, jsonify, request, abort
from moviesDAO import moviesDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/movies')
def getAll():
    results = moviesDAO.getAll()
    return jsonify(results)


# View all titles
@app.route('/movies', methods=['GET'])
def get_all_products():
    titles = moviesdao.getAll()
    return jsonify(products)


@app.route('/movies/<int:id>')
def findById(id):
    foundBook = moviesDAO.findByID(id)
    
    return jsonify()


@app.route('/movies', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    movies = {
        "movie": request.json['title'],
        "rating": request.json['rating'],
        "year": request.json['year'],
    }
    values =(['movie'],movies['rating'],movies['year'])
    newId = moviesDAO.create(values)
    title['id'] = newId
    return jsonify(title)


@app.route('/movies/<int:id>', methods=['PUT'])
def update(id):
    foundmovie = moviesDAO.findByID(id)
    if not foundmovie:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'movie' in reqJson and type(reqJson['movie']) is not int:
        abort(400)

    if 'title' in reqJson:
        foundmovie['title'] = reqJson['title']
    if 'rating' in reqJson:
        foundmovie['rating'] = reqJson['rating']
    if 'year' in reqJson:
        foundmovie['year'] = reqJson['year']
    values = (foundmovie['movie'],foundmovie['rating'],foundmovie['year'])
    movieDAO.update(values)
    
    return jsonify(foundmovie)
        

@app.route('/movies/<int:id>' , methods=['DELETE'])
def delete(id):
    moviesDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)
    