# Capstone - Casting Agency API project

## Introduction
The mission of this API project is to help users manage actors and movies in an orderly manner.

## Getting Started
URL where project is deployed: <URL>
Authentication:
> Information of users who has permissions:
>*  castingassistant@gmail.com
>*  castingdirector@gmail.com
>*  castingproducer@gmail.com
>-  password: 571632Sav@
>-  authorization link: https://moscod.us.auth0.com/authorize?audience=casting&response_type=token&client_id=NdOwf1JiSKnNuX1K32UzqOqTZ2KnzQV7&redirect_uri=http://127.0.0.1:5000/

There are three user-roles in this project:
They are:
 - Casting Assistant
 - Casting Director
 - Executive Producer

Permissions on roles:
 - Casting Assistant:
	- `get:movies`
	- `get:actors`
 - Casting Director:
	- `get:movies`
	- `get:actors`
	- `add:actors`
	- `delete:actors`
	- `patch:movies`
	- `patch:actors`
 - Executive Producer:
	- `get:movies`
	- `get:actors`
	- `add:movies`
	- `add:actors`
	- `delete:actors`
	- `delete:movies`
	- `patch:movies`
	- `patch:actors`

#### Instructions for testing the project:
Requirements - what you need to have to try this project:
	- Python3 (https://www.python.org/downloads/)
	- Postgresql database (https://www.postgresql.org/download/)
	- Python pip packages
	- Postman (for testing)

First step is clone this repo:

```bash
 git clone https://github.com/MosCod/capstone.git
 cd capstone
```

Install all required pip packages:

```bash
 pip install -r requirements.txt
```
 
Create dotenv file and change some config vars in your enviroment file:

```bash
 touch .env 
 nano .env
--------------------
DATABASE_URL = "url"
--------------------
```

Before running server, prepare your database.

```bash
 python manage.py db init
 python manage.py db migrate
 python manage.py db upgrade
```

Run:

```bash
 python manage.py 
```
#### Testing API
You can use Postman to test this API.
* First you download postman, install it and register. (https://www.postman.com/downloads/)

> I have written postman collection tests for testing this project in this project folder.

* Open your postman and import my collection test.

* Prepare your enviroment. Define api host and JWT tokens from Globals tab

* Then open collection runner in this collection and press run.


# API reference 

### Error handling

Errors are returned in JSON format in the following format:

	{
    	"error": 404,
    	"message": "Resource not found",
    	"success": false
    }

This API will return three types of errors:

* 404 - Resource not found
* 401 - Unauthorized
* 400 - Bad request

### Endpoints

#### Movies endpoints: 
 `/movies` - methods: [GET]. Retrieve all movies data.
*   `/movie/<movie_id>` - methods: [GET,PATCH,DELETE].
    *   **GET** - get movie data by id.
    *   **PATCH** - update movie.
    *   **DELETE** - delete movie.
*   `/movies/add` - methods: [POST]. Add new Movie.


**Actor** endpoints:
*   `/actors` - methods: [GET]. Retrieve all actor data.
*   `/actor/<actor_id>` - methods: [GET,PATCH,DELETE].
    *   **GET** - get actor data by id.
    *   **PATCH** - update actor.
    *   **DELETE** - delete actor.
*   `/actors/add` - methods: [POST]. Add new Actor.


#### Get /movies
* Methods: **GET**
* URL: `/movies`
* Permission: `get:movies`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/actors' \                       33333333333333333333333
--header 'Authorization: Bearer <token>'
```

Response:
```json
	{
    	"movies": [
        	{
            	"id": 1,
            	"release_date": "Wed, 01 Jan 2020 00:00:00 GMT",
            	"title": "Titanic movie"
        	},
			//........ all movies data in database
		],
		"success": true,
		"total_movies": 16
	}
```


#### Get /actors
* Methods: **GET**
* URL: `/actors`
* Permission: `get:actors`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://abduaziz-casting-agency.herokuapp.com/api/actors' \                       33333333333333333333333
--header 'Authorization: Bearer <token>'
```

Response:
```json
	{
    	"actors": [
        	{
            	"age": 2,
            	"gender": "F",
            	"id": 2,
            	"name": "George"
        	},
			//........ all actors data in database
		],
		"success": true,
		"total_actors": 13
	}
```


#### Get /movies/<movie_id>
* Methods: **GET**
* URL: `/movies<movie_id>`
* Permission: `get:movies`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://capstone-casting-agency.herokuapp.com/api/actors' \                       33333333333333333333333
--header 'Authorization: Bearer <token>'
```

Response:
```json
	{
    	"movie": {
        	"id": 2,
        	"release_date": "Thu, 01 Apr 2021 00:00:00 GMT",
        	"title": "Age of the Medici, The (L'eta di Cosimo de Medici) "
    		}, 
		"success": true,
	}
```


#### Get /actors/<actor_id>
* Methods: **GET**
* URL: `/actors/<actor_id>`
* Permission: `get:actors`

Sample Request using CURL:

```bash
curl --location --request GET \
'https://capstone-casting-agency.herokuapp.com/api/actors' \                       33333333333333333333333
--header 'Authorization: Bearer <token>'
```

Response:
```json
	{
    	"actor": {
        	"age": 35,
        	"gender": "M",
        	"id": 4,
        	"name": "Bronny"
    		},
    	"success": true
	}
```



### Post - movies

* Methods: **POST**
* URL: `/movies/add`
* Permission: `add:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": datetime,
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "New Some Film",
	"release_date": "02.11.2001"
}'
```
Response:
```json
{
    	"movies": [
        	{
            	"id": 1,
            	"release_date": "Wed, 01 Jan 2020 00:00:00 GMT",
            	"title": "Titanic movie"
        	},
			//........ all movies data in database
		],
		"success": true,
		"total_movies": 16
	}
```


### Post - actors

* Methods: **POST**
* URL: `/actors/add`
* Permission: `add:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
	"age": int,
	"gender": Boolean
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Amitabh Bachchan",
    "age": 99,
    "gender": "M"
}'
```

Response:
```json
{
    "actors": [
        {
            "age": 2,
            "gender": "F",
            "id": 2,
            "name": "George"
        },
		//........ all actors data in database
	],
	"success": true,
	"total_actors": 13
	}
```



### Patch - movies

* Methods: **PATCH**
* URL: `/movies/<movie_id>`
* Permission: `patch:movies`

>[!] Required Request Body

Request body structure:

```json
{
    "title": str,
    "release_date": datetime,
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "New Some Film",
	"release_date": "02.11.2001"
}'
```
Response:
```json
	{
		"success": true,
		"movie": <movie_id>
	}
```


### Patch - actors

* Methods: **PATCH**
* URL: `/actors/<actor_id>`
* Permission: `patch:actors`

>[!] Required Request Body

Request body structure:

```json
{
    "name": str,
	"age": int,
	"gender": Boolean
}
```

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 100,
    "gender": "M"
}'
```

Response:
```json
	{
		"success": true,
		"actor": <actor_id>
	}
```


### Delete - movies

* Methods: **DELETE**
* URL: `/movies/<movie_id>`
* Permission: `delete:movies`

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
```
Response:
```json
	{
		"success": true,
		"movie": <movie_id>
	}
```


### Delete - actors

* Methods: **DELETE**
* URL: `/actors/<movie_id>`
* Permission: `delete:actors`

Sample Request using Curl:

```bash
curl --location --request POST \
'https://abduaziz-casting-agency.herokuapp.com/api/movies/add' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
```
Response:
```json
	{
		"success": true,
		"actor": <actor_id>
	}
```


## Author

Xusniddin Aliqulov Muxiddin o'g'li.
Gmail: Ummat1Muhammad1571@gmail.com