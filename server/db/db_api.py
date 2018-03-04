# import db_model
from . import db_model
import copy
import datetime
from functools import wraps
import sys
import uuid
import warnings


# from oslo_config import cfg
# from oslo_db import api as oslo_db_api
# from oslo_db import exception as db_exception
# from oslo_db import options as db_options
# from oslo_db.sqlalchemy import session
# from oslo_db.sqlalchemy import utils as db_utils
# from oslo_log import log
# from oslo_utils import timeutils
# from oslo_utils import uuidutils
# import six
from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import true
from sqlalchemy.sql import func


def list_users():
    session = db_model.get_session()
    # print(session)
    # print(dir(session))
    obj = session.query(db_model.User).all()
    if not obj:
        return []
    return obj


def get_users(user_id):
    session = db_model.get_session()
    user = session.query(db_model.User).filter_by(id=user_id).first()
    if not user:
        raise Exception("user no found")
    return user


def list_materiel_types():
    session = db_model.get_session()
    obj = session.query(db_model.MaterielType).all()
    if not obj:
        return []
    return obj


def list_materiels():
    session = db_model.get_session()
    obj = session.query(db_model.Materiel).all()
    if not obj:
        return []
    return obj


def list_exhibitions(start_time=None, end_time=None, limit=100, offset=0):
    session = db_model.get_session()
    query = session.query(db_model.Exhibition)
    if start_time:
        query = query.filter(db_model.Exhibition.start_time > start_time)
    if end_time:
        query = query.filter(db_model.Exhibition.end_time < end_time)

    query = query.limit(limit)
    if offset:
        query = query.offset(offset)
    obj = query.all()
    if not obj:
        return []
    return obj


def get_exhibition(exhibition_id, session=None):
    if not session:
        session = db_model.get_session()
    query = session.query(db_model.Exhibition).filter_by(id=exhibition_id)
    exhibition = query.first()
    return exhibition


def create_exhibition(values, session=None):
    if not session:
        session = db_model.get_session()

    exhibition = db_model.Exhibition()
    exhibition.update(values)
    # exhibition.save(session=session)
    session.add(exhibition)
    session.commit()

    return get_exhibition(exhibition.id, session=session)


def list_materiel_in_exhibition(exhibition_id):
    session = db_model.get_session()
    obj = session.query(db_model.ExhibitionMaterielRelationShip).\
        filter_by(exhibition_id=exhibition_id).all()
    if not obj:
        return []
    return obj


def list_participant_in_exhibition(exhibition_id):
    session = db_model.get_session()
    obj = session.query(db_model.ExhibitionParticipants, db_model.User.user_name).\
        join(db_model.User, db_model.ExhibitionParticipants.user_id == db_model.User.id).\
        filter(db_model.ExhibitionParticipants.exhibition_id == exhibition_id).\
        all()
    if not obj:
        return []
    return obj


if __name__ == "__main__":
    # list_users()
    # get_users(11)
    print(list_participant_in_exhibition(1))