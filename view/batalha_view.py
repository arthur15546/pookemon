from rich.panel import Panel
from rich import print
class Batalhaview():
    def escolher_inicial(planta, fogo, agua):
        conteudo  = f"[1] [green]{planta.nome}[/green]\n"
        conteudo += f"[2] [red]{fogo.nome}[/red]"
        conteudo += f"[3] [blue]{agua.nome}[/blue]"
        painel  = Panel(conteudo, title="escolha seu inicial", style="bold")
        print(painel)
    
    def receber_input():
        while True:
            get = input("")
            if get is int:
                return get
            else:
                print("[red] VALOR ERRADO, DOGITE UM VALOR VALIDO")
    
    def batalha_layout(pkm1, pkm2):
        conteudo  = f"seu pokemon: \t pokemon oponente"
        conteudo += f"nome = {pkm1.nome} \t nome = {pkm2.nome}"
        conteudo += f"HP = {pkm1.hp} \t HP = {pkm2.hp}"
        conteudo += f"HP = {pkm1.hp} \t HP = {pkm2.hp}"
        