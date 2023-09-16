from flask import Flask
app = Flask(__name__)
#app.secret_key = "" # python -c 'import secrets; print(secrets.token_hex())'
print('app.root_path+++++++++++++',app.root_path)