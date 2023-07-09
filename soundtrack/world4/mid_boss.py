```python
# Importing the required dependencies
from track_schema import TrackSchema

# Defining the world number and scene type
worldNumber = 4
sceneType = "Mid-Boss"

# Defining the track details
trackDetails = {
    "key": "D# minor",
    "bpm": 130,
    "genre": "Electronic",
    "synths": ["Moog Subsequent 37", "Roland Juno-60", "Korg Minilogue XD"],
    "vibe": "A tense and suspenseful track with a driving beat and dark, brooding synths. Perfect for a mid-boss fight."
}

# Validating the track details against the schema
TrackSchema.validate(trackDetails)

# Creating the track
createTrack(worldNumber, sceneType, trackDetails)

# Sending a message that the track has been created
TrackCreated(worldNumber, sceneType, trackDetails)
```