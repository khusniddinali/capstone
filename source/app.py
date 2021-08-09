import os
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from database.models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


############## Create app ###############
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    ################# Retrieve movies ################
    @app.route('/movies')
    def retrieve_movies():
        movies = Movie.query.all()
        current_movies = [movie.format() for movie in movies]
        if current_movies is None:
            abort(404)

        return jsonify({
            'success': True,
            'movies': current_movies
        }), 200


    @app.route('/movies/<int:movie_id>')
    def retireve_movie_(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        
        return jsonify({
            'success': True,
            'movie': movie
        }), 200

    
    ################ Retrieve actors #################
    @app.route('/actors')
    def retrieve_actors():
        actors = Actor.query.all()
        current_actors = [actor.format() for actor in actors]
        if current_actors is None:
            abort(404)

        return jsonify({
            'success': True,
            'actors': current_actors
        }), 200


    @app.route('/actors/<int:actor_id>')
    def retireve_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        
        return jsonify({
            'success': True,
            'movie': actor
        }), 200        
    

    ################ Delete movie #####################
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            'success': True,
            'deleted': movie_id
        }), 200


    ################# Delete Actor ###################
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'deleted': actor_id
        })


    ################### Create movies #####################
    @app.route('/movies/add', methods=['POST'])
    def create_new_movie():
        body = request.get_json()
        if body is None:
            abort(400)
        new_title = body['title']
        release_date = body['release_date']

        new_movie = Movie(title = new_title, release_date = release_date)

        new_movie.insert()

        return jsonify({
            'success': True,
            'movies': Movie.query.all()
        }), 200


    #################### Create Actor #####################
    @app.route('/actors/add', methods=['POST'])
    def create_new_actor():
        body = request.get_json()
        if body is None:
            abort(400)
        new_name = body['name']
        age = body['age']
        gender = body['gender']

        new_actor = Actor(name = new_name, age = age, gender = gender)

        new_actor.insert()

        return jsonify({
            'success': True,
            'movies': Actor.query.all()
        }), 200


    ################### Update Movie ######################
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        data = request.get_json()
        if 'title' in data:
            movie.title = data['title']
        if 'release_date' in data:
            movie.release_date = data['release_date']
        
        movie.update()

        return jsonify({
            'success': True,
            'movie': movie_id
        })


    #################### Update Actor ######################
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actor(actor_id):
        data = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        if 'name' in data:
            actor.name = data['name']
        if 'age' in data:
            actor.age = data['age']
        if 'gender' in data:
            actor.gender = data['gender']
        
        actor.update()

        return jsonify({
            'success': True,
            'actor': actor_id
        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()