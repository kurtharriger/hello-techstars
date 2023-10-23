from flask import redirect
from pydantic import BaseModel
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from prometheus_flask_exporter import PrometheusMetrics

info = Info(title="Greeting API", version="1.0")
app = OpenAPI(__name__, info=info)

metrics = PrometheusMetrics(app)
metrics.info('greeting_api', 'Greeting API', version='1.0')

greeting_tag = Tag(name='greeting', description='Friendly Greeting')
class GreetingQuery(BaseModel):
    """Query parameters for greeting"""
    name: str

class Greeting(BaseModel):
    """Greeting response model"""
    message: str

@app.get('/greeting', tags=[greeting_tag])
def get_greeting(query: GreetingQuery):
    """Return a friendly greeting."""
    greeting = Greeting(message=f"Hello {query.name}!")
    return greeting.model_dump()

@app.route('/')
def root():
    """Redirect to the API documentation"""
    return redirect('/openapi/rapidoc')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
