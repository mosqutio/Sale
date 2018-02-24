# coding: utf-8

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Text
from sqlalchemy import Float, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ENUM
Base = declarative_base()


class SaleBase:
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, default=False)


class BillType(SaleBase, Base):
    __tablename__ = "bill_type"
    name = Column(String)
    description = Column(Text)


class Bill(SaleBase, Base):
    __tablename__ = "bill"
    bill_type_id = Column(Integer, ForeignKey("bill_type.id"))
    object_id = Column(Integer, nullable=False)  #
    money = Column(Float, default=0.0)
    in_out = Column(ENUM("0", "1", name="in_or_out"), default="0")
    description = Column(Text)
    pay_from = Column(Integer)
    pay_to = Column(Integer)
    pay_recorder = Column(Integer)


class User(SaleBase, Base):
    __tablename__ = "user"
    user_name = Column(String)
    user_pwd = Column(String)
    mail = Column(String)
    sex = Column(ENUM("male", "famale", name="sex"))
    user_type = Column(String)
    tel_phone = Column(String)


class MaterielType(SaleBase, Base):
    __tablename__ = "materiel_type"
    name = Column(String)
    description = Column(Text)


class Materiel(SaleBase, Base):
    __tablename__ = "materiel"
    materiel_type_id = Column(Integer, ForeignKey("materiel_type.id"))
    description = Column(Text)
    price = Column(Float)
    buy_time = Column(DateTime)


class Exhibition(SaleBase, Base):
    __tablename__ = "exhibition"
    locale = Column(String)
    owner = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(ENUM("plan", "doing", "give_up", name="exhibition_status"))
    description = Column(Text)


class ExhibitionMaterielRelationShip(SaleBase, Base):
    __tablename__ = "exhibition_materiel_relationship"
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))
    materiel_id = Column(Integer, ForeignKey("materiel.id"))


class ExhibitionParticipants(SaleBase, Base):
    __tablename__ = "exhibition_participants"
    exhibition_id = Column(Integer, ForeignKey("exhibition.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    salary = Column(Float)

#
# class GoodType(SaleBase, Base):  # 货物类型
#     __tablename__ = "good_type"
#     name = Column(String)
#     description = Column(Text)
#
#
# class BuyGoods(SaleBase, Base):  # 进货记录
#     __tablename__ = "buy_good"
#     good_type = Column(Integer, ForeignKey("good_type.id"))
#     buy_price = Column(Float)
#     buy_num = Column(Integer)
#     buy_from = Column(String)
#     description = Column(Text)
#
#
# class KeepGoods(SaleBase, Base):  # 库存记录
#     __tablename__ = "keep_good"
#     good_type = Column(Integer, ForeignKey("good_type.id"))
#     logic_good_num = Column(Integer)
#     real_good_num = Column(Integer)
#
#
# class ExhibitionGoods(SaleBase, Base):  # 展会货物记录
#     __tablename__ = "exhibition_good"
#     exhibition_id = Column(Integer, ForeignKey("exhibition.id"))
#     good_type = Column(Integer, ForeignKey("good_type.id"))
#     out_good_num = Column(Integer)
#     in_good_num = Column(Integer)
#     sale_price = Column(Float)


def get_engine():
    engine = create_engine('postgresql://postgres:wangwenkl321.@127.0.0.1/sale', echo=True)
    return engine


def get_session():
    engine = get_engine()
    session = sessionmaker(bind=engine)
    # session.configure()
    return session()


if __name__ == '__main__':
    engine = get_engine()
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)
