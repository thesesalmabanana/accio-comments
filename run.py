def main():
    # Dictionnaire des programmes disponibles
    programmes = {
        "1": ("Scrap Reddit", "scraps.scrap_reddit.scrap_reddit"),
        "2": ("Scrap Youtube", "scraps.scap_youtube.scrap_youtube"),
        "3": ("Scrap X", "scraps.scrap_x.scrap_x"),
    }

    print("Quel programme veux-tu lancer ?")
    for key, (nom, _) in programmes.items():
        print(f"{key} - {nom}")

    choix = input("Choix : ").strip()

    if choix not in programmes:
        print("Choix invalide.")
        return

    match choix:
        case "1":
            from scraps.scrap_reddit import run_scraper 
        case "2":
            from scraps.scrap_youtube import run_scraper
        case "3":
            from scraps.scrap_x import run_scraper
            
    run_scraper()

if __name__ == "__main__":
    main()