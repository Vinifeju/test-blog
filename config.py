# == App Config ==
class AppConfig:
	SECRET_KEY = '1D8nKdIsQ2ncXzguMdX'
	PERMANENT_SESSION_LIFETIME = 31557600
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://Vinifeju:1@localhost/mybase'
	SQLALCHEMY_TRACK_MODIFICATIONS = False