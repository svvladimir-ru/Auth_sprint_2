from redis import StrictRedis

from app.settings import settings


# def redis_conn(db: int = 0):
#     return StrictRedis(
#         host=settings.REDIS.HOST, port=settings.REDIS.PORT, decode_responses=True, db=db
#     )

redis_conn = StrictRedis(
    host=settings.REDIS.HOST, port=settings.REDIS.PORT, decode_responses=True
)

"""Не стал выносить в отдельную функцию, так как много завязано с этой переменной,
# о чем знает только ушедший от нас разработчик"""
redis_conn_db1 = StrictRedis(
    host=settings.REDIS.HOST, port=settings.REDIS.PORT, decode_responses=True, db=1
)
