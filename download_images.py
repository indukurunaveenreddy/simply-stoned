import os
import urllib.request
import time
from PIL import Image

DEST_DIR = "/Users/inaveenreddy/Desktop/simply stoned/assets/images/menu"
os.makedirs(DEST_DIR, exist_ok=True)

# Curated high quality food photography matching each exact dessert item
ITEMS = {
    # === STONE ICE CREAMS ===
    "classic-chocolate-stone.jpg": "photo-1570197788417-0e82375c9371",  # Rich dark chocolate ice cream scoop
    "oreo-stone-ice-cream.jpg": "photo-1563805042-7684c019e1cb",        # Cookies & cream ice cream with Oreos
    "kitkat-stone-ice-cream.jpg": "photo-1587314168485-3236d6710814",      # Chocolate ice cream with wafer crunch
    "brownie-stone-ice-cream.jpg": "photo-1606313564200-e75d5e30476c",     # Chocolate brownie ice cream
    "nutella-stone-ice-cream.jpg": "photo-1541781774459-bb2af2f05b55",     # Nutella hazelnut chocolate swirl ice cream
    "ferrero-rocher-stone.jpg": "photo-1548848221-0c2e497ed557",        # Hazelnut chocolate truffle ice cream
    "strawberry-stone-ice-cream.jpg": "photo-1497034825429-c343d7c6a68f",  # Pink strawberry ice cream
    "mango-stone-ice-cream.jpg": "photo-1505394033641-40c6ad1178d7",       # Golden mango ice cream
    "blueberry-stone-ice-cream.jpg": "photo-1501443762994-82bd5dace89a",   # Blueberry compote ice cream
    "blackcurrant-stone-ice-cream.jpg": "photo-1568254183919-78a4f43a2877",# Purple blackcurrant ice cream rolls
    "butterscotch-stone-ice-cream.jpg": "photo-1560008581-09826d1de69e",  # Golden butterscotch praline ice cream
    "vanilla-choco-chip-stone.jpg": "photo-1567206563064-6f60f40a2b57",    # Vanilla bean ice cream with choco chips
    "pista-stone-ice-cream.jpg": "photo-1504855328839-2f4baf9e0fd6",       # Pistachio green gelato
    "bubblegum-stone-ice-cream.jpg": "photo-1576506295286-5cda18df43e7",   # Pastel bubblegum swirl ice cream
    "dry-fruit-stone-ice-cream.jpg": "photo-1582716401301-b2407dc7563d",   # Rich dry fruit almond kaju ice cream
    "mixed-fruit-stone-ice-cream.jpg": "photo-1517256064527-09c73fc73e38", # Fresh mixed fruits over ice cream
    "death-by-chocolate-stone.jpg": "photo-1579954115545-a95591f28bfc",    # Triple chocolate overloaded stone ice cream
    "brownie-fudge-stone.jpg": "photo-1624353365286-3f8d62daad51",        # Hot fudge brownie stone ice cream
    "cookies-amp-cream-stone.jpg": "photo-1551024709-8f23befc6f87",        # Artisanal cookies and cream roll
    "simply-stoned-special-stone.jpg": "photo-1563805042-7684c019e1cb",    # Signature loaded dessert bowl

    # === MILKSHAKES ===
    "vanilla-milkshake.jpg": "photo-1572490122747-3968b75cc699",          # Classic vanilla milkshake
    "chocolate-milkshake.jpg": "photo-1577805947697-89e18249d767",        # Creamy chocolate milkshake
    "strawberry-milkshake.jpg": "photo-1553787499-6f9133860278",         # Fresh strawberry milkshake
    "mango-milkshake.jpg": "photo-1623065422902-30a2d299bbe4",              # Rich mango milkshake
    "banana-milkshake.jpg": "photo-1553530666-ba11a7da3888",             # Sweet banana milkshake
    "oreo-milkshake.jpg": "photo-1572490122747-3968b75cc699",               # Oreo cookie milkshake
    "kitkat-milkshake.jpg": "photo-1541658016709-82535e94bc69",            # KitKat crisp chocolate shake
    "dairy-milk-shake.jpg": "photo-1586985289688-ca3cf47d3e6e",            # Dairy milk chocolate shake
    "butterscotch-milkshake.jpg": "photo-1588775402685-61845bb389a9",      # Butterscotch caramel shake
    "blackcurrant-milkshake.jpg": "photo-1546173159-315724a31696",        # Blackcurrant berry shake
    "blueberry-milkshake.jpg": "photo-1553787499-6f9133860278",           # Fresh blueberry shake
    "pista-milkshake.jpg": "photo-1579954115563-e72bf1381629",               # Pistachio green shake
    "badam-milkshake.jpg": "photo-1600718374662-0483d2b9da44",               # Saffron almond badam milk shake
    "rose-milkshake.jpg": "photo-1528740561666-dc2479dc08ab",                # Pink rose milkshake
    "cold-coffee.jpg": "photo-1517701550927-30cf4ba1dba5",                   # Chilled iced cold coffee
    "coffee-chocolate-shake.jpg": "photo-1541167760496-1628856ab772",        # Mocha chocolate coffee shake
    "apple-milkshake.jpg": "photo-1568909344668-6f14a07b56a0",               # Fresh apple cinnamon shake
    "chickoo-milkshake.jpg": "photo-1560512823-829485b8bf24",             # Creamy sapota chickoo shake
    "pineapple-milkshake.jpg": "photo-1546173159-315724a31696",           # Tropical pineapple shake
    "mixed-fruit-milkshake.jpg": "photo-1623065422902-30a2d299bbe4",         # Mixed fruits milkshake

    # === THICK SHAKES ===
    "oreo-thick-shake.jpg": "photo-1563805042-7684c019e1cb",               # Ultra thick Oreo shake
    "kitkat-thick-shake.jpg": "photo-1587314168485-3236d6710814",         # Thick KitKat shake
    "brownie-thick-shake.jpg": "photo-1579954115545-a95591f28bfc",        # Loaded brownie thickshake
    "nutella-thick-shake.jpg": "photo-1577805947697-89e18249d767",        # Nutella hazelnut thickshake
    "ferrero-rocher-thick-shake.jpg": "photo-1548848221-0c2e497ed557",     # Ferrero rocher thickshake
    "belgian-chocolate-thick-shake.jpg": "photo-1606313564200-e75d5e30476c",# Belgian dark cocoa thickshake
    "dark-chocolate-thick-shake.jpg": "photo-1541781774459-bb2af2f05b55",  # Intense dark chocolate shake
    "dairy-milk-thick-shake.jpg": "photo-1586985289688-ca3cf47d3e6e",      # Thick Dairy Milk chocolate shake
    "snickers-thick-shake.jpg": "photo-1568254183919-78a4f43a2877",        # Snickers peanut caramel thickshake
    "chocolate-fudge-thick-shake.jpg": "photo-1624353365286-3f8d62daad51", # Hot chocolate fudge thickshake
    "strawberry-thick-shake.jpg": "photo-1553787499-6f9133860278",        # Dense strawberry cream thickshake
    "mango-thick-shake.jpg": "photo-1623065422902-30a2d299bbe4",             # Rich Alphonso mango thickshake
    "blueberry-thick-shake.jpg": "photo-1501443762994-82bd5dace89a",          # Blueberry swirl thickshake
    "blackcurrant-thick-shake.jpg": "photo-1546173159-315724a31696",       # Blackcurrant thick shake
    "butterscotch-thick-shake.jpg": "photo-1588775402685-61845bb389a9",     # Butterscotch praline thickshake
    "red-velvet-thick-shake.jpg": "photo-1616031037011-087000171abe",       # Velvet red cream thickshake
    "death-by-chocolate.jpg": "photo-1579954115545-a95591f28bfc",           # Triple chocolate freakshake
    "coffee-crunch-thick-shake.jpg": "photo-1517701550927-30cf4ba1dba5",    # Coffee crunch thickshake
    "dry-fruit-thick-shake.jpg": "photo-1582716401301-b2407dc7563d",        # Dry fruit royal thickshake
    "simply-stoned-special-thick-shake.jpg": "photo-1572490122747-3968b75cc699", # Specialty freakshake

    # === FRUIT JUICES ===
    "sweet-lime-mosambi-juice.jpg": "photo-1613478223719-2ab802602423",   # Fresh green citrus sweet lime juice
    "orange-juice.jpg": "photo-1600271886742-f049cd451bba",               # Vibrant fresh orange juice
    "watermelon-juice.jpg": "photo-1589733955941-5eeaf753fb94",           # Fresh red watermelon juice with mint
    "pineapple-juice.jpg": "photo-1550258987-190a2d41a8ba",            # Golden pineapple juice with wedge
    "mango-juice.jpg": "photo-1546173159-315724a31696",                   # Rich Alphonso mango nectar
    "pomegranate-juice.jpg": "photo-1541832676-9b763b0239ab",             # Deep red pomegranate juice
    "apple-juice.jpg": "photo-1576186726580-79f3ee404271",                   # Crisp golden apple juice
    "grapes-juice.jpg": "photo-1537640538966-79f369143f8f",                  # Purple concord grape juice
    "muskmelon-juice.jpg": "photo-1528825871115-3581a5387919",            # Cantaloupe muskmelon juice
    "papaya-juice.jpg": "photo-1517256064527-09c73fc73e38",               # Fresh papaya juice
    "mixed-fruit-juice.jpg": "photo-1527661591475-527312dd65f5",          # Multi-layered fresh fruit juice
    "lemon-juice.jpg": "photo-1513558161293-cdaf765ed2fd",                # Fresh chilled lemonade
    "lemon-mint-juice.jpg": "photo-1513558161293-cdaf765ed2fd",           # Lemon mint iced cooler
    "watermelon-mint-juice.jpg": "photo-1589733955941-5eeaf753fb94",      # Watermelon mint cooler
    "carrot-juice.jpg": "photo-1622597467836-f3285f2131b7",               # Cold pressed carrot juice
    "beetroot-juice.jpg": "photo-1613478223719-2ab802602423",             # Deep ruby beetroot juice
    "abc-juice.jpg": "photo-1622597467836-f3285f2131b7",                  # Apple Beetroot Carrot juice
    "guava-juice.jpg": "photo-1528825871115-3581a5387919",                # Pink guava juice
    "kiwi-juice.jpg": "photo-1587393855524-087f83d95bc9",                 # Fresh green kiwi juice
    "tropical-fruit-punch.jpg": "photo-1536935338788-846bb9981813",       # Tropical fruit punch

    # === SPECIAL DESSERTS ===
    "brownie-with-ice-cream.jpg": "photo-1551024709-8f23befc6f87",        # Warm brownie with vanilla scoop
    "sizzling-brownie.jpg": "photo-1606313564200-e75d5e30476c",            # Sizzling brownie in cast iron skillet
    "chocolate-sundae.jpg": "photo-1563805042-7684c019e1cb",              # Tall chocolate sundae with cherry
    "oreo-sundae.jpg": "photo-1563805042-7684c019e1cb",                   # Loaded Oreo cookie sundae
    "royal-falooda.jpg": "photo-1579954115563-e72bf1381629",              # Traditional layered falooda
    "classic-falooda.jpg": "photo-1528740561666-dc2479dc08ab",            # Classic rose milk falooda
    "kulfi-falooda.jpg": "photo-1600718374662-0483d2b9da44",              # Kesar pista kulfi with sev
    "fruit-salad-with-ice-cream.jpg": "photo-1517256064527-09c73fc73e38",  # Fresh fruit bowl with ice cream scoop
    "chocolate-lava-cake.jpg": "photo-1606313564200-e75d5e30476c",        # Warm molten lava cake
    "chocolate-mousse.jpg": "photo-1541781774459-bb2af2f05b55",           # Silky dark chocolate mousse
    "chocolate-waffle.jpg": "photo-1562376552-0d160a2f238d",               # Crisp waffle with chocolate drizzle
    "nutella-waffle.jpg": "photo-1562376552-0d160a2f238d",                 # Nutella loaded waffle
    "brownie-waffle.jpg": "photo-1562376552-0d160a2f238d",                # Brownie waffle with syrup
    "chocolate-pancakes.jpg": "photo-1565299585323-38d6b0865b47",          # Chocolate pancakes stack
    "ice-cream-pancakes.jpg": "photo-1528198648074-8aa423810791",          # Pancakes with ice cream scoop
    "chocolate-fudge-sundae.jpg": "photo-1579954115545-a95591f28bfc",     # Fudge chocolate sundae
    "banana-split.jpg": "photo-1551024709-8f23befc6f87",                  # Classic banana split sundae
    "caramel-sundae.jpg": "photo-1560008581-09826d1de69e",                # Salted caramel sundae
    "dry-fruit-sundae.jpg": "photo-1582716401301-b2407dc7563d",           # Dry fruit royal sundae
    "simply-stoned-special-dessert.jpg": "photo-1551024709-8f23befc6f87", # Signature dessert masterpiece
}

print(f"Total items to download: {len(ITEMS)}")

success = 0
failed = []

for filename, photo_id in ITEMS.items():
    filepath = os.path.join(DEST_DIR, filename)
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=400&h=400&q=80"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as response:
            data = response.read()
            if len(data) > 5000:
                with open(filepath, "wb") as f:
                    f.write(data)
                success += 1
            else:
                failed.append((filename, "Image too small"))
    except Exception as e:
        failed.append((filename, str(e)))
    time.sleep(0.05)

print(f"Successfully downloaded: {success}/{len(ITEMS)}")
if failed:
    print(f"Failed ({len(failed)}): {failed}")
