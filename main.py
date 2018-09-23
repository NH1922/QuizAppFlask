from flask import Flask, render_template, request

app = Flask(__name__)

code_question1 = '''
#include<iostream>
using namespace std;

int main()
{
    cout<<"Hello world";
}
'''

questions = {1:"On a 32 bit processor, what is the size of int ?",
2:'Find the output'+code_question1,
3:'2+2 is ?'}
choices = {1:['2 bytes','3 bytes','4 bytes','5 bytes'],2:['Hello world','No hellos','Error','Bye world'],3:['2','3','4','5','6']}
answers = {1:'4 bytes',2:'Hello world',3:'4'}

@app.route("/")
def quiz():
    return render_template("Questions.html",q = questions,c = choices)

@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for key,value in request.form.items():
    if value == answers[int(key)]:
        correct = correct + 1
 print(correct)
 return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
 app.run(debug=True)