import os
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

from .database.models import setup_db, Movie, Actor
from .auth.auth import AuthError, requires_auth


########### Paginate pages #############
item_per_page = 10


def paginate_page(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1)*item_per_page
    end = start + item_per_page
    items = [item.format() for item in selection]
    cur_items = items[start:end]
    return cur_items


############## Create app ###############
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    ####### Home page #######

    @app.route('/')
    def home_page():
        return jsonify({
            'success': True,
            'message': "Congrats, home page is working :)"
        })

    ################# Retrieve movies ################

    @app.route('/movies')
    @requires_auth('get:movies')
    def retrieve_movies(token):
        movies = Movie.query.order_by(Movie.id).all()
        if not movies:
            abort(404)
        current_movies = paginate_page(request, movies)

        return jsonify({
            'success': True,
            'movies': current_movies,
            'total_movies': len(movies)
        }), 200

    @app.route('/movies/<int:movie_id>')
    @requires_auth('get:movies')
    def retireve_movie_(token, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    ################ Retrieve actors #################

    @app.route('/actors')
    @requires_auth('get:actors')
    def retrieve_actors(token):
        actors = Actor.query.order_by(Actor.id).all()
        if actors is None:
            abort(404)
        current_actors = paginate_page(request, actors)

        return jsonify({
            'success': True,
            'actors': current_actors,
            'total_actors': len(actors)
        }), 200

    @app.route('/actors/<int:actor_id>')
    @requires_auth('get:actors')
    def retireve_actor(token, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    ################ Delete movie #####################

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):
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
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'deleted': actor_id
        }), 200

    ################### Create movies #####################

    @app.route('/movies/add', methods=['POST'])
    @requires_auth('add:movies')
    def create_new_movie(token):
        body = request.get_json()
        if body is None:
            abort(400)
        new_title = body['title']
        release_date = body['release_date']

        new_movie = Movie(title=new_title, release_date=release_date)
        movies = Movie.query.all()
        cur_movies = paginate_page(request, movies)

        new_movie.insert()

        return jsonify({
            'success': True,
            'movies': cur_movies,
            'total_movies': len(movies)
        }), 200

    #################### Create Actor #####################

    @app.route('/actors/add', methods=['POST'])
    @requires_auth('add:actors')
    def create_new_actor(token):
        body = request.get_json()
        if body is None:
            abort(400)
        new_name = body['name']
        age = body['age']
        gender = body['gender']

        new_actor = Actor(name=new_name, age=age, gender=gender)
        actors = Actor.query.all()
        cur_actors = paginate_page(request, actors)

        new_actor.insert()

        return jsonify({
            'success': True,
            'actors': cur_actors,
            'total_actors': len(actors)
        }), 200

    ################### Update Movie ######################

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(token, movie_id):
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
    @requires_auth('patch:actors')
    def update_actor(token, actor_id):
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

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(AuthError)
    def autherror_handling(fault):
        response = jsonify(fault.error)
        response.status_code = fault.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
