""" main.py ? FastAPI dispatcher for the memory-palace module """

from fastapi import FastAPI
from .observe import observe
from .memorize import memorize
from .recall import recall
from .suggest import suggest
from .cortex import update_focus, add_thread
from .plasticity import trigger_plasticity

app = FastAPI()

@app.post("/observe")
def api_observe(payload: dict):
    return observe(payload)

@app.post("/memorize")
def api_memorize(payload: dict):
    return memorize(payload)

@app.get("/recall")
def api_recall(topic: str):
    return recall(topic)

@app.get("/suggest")
def api_suggest(trigger: str):
    return suggest(trigger)

@app.post("/focus")
def api_focus(topic: str):
    return update_focus(topic)

@app.post("/thread")
def api_thread(note: str):
    return add_thread(note)

@app.post("/plasticity")
def api_plasticity(reason: str, structure_hint: str = "topic-cluster"):
    return trigger_plasticity(reason, structure_hint)
