class LabelRecord:
    def __init__(self, timestamp=None,
                 label_id=None, label_name=None,
                 card_id=None, card_name=None,
                 list_id=None, list_name=None,
                 closed=False, progress=0):
        self.timestamp = timestamp
        self.label_id = label_id
        self.card_id = card_id
        self.list_id = list_id
        self.label_name = label_name
        self.card_name = card_name
        self.list_name = list_name
        self.closed = closed
        self.progress = progress
