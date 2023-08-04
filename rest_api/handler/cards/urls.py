from .views import CardsV1,AdminCards,AdminFailedCards,AdminSuccessfullCards
def card_urls_v1(app,prefix):
    app.add_url_rule(
        f"/{prefix}/cards",
        view_func = CardsV1.as_view('cards'),
        methods=["GET","POST","PATCH"],
    )
    app.add_url_rule(
        f"/{prefix}/admin/cards",
        view_func = AdminCards.as_view('cards_all_or_one'),
        methods=["GET","DELETE"],
    )
    app.add_url_rule(
        f"/{prefix}/admin/cards/success",
        view_func = AdminSuccessfullCards.as_view('cards_successfull'),
        methods=["GET"],
    )
    app.add_url_rule(
        f"/{prefix}/admin/cards/failed",
        view_func = AdminFailedCards.as_view('cards_failed'),
        methods=["GET"],
    )