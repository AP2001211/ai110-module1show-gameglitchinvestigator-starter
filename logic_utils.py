def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a given difficulty."""
    # FIX: Corrected difficulty scaling so Hard is actually harder than Normal.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns:
        (is_valid, parsed_value, error_message)
    """
    # FIX: Centralized input parsing here so it can be tested outside the UI.
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare a guess to the secret number.

    Returns:
        "Win", "Too High", or "Too Low"
    """
    # FIX: Keep comparisons numeric so the hint logic stays consistent.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the player's score based on the outcome and attempt number."""
    # FIX: Moved scoring logic into logic_utils.py so pytest can cover it later.
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        return current_score + max(points, 10)

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score