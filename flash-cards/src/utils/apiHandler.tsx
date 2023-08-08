import apiclient from "./apiConnection"

export const getCard = () => {
    const data = apiclient.get(`/cards`);
    return data;
}

export const saveCard = (card_id: number, card_answered: string) => {
    const data = apiclient.patch(`/cards`, {
        id: card_id,
        answered: card_answered
    });
    return data;
}

export const adminFetchOneCard = (card_id: number) => {

    const data = apiclient.get(`/admin/cards?card_id=${card_id}`);

    return data;
}


export const adminResetAllcards = () => {

    const data = apiclient.delete(`/admin/cards`);

    return data;
}


export const adminResetOnecards = (card_id: number) => {

    const data = apiclient.delete(`/admin/cards?card_id=${card_id}`);

    return data;
}


export const adminGetAllCorrectCards = () => {

    const data = apiclient.delete(`/admin/cards/success`);

    return data;
}

export const adminGetAllFailedCards = () => {

    const data = apiclient.delete(`/admin/cards/failed`);

    return data;
}


export const adminFetchall = () => {

    const data = apiclient.get(`/admin/cards`);

    return data;
}

export const createCard = (card_key: string, card_desc: string) => {
    const data = apiclient.post(`/cards`, {
        card_key: card_key,
        card_desc: card_desc
    });
    return data;

}
