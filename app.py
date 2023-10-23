from flask import Flask, redirect, jsonify
from pydantic import BaseModel
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

info = Info(title="Greeting API", version="1.0")
app = OpenAPI(__name__, info=info)

greeting_tag = Tag(name='greeting', description='Friendly Greeting')

class GreetingQuery(BaseModel):
    name: str

class Greeting(BaseModel):
    message: str

@app.get('/greeting', tags=[greeting_tag])
def get_greeting(query: GreetingQuery):
      greeting = Greeting(message=f"Hello {query.name}!")
      return jsonify(greeting.dict())

@app.route('/')
def hello_world():
    """Return a friendly greeting."""
    return redirect('/openapi')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
