from flask import Flask

FAI=Flask(__name__)


@FAI.route('/stringResponse')
def stringResponse():
    return '<center><h1> This Is My First Flask StringResponse..</h1></center>'

if __name__=='__main__':
    FAI.run(debug=True)