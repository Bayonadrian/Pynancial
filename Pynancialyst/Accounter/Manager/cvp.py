# CVP

def revenue(selling_price, quantity_sold):

    return selling_price * quantity_sold

def total_variable_cost(variable_cost_unit, quantity_sold):

    return variable_cost_unit * quantity_sold

def operating_income(revenue, total_variable_cost: total_variable_cost, fixed_cost):

    return revenue - total_variable_cost, fixed_cost

# Contribution marging

def contribution_margin(revenue, total_variable_cost: total_variable_cost):

    return revenue - total_variable_cost

def contibution_margin_unit(unit_price, unit_variable_cost):

    return unit_price - unit_variable_cost

def contribution_margin_perc(cmu: contibution_margin_unit, unit_price):

    return cmu / unit_price

def gross_margin(revenue: revenue, cost_of_goods_sold):

    return revenue - cost_of_goods_sold

def operating_margin(net_income, tax_rate):

    return net_income / (1 - tax_rate)

def net_income_margin(net_income, revenue: revenue):

    return net_income / revenue

def net_income(revenue: revenue, total_variable_cost: total_variable_cost, fixed_cost, tax_rate):

    return (revenue - total_variable_cost - fixed_cost) * (1 - tax_rate)

# BEP

def break_even_point_unit(fixed_cost, cmu: contibution_margin_unit):

    return fixed_cost / cmu

def break_even_point_money(fixed_cost, cmp: contribution_margin_perc):

    return fixed_cost / cmp

def bep_profit_units(fixed_cost, profit, cmu: contibution_margin_unit):

    return (fixed_cost + profit) / cmu

def bep_profit_money(fixed_cost, profit, cmp: contribution_margin_perc):

    return (fixed_cost + profit) / cmp
