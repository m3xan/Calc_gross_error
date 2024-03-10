import functools

from sqlalchemy import Engine
from sqlalchemy.orm import Session

def with_session(engine: Engine):
    """
    create session.

    with Session(engine) as session
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with Session(engine) as session:
                result = func(session, *args, **kwargs)
                return result
        return wrapper
    return decorator

def commit_(func):
    """
    не использовать без
    @with_session
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            session: Session = args[0]
            session.commit()
            return result
        except:
            session.rollback()
            raise
    return wrapper
