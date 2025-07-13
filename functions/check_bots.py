from functions.load_config import get_config

# ========== BOT DETECTION ==========
def is_bot(comment):
    username = str(comment.author).lower()
    
    # Liste étendue de bots connus
    config = get_config()
    known_bots = config["knowBots"]


    # Match exact (bots connus) ou partiel (indicateurs)
    return (
        username in known_bots
    )