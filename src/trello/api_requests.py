import requests

from trello.settings import trello_credentials, board


def get_cards():
    url = "https://api.trello.com/1/boards/{board_id}/cards?fields=labels,idList,name&key={key}&token={token}" \
        .format(board_id=board['id'],
                key=trello_credentials['key'],
                token=trello_credentials['token']
                )
    resp = requests.get(url)
    return resp.json()


def get_list(list_id: str):
    url = "https://api.trello.com/1/lists/{list_id}?fields=name&key={key}&token={token}" \
        .format(board_id=board['id'],
                list_id=list_id,
                key=trello_credentials['key'],
                token=trello_credentials['token']
                )
    resp = requests.get(url)
    return resp.json()