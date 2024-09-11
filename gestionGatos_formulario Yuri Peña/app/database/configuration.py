dataBaseName = "gestion_de_gastos"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)