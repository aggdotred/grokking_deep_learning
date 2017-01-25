weight = 0.5
goal_pred = 0.8
input = 2
alpha = 0.1

for iteration in range(20):
    pred = input * weight
    error = (pred -  goal_pred) ** 2
    deriv = input * (pred - goal_pred)
    weight = weight - (alpha * deriv)

    print ("Error:" + str(error) + " Prediction:" + str(pred))
