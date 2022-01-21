from flask import Flask, request
from flask_restful import Api , Resource, reqparse
from booking import Booking


app = Flask(__name__)
api = Api(app)

search_args = reqparse.RequestParser()
search_args.add_argument('city', type=str, required=False)
search_args.add_argument('adults', type=str, required=False)
search_args.add_argument('children', type=str, required=False)
search_args.add_argument('checkin_year', type=str, required=False)
search_args.add_argument('checkin_month', type=str, required=False)
search_args.add_argument('checkin_day', type=str, required=False)
search_args.add_argument('checkout_year', type=str, required=False)
search_args.add_argument('checkout_month', type=str, required=False)
search_args.add_argument('checkout_day', type=str, required=False)
search_args.add_argument('selected_currency', type=str, required=False)

class Bot(Resource):
    def get(self):
        # arg = request.headers
        args = search_args.parse_args()
        print(args)
        result = Booking().scraper(args['city'], args['adults'], args['children'], args['checkin_year'],args['checkin_month'],args['checkin_day'],args['checkout_year'],args['checkout_month'],args['checkout_day'],selected_currency='USD')
        return {'data':result}
api.add_resource(Bot,'/search/')

if __name__ == "__main__":
    app.run(host='192.168.8.105',port=3000,debug = True)