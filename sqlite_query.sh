# Get list of routes that pass a specific stop
STOPID="10003781"; sqlite3 data/db.db "select route_id from route_path where route_seq LIKE '%${STOPID}%';"

# Search for a stopid
STOPID="10012473"; sqlite3 data/db.db "select * from stop where stop_id = '${STOPID}';"

# Search for a stop description
STOPDESC="trigo"; sqlite3 data/db.db "select * from stop where stop_name LIKE '%${STOPDESC}%';"
