from locust import task, HttpUser


class QaPractice(HttpUser):
    object_id = None
    object_id_for_delete = None

    def on_start(self):
        response = self.client.post("", json={
            "name": "First object",
            "data": {
                "color": "black",
                "size": "small"
            }
        }
        )

        self.object_id = response.json()["id"]

    @task(1)
    def get_all_objects(self):
        self.client.get("")

    @task(3)
    def get_one_object(self):
        self.client.get(f"/{self.object_id}")

    @task(1)
    def put_object(self):
        self.client.put(f"/{self.object_id}", json={
            "name": "First object",
            "data": {
                "color": "black-UPD",
                "size": "small-UPD"
            }
        }
        )

    @task(1)
    def patch_object(self):
        self.client.patch(f"/{self.object_id}", json={
            "name": "First object",
            "data": {
                "size": "small-UPD"
            }
        }
        )

    @task(1)
    def delete_object(self):
        response = self.client.post("", json={
            "name": "Object for delete",
            "data": {
                "color": "orange",
                "size": "small"
            }
        }
        )

        self.object_id_for_delete = response.json()["id"]
        self.client.delete(f"/{self.object_id_for_delete}")
