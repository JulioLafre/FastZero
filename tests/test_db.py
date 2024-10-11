from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Julio', email='teste@mail.com', password='testpassword'
    )
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'teste@mail.com'))

    assert result.id == 1
