from flask import Flask, request, jsonify
import pickle
import numpy as np
print("Start of the program")
app = Flask(__name__)
# creating Flask App
@app.route("/")
def hello_world():
    return "<p>Hello, we welcome you for our insurance premium prediction Application</p>"

@app.route("/ping", methods=["GET"])
def ping():
    return {"Message" : "Ping successfully"}

model_pickle = open("./artifacts/Random_forest_model.pkl", "rb")
model = pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def prediction():
    """
    This function will thake the input json and pass it to the model for prediction and return the predicted insurance price
    """
    try:
        query_req = request.get_json() 
        print(query_req)
        samlple_query = {
                        "Age": 20, 
                        "Diabetes": 0,
                        "BloodPressureProblems": 0,
                        "AnyTransplants": 0,
                        "AnyChronicDiseases": 0,
                        "Height": 166,
                        "Weight": 88,
                        "HistoryOfCancerInFamily":0,
                        "NumberOfMajorSurgeries": 0    
                    }
        query = [query_req["Age"], query_req["Diabetes"], query_req["BloodPressureProblems"], query_req["AnyTransplants"], query_req["AnyChronicDiseases"], 
                query_req["Height"],query_req["Weight"], query_req["HistoryOfCancerInFamily"], query_req["NumberOfMajorSurgeries"]]
        features_array = np.array(query).reshape(1, -1)
        def predict_confidence(model, X, confidence=0.95):
            """
            Calculate prediction intervals using individual trees in a Random Forest.
            
            Parameters:
                model: Trained Random Forest Regressor.
                X: Single input sample (2D array).
                confidence: Confidence level for interval.
                
            Returns:
                mean_prediction: Mean prediction across all trees.
                lower_bound: Lower bound of confidence interval.
                upper_bound: Upper bound of confidence interval.
            """
            tree_predictions = np.array([tree.predict(X) for tree in model.estimators_])
            mean_prediction = tree_predictions.mean(axis=0)
            lower_bound = np.percentile(tree_predictions, (1 - confidence) / 2 * 100, axis=0)
            upper_bound = np.percentile(tree_predictions, (1 + confidence) / 2 * 100, axis=0)
            
            return mean_prediction[0], lower_bound[0], upper_bound[0]
        result = model.predict(features_array) 
        mean_pred, lower_ci, upper_ci = predict_confidence(model, features_array)
        return {"Predicted insurance price": round(result[0], 2),
                "95% Prediction Interval": (round(lower_ci, 2), round(upper_ci, 2))
                }
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400 

print("End of the program")
if __name__ == "__main__":
   app.run(debug=True)