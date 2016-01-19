from booklist.celery import app


@app.task(bind=True)
def tsk(self):
    counter = 0

    for i in range(0, 100000):
        print(i)
        counter += 1

        self.update_state(state="PROGRESS", meta={
            "counter": i
        })


@app.task(bind=True)
def import_task(self, deserialized_objects):
    total = len(deserialized_objects)
    counter = 0

    for deserialized_object in deserialized_objects:
        # deserialized_object.save()

        counter += 1

        self.update_state(state="PROGRESS", meta={
            "done": counter,
            "total": total
        })
