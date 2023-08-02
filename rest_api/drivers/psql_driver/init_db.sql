create table cards(
    id serial primary key ,
    created_at bigint default  extract (epoch from now()),
    up_in bigint default  extract (epoch from now()) + 5,
    card_key text not null,
    card_desc text not null,
    current_stage int default 0,
    wrong_choices int default 0
);

create table forgotten_cards(
    answered_wrong bool default true,
    card_id int not null,
    card_key text not null,
    card_desc text not null
);

