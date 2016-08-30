from flask import Blueprint, request, jsonify

# Define blueprint
fizz_buzz_api_app = Blueprint('fizz_buzz_api_app', __name__)

# Register
@fizz_buzz_api_app.route('/fizzbuzz', methods=('GET',))
def fizz_buzz_api():
    from_number = request.args.get('from')
    to_number = request.args.get('to')
    page_size = request.args.get('page_size')
    access_token = request.args.get('access_token')
    
    return jsonify({"meta": {"code":200},
                    "data": [{"from":from_number},]})
        
def fizz_buzz(number):
    """Divisible by 3 is Fizz, by 5 is Buzz, by both FizzBuzz."""
    
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    
