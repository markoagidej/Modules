def mood_response(mood):
    mood_lowered = mood.lower()
    if mood_lowered == "happy":
        return "Great! Keep having a good day then!"
    if mood_lowered == "sad":
        return "Maybe you should havea bowl of ice-cream."
    if mood_lowered == "excited":
        return "WOAH NO WAY ME TOO"
    else:
        return f"Sorry, I don't recognize {mood} as a mood!"