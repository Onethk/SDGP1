import pickle
import json

from flask import request

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('quiz.php')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output) #this converts the json output to a python dictionary
    print(result) # Printing the new dictionary
    keys = list(result.keys())
    firstKey = keys[0]
    firstValue = result[firstKey]
    print(firstValue)
    
    import pickle

    with open('model_pickle_final.h5','rb') as f:
     mod =  pickle.load(f)
    
    test = mod.predict([firstValue])
    print(test)
    
    return result


if __name__ == "__main__":
    app.run(port= 3000, debug=True)
  
   
# test = mod.predict([output])
# print(test); 