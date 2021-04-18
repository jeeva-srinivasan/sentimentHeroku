from flask import Flask,render_template,request
import pickle
from  predict import predict_sentiment


recc_df=pickle.load(open("recom_engine_cosine.pickle", "rb"))

app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def home():
    if request.method == "POST":
        user_id = request.form.get("userName")
        user_id=user_id.lower().strip()
        if len(user_id)==0:
            return render_template('base.html') + 'PLEASE ENTER USER ID'
        if user_id not in recc_df.index:
            return render_template('base.html') + 'THE USER ID IS NOT AVILABLE IN DATASET PLEASE USE VALID USER ID'
        else:  
            result_df=predict(user_id,recc_df)
            return render_template('home.html',predict=result_df.head(5),user=user_id) 
            
    else:
        return render_template('base.html')  
    

if __name__ == "__main__":
    app.run(debug=True)
