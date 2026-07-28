from sqlalchemy.orm import Session

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from backend import models


def get_similar_products(

    db: Session,

    product_id: int,

    limit: int = 6

):

    # ============================================
    # CURRENT PRODUCT
    # ============================================

    current_product = (

        db.query(models.Product)

        .filter(

            models.Product.id == product_id

        )

        .first()

    )


    if not current_product:

        return []


    # ============================================
    # OTHER PRODUCTS
    # ============================================

    products = (

        db.query(models.Product)

        .filter(

            models.Product.id != product_id

        )

        .all()

    )


    if not products:

        return []


    # ============================================
    # CREATE TEXT FEATURES
    # ============================================

    all_products = [

        current_product

    ] + products


    product_texts = []


    for product in all_products:

        text = " ".join([

            product.name or "",

            product.description or "",

            product.colors or "",

            product.sizes or "",

            str(product.category_id or "")

        ])


        product_texts.append(text)


    # ============================================
    # TF-IDF
    # ============================================

    vectorizer = TfidfVectorizer(

        stop_words="english"

    )


    tfidf_matrix = (

        vectorizer.fit_transform(

            product_texts

        )

    )


    # ============================================
    # TEXT SIMILARITY
    # ============================================

    text_similarity = cosine_similarity(

        tfidf_matrix[0:1],

        tfidf_matrix[1:]

    )[0]


    # ============================================
    # CALCULATE FINAL SCORE
    # ============================================

    scored_products = []


    current_price = (

        current_product.price or 0

    )


    current_rating = (

        current_product.rating or 0

    )


    for index, product in enumerate(products):


        # ----------------------------------------
        # TF-IDF SCORE
        # ----------------------------------------

        tfidf_score = (

            float(text_similarity[index])

        )


        # ----------------------------------------
        # CATEGORY SCORE
        # ----------------------------------------

        category_score = (

            1.0

            if product.category_id ==

            current_product.category_id

            else 0.0

        )


        # ----------------------------------------
        # PRICE SIMILARITY
        # ----------------------------------------

        product_price = (

            product.price or 0

        )


        max_price = max(

            current_price,

            product_price,

            1

        )


        price_difference = abs(

            current_price -

            product_price

        )


        price_score = max(

            0,

            1 -

            (

                price_difference /

                max_price

            )

        )


        # ----------------------------------------
        # RATING SCORE
        # ----------------------------------------

        rating_score = (

            (product.rating or 0) / 5

        )


        # ----------------------------------------
        # FINAL WEIGHTED SCORE
        # ----------------------------------------

        final_score = (

            (tfidf_score * 0.60)

            +

            (category_score * 0.25)

            +

            (price_score * 0.10)

            +

            (rating_score * 0.05)

        )


        scored_products.append(

            (

                product,

                final_score

            )

        )


    # ============================================
    # SORT BY FINAL SCORE
    # ============================================

    scored_products.sort(

        key=lambda item: item[1],

        reverse=True

    )


    # ============================================
    # RETURN TOP PRODUCTS
    # ============================================

    return [

        product

        for product, score

        in scored_products[:limit]

    ]