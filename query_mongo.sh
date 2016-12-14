# mongo

conn = new Mongo();
db = conn.getDB("nobel_prize");
coll = db.country_data ;
coll.find() ;
coll.find( { name : "Spain" } ) ;

# ctrl+d
