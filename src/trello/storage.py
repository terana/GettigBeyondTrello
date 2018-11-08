from datetime import datetime
from typing import List

import mysql.connector

from models import LabelRecord
from settings import mysql_credentials


def connect():
    return mysql.connector.connect(
        host=mysql_credentials['host'],
        port=mysql_credentials['port'],
        user=mysql_credentials['user'],
        password=mysql_credentials['password'],
        database=mysql_credentials['database'],
        auth_plugin='mysql_native_password')


def table_exists(db, name: str):
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    for record in cursor:
        if name in record:
            return True
    return False


def create_labels_table(db):
    cursor = db.cursor()
    sql = """CREATE TABLE `tickets` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NULL DEFAULT NULL,
  `label_id` varchar(30) NOT NULL DEFAULT '',
  `label_name` varchar(30) DEFAULT NULL,
  `card_id` varchar(30) NOT NULL DEFAULT '',
  `card_name` varchar(255) DEFAULT NULL,
  `list_id` varchar(30) NOT NULL DEFAULT '',
  `list_name` varchar(30) DEFAULT NULL,
  `closed` tinyint(1) NOT NULL DEFAULT 0,
  `progress` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
)"""
    cursor.execute(sql)
    db.commit()


def store_records(records: List[LabelRecord]):
    db = connect()
    if not table_exists(db, "tickets"):
        create_labels_table(db)
    cursor = db.cursor()

    sql = """INSERT INTO tickets (timestamp, label_id, label_name, card_id, card_name, list_id, list_name, closed, progress) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for index, record in enumerate(records):

        if index % 10 == 0:
            print("{} from {}...".format(index, len(records)))

        cursor.execute(sql, (record.timestamp if record.timestamp else datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             record.label_id, record.label_name, record.card_id, record.card_name, record.list_id,
                             record.list_name, record.closed, record.progress))
    db.commit()
