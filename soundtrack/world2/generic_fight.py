```python
class TrackSchema:
    def __init__(self, key, bpm, genre, synths, vibe):
        self.key = key
        self.bpm = bpm
        self.genre = genre
        self.synths = synths
        self.vibe = vibe

worldNumber = 2
sceneType = "Generic Fight"

trackDetails = TrackSchema(
    key="D minor",
    bpm=130,
    genre="Techno",
    synths=["Roland Jupiter-8", "Moog Subsequent 37", "Korg Minilogue XD"],
    vibe="Fast-paced and intense with a steady rhythm, perfect for a generic fight scene."
)

def createTrack(worldNumber, sceneType, trackDetails):
    track = {
        "worldNumber": worldNumber,
        "sceneType": sceneType,
        "key": trackDetails.key,
        "bpm": trackDetails.bpm,
        "genre": trackDetails.genre,
        "synths": trackDetails.synths,
        "vibe": trackDetails.vibe
    }
    return track

def updateTrack(worldNumber, sceneType, trackDetails):
    track = getTrack(worldNumber, sceneType)
    track["key"] = trackDetails.key
    track["bpm"] = trackDetails.bpm
    track["genre"] = trackDetails.genre
    track["synths"] = trackDetails.synths
    track["vibe"] = trackDetails.vibe
    return track

def getTrack(worldNumber, sceneType):
    # This function would typically interact with a database to retrieve the track details
    # For the purpose of this example, we'll return a placeholder track
    return {
        "worldNumber": worldNumber,
        "sceneType": sceneType,
        "key": "Placeholder Key",
        "bpm": 0,
        "genre": "Placeholder Genre",
        "synths": ["Placeholder Synth"],
        "vibe": "Placeholder Vibe"
    }

newTrack = createTrack(worldNumber, sceneType, trackDetails)
```