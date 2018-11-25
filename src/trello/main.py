from api_requests import get_cards, get_list, add_to_checklist
from models import LabelRecord
from storage import store_records
from typing import List

import datetime
import sys
import getopt


def store_cards() -> None:
    print("Getting cards...")

    cards = get_cards()
    records = []
    for index, card in enumerate(cards):

        if index % 10 == 0:
            print("{} from {}".format(index, len(cards)))

        list_name = get_list(card['idList'])['name']
        progress = card['badges']['checkItemsChecked'] + (list_name == 'Done')

        for label in card['labels']:
            records.append(LabelRecord(label_id=label['id'],
                                       label_name=label['name'],
                                       card_id=card['id'],
                                       card_name=card['name'],
                                       list_id=card['idList'],
                                       list_name=list_name,
                                       closed=card['closed'],
                                       progress=progress))

    print("Storing in database...")

    store_records(records)

    print("Done.")


def add_today_to_checklist(cards_file: str, checked=True) -> None:
    all_cards = get_cards()

    with open(cards_file) as f:
        card_names = [card for card in f]
    today = datetime.date.today()

    for card in all_cards:
        if card['name'] in card_names:
            for checklist_id in card['idChecklists']:
                add_to_checklist(checklist_id=checklist_id,
                                 checkitems=[today.strftime('%a, %d  %b %Y')],
                                 checked=checked)


def process_checkitem_options(argv: List):
    try:
        opts, args = getopt.getopt(argv, "i:c", ["item="])
    except getopt.GetoptError:
        print(f'Usage: {sys.argv[0]} add-checkitem -i <week | today> [-c]')
        sys.exit(2)
    check = False
    item = None
    for opt, arg in opts:
        if opt in ("-i", "--item"):
            item = arg
        elif opt == "-c":
            check = True
    if item != 'today' and item != 'week':
        print(f'Usage: {sys.argv[0]} add-checkitem -i <week | today> [-c]')
        sys.exit(2)

    return item, check


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [store | add-checkitem -i <week | today> [-c]]")
        sys.exit(2)
    command = sys.argv[1]
    if command == 'store':
        store_cards()
    elif command == 'add-checkitem':
        item, check = process_checkitem_options(argv=sys.argv[2:])
        if item == 'today':
            add_today_to_checklist(cards_file="days_checklist_cards.txt", checked=check)
