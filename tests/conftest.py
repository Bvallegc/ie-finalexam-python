import pytest
import sys
import os

# Get the absolute path of the current file (conftest.py)
current_file_path = os.path.abspath(__file__)

# Get the directory containing the current file
current_dir = os.path.dirname(current_file_path)

# Get the parent directory (root directory) of the current file
root_dir = os.path.dirname(current_dir)

sys.path.append(root_dir)

from iebank_api.models import Account

from iebank_api import db, app


@pytest.fixture
def testing_client(scope='class'):
    db.create_all()
    account = Account('Test Account', '€')
    db.session.add(account)
    db.session.commit()

    with app.app_context() as testing_client:
        yield testing_client

    db.drop_all()