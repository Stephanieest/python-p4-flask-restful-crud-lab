import json
from app import app, db, Plant

class TestPlant:
    '''Flask application in app.py'''

    def test_plant_by_id_get_route(self):
        '''has a resource available at /plants/<id>'''
        with app.test_client() as client:
            response = client.get('/plants/1')
            assert response.status_code == 200

    def test_update_plant(self):
        '''Test PATCH /plants/<id>'''
        with app.test_client() as client:
            response = client.patch('/plants/1', 
                                    data=json.dumps({"is_in_stock": False}),
                                    content_type='application/json')
            assert response.status_code == 200
            updated_plant = json.loads(response.data)
            assert updated_plant['is_in_stock'] == False

    def test_delete_plant(self):
        '''Test DELETE /plants/<id>'''
        with app.test_client() as client:
            response = client.delete('/plants/1')
            assert response.status_code == 204
