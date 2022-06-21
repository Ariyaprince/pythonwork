# accounts = [
#     {
#         "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
#         {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
#         {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
#         {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
#     ]
#     },
#     {
#         "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
#         {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
#         {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
#         {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
#     ]
#     },
#     {
#         "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
#         {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
#         {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
#         {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
#     ]
#     },
#     {
#         "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
#         {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
#         {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
#         {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
#     ]
#     },
#     {
#         "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
#         {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
#         {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
#         {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
#     ]
#     },
#
# ]
#
# # print details of 1002
# # for ac in accounts:
# #     if ac["acno"]==1002:
# #         print(ac)
#
# # ac_details=[ac for ac in accounts if ac["acno"]==1002]
# # print(ac_details)
#
# # print savings
# # savings=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# # print(savings)
#
# # sort accounts based on balance
# #
#
# # for ac in accounts:
# #     for tr in ac["transactions"]:
# #         if tr["method"]=="phone-pay":
# #             print(tr)
#
#
# # print transactions of 1002
#
# # all_transactions=[ac["transactions"] for ac in accounts]
# # credit_transaction=[trans for tlist in all_transactions for trans in tlist if trans["to"]==1002]
# # print(credit_transaction)
#
# pms={}
# all_transactions=[ac["transactions"] for ac in accounts]
# transactions=[t for tlist in all_transactions for t in tlist]
# for transaction in transactions:
#     p_method=transaction["method"]
#     amount=transaction["amount"]
#     if p_method in pms:
#         pms[p_method]+=amount
#     else:
#         pms[p_method]=amount
# print(pms)
# print(max(pms.items(),key= lambda item:item[1]))
#
#
#
#
#
#


def add(*args):
    return sum(args)
print(add(2,3))


def max_fun(*args):
    return  max(args)
print(max_fun(2,3,4,6))


def min_fun(*args):
    return min(args)
print(min_fun(4,5,19,5))