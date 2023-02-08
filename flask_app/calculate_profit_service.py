"""
    @author: Akshay Hartalkar
    @date - 08-02-2023

    @description - 
    This file contains core logic to generate contract path for maximum profit
"""

def calculate_profit(contracts):
    """
        This function returns contract path by calculating maximum profit.

        @args:
        contracts - [{"name": "Contract1", "start": 0, "duration": 5, "price": 10}, ...]
        
        @returns:
        {'income': 25, 'path': ['Contract1', 'Contract3', ...]}
    """

    # adding `end` and `price_per_hour` for sorting
    for c in contracts:
        c["end"] = c["start"] + c["duration"]
        c["price_per_hour"] = c["price"]/c["duration"]

    # creating two multi-level sorts considering different parameters
    sorted_contracts = sorted(contracts, key=lambda s: (s["end"], -s["price_per_hour"]))
    sorted_contracts_1 = sorted(contracts, key=lambda s: (-s["price"], s["end"]))

    # for `sorted_contracts` calculating conitnued contracts income
    output_1 = []
    start = 0
    income = 0
    for c in sorted_contracts:
        if(start <= c["start"]): 
            start = c["start"] + c["duration"]
            income += c["price"]
            output_1.append(c["name"])

    output_1 = {"income": income, "path": output_1}
    
    # for `sorted_contracts_1` calculating conitnued contracts income
    output_2 = []
    start = 0
    income = 0
    for c in sorted_contracts_1:
        if(start <= c["start"]): 
            start = c["start"] + c["duration"]
            income += c["price"]
            output_2.append(c["name"])

    output_2 = { "income": income, "path": output_2}

    # final output will be one with max income of 2 outputs generated
    output = output_1 if output_1["income"]>=output_2["income"] else output_2

    return output