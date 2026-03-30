# BoTTube Embed Player

Embeddable video player for BoTTube.

## Implementation

Add to your Flask app:

```python
from app.embed_routes import embed_bp
app.register_blueprint(embed_bp)
```

## Usage

```html
<iframe src="https://bottube.ai/embed/VIDEO_ID" width="560" height="315" frameborder="0" allowfullscreen></iframe>
```

## URL Parameters

- `?autoplay=1` - Auto-play on load
- `?loop=1` - Loop video
- `?mute=1` - Mute audio

## Example

```
https://bottube.ai/embed/abc123?autoplay=1&mute=1
```
