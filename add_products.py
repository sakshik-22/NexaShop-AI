import requests
import json

base_url = "http://localhost:8000/products/"

new_products = [
    {
        "name": "Neon Cyberpunk Jacket",
        "description": "A futuristic glowing jacket for nightlife.",
        "price": 199.99,
        "discount": 0.0,
        "rating": 4.8,
        "image_url": "https://images.unsplash.com/photo-1551028719-01c8cd9920b7?w=500&q=80",
        "category_id": 1,
        "colors": "Black,Neon Green",
        "sizes": "M,L"
    },
    {
        "name": "Urban Techwear Cargo Pants",
        "description": "Water-resistant techwear pants with multiple utility pockets.",
        "price": 89.99,
        "discount": 10.0,
        "rating": 4.6,
        "image_url": "https://images.unsplash.com/photo-1521235122557-41a457ee5b13?w=500&q=80",
        "category_id": 1,
        "colors": "Black,Grey",
        "sizes": "S,M,L,XL"
    },
    {
        "name": "Minimalist White Sneakers",
        "description": "Classic all-white leather sneakers suitable for every outfit.",
        "price": 75.0,
        "discount": 0.0,
        "rating": 4.9,
        "image_url": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=500&q=80",
        "category_id": 4,
        "colors": "White",
        "sizes": "8,9,10,11"
    },
    {
        "name": "Sapphire Statement Ring",
        "description": "Elegant silver ring featuring a deep blue sapphire.",
        "price": 250.0,
        "discount": 20.0,
        "rating": 4.7,
        "image_url": "https://images.unsplash.com/photo-1605100804763-247f67b2548e?w=500&q=80",
        "category_id": 6,
        "colors": "Silver",
        "sizes": "6,7,8"
    }
]

for p in new_products:
    try:
        response = requests.post(base_url, json=p)
        if response.status_code == 200:
            print(f"Added: {p['name']}")
        else:
            print(f"Failed to add {p['name']}: {response.text}")
    except Exception as e:
        print(f"Error adding {p['name']}: {e}")
