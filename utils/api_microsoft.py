import httplib
import urllib


def make_post_api_microsoft(num_ngram, query):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '042e3c58b130491482e8cf2282303361',
    }

    params = urllib.urlencode({
        # Request parameters
        'model': 'body',
        'order': str(num_ngram),
    })

    data = 0
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/text/weblm/v1.0/calculateConditionalProbability?%s" % params, query, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print "error"
        return None

    return data
