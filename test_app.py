
from urllib import request
from flask import Flask

from index import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_add_admin_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/AddAdmin'
    request_data = {
        'name': 'admin',
        'pwd': 'admin@213'
    }
    response = client.get(url,
                          data=request_data)

    assert response.status_code == 200


def test_login_admin_route():
    # APPCONFIG
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }

    # Calling Admin Login Method
    configure_routes(app)

    client = app.test_client()
    url = '/adminLogin'
    request_data = {
        'userName': 'admin',
        'pwd': 'admin@213'
    }
    response = client.post(url, data=request_data)
    assert response.status_code == 200


def test_admin_page_route():
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }
    configure_routes(app)
    client = app.test_client()
    url = '/admin'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 400


def test_user_signup_route():
    # APPCONFIG
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }

    # Calling Admin Login Method
    configure_routes(app)

    client = app.test_client()
    url = '/signup'
    request_data = {
        'fname': 'Sainath',
        'lname': 'Sapa',
        'email': 'sainath@gmail.com',
        'pwd': 'sainath@123'
    }
    # Check GET parameters
    reponse_get = client.get(url)
    responseCode = reponse_get.status_code
    assert responseCode == 400 or responseCode == 200

    # Check POST parameters
    response_post = client.post(url, data=request_data)
    responseCode = response_post.status_code
    assert responseCode == 400 or responseCode == 200


def test_user_login_route():
    # APPCONFIG
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }

    # Calling Admin Login Method
    configure_routes(app)

    client = app.test_client()
    url = '/login'
    request_data = {
        'email': 'sainath@gmail.com',
        'pwd': 'sainath@123'
    }
    # Check GET parameters
    reponse_get = client.get(url)
    responseCode = reponse_get.status_code
    assert responseCode == 200 or responseCode == 200

    # Check POST parameters
    response_post = client.post(url, data=request_data)
    responseCode = response_post.status_code
    assert responseCode == 200 or responseCode == 400


def test_user_logout_route():
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }
    configure_routes(app)
    client = app.test_client()
    url = '/logout'

    response = client.get(url)
    assert response.status_code == 200


def test_user_view_products_route():
    app = Flask(__name__)
    app.secret_key = 'TigerAnalyticsIndiaConsultingPrivateLimited'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'tig',
        'host': 'localhost',
        'port': 27017
    }
    configure_routes(app)
    client = app.test_client()
    url = '/products'

    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 400

