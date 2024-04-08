from flask import Flask, render_template, request, redirect, session, flash

class jogo:
    def __init__(self, nome, categoria, console ):
        self.nome = nome
        self.categoria = categoria  
        self.console = console

class usuario:  
    def __init__(self, nome, nickname, senha) -> None:
        self.nome = nome
        self.nickname = nickname
        self.senha = senha 

usuario1 = usuario('Pedro', 'Hurtz', '090407')
usuario2 = usuario('cinthia', 'doida', '1234')
usuario3 = usuario(' stella', 'perfeita', 'teamo')

usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3 }
        

jogo1 = jogo('Gartic', 'Multijogador', 'Navegadores')
jogo2 = jogo('Spider Man', 'Aventura', 'Playstation')
jogo3 = jogo('F1 2023', 'Esportes', 'Consoles e Computadores')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'p090407p'

@app.route('/')
def index():
   return render_template('lista.html' , titulo= 'jogos', jogos= lista )

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or 'usuario_logado' == None:
        return redirect ('/login')

    return render_template('novo.html', titulo= 'Novo Jogo')

@app.route("/criar", methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo4 = jogo(nome, categoria, console)
    lista.append(jogo4)
    return redirect ('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']].senha 
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(session['usuario_logado']  + 'logado com sucesso')
            return redirect ('/')
        
    else:
        flash('Usuário não encontrado ou senha incorreta')
        return redirect ('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash ('Logout efetuado com sucesso!')
    return redirect ('/')

        

app.run(debug= True)  