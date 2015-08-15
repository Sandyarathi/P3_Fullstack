# Udacity Fullstack Nanodegree P3 Item Catalog
# Populate initial database for City Events Application
# author: Yongkie Wiyogo

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_JSON import Category, Base, Event, User

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

# Create initial user
User1 = User(name="Why", email="whytwokie@gmail.com",
             picture='')
session.add(User1)
session.commit()
User2 = User(name="Yongkie", email="yongkie@wiyogo.com",
             picture='')
session.add(User2)
session.commit()

#--------Culture---------
category_culture = Category(name="Culture")

session.add(category_culture)
session.commit()

event1 = Event(name="Piccaso 3.0", description="Modern arts",
			   image="https://upload.wikimedia.org/wikipedia/en/7/76/Pablo_Picasso%2C_1918%2C_Pierrot%2C_oil_on_canvas%2C_92.7_x_73_cm%2C_Museum_of_Modern_Art.jpg",
               price="$7.50", category=category_culture, user_id=User1.id)

session.add(event1)
session.commit()


event2 = Event(name="Asia Europe Meetup",
			   description="Meetup for all asian and europe people",
               price="$22.99", category=category_culture, user_id=User2.id,
               image="http://cdn.eso.org/images/newsfeature/ann15033a.jpg")

session.add(event1)
session.commit()


#--------Night Life---------
category_nightlife = Category(name="Night Life")

session.add(category_nightlife)
session.commit()


party1 = Event(name="Party party", description="Our party",
		   	   image="http://us.123rf.com/450wm/chagin/chagin1310/chagin131000169/23221929-young-people-having-fun-dancing-at-party.jpg",
               price="$7.99", category=category_nightlife, user_id=User2.id)
session.add(party1)
session.commit()

party2 = Event(name="90ies Party ", description="Party with 90ies music",
			   image="http://diginights.com/uploads/images/event/2013/05/08/2013-05-08-90er-party-garage-saarbruecken/flyer_image-default-1.jpg",
               price="$9.99", category=category_nightlife, user_id=User1.id)

session.add(party2)
session.commit()

#--------Sport---------
category_sport = Category(name="Sport")

session.add(category_sport)
session.commit()

sport1 = Event(name="Marathon ", description="Sport marathon 2015",
			   image ="http://www.sportonline-foto.de/thumbs/KBM14/ip/KBM14CF011000_0032.jpg",
               price="$15.00", category=category_sport)

session.add(sport1)
session.commit()

sport2 = Event(name="Chicago Bulls vs LA Lakers", description="Basketball event",
			   image="http://cdn.fansided.com/wp-content/blogs.dir/24/files/2011/12/Chicago-Bulls-vs-LA-Lakers.jpg",
               price="$45.00", category=category_sport, user_id=User1.id)

session.add(sport2)
session.commit()

#-------Culinary----------
category_culinary = Category(name="Culinary")

session.add(category_culinary)
session.commit()
cookevent1 = Event( name="Peking Duck Cooking", category=category_culinary,
	description=" the diners by the cook", price="$8", user_id=User1.id,
    image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Peking_Duck_1.jpg/800px-Peking_Duck_1.jpg")

session.add(cookevent1)
session.commit()
cookevent1 = Event(
    name="Organic Burger", description="Meet and Cook organic burger",
    image="http://thumbs.dreamstime.com/x/organic-grilled-black-bean-burger-tomato-lettuce-35167678.jpg",
     price="$10", category=category_culinary, user_id=User1.id)

session.add(cookevent1)
session.commit()
print "added events!"
