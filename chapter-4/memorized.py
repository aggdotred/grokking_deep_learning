pred = input * weight
error = (pred - goal_pred) ** 2
delta = pred - goal_pred
deriv = input * delta
weight = weight - (alpha * deriv)
