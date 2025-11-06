import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response=requests.get(url)
        return response.content

    def load_json(self):
        formatted_response=f"name: {response['docs'][0]['title']}\noccupation: {response['docs'][0]['author_name'][0]}"
        return formatted_response