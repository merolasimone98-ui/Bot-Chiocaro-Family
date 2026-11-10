import os
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

# Servizio Web Flask per mantenere aperta la porta su Render (Gratuito)
app = Flask('')


@app.route('/')
def home():
  return "Bot online!"


def run_flask():
  app.run(host='0.0.0.0', port=10000)


def keep_alive():
  t = Thread(target=run_flask)
  t.start()


# Configurazione Bot Discord
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
  print(f"Bot online come {bot.user}")

  # ID del canale in cui vuoi inviare il regolamento
  ID_CANALE = 1569483884465225861
  canale = bot.get_channel(ID_CANALE)

  if canale:
    # Controlla se il bot ha già inviato il messaggio per evitare doppioni
    async for msg in canale.history(limit=5):
      if msg.author == bot.user:
        print("Il messaggio di regolamento è già presente nel canale.")
        return

    # Creo l'embed con il regolamento
    embed = discord.Embed(
        title="📜 REGOLAMENTO GENERALE DELLE FAMIGLIE 🔥",
        description=(
            "# Oh, teste di cazzo, ascoltate bene. Visto che qui dentro ci sono"
            " diverse famiglie\n, vige una regola fondamentale: portate rispetto a"
            " tutti o vi spediamo a zappare terra e sabbia con il pisello.\n\n"
            "### 1. Rispetto tra le famiglie (e niente guerre civili gratis)\n"
            "# Ogni famiglia ha il suo blocco e i suoi spazi\n"
            ". Potete sfottervi quanto volete, ma se si esagera con le offese"
            " pesanti o si rompono i coglioni fuori dai canali appositi, partono"
            " i provvedimenti. La guerra si fa coi meme, non facendo i ritardati"
            " mentali.\n\n"
            "### 2. Meno pippe mentali e chiudete quella fogna\n"
            "# A nessuno frega un cazzo dei vostri drammi personali\n"
            ". Se avete problemi o crisi isteriche, andate a piangere da vostra"
            " madre. Qua dentro si viene per cazzeggiare, giocare e postare"
            " ignoranza.\n\n"
            "### 3. Niente spam o porcherie in giro\n"
            "# Non intasate le chat generali con link di merda, spam o pubblicità"
            " non autorizzate\n"
            ". Chi rompe i maroni fuori posto viene defenestrato a calci in"
            " culo.\n\n"
            "### 4. Chi non ride è un pezzo di merda patentato\n"
            "# Se qualcuno manda un meme cringe o fa una battuta pessima, si"
            " ride per pietà, brutti stronzi\n"
            ". Chi fa il fighetto e rovina l'atmosfera viene marchiato a fuoco"
            " come infame."
        ),
        color=discord.Color.red(),
    )

    embed.set_footer(
        text=(
            "Firmato: La superiorità di tutte le Famiglie. O le rispettate, o vi"
            " mandiamo a raccogliere pomodori marci con le orecchie. 🤌🚜💨"
        )
    )

    await canale.send(embed=embed)
    print("Regolamento inviato con successo nel canale!")
  else:
    print(f"❌ Impossibile trovare il canale con ID {ID_CANALE}")


# Avvia Flask e il bot
keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
  bot.run(TOKEN)
