from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_JSON import Category, Base, Event

engine = create_engine('sqlite:///eventlist.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#--------Culture---------
category_culture = Category(name="Culture")

session.add(category_culture)
session.commit()

event1 = Event(name="Piccaso 3.0", description="Modern arts",
                     price="$7.50", category=category_culture)

session.add(event1)
session.commit()


event2 = Event(name="Asia-Europe Traditional Dance", description="A new combination of dancing styles",
                     price="$22.99", category=category_culture)

session.add(event1)
session.commit()


#--------Night Life---------
category_nightlife = Category(name="Night Life")

session.add(category_nightlife)
session.commit()


party1 = Event(name="Party party", description="",
                     price="$7.99", category=category_nightlife)
session.add(party1)
session.commit()

party2 = Event(name="90ies Party ", description="",
                     price="$9.99", category=category_nightlife)

session.add(party2)
session.commit()

#--------Sport---------
category_sport = Category(name="Sport")

session.add(category_sport)
session.commit()

sport1 = Event(name="Marathon ", description="",
                     price="$15.00", category=category_sport)

session.add(sport1)
session.commit()

sport2 = Event(name="LA Lakers vs Chicago Bulls", description="",
                     price="$45.00", category=category_sport)

session.add(sport2)
session.commit()

#-------Culinary----------
category_culinary = Category(name="Culinary")

session.add(category_culinary)
session.commit()
cookevent1 = Event(
    name="Peking Duck Cooking", description=" the diners by the cook",
     price="$8", category=category_culinary)

session.add(cookevent1)
session.commit()
print "added events!"
