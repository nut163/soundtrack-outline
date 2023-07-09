```python
# Importing the required dependencies
from track_schema import TrackSchema

# Defining the world number and scene type
worldNumber = 1
sceneType = "Generic Fight"

# Defining the track details
trackDetails = {
    "key": "C Major",
    "bpm": 128,
    "genre": "Electronic",
    "synths": ["Moog Sub 37", "Roland Juno-60", "Korg Minilogue"],
    "vibe": "Fast-paced and energetic with a heavy bassline to keep the player engaged during fights."
}

# Validating the track details with the schema
TrackSchema.validate(trackDetails)

# Creating the track
createTrack(worldNumber, sceneType, trackDetails)

# Sending a message that the track has been created
TrackCreated(worldNumber, sceneType)
```