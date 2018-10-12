class Config():

	debug = False

class Develop(Config):
	
	debug=True

app_config={
	"development":Develop
}