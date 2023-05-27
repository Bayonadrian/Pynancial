def prime_cost(direct_manufacturing_labour_cost, direct_material_cost):

    return direct_manufacturing_labour_cost + direct_material_cost

def conversion_cost(direct_manufacturing_labour_cost, indirect_manufacturing_cost):

    return direct_manufacturing_labour_cost + indirect_manufacturing_cost

def fixed_cost_unit(fixed_cost, quantity):

    return fixed_cost / quantity

def total_cost(variable_cost, fixed_cost):

    return variable_cost + fixed_cost

def total_cost_unit(total_cost: total_cost, quantity):

    return total_cost / quantity

def budget_evaluation(budget, real):

    return budget - real

def budget_evaluation_perc(budget_evaluation: budget_evaluation, budget):

    return budget_evaluation / budget


