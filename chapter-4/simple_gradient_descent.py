weight = 0.5
input = 0.5
goal_prediction = 0.8

for iteration in range(20):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    direction_and_amount = (prediction - goal_prediction) * input
    weight = weight - direction_and_amount

    print ("Error: " + str(error) + " Prediction: " + str(prediction))
