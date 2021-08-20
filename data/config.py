from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Забираем значение типа str
BOT_TOKEN = env.str("BOT_TOKEN")
# Тут у нас будет список из админов
ADMINS = env.list("ADMINS")
# Тоже str, но для айпи адреса хоста
#IP = env.str("ip")

LINK_THIS = env.str("LINK_THIS")
LINK_THEN = env.str("LINK_THEN")