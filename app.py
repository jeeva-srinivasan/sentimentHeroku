from flask import Flask,render_template,request
import pickle
from  predict import predict


recom_df=pickle.load(open("recc_sys_cosine_corr.pickle", "rb"))

app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def home():
    if request.method == "POST":
        user_name = request.form.get("userName")
        user_name=user_name.lower().strip()
        if len(user_name)==0:
            return render_template('base.html') + 'PLEASE ENTER USER ID'
        if user_name not in recom_df.index:
            return render_template('base.html') + 'THE USER ID IS NOT AVILABLE IN DATASET PLEASE USE VALID USER ID'
        else:  
            result_df=predict(user_name,recom_df)
            return render_template('home.html',predict=result_df.head(5),user=user_name) 
            
    else:
        return render_template('base.html')  
    

if __name__ == "__main__":
    app.run(debug=True)
