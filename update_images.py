from backend.database import SessionLocal
from backend import models


# ============================================================
# MANUALLY SELECTED IMAGE URLS
# ============================================================

image_updates = {

    # =========================
    # MEN'S FASHION
    # =========================

    "Classic Cotton T-Shirt":
        "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800",

    "Slim Fit Denim Jeans":
        "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=800",

    "Casual Oxford Shirt":
        "https://images.unsplash.com/photo-1603252110481-7ba873bf42ab?w=800",

    "Premium Leather Jacket":
        "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800",

    "Athletic Joggers":
        "https://images.unsplash.com/photo-1552902865-b72c031ac5ea?w=800",

    "Classic Polo T-Shirt":
        "https://images.unsplash.com/photo-1625910513413-5fc45e9ae5d5?w=800",

    "Formal Blazer":
        "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800",

    "Winter Hoodie":
        "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800",

    "Classic Chino Pants":
        "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=800",

    "Premium Casual Shirt":
        "https://images.unsplash.com/photo-1617127365659-c47fa864d8bc?w=800",


    # =========================
    # WOMEN'S FASHION
    # =========================

    "Elegant Floral Dress":
        "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=800",

    "Casual Denim Jacket":
        "https://images.unsplash.com/photo-1543076447-215ad9ba6923?w=800",

    "Premium Handbag":
        "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800",

    "Classic Women's Top":
        "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=800",

    "Traditional Saree":
        "https://images.unsplash.com/photo-1610030469983-98e550d6193c?w=800",

    "Women's Wide Leg Pants":
        "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=800",

    "Stylish Sunglasses":
        "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=800",

    "Elegant Party Gown":
        "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=800",

    "Minimalist Watch":
        "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=800",

    "Comfortable Cotton Kurti":
        "https://images.unsplash.com/photo-1583391733956-6c78276477e2?w=800",


    # =========================
    # ELECTRONICS
    # =========================

    "Wireless Bluetooth Headphones":
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800",

    "Smart Fitness Watch":
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800",

    "Portable Bluetooth Speaker":
        "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800",

    "Wireless Mechanical Keyboard":
        "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800",

    "Ergonomic Wireless Mouse":
        "https://images.unsplash.com/photo-1527814050087-3793815479db?w=800",

    "Smartphone Pro":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",

    "HD Webcam":
        "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800",

    "Fast Charging Power Bank":
        "https://images.unsplash.com/photo-1609592424754-7e0a7b7f3a3c?w=800",

    "Wireless Earbuds":
        "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800",

    "LED Desk Lamp":
        "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800",


    # =========================
    # HOME DECOR
    # =========================

    "Modern Wall Art":
        "https://images.unsplash.com/photo-1549490349-8643362247b5?w=800",

    "Decorative Table Lamp":
        "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800",

    "Indoor Green Plant":
        "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800",

    "Luxury Cushion Set":
        "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=800",

    "Minimalist Wall Clock":
        "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=800",

    "Decorative Ceramic Vase":
        "https://images.unsplash.com/photo-1612196808214-b8e1d6145a8c?w=800",

    "Soft Area Rug":
        "https://images.unsplash.com/photo-1600166898405-da9535204843?w=800",

    "Scented Candle Set":
        "https://images.unsplash.com/photo-1603006905003-be475563bc59?w=800",

    "Modern Mirror":
        "https://images.unsplash.com/photo-1618220179428-22790b461013?w=800",

    "Decorative Storage Basket":
        "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800",


    # =========================
    # KITCHEN
    # =========================

    "Non Stick Cookware Set":
        "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800",

    "Electric Coffee Maker":
        "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?w=800",

    "Stainless Steel Water Bottle":
        "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800",

    "Modern Dinner Set":
        "https://images.unsplash.com/photo-1603199506016-b9a594b593c0?w=800",

    "Smart Electric Kettle":
        "https://images.unsplash.com/photo-1594213114663-d94db9b17119?w=800",

    "Kitchen Knife Set":
        "https://images.unsplash.com/photo-1593618998160-e34014e67546?w=800",

    "Bamboo Cutting Board":
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=800",

    "Digital Kitchen Scale":
        "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800",

    "Glass Storage Container Set":
        "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=800",

    "Automatic Spice Organizer":
        "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=800",


    # =========================
    # TOYS
    # =========================

    "Remote Control Racing Car":
        "https://images.unsplash.com/photo-1594787318286-3d835c1d207f?w=800",

    "Building Blocks Set":
        "https://images.unsplash.com/photo-1587654780291-39c9404d746b?w=800",

    "Strategy Board Game":
        "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?w=800",

    "Soft Teddy Bear":
        "https://images.unsplash.com/photo-1559454403-b8fb88521f11?w=800",

    "Kids Art Creativity Kit":
        "https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=800",

    "Mini Drone":
        "https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=800",

    "Educational Puzzle Set":
        "https://images.unsplash.com/photo-1606503153255-59d8b8b7f6e8?w=800",

    "Classic Toy Train":
        "https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?w=800",

    "Basketball Game Set":
        "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800",

    "Kids Musical Keyboard":
        "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?w=800",


    # =========================
    # SHOES
    # =========================

    "Classic White Sneakers":
        "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=800",

    "Running Sports Shoes":
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",

    "Leather Formal Shoes":
        "https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=800",

    "Comfortable Casual Loafers":
        "https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=800",

    "Women's Fashion Heels":
        "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=800",

    "Comfortable Women's Flats":
        "https://images.unsplash.com/photo-1560343090-f0409e92791a?w=800",

    "Outdoor Hiking Boots":
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",

    "Classic Canvas Shoes":
        "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=800",

    "Comfort Walking Shoes":
        "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=800",

    "Stylish Ankle Boots":
        "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=800",


    # =========================
    # PHONES
    # =========================

    "iPhone 15 Pro":
        "https://images.unsplash.com/photo-1696446701796-da61225697cc?w=800",

    "Samsung Galaxy S24":
        "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=800",

    "Google Pixel 8":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800",

    "OnePlus 12":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",

    "Xiaomi 14":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",

    "Nothing Phone 2":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800",

    "Vivo V30 Pro":
        "https://images.unsplash.com/photo-1556656793-08538906a9f8?w=800",

    "OPPO Reno 11 Pro":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800",

    "Motorola Edge 50 Pro":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",

    "Realme GT 6":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=800",


    # =========================
    # LAPTOPS
    # =========================

    "MacBook Air M3":
        "https://images.unsplash.com/photo-1517336714739-489689fd1ca8?w=800",

    "Dell XPS 15":
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800",

    "HP Pavilion 15":
        "https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=800",

    "Lenovo IdeaPad Slim 5":
        "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=800",

    "ASUS ROG Gaming Laptop":
        "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=800",


    # =========================
    # AUDIO
    # =========================

    "Sony WH-1000XM5":
        "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=800",

    "Apple AirPods Pro":
        "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=800",

    "Bose QuietComfort":
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800",

    "JBL Live 660NC":
        "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=800",

    "Samsung Galaxy Buds":
        "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=800",


    # =========================
    # EXTRA FASHION
    # =========================

    "Premium Linen Shirt":
        "https://images.unsplash.com/photo-1602810319428-019690571b5b?w=800",

    "Relaxed Fit Cargo Pants":
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800",

    "Premium Crewneck Sweatshirt":
        "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=800",

    "Denim Trucker Jacket":
        "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=800",

    "Athletic Performance T-Shirt":
        "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800",

    "Premium Wool Coat":
        "https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?w=800",

    "Casual Printed Shirt":
        "https://images.unsplash.com/photo-1603252110481-7ba873bf42ab?w=800",

    "Stretch Denim Shorts":
        "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=800",

    "Premium Track Jacket":
        "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=800",

    "Classic V-Neck Sweater":
        "https://images.unsplash.com/photo-1610652492500-ded49ceeb378?w=800",


    # =========================
    # WOMEN'S EXTRA
    # =========================

    "Elegant Satin Blouse":
        "https://images.unsplash.com/photo-1564257577054-1c4f7a1b3c1d?w=800",

    "High Waist Denim Jeans":
        "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=800",

    "Casual Cotton Jumpsuit":
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=800",

    "Premium Shoulder Bag":
        "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800",

    "Elegant Long Skirt":
        "https://images.unsplash.com/photo-1583496661160-fb5886a13d27?w=800",

    "Women's Winter Sweater":
        "https://images.unsplash.com/photo-1485968579580-b6d095142e6e?w=800",

    "Stylish Crossbody Bag":
        "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?w=800",

    "Casual Summer Skirt":
        "https://images.unsplash.com/photo-1551028719-01c8cd9920b7?w=800",

    "Premium Women's Blazer":
        "https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=800",

    "Elegant Evening Clutch":
        "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=800",


    # =========================
    # HOME EXTRA
    # =========================

    "Modern Floor Lamp":
        "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800",

    "Bohemian Wall Decor":
        "https://images.unsplash.com/photo-1549490349-8643362247b5?w=800",

    "Decorative Throw Blanket":
        "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=800",

    "Wooden Coffee Table":
        "https://images.unsplash.com/photo-1532372320572-cda25653a26d?w=800",

    "Decorative Photo Frame Set":
        "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=800",

    "Luxury Bedding Set":
        "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800",

    "Ceramic Plant Pot Set":
        "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800",

    "Decorative Wall Shelf":
        "https://images.unsplash.com/photo-1594620302200-9a762244a156?w=800",

    "Luxury Table Centerpiece":
        "https://images.unsplash.com/photo-1618220179428-22790b461013?w=800",

    "Modern Decorative Lantern":
        "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=800",


    # =========================
    # KITCHEN EXTRA
    # =========================

    "Air Fryer":
        "https://images.unsplash.com/photo-1585515320310-259814833e62?w=800",

    "Electric Hand Blender":
        "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=800",

    "Premium Mixer Grinder":
        "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=800",

    "Bamboo Kitchen Organizer":
        "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800",

    "Ceramic Coffee Mug Set":
        "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=800",

    "Glass Food Storage Set":
        "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=800",

    "Modern Kitchen Utensil Set":
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=800",

    "Electric Toaster":
        "https://images.unsplash.com/photo-1585238342024-78d387f4a707?w=800",

    "Premium Ceramic Dinner Plates":
        "https://images.unsplash.com/photo-1603199506016-b9a594b593c0?w=800",

    "Reusable Silicone Food Bags":
        "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=800",


    # =========================
    # FITNESS
    # =========================

    "Premium Yoga Mat":
        "https://images.unsplash.com/photo-1592432678016-e910b452f9a2?w=800",

    "Adjustable Dumbbell Set":
        "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=800",

    "Fitness Resistance Bands":
        "https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=800",

    "Sports Water Bottle":
        "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800",


    # =========================
    # BEAUTY
    # =========================

    "Skincare Essentials Kit":
        "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=800",

    "Premium Makeup Brush Set":
        "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=800",

    "Hair Styling Tool":
        "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=800",

    "Luxury Perfume":
        "https://images.unsplash.com/photo-1541643600914-78b084683601?w=800",

    "Moisturizing Body Lotion":
        "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=800",


    # =========================
    # BOOKS
    # =========================

    "The Psychology of Money":
        "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800",

    "Atomic Habits":
        "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=800",

    "Deep Work":
        "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800",

    "Rich Dad Poor Dad":
        "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=800",

    "The Alchemist":
        "https://images.unsplash.com/photo-1511108690759-009324a90311?w=800",
}


# ============================================================
# UPDATE DATABASE
# ============================================================

db = SessionLocal()

try:

    products = db.query(models.Product).all()

    updated_count = 0

    for product in products:

        # If exact product URL exists
        if product.name in image_updates:

            product.image_url = image_updates[product.name]

            print(f"Updated: {product.name}")

        else:

            # Automatic fallback image
            safe_name = (
                product.name
                .replace(" ", ",")
                .replace("'", "")
            )

            product.image_url = (
                f"https://loremflickr.com/800/800/"
                f"{safe_name}?lock={product.id}"
            )

            print(f"Fallback image added: {product.name}")

        updated_count += 1


    db.commit()


    print("\n========================================")
    print("IMAGE URL UPDATE COMPLETED")
    print("========================================")
    print(f"Total products processed: {updated_count}")
    print("Empty image URLs: 0")
    print("========================================\n")


except Exception as error:

    db.rollback()

    print("\nERROR:")
    print(error)


finally:

    db.close()