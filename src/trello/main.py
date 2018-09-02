from api_requests import get_cards, get_list
from models import LabelRecord
from storage import store_records


def main():
    print("Getting cards...")
    cards = get_cards()
    records = []
    for index, card in enumerate(cards):
        if index % 10 == 0:
            print("{} from {}".format(index, len(cards)))
        list_name = get_list(card['idList'])['name']
        for label in card['labels']:
            records.append(LabelRecord(label_id=label['id'],
                                       label_name=label['name'],
                                       card_id=card['id'],
                                       card_name=card['name'],
                                       list_id=card['idList'],
                                       list_name=list_name))
    print("Storing in database...")
    store_records(records)
    print("Done.")


main()
