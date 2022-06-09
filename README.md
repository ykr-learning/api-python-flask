# api-python-flask

## prerequisite
install flask: `pip install flask`

## run unit tests
run the command: `pytest`

## run api
run the command: `python3 src/main.py`

## Install postman
follow the link: https://linuxize.com/post/how-to-install-postman-on-ubuntu-20-04/

Or run the ubuntu command: `sudo snap install postman`

## Test the api with postman

1. Test the home
   
With a browser, go to: http://127.0.0.1:5000/

2. List the stores

With postman or a browser, go to: http://127.0.0.1:5000/store

3. Add a store

With postman:
- Url: http://127.0.0.1:5000/store
- Method: POST
- Body (type raw & json):
```
{
    "name": "other store"
}
```


4. List items
With postman or a browser, go to: http://127.0.0.1:5000/store/My_wonderful_store


5. Add item

With postman:
- Url: http://127.0.0.1:5000/store/My_wonderful_store/
- Method: POST
- Body (type raw & json):
```
{
    "name": "article 1",
    "price": 10.99
}
```

## To do calls with curl

```
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Post_Store_1"}' \
    <url>
```


## pytest.ini ?
Added to fix the error: `ModuleNotFoundError: No module named 'src'`, more info: https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada

## to read

https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414176-implementez-vos-tests-pour-le-framework-flask-avec-pytest-flask


