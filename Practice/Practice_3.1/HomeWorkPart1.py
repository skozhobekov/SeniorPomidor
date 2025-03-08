from datetime import datetime
dict = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}
def checkOrdersExistance(dict):
    if not dict.get("data"):
        print("Заказы отсутствуют в ответе от сервера.")
    else:
        print("Заказы найдены. Выполняем проверку...")

checkOrdersExistance(dict)

# def checkTimeDifference(order):
#     started_at = order["startedAt"]
#     completed_at = order["completedAt"]
#     started_at = datetime.strptime(started_at, "%Y-%m-%dT%H:%M:%S.%fZ")
#     completed_at = datetime.strptime(completed_at, "%Y-%m-%dT%H:%M:%S.%fZ")
#     time_diff = completed_at - started_at
#     hours = time_diff.total_seconds() / 3600
#     print(f"Разница во времени: {hours:.2f} часов")
#
# checkTimeDifference(dict["data"][0])
# checkTimeDifference(dict["data"][1])

def checkIfServicesCompleted(order):
    count = order["count"]
    completed = order["completed"]
    wait_refund = order["wait_refund"]
    refunded = order["refunded"]
    if completed + wait_refund + refunded == count:
        print("Все услуги обработаны")
    else:
        print("не все услуги не обработаны")

checkIfServicesCompleted(dict["data"][2])


# Надо убедиться, что время выполнение первого и второго заказов не превышает 6 часов
# def check_time_difference(order):
# #     start_time = datetime.fromisoformat(dict['startedAt'][:-1])
# #     # completed_time = datetime.fromisoformat(dict['completedAt'][:-1])
# #     start_time = datetime.strptime(order['startedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
# #     completed_time = datetime.strptime(order['completedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
# #
# #
# #     time_diff = (completed_time - start_time).total_seconds() / 3600
# #     #print(f"Время выполнения заказа: {time_diff:.2f} ч")
# #
# # check_time_difference(dict["data"][0])
# # check_time_difference(dict["data"][1])

