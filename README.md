# Gettig Beyond Trello

*Do you like analytics, metrics and dashboards as much as I do?*

This is my personal tool for retrieving data from Trello boards and performing some analytics on cards.\
Why?\
Because I use Trello a lot and build custom dashboards from my stats. 

## Usage
Storing board snapshot in MySQL database:
```bash
python main.py store
```

Add today as a checkitem to cards listed in days_checklist_cards.txt:
```bash
python main.py add-checkitem -i today -c
```

To be continued...
