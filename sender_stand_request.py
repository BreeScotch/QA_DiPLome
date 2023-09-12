# Андрей Шушков, 8-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

# запрос на создание заказа.
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

# запрос на получение заказа по треку заказа.
def get_order_info(track_number):
  return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH, params={"t": track_number})