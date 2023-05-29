import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from forms import CreateSearchByQueryForm, CreateSearchByFilterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route("/")
def get_brewery_list():
    return render_template('index.html')


@app.route("/search_by_query", methods=['GET', 'POST'])
def search_by_query():
    form = CreateSearchByQueryForm()
    if form.validate_on_submit():
        query = form.query.data
        search_api_url = f'https://api.openbrewerydb.org/v1/breweries/search?query={query}'
        response = requests.get(search_api_url)
        breweries_list = response.json()
        count_brew = 10
        print(breweries_list)

        return render_template('result.html', breweries_list=breweries_list, count_brew=count_brew)
    return render_template('search_by_query.html', form=form)


@app.route("/search_by_filters", methods=['GET', 'POST'])
def search_by_filters():
    form = CreateSearchByFilterForm()
    if form.validate_on_submit():

        search_api_url = f'https://api.openbrewerydb.org/v1/breweries?'
        params = {
            "city": form.city.data,
            "id": form.id.data,
            "name": form.name.data,
            "state": form.state.data,
            "type": form.type.data,
            "per_page": form.per_page.data,
            "sort": form.sort.data,

        }
        response = requests.get(search_api_url, params=params)
        breweries_list = response.json()
        count_brew = int(form.per_page.data)
        print(breweries_list)

        return render_template('result.html', breweries_list=breweries_list, count_brew=count_brew)
    return render_template('search_by_query.html', form=form)


@app.route("/random_brewery", methods=['GET', 'POST'])
def show_random():
    search_api_url = f'https://api.openbrewerydb.org/v1/breweries/random'
    response = requests.get(search_api_url)
    breweries_list = response.json()
    count_brew = 1
    return render_template('result.html', breweries_list=breweries_list, count_brew=count_brew)


if __name__ == "__main__":
    app.run(debug=True)


# response = requests.get(search_api_url)
