fichier app.py, initialement:

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello world'
app.run(port=5000)


pip install flask
python3 app.py

aller sur:
http://127.0.0.1:5000/
display:
hello world

http://127.0.0.1:5000/store

la fonction render_template cherche les fichiers dans le dossier templates.
le fichier index.html doit donc etre dans le dossier templates

pour installer postman sur ubuntu:
https://linuxize.com/post/how-to-install-postman-on-ubuntu-20-04/
sudo snap install postman

tests avec postman:
1/
http://127.0.0.1:5000/store

2/
http://127.0.0.1:5000/store
Method: POST
Body (type raw & json):
{
    "name": "autre store"
}

3/
http://127.0.0.1:5000/store/My wonderful store/item

4/
http://127.0.0.1:5000/store/My wonderful store2/item
reponse:
{
    "message": "store not found"
}

5/
http://127.0.0.1:5000/store/My wonderful store/item
Method: POST
Body (type raw & json):
{
    "name": "article 1",
    "price": 10.99
}


pour faire les appels en curl:
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Post_Store_1"}' \
    <url>

