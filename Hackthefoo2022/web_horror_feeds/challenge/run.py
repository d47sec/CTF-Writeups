from application.main import app
import ptvsd 
ptvsd.enable_attach(redirect_output=True)
print("Listenning for debug")
app.run(host='0.0.0.0', port=1337, debug=False, use_evalex=False)