from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup_JSON import Base, Category, Event

app = Flask(__name__)

engine = create_engine('sqlite:///eventlist.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/categories/<int:category_id>/events/JSON')
def showAllEventJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Event).filter_by(category_id=category_id).all()
    return jsonify(Events=[i.serialize for i in items])


# ADD JSON ENDPOINT HERE
@app.route('/categories/<int:category_id>/events/<int:event_id>/JSON')
def eventJSON(category_id, event_id):
    event = session.query(Event).filter_by(id=event_id).one()
    return jsonify(Event=event.serialize)


@app.route('/')
def home():
    categories = session.query(Category)
    events = session.query(Event).order_by(desc(Event.id))
    return render_template('base.html', categories=categories, events=events, category_id=0)


@app.route('/categories/<int:category_id>/events')
def showEvents(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    events = session.query(Event).filter_by(category_id=category_id)

    return render_template('showevent.html', categories=session.query(Category), events = events, category = category)


@app.route('/categories/<int:category_id>/add', methods=['GET', 'POST'])
def addEvent(category_id):

    if request.method == 'POST':
        newEvent = Event(name=request.form['name'], 
                         description=request.form['description'], 
                         price=request.form['price'], 
                         category_id=category_id)
        session.add(newEvent)
        session.commit()
        return redirect(url_for('showEvents', category_id=category_id))
    else:
        return render_template('addevent.html', categories=session.query(Category), category_id=category_id)


@app.route('/categories/<int:category_id>/<int:event_id>/edit',
           methods=['GET', 'POST'])
def editEvent(category_id, event_id):
    editedEvent = session.query(Event).filter_by(id=event_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedEvent.name = request.form['name']
        if request.form['description']:
            editedEvent.description = request.form['description']
        if request.form['price']:
            editedEvent.price = request.form['price']
        session.add(editedEvent)
        session.commit()
        return redirect(url_for('showEvents', category_id=editedEvent.category_id))
    else:
        return render_template(
            'editevent.html', category_id=category_id, event= editedEvent)


@app.route('/categories/<int:category_id>/<int:event_id>/delete',
           methods=['GET', 'POST'])
def deleteEvent(category_id, event_id):
    eventToDelete = session.query(Event).filter_by(id=event_id).one()
    if request.method == 'POST':
        session.delete(eventToDelete)
        session.commit()
        return redirect(url_for('showEvents', category_id=category_id))
    else:
        return render_template('deleteevent.html', event=eventToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
