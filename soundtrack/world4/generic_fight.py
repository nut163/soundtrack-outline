```python
# Importing the required dependencies
from track_schema import TrackSchema

# Defining the world number and scene type
worldNumber = 4
sceneType = "Generic Fight"

# Defining the track details
trackDetails = {
    "key": "C Minor",
    "bpm": 130,
    "genre": "Electronic",
    "synths": ["Moog Subsequent 37", "Roland Juno-106", "Korg Minilogue XD"],
    "vibe": "Fast-paced and intense with a heavy bassline and sharp synth melodies to keep the player on edge."
}

# Validating the track details against the schema
TrackSchema.validate(trackDetails)

# Creating the track
createTrack(worldNumber, sceneType, trackDetails)

# Sending a message that the track has been created
TrackCreated.send(worldNumber, sceneType)
```