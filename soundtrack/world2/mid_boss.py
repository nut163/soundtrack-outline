```python
class TrackSchema:
    def __init__(self, key, bpm, genre, synths, vibe):
        self.key = key
        self.bpm = bpm
        self.genre = genre
        self.synths = synths
        self.vibe = vibe

worldNumber = 2
sceneType = "Mid-Boss"

trackDetails = TrackSchema(
    key = "D minor",
    bpm = 130,
    genre = "Electronic",
    synths = ["Moog Sub 37", "Roland Juno", "Korg Minilogue"],
    vibe = "Tense and suspenseful with a fast tempo and heavy bassline to signify the challenge of the mid-boss fight."
)

def createTrack(worldNumber, sceneType, trackDetails):
    track = {
        "world": worldNumber,
        "scene": sceneType,
        "details": {
            "key": trackDetails.key,
            "bpm": trackDetails.bpm,
            "genre": trackDetails.genre,
            "synths": trackDetails.synths,
            "vibe": trackDetails.vibe
        }
    }
    return track

def updateTrack(worldNumber, sceneType, trackDetails):
    track = getTrack(worldNumber, sceneType)
    if track:
        track["details"] = {
            "key": trackDetails.key,
            "bpm": trackDetails.bpm,
            "genre": trackDetails.genre,
            "synths": trackDetails.synths,
            "vibe": trackDetails.vibe
        }
    return track

def getTrack(worldNumber, sceneType):
    # This function would typically interact with a database to retrieve the track
    # For the purpose of this example, we'll return a placeholder track
    return {
        "world": worldNumber,
        "scene": sceneType,
        "details": {
            "key": "Placeholder Key",
            "bpm": 0,
            "genre": "Placeholder Genre",
            "synths": ["Placeholder Synth"],
            "vibe": "Placeholder Vibe"
        }
    }

track = createTrack(worldNumber, sceneType, trackDetails)
```