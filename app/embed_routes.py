# Embed Blueprint for BoTTube
from flask import Blueprint, render_template, request

embed_bp = Blueprint('embed', __name__)

@embed_bp.route('/embed/<video_id>')
def embed_player(video_id):
    """Embeddable video player
    
    Args:
        video_id: The BoTTube video ID
        
    Query Params:
        autoplay: Set to 1 for autoplay
        loop: Set to 1 for looping
        mute: Set to 1 for muted playback
    """
    return render_template('embed.html', video_id=video_id)

@embed_bp.route('/embed/<video_id>.json')
def embed_metadata(video_id):
    """Embed metadata endpoint for API access"""
    return {
        'video_id': video_id,
        'player_url': f'/embed/{video_id}',
        'embed_params': ['autoplay', 'loop', 'mute']
    }
