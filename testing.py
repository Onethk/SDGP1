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
     
    # myarray = [2, 1, 1, 2, 2, 3, 2, 1, 1, 2, 1, 1]
    # myarray = [4,0,0,2,1,1,3,1,0,3,0,1] 
    # 3	0	0	2	2	4	2	2	1	2	0	1

    # print(myarray)
    test = mod.predict([firstValue])
    print(test)
    
    return result


if __name__ == "__main__":
    app.run(port= 4000, debug=True)
  
   
# test = mod.predict([output])
# print(test); 