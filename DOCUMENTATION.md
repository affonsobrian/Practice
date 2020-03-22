# Olist Library

This document has the purpose of help you to use this API.

## Commands
#### Import Author from CSV
You can import authors from csv automatically by running the following command:
```sh
python manage.py import_authors file_name.csv
```

## API
### Authors
#### GET (list)
url: https://thawing-spire-26906.herokuapp.com/authors/

Result: 
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Albert Einstein",
            "books": []
        },
        {
            "id": 2,
            "name": "Machado de Assis",
            "books": []
        }
    ]
}
```

#### GET (specific)
url: https://thawing-spire-26906.herokuapp.com/authors/< id >/

result:
```json
{
    "id": 1,
    "name": "Albert Einstein",
    "books": []
}
```

#### POST

url: https://thawing-spire-26906.herokuapp.com/authors/

body:
```json
{
  "name": "author name"
}
```
#### PUT / PATCH
url: https://thawing-spire-26906.herokuapp.com/authors/< id >/
```json
{
  "name": "author name"
}
```

#### DELETE
url: https://thawing-spire-26906.herokuapp.com/authors/< id >/

### Books
#### GET (list)
url: https://thawing-spire-26906.herokuapp.com/books/

Result: 
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Physics III",
            "edition": 1,
            "publication_year": 1880,
            "authors": [
                1
            ]
        },
        {
            "id": 2,
            "name": "Physics II",
            "edition": 1,
            "publication_year": 1870,
            "authors": [
                1
            ]
        }
    ]
}


```

#### GET (specific)
url: https://thawing-spire-26906.herokuapp.com/books/< id >/

result:
```json
{
    "id": 1,
    "name": "Physics III",
    "edition": 1,
    "publication_year": 1880,
    "authors": [
        1
    ]
}
```

#### POST

url: https://thawing-spire-26906.herokuapp.com/books/

body:
```json
{
    "name": "Physics III",
    "edition": 1,
    "publication_year": 1880,
    "authors": [
        1
    ]
}
```
#### PUT / PATCH
url: https://thawing-spire-26906.herokuapp.com/books/< id >/
```json
{
    "name": "Physics III",
    "edition": 1,
    "publication_year": 1880,
    "authors": [
        1, 2
    ]
}
```

#### DELETE
url: https://thawing-spire-26906.herokuapp.com/books/< id >/