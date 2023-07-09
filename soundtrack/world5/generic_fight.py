```python
# Importing the required dependencies
from track_schema import TrackSchema

# Defining the world number and scene type
worldNumber = 5
sceneType = "Generic Fight"

# Defining the track details
trackDetails = {
    "key": "C# minor",
    "bpm": 130,
    "genre": "Electronic",
    "synths": ["Moog Sub 37", "Roland Juno-60", "Korg Minilogue"],
    "vibe": "Fast-paced and intense with a heavy bassline and sharp synth melodies to match the high-stakes combat scenario."
}

# Validating the track details with the schema
TrackSchema.validate(trackDetails)

# Creating the track
createTrack(worldNumber, sceneType, trackDetails)

# Sending a message that the track has been created
TrackCreated(worldNumber, sceneType, trackDetails)
```