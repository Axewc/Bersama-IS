from app import Usuario

def obtenUsuario(email_arg):
    ans = Usuario.query.filter(Usuario.email==email_arg).first()
    return ans