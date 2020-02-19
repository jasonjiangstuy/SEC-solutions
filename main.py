from flask import Flask, render_template, session, request
import eventFinder
app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        print('nycparks: ' + str(request.form.get('nycparks')))
        print('all: ' + str(request.form.get('all')))
        EventDates = []
        #---- add more scraping programs
        if request.form.get('all') == 'on':
            EventDates = eventFinder.allevents()

        if request.form.get('nycparks') == 'on':
            EventDates.append(eventFinder.eventsfromnycparks())
            print(EventDates[len(EventDates) - 1])


    return render_template(
    'index.html'
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')

#useful modules
#picking -> method of database storage: can preserve classes
#www.MYURL/showcase.com#isFake?=True
