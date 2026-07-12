"""
routes/watchlist.py — CineLog (feature/watchlist branch)

Endpoints for the watchlist feature.
"""

from flask import Blueprint, jsonify, request, current_app
# Update the import and the endpoint call site
# Import AlreadyInWatchlistError so the route can catch it
from services.watchlist_service import add_to_watchlist, get_watchlist, AlreadyInWatchlistError
from services.collection_service import FilmNotFoundError

watchlist_bp = Blueprint("watchlist", __name__)


@watchlist_bp.route("/<user_id>", methods=["GET"])
def view_watchlist(user_id):
    """GET /watchlist/<user_id> — Return the user's watchlist."""
    with current_app.app_context():
        films = get_watchlist(user_id)
        # Evaluate to a standard python list/dict while session is active
        return jsonify(films)


@watchlist_bp.route("/<user_id>/add", methods=["POST"])
def add_film(user_id):
    """
    POST /watchlist/<user_id>/add

    Body: { "film_id": <int> }
    """
    data = request.get_json()
    if not data or "film_id" not in data:
        return jsonify({"error": "film_id is required"}), 400

    try:
        with current_app.app_context():
            # Update call site here
            entry = add_to_watchlist(user_id=user_id, film_id=data["film_id"])
            # Move this INSIDE the context block so it has session access
            response_data = entry.to_dict()
        return jsonify(response_data), 201
        
    except FilmNotFoundError as e:
        return jsonify({"error": str(e)}), 404
        
    except AlreadyInWatchlistError as e:
        # Catch the duplicate error gracefully and return a 400 Bad Request
        return jsonify({"error": str(e)}), 400
