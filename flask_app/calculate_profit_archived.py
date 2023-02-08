# DISCONTINUED

# def calculate_profit(contracts):

#     for c in contracts:
#         c["end"] = c["start"] + c["duration"]
#         c["price_per_hour"] = c["price"]/c["end"]

#     contracts = sorted(contracts, key=lambda s: s["end"])
#     continous_contracts = False

#     for i in range(len(contracts)):
#         for j in range(i+1, len(contracts)):
#             c1, c2 = contracts[i], contracts[j]
#             if(contracts[i]["end"] - contracts[j]["start"] == 0): 
#                 continous_contracts = True
#                 break

#     if(continous_contracts): sorted_contracts = sorted(contracts, key=lambda s: (s["start"], -s["price"]))
#     else: sorted_contracts = sorted(contracts, key=lambda s: (-s["price"], s["start"], -s["price_per_hour"]))

#     output = []
#     start = 0
#     income = 0
#     for c in sorted_contracts:
#         if(start <= c["start"]): 
#             start = c["start"] + c["duration"]
#             income += c["price"]
#             output.append(c["name"])
#     output = {
#         "income": income,
#         "path": output
#     }
#     return output