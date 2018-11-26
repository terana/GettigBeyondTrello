# GettigBeyondTrello

*Do you like analytics, metrics and dashboards as much as I do?
Not sure if it is possible.*

So this is my personal tool for retrieving data from Trello boards and performing some actions on cards.\
Why?\
Because I use Trello a lot and build custom dashboards from this data. 

## Usage
Just run this python script like this for storing board snapshot in MySQL database:
```bash
python main.py store
```

Or like this to add today as a checkitem to cards listed in days_checklist_cards.txt:
```bash
python main.py add-checkitem -i today -c
```

That's it.\
The tool is for personal use, so I will add some functionality when I need it.
