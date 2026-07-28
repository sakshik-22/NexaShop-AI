from backend.database import SessionLocal
from backend import models


# ============================================
# ALL PRODUCTS DATA
# ============================================

products_data = [

    # ========================================
    # ELECTRONICS - MOBILE PHONES
    # ========================================

    {
        "name": "iPhone 15 Pro",
        "description": "Premium smartphone with powerful performance and advanced camera system.",
        "price": 99999,
        "discount": 8,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1696446701796-da61225697cc?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,Natural Titanium",
        "sizes": "128GB,256GB,512GB"
    },

    {
        "name": "Samsung Galaxy S24",
        "description": "Flagship Android smartphone with vibrant display and powerful performance.",
        "price": 74999,
        "discount": 10,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,Silver",
        "sizes": "128GB,256GB"
    },

    {
        "name": "Google Pixel 8",
        "description": "Smartphone with excellent camera technology and clean Android experience.",
        "price": 59999,
        "discount": 12,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,White",
        "sizes": "128GB,256GB"
    },

    {
        "name": "OnePlus 12",
        "description": "High performance smartphone with fast charging and premium display.",
        "price": 64999,
        "discount": 10,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500",
        "category": "Electronics",
        "colors": "Black,Green,Silver",
        "sizes": "256GB,512GB"
    },

    {
        "name": "Xiaomi 14",
        "description": "Powerful compact smartphone with premium camera and flagship performance.",
        "price": 69999,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500",
        "category": "Electronics",
        "colors": "Black,White,Green",
        "sizes": "256GB,512GB"
    },

    {
        "name": "Nothing Phone 2",
        "description": "Modern smartphone with unique design, smooth display and strong performance.",
        "price": 44999,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500",
        "category": "Electronics",
        "colors": "Black,White",
        "sizes": "128GB,256GB"
    },

    {
        "name": "Vivo V30 Pro",
        "description": "Stylish smartphone with high quality camera and vibrant curved display.",
        "price": 41999,
        "discount": 12,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1556656793-08538906a9f8?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,Gold",
        "sizes": "256GB"
    },

    {
        "name": "OPPO Reno 11 Pro",
        "description": "Elegant smartphone with portrait photography and fast charging features.",
        "price": 38999,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500",
        "category": "Electronics",
        "colors": "Black,Blue",
        "sizes": "256GB"
    },

    {
        "name": "Motorola Edge 50 Pro",
        "description": "Premium smartphone with smooth performance and immersive display.",
        "price": 34999,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,White",
        "sizes": "256GB"
    },

    {
        "name": "Realme GT 6",
        "description": "Performance focused smartphone with fast processor and premium display.",
        "price": 39999,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500",
        "category": "Electronics",
        "colors": "Black,Silver,Green",
        "sizes": "256GB,512GB"
    },


    # ========================================
    # ELECTRONICS - LAPTOPS
    # ========================================

    {
        "name": "MacBook Air M3",
        "description": "Powerful lightweight laptop with Apple M3 chip and long battery life.",
        "price": 114999,
        "discount": 8,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8?w=500",
        "category": "Electronics",
        "colors": "Silver,Midnight,Starlight",
        "sizes": "256GB,512GB"
    },

    {
        "name": "Dell XPS 15",
        "description": "Premium performance laptop with powerful processor and stunning display.",
        "price": 129999,
        "discount": 10,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500",
        "category": "Electronics",
        "colors": "Silver,Black",
        "sizes": "512GB,1TB"
    },

    {
        "name": "HP Pavilion 15",
        "description": "Reliable everyday laptop for work, study and entertainment.",
        "price": 59999,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1484788984921-03950022c9ef?w=500",
        "category": "Electronics",
        "colors": "Silver,Black",
        "sizes": "512GB"
    },

    {
        "name": "Lenovo IdeaPad Slim 5",
        "description": "Slim and powerful laptop designed for productivity and daily use.",
        "price": 64999,
        "discount": 12,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=500",
        "category": "Electronics",
        "colors": "Grey,Silver",
        "sizes": "512GB"
    },

    {
        "name": "ASUS ROG Gaming Laptop",
        "description": "High performance gaming laptop with powerful graphics and cooling.",
        "price": 139999,
        "discount": 10,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=500",
        "category": "Electronics",
        "colors": "Black",
        "sizes": "1TB"
    },


    # ========================================
    # ELECTRONICS - HEADPHONES
    # ========================================

    {
        "name": "Sony WH-1000XM5",
        "description": "Premium wireless noise cancelling headphones with immersive sound.",
        "price": 29999,
        "discount": 15,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500",
        "category": "Electronics",
        "colors": "Black,Silver",
        "sizes": "One Size"
    },

    {
        "name": "Apple AirPods Pro",
        "description": "Premium wireless earbuds with active noise cancellation and spatial audio.",
        "price": 24999,
        "discount": 10,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=500",
        "category": "Electronics",
        "colors": "White",
        "sizes": "One Size"
    },

    {
        "name": "Bose QuietComfort",
        "description": "Comfortable wireless headphones with powerful noise cancellation.",
        "price": 27999,
        "discount": 12,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "category": "Electronics",
        "colors": "Black,White",
        "sizes": "One Size"
    },

    {
        "name": "JBL Live 660NC",
        "description": "Wireless noise cancelling headphones with powerful JBL sound.",
        "price": 8999,
        "discount": 20,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1484704849700-f032a568e944?w=500",
        "category": "Electronics",
        "colors": "Black,Blue,White",
        "sizes": "One Size"
    },

    {
        "name": "Samsung Galaxy Buds",
        "description": "Compact wireless earbuds with clear sound and comfortable fit.",
        "price": 9999,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500",
        "category": "Electronics",
        "colors": "Black,White",
        "sizes": "One Size"
    },


    # ========================================
    # MEN FASHION
    # ========================================

    {
        "name": "Premium Linen Shirt",
        "description": "Breathable premium linen shirt for stylish summer and casual wear.",
        "price": 1699,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1602810319428-019690571b5b?w=500",
        "category": "Men",
        "colors": "White,Blue,Beige",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Relaxed Fit Cargo Pants",
        "description": "Comfortable utility cargo pants with a modern relaxed fit.",
        "price": 1799,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=500",
        "category": "Men",
        "colors": "Black,Olive,Beige",
        "sizes": "30,32,34,36"
    },

    {
        "name": "Premium Crewneck Sweatshirt",
        "description": "Soft premium cotton sweatshirt for comfortable everyday styling.",
        "price": 1599,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=500",
        "category": "Men",
        "colors": "Black,Grey,Navy",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Denim Trucker Jacket",
        "description": "Classic denim trucker jacket with a timeless casual design.",
        "price": 2499,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=500",
        "category": "Men",
        "colors": "Blue,Black",
        "sizes": "M,L,XL"
    },

    {
        "name": "Athletic Performance T-Shirt",
        "description": "Lightweight breathable performance t-shirt for sports and workouts.",
        "price": 899,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500",
        "category": "Men",
        "colors": "Black,Blue,Green",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Premium Wool Coat",
        "description": "Elegant warm wool coat designed for a sophisticated winter look.",
        "price": 5999,
        "discount": 20,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1539533113208-f6df8cc8b543?w=500",
        "category": "Men",
        "colors": "Black,Grey,Beige",
        "sizes": "M,L,XL"
    },

    {
        "name": "Casual Printed Shirt",
        "description": "Modern printed shirt perfect for casual outings and vacations.",
        "price": 1299,
        "discount": 10,
        "rating": 4.4,
        "image_url": "https://images.unsplash.com/photo-1603252110481-7ba873bf42ab?w=500",
        "category": "Men",
        "colors": "Blue,White,Green",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Stretch Denim Shorts",
        "description": "Comfortable stretch denim shorts for relaxed everyday wear.",
        "price": 999,
        "discount": 10,
        "rating": 4.4,
        "image_url": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=500",
        "category": "Men",
        "colors": "Blue,Black",
        "sizes": "30,32,34,36"
    },

    {
        "name": "Premium Track Jacket",
        "description": "Sporty lightweight track jacket for active and casual lifestyles.",
        "price": 2199,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=500",
        "category": "Men",
        "colors": "Black,Navy,Grey",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Classic V-Neck Sweater",
        "description": "Soft knitted sweater with a classic fit for smart casual styling.",
        "price": 1999,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1610652492500-ded49ceeb378?w=500",
        "category": "Men",
        "colors": "Grey,Navy,Brown",
        "sizes": "M,L,XL"
    },

        # ========================================
    # WOMEN FASHION
    # ========================================

    {
        "name": "Elegant Satin Blouse",
        "description": "Elegant satin blouse with a smooth premium finish for modern styling.",
        "price": 1499,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1564257577054-1c4f7a1b3c1d?w=500",
        "category": "Women",
        "colors": "White,Pink,Black",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "High Waist Denim Jeans",
        "description": "Comfortable high waist denim jeans with a flattering modern fit.",
        "price": 1899,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500",
        "category": "Women",
        "colors": "Blue,Black",
        "sizes": "26,28,30,32"
    },

    {
        "name": "Casual Cotton Jumpsuit",
        "description": "Stylish comfortable cotton jumpsuit for effortless everyday fashion.",
        "price": 2199,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=500",
        "category": "Women",
        "colors": "Black,Beige,Blue",
        "sizes": "S,M,L"
    },

    {
        "name": "Premium Shoulder Bag",
        "description": "Elegant shoulder bag with spacious compartments for everyday use.",
        "price": 1999,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?w=500",
        "category": "Women",
        "colors": "Black,Brown,Beige",
        "sizes": "One Size"
    },

    {
        "name": "Elegant Long Skirt",
        "description": "Flowing elegant long skirt perfect for casual and special occasions.",
        "price": 1399,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1583496661160-fb5886a13d27?w=500",
        "category": "Women",
        "colors": "Black,Blue,Beige",
        "sizes": "S,M,L"
    },

    {
        "name": "Women's Winter Sweater",
        "description": "Warm soft sweater designed for comfortable winter fashion.",
        "price": 1799,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1485968579580-b6d095142e6e?w=500",
        "category": "Women",
        "colors": "White,Grey,Pink",
        "sizes": "S,M,L,XL"
    },

    {
        "name": "Stylish Crossbody Bag",
        "description": "Compact stylish crossbody bag perfect for everyday essentials.",
        "price": 1299,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1594223274512-ad4803739b7c?w=500",
        "category": "Women",
        "colors": "Black,Brown,Red",
        "sizes": "One Size"
    },

    {
        "name": "Casual Summer Skirt",
        "description": "Lightweight summer skirt with a comfortable stylish design.",
        "price": 999,
        "discount": 10,
        "rating": 4.4,
        "image_url": "https://images.unsplash.com/photo-1551028719-01c8cd9920b7?w=500",
        "category": "Women",
        "colors": "Blue,White,Yellow",
        "sizes": "S,M,L"
    },

    {
        "name": "Premium Women's Blazer",
        "description": "Modern tailored blazer for professional and smart casual outfits.",
        "price": 2999,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=500",
        "category": "Women",
        "colors": "Black,Navy,Beige",
        "sizes": "S,M,L"
    },

    {
        "name": "Elegant Evening Clutch",
        "description": "Stylish compact clutch designed for parties and special occasions.",
        "price": 1199,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500",
        "category": "Women",
        "colors": "Black,Gold,Silver",
        "sizes": "One Size"
    },


    # ========================================
    # HOME & DECOR
    # ========================================

    {
        "name": "Modern Floor Lamp",
        "description": "Stylish floor lamp that adds warm ambient lighting to modern interiors.",
        "price": 2499,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500",
        "category": "Home & Decor",
        "colors": "Black,Gold,White",
        "sizes": "Large"
    },

    {
        "name": "Bohemian Wall Decor",
        "description": "Beautiful bohemian wall decor for adding personality to your home.",
        "price": 999,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1549490349-8643362247b5?w=500",
        "category": "Home & Decor",
        "colors": "Beige,Brown,White",
        "sizes": "Medium"
    },

    {
        "name": "Decorative Throw Blanket",
        "description": "Soft decorative throw blanket for cozy living rooms and bedrooms.",
        "price": 1299,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=500",
        "category": "Home & Decor",
        "colors": "Beige,Grey,Blue",
        "sizes": "Large"
    },

    {
        "name": "Wooden Coffee Table",
        "description": "Minimalist wooden coffee table designed for modern living spaces.",
        "price": 4999,
        "discount": 20,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1532372320572-cda25653a26d?w=500",
        "category": "Home & Decor",
        "colors": "Brown,Black",
        "sizes": "Medium"
    },

    {
        "name": "Decorative Photo Frame Set",
        "description": "Elegant photo frame set for displaying memorable moments at home.",
        "price": 899,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=500",
        "category": "Home & Decor",
        "colors": "Black,White,Gold",
        "sizes": "Set of 3"
    },

    {
        "name": "Luxury Bedding Set",
        "description": "Soft premium bedding set designed for comfortable restful sleep.",
        "price": 2999,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=500",
        "category": "Home & Decor",
        "colors": "White,Grey,Beige",
        "sizes": "Queen,King"
    },

    {
        "name": "Ceramic Plant Pot Set",
        "description": "Modern ceramic plant pots perfect for indoor plants and decor.",
        "price": 799,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=500",
        "category": "Home & Decor",
        "colors": "White,Beige,Grey",
        "sizes": "Set of 3"
    },

    {
        "name": "Decorative Wall Shelf",
        "description": "Modern wall shelf for organizing books, plants and decorative items.",
        "price": 1199,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1594620302200-9a762244a156?w=500",
        "category": "Home & Decor",
        "colors": "Brown,Black,White",
        "sizes": "Medium"
    },

    {
        "name": "Luxury Table Centerpiece",
        "description": "Elegant centerpiece designed to enhance dining and living room decor.",
        "price": 1099,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1618220179428-22790b461013?w=500",
        "category": "Home & Decor",
        "colors": "Gold,White,Black",
        "sizes": "Medium"
    },

    {
        "name": "Modern Decorative Lantern",
        "description": "Stylish decorative lantern that creates a warm relaxing atmosphere.",
        "price": 899,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=500",
        "category": "Home & Decor",
        "colors": "Black,Gold,White",
        "sizes": "Medium"
    },


    # ========================================
    # KITCHEN
    # ========================================

    {
        "name": "Air Fryer",
        "description": "Modern air fryer for preparing crispy meals with less oil.",
        "price": 4999,
        "discount": 20,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=500",
        "category": "Kitchen",
        "colors": "Black,Silver",
        "sizes": "4L,6L"
    },

    {
        "name": "Electric Hand Blender",
        "description": "Powerful hand blender for smoothies, soups and everyday cooking.",
        "price": 1499,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=500",
        "category": "Kitchen",
        "colors": "Black,White",
        "sizes": "One Size"
    },

    {
        "name": "Premium Mixer Grinder",
        "description": "Powerful mixer grinder for blending, grinding and everyday kitchen tasks.",
        "price": 3499,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=500",
        "category": "Kitchen",
        "colors": "Black,Silver",
        "sizes": "750W"
    },

    {
        "name": "Bamboo Kitchen Organizer",
        "description": "Eco-friendly organizer for neatly storing kitchen essentials.",
        "price": 899,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1556911220-bff31c812dba?w=500",
        "category": "Kitchen",
        "colors": "Brown",
        "sizes": "Medium"
    },

    {
        "name": "Ceramic Coffee Mug Set",
        "description": "Elegant ceramic coffee mugs perfect for everyday beverages and gifting.",
        "price": 699,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=500",
        "category": "Kitchen",
        "colors": "White,Black,Blue",
        "sizes": "Set of 4"
    },

    {
        "name": "Glass Food Storage Set",
        "description": "Durable airtight glass containers for organized food storage.",
        "price": 1299,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=500",
        "category": "Kitchen",
        "colors": "Transparent",
        "sizes": "Set of 6"
    },

    {
        "name": "Modern Kitchen Utensil Set",
        "description": "Complete durable utensil set for everyday cooking and serving.",
        "price": 1199,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=500",
        "category": "Kitchen",
        "colors": "Black,Silver",
        "sizes": "12 Piece"
    },

    {
        "name": "Electric Toaster",
        "description": "Compact electric toaster for quick and perfectly toasted breakfast.",
        "price": 1799,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1585238342024-78d387f4a707?w=500",
        "category": "Kitchen",
        "colors": "Black,Silver,White",
        "sizes": "2 Slice"
    },

    {
        "name": "Premium Ceramic Dinner Plates",
        "description": "Elegant ceramic plates designed for everyday meals and special occasions.",
        "price": 1499,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1603199506016-b9a594b593c0?w=500",
        "category": "Kitchen",
        "colors": "White,Blue",
        "sizes": "Set of 6"
    },

    {
        "name": "Reusable Silicone Food Bags",
        "description": "Reusable leak-proof silicone bags for convenient food storage.",
        "price": 799,
        "discount": 10,
        "rating": 4.4,
        "image_url": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=500",
        "category": "Kitchen",
        "colors": "Transparent,Blue",
        "sizes": "Set of 4"
    },

        # ========================================
    # SPORTS & FITNESS
    # ========================================

    {
        "name": "Premium Yoga Mat",
        "description": "Non-slip comfortable yoga mat for yoga, stretching and home workouts.",
        "price": 999,
        "discount": 10,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1592432678016-e910b452f9a2?w=500",
        "category": "Sports",
        "colors": "Black,Blue,Purple",
        "sizes": "Standard"
    },

    {
        "name": "Adjustable Dumbbell Set",
        "description": "Adjustable dumbbell set for strength training and home workouts.",
        "price": 2999,
        "discount": 15,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?w=500",
        "category": "Sports",
        "colors": "Black",
        "sizes": "10kg,20kg"
    },

    {
        "name": "Running Sports Shoes",
        "description": "Lightweight running shoes designed for comfort and daily workouts.",
        "price": 2499,
        "discount": 20,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
        "category": "Sports",
        "colors": "Black,White,Blue",
        "sizes": "6,7,8,9,10"
    },

    {
        "name": "Fitness Resistance Bands",
        "description": "Durable resistance bands for strength training and full body workouts.",
        "price": 799,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=500",
        "category": "Sports",
        "colors": "Black,Red,Blue",
        "sizes": "Set of 5"
    },

    {
        "name": "Sports Water Bottle",
        "description": "Durable leak-proof water bottle for gym, sports and outdoor activities.",
        "price": 699,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500",
        "category": "Sports",
        "colors": "Black,Blue,Green",
        "sizes": "750ml,1L"
    },


    # ========================================
    # BEAUTY & PERSONAL CARE
    # ========================================

    {
        "name": "Skincare Essentials Kit",
        "description": "Complete skincare essentials kit for a simple daily skincare routine.",
        "price": 1499,
        "discount": 15,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=500",
        "category": "Beauty",
        "colors": "Standard",
        "sizes": "Set"
    },

    {
        "name": "Premium Makeup Brush Set",
        "description": "Professional makeup brush set with soft and high quality bristles.",
        "price": 999,
        "discount": 20,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=500",
        "category": "Beauty",
        "colors": "Black,Pink",
        "sizes": "Set of 12"
    },

    {
        "name": "Hair Styling Tool",
        "description": "Multi-purpose hair styling tool for creating beautiful everyday hairstyles.",
        "price": 1999,
        "discount": 15,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=500",
        "category": "Beauty",
        "colors": "Black,Pink",
        "sizes": "One Size"
    },

    {
        "name": "Luxury Perfume",
        "description": "Elegant long-lasting fragrance with a premium sophisticated aroma.",
        "price": 2499,
        "discount": 10,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=500",
        "category": "Beauty",
        "colors": "Standard",
        "sizes": "50ml,100ml"
    },

    {
        "name": "Moisturizing Body Lotion",
        "description": "Hydrating body lotion for soft and smooth skin throughout the day.",
        "price": 599,
        "discount": 10,
        "rating": 4.5,
        "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=500",
        "category": "Beauty",
        "colors": "Standard",
        "sizes": "200ml,400ml"
    },


    # ========================================
    # BOOKS
    # ========================================

    {
        "name": "The Psychology of Money",
        "description": "Insightful book about money, investing, behavior and personal finance.",
        "price": 499,
        "discount": 10,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=500",
        "category": "Books",
        "colors": "Standard",
        "sizes": "Paperback"
    },

    {
        "name": "Atomic Habits",
        "description": "Practical guide to building good habits and breaking bad ones.",
        "price": 599,
        "discount": 15,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=500",
        "category": "Books",
        "colors": "Standard",
        "sizes": "Paperback,Hardcover"
    },

    {
        "name": "Deep Work",
        "description": "Guide to focused success in a distracted world.",
        "price": 499,
        "discount": 10,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500",
        "category": "Books",
        "colors": "Standard",
        "sizes": "Paperback"
    },

    {
        "name": "Rich Dad Poor Dad",
        "description": "Popular personal finance book about financial education and wealth building.",
        "price": 399,
        "discount": 10,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1519682337058-a94d519337bc?w=500",
        "category": "Books",
        "colors": "Standard",
        "sizes": "Paperback"
    },

    {
        "name": "The Alchemist",
        "description": "Inspirational novel about dreams, courage and following your purpose.",
        "price": 299,
        "discount": 10,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1511108690759-009324a90311?w=500",
        "category": "Books",
        "colors": "Standard",
        "sizes": "Paperback"
    },

]


# ============================================
# INSERT PRODUCTS INTO DATABASE
# ============================================

db = SessionLocal()

try:

    added_count = 0
    skipped_count = 0

    # Get existing categories
    categories = {
        category.name: category
        for category in db.query(models.Category).all()
    }

    for product_data in products_data:

        # Check duplicate product
        existing_product = (
            db.query(models.Product)
            .filter(
                models.Product.name == product_data["name"]
            )
            .first()
        )

        if existing_product:

            skipped_count += 1
            continue

        # Get category
        category_name = product_data["category"]

        category = categories.get(category_name)

        # Create category if not exists
        if not category:

            category = models.Category(
                name=category_name
            )

            db.add(category)
            db.commit()
            db.refresh(category)

            categories[category_name] = category

        # Create product
        product = models.Product(

            name=product_data["name"],

            description=product_data["description"],

            price=product_data["price"],

            discount=product_data["discount"],

            rating=product_data["rating"],

            image_url=product_data["image_url"],

            category_id=category.id,

            colors=product_data["colors"],

            sizes=product_data["sizes"],

        )

        db.add(product)

        added_count += 1

    db.commit()

    print("\n====================================")
    print("PRODUCT SEEDING COMPLETED")
    print("====================================")
    print(f"Products added: {added_count}")
    print(f"Products skipped: {skipped_count}")
    print("====================================\n")


except Exception as error:

    db.rollback()

    print("\nERROR OCCURRED:")
    print(error)


finally:

    db.close()