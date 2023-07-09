Shared Dependencies:

1. Exported Variables: 
   - `worldNumber`: The number of the world for which the track is being created.
   - `sceneType`: The type of scene for which the track is being created (Generic Fight, Overworld, Mid-Boss, Boss, Shop Music).
   - `trackDetails`: A dictionary containing the Key, BPM, Genre, synths used, and a description of the vibe of each track.

2. Data Schemas:
   - `TrackSchema`: A schema defining the structure of `trackDetails` which includes `key`, `bpm`, `genre`, `synths`, and `vibe`.

3. ID Names of DOM Elements:
   - `world-id`: The ID of the world element in the DOM.
   - `scene-id`: The ID of the scene element in the DOM.
   - `track-details-id`: The ID of the track details element in the DOM.

4. Message Names:
   - `TrackCreated`: A message sent when a new track is created.
   - `TrackUpdated`: A message sent when a track is updated.

5. Function Names:
   - `createTrack(worldNumber, sceneType, trackDetails)`: A function to create a new track.
   - `updateTrack(worldNumber, sceneType, trackDetails)`: A function to update an existing track.
   - `getTrack(worldNumber, sceneType)`: A function to retrieve the details of a track.