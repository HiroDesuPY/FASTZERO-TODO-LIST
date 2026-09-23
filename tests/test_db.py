from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):

    new_user = User(username='test', email='test@teste', password='secret')
    session.add(new_user)
    session.commit()

    # scalar: tudo que vier do db, vira objeto do python.
    user = session.scalar(select(User).where(User.username == 'test'))

    assert user.username == {
        'id': 1,
        'username': 'test',
        'email':'test@test',
        'password': 'secret'
    }
