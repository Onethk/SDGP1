import pickle
import json
import sys
import numpy as np

from flask import request

from flask import Flask,session, request, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def home():   
    return render_template('homepage.html')

@app.route('/quiz')
def quiz():   
    return render_template('quiz.html')

@app.route('/testo1')
def testo1():
    return render_template('testo1.html')

#testcomment

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
     
    # print(myarray)
    temp = mod.predict([firstValue])
    print(temp)
    #test comment added 
    arr_str = np.array2string(temp)

    # Print string representation of numpy array
    print(type(arr_str))

    session['mark'] = arr_str
    session['behav_Arr']=firstValue
    
    return jsonify({'arr_str':arr_str})
    # return render_template('quiz.html', arr_str=arr_str)
    # return result

@app.route('/tips')
def tips():
    mark = session.pop('mark', None)
    print(mark)
    

    behav_Arr= session.pop('behav_Arr',None)
    print(behav_Arr)
    return render_template('tips.html', mark=mark, behav_Arr=behav_Arr)


if __name__ == "__main__":
    app.run(port= 4000, debug=True)
  
   
# test = mod.predict([output])
# print(test); 