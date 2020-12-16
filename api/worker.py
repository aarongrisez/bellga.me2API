import schedule
import functools
import time
import requests
import random
import os
from models.event import SynthesizedEvent
from models.note import SynthesizedNote
import logging

CHANNELS = list(map(str, [1, 2, 3, 4, 5, 6]))
PITCHES = list(map(str, [120, 220, 320, 420, 520, 620, 720, 820]))
DURATIONS = list(map(str, [.5, .5, .5, .4, .5, .4, .1]))
TIMES = list(map(str, [1, 2, 4, 8, 7, 8, 8, 16, 3, 9, 7]))
VELOCITIES = list(map(str, [0.25, 0.33, 0.33, 0.25, 0.24, 0.44, 0.33, 0.1, 0.2]))

def job(*args, **kwargs):
    note = SynthesizedNote(
        note = random.choice(PITCHES),
        duration = random.choice(DURATIONS),
        time = random.choice(TIMES),
        velocity = random.choice(VELOCITIES),
    )
    event = SynthesizedEvent(
        channel = random.choice(CHANNELS),
        notes = [note]
    )
    r = requests.post(os.environ.get("API_URL") + "push/", json=event.dict())

schedule.every(0.87).seconds.do(lambda: job(1))
schedule.every(0.47).seconds.do(lambda: job(1))
schedule.every(0.37).seconds.do(lambda: job(1))
schedule.every(0.27).seconds.do(lambda: job(1))
schedule.every(0.29).seconds.do(lambda: job(1))
schedule.every(1.87).seconds.do(lambda: job(2))
schedule.every(0.97).seconds.do(lambda: job(3))
schedule.every(1.89).seconds.do(lambda: job(4))

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)