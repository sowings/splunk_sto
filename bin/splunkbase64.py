import re,sys,time, splunk.Intersplunk
from base64 import b64encode, b64decode

def dobase64(results, settings):

	try:
		fields, argvals = splunk.Intersplunk.getKeywordsAndOptions()
		actionstr        = argvals.get("action", "decode")

		if actionstr == "encode":
			meth=b64encode
		if actionstr == "decode":
			meth=b64decode


		for r in results:
			for f in fields:
				if f in r:
					r[f]=meth(r[f])

		splunk.Intersplunk.outputResults(results)

	except:
		import traceback
		stack =  traceback.format_exc()
		results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))

        

results, dummyresults, settings = splunk.Intersplunk.getOrganizedResults()
results = dobase64(results, settings)


