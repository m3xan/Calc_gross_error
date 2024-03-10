from data_base.main import session
from data_base.models import User ,Comment
from sqlalchemy import select


def test_select_join():
    statement = select(Comment).join(Comment.user).where(
    User.username == 'jona'
    ).where(
        Comment.text == 'Hello World'
    )

    result = session.scalars(statement).one()

    print(f'{result.text} от {result.user.username}')
    
