from .views import CardsV1
def card_urls_v1(app,prefix):
    app.add_url_rule(
        f"/{prefix}/cards",
        view_func = CardsV1.as_view('cards'),
        methods=["GET","POST"],
    )