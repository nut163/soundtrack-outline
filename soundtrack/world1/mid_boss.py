```python
# Importing the required dependencies
from schemas import TrackSchema
from messages import TrackCreated, TrackUpdated
from functions import createTrack, updateTrack, getTrack

# Setting the world number and scene type
worldNumber = 1
sceneType = "Mid-Boss"

# Defining the track details
trackDetails = {
    "key": "C Minor",
    "bpm": 128,
    "genre": "Techno",
    "synths": ["Moog Sub 37", "Roland Juno-60", "Korg Minilogue"],
    "vibe": "A tense and suspenseful track with a driving beat and dark synths, perfect for a mid-boss fight."
}

# Creating the track
createTrack(worldNumber, sceneType, trackDetails)

# Sending a message that the track has been created
TrackCreated(worldNumber, sceneType)

# If you need to update the track details, you can do so like this:
# updatedTrackDetails = {
#     "key": "D Minor",
#     "bpm": 130,
#     "genre": "Techno",
#     "synths": ["Moog Sub 37", "Roland Juno-60", "Korg Minilogue", "Arturia MatrixBrute"],
#     "vibe": "An even more tense and suspenseful track with a faster beat and additional synths."
# }
# updateTrack(worldNumber, sceneType, updatedTrackDetails)
# TrackUpdated(worldNumber, sceneType)

# If you need to get the track details, you can do so like this:
# print(getTrack(worldNumber, sceneType))
```