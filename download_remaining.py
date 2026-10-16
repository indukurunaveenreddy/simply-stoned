import os, urllib.request, time

DEST_DIR = "/Users/inaveenreddy/Desktop/simply stoned/assets/images/menu"

REMAINING = {
    "pista-stone-ice-cream.jpg": "photo-1579954115563-e72bf1381629",     # Pistachio green ice cream
    "butterscotch-milkshake.jpg": "photo-1553530666-ba11a7da3888",    # Creamy golden caramel shake
    "butterscotch-thick-shake.jpg": "photo-1560008581-09826d1de69e",  # Thick caramel butterscotch shake
    "watermelon-juice.jpg": "photo-1567206563064-6f60f40a2b57",        # Red watermelon drink / juice
    "apple-juice.jpg": "photo-1568909344668-6f14a07b56a0",             # Fresh apple juice
    "watermelon-mint-juice.jpg": "photo-1527661591475-527312dd65f5",   # Watermelon mint cooler
    "carrot-juice.jpg": "photo-1600271886742-f049cd451bba",            # Vibrant orange juice / carrot juice
    "abc-juice.jpg": "photo-1541832676-9b763b0239ab",                 # Deep red detox blend
    "ice-cream-pancakes.jpg": "photo-1565299585323-38d6b0865b47",       # Fluffy pancakes with scoop
}

for filename, photo_id in REMAINING.items():
    filepath = os.path.join(DEST_DIR, filename)
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=400&h=400&q=80"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as response:
            data = response.read()
            if len(data) > 5000:
                with open(filepath, "wb") as f:
                    f.write(data)
                print(f"Downloaded: {filename} ({len(data)} bytes)")
            else:
                print(f"Too small: {filename}")
    except Exception as e:
        print(f"Error for {filename}: {e}")
    time.sleep(0.1)

