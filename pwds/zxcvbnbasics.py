from zxcvbn import zxcvbn
import json
import decimal
import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        if isinstance(o, datetime.timedelta):
            return str(o)
            #return str(o.days) + " Days, " + str(o.seconds) + " seconds"
        return super(CustomEncoder, self).default(o)

results = zxcvbn('JohnSmith123', user_inputs=['John', 'Smith'])
#print(results)
#print(isinstance(results, str))
#json_results = json.loads(results +"")
str_results = json.dumps(results, indent=2, cls=CustomEncoder)
print(str_results)