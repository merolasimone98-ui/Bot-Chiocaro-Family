import os
import random
from threading import Thread
import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask

# ==========================================
# 1. CONFIGURAZIONE SERVER FLASK (RENDER FREE)
# ==========================================
app = Flask('')


@app.route('/')
def home():
  return "Chiocaro Bot è attivo e operativo!"


def run_flask():
  app.run(host='0.0.0.0', port=10000)


def keep_alive():
  thread = Thread(target=run_flask)
  thread.start()


# ==========================================
# 2. INIZIALIZZAZIONE BOT DISCORD & ID
# ==========================================
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

ID_CANALE_REGOLAMENTO = 1569483884465225861
ID_RUOLO_CITTADINO = 1569719339198845112
ID_CANALE_RICHIESTA = 1569720582474571806
ID_CANALE_STAFF = 1569720656541515866
ID_CANALE_FORUM = 1569721095345405993
ID_TAG_CITTADINANZA = 1569724498385571921


# ==========================================
# 3. GESTIONE PULSANTI STAFF (ACCETTA / RIFIUTA)
# ==========================================
class VistaStaffDecisione(discord.ui.View):

  def __init__(
      self,
      utente_id: int,
      nome_ic: str,
      eta_ic: str,
      data_nascita: str,
      famiglia: str,
  ):
    super().__init__(timeout=None)
    self.utente_id = utente_id
    self.nome_ic = nome_ic
    self.eta_ic = eta_ic
    self.data_nascita = data_nascita
    self.famiglia = famiglia

  @discord.ui.button(
      label="Accetta 🟢",
      style=discord.ButtonStyle.green,
      custom_id="staff_accetta",
  )
  async def accetta(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    if not interaction.user.guild_permissions.manage_roles:
      await interaction.response.send_message(
          "❌ Non hai i permessi per eseguire questa azione.", ephemeral=True
      )
      return

    guild = interaction.guild
    utente = guild.get_member(self.utente_id)
    ruolo = guild.get_role(ID_RUOLO_CITTADINO)

    # 1. Assegna il ruolo all'utente
    if utente and ruolo:
      try:
        await utente.add_roles(ruolo)
      except Exception as e:
        print(f"Errore assegnazione ruolo: {e}")

    # 2. Crea il post nel Forum con il formato "CITTADINANZA = utente" e applica il Tag
    canale_forum = guild.get_channel(ID_CANALE_FORUM)
    if canale_forum and isinstance(canale_forum, discord.ForumChannel):
      try:
        embed_forum = discord.Embed(
            title=f"🪪 Documento Ufficiale: {self.nome_ic}",
            description=(
                f"👤 **Nome e Cognome IC:** {self.nome_ic}\n📅 **Età IC:**"
                f" {self.eta_ic}\n🎂 **Data di Nascita:**"
                f" {self.data_nascita}\n🏠 **Famiglia:** {self.famiglia}\n\n🎮"
                f" **Utente Discord:** {f'<@{self.utente_id}>'}\n✅"
                f" **Approvato da:** {interaction.user.mention}"
            ),
            color=discord.Color.green(),
        )

        # Recupera l'oggetto tag tramite ID
        tag_oggetti = []
        for tag in canale_forum.available_tags:
          if tag.id == ID_TAG_CITTADINANZA:
            tag_oggetti.append(tag)
            break

        # Crea il thread nel forum con il titolo formattato
        await canale_forum.create_thread(
            name=f"CITTADINANZA = {self.nome_ic}",
            embed=embed_forum,
            applied_tags=tag_oggetti,
        )
      except Exception as e:
        print(f"Errore creazione post nel forum o applicazione tag: {e}")

    # 3. Invia DM di conferma all'utente
    if utente:
      try:
        embed_dm = discord.Embed(
            title="✅ CITTADINANZA APPROVATA!",
            description=(
                f"Congratulazioni **{self.nome_ic}**! I tuoi documenti sono"
                " stati **approvati** dallo staff.\n\nTi è stato assegnato il"
                " ruolo di Cittadino ed è stato aperto il tuo fascicolo"
                " ufficiale nel Forum."
            ),
            color=discord.Color.green(),
        )
        await utente.send(embed=embed_dm)
      except Exception:
        pass

    # 4. Aggiorna il messaggio nello staff channel
    embed_modificato = interaction.message.embeds[0]
    embed_modificato.color = discord.Color.green()
    embed_modificato.add_field(
        name="Stato Pratica",
        value=(
            "🟢 **Accettato e Registrato nel Forum** da"
            f" {interaction.user.mention}"
        ),
        inline=False,
    )

    for child in self.children:
      child.disabled = True

    await interaction.message.edit(embed=embed_modificato, view=self)
    await interaction.response.send_message(
        "Richiesta accettata, post creato nel forum e tag applicato!",
        ephemeral=True,
    )

  @discord.ui.button(
      label="Rifiuta 🔴",
      style=discord.ButtonStyle.red,
      custom_id="staff_rifiuta",
  )
  async def rifiuta(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    if not interaction.user.guild_permissions.manage_roles:
      await interaction.response.send_message(
          "❌ Non hai i permessi per eseguire questa azione.", ephemeral=True
      )
      return

    guild = interaction.guild
    utente = guild.get_member(self.utente_id)

    # Invia DM di rifiuto all'utente
    if utente:
      try:
        embed_dm = discord.Embed(
            title="❌ CITTADINANZA RIFIUTATA",
            description=(
                "I tuoi documenti per la cittadinanza sono stati"
                " **rifiutati** dallo staff.\n\nRileggi le regole o contatta"
                " uno staffer prima di riprovare a compilare il modulo."
            ),
            color=discord.Color.red(),
        )
        await utente.send(embed=embed_dm)
      except Exception:
        pass

    # Aggiorna il messaggio dello staff
    embed_modificato = interaction.message.embeds[0]
    embed_modificato.color = discord.Color.red()
    embed_modificato.add_field(
        name="Stato Pratica",
        value=f"🔴 **Rifiutato** da {interaction.user.mention}",
        inline=False,
    )

    for child in self.children:
      child.disabled = True

    await interaction.message.edit(embed=embed_modificato, view=self)
    await interaction.response.send_message(
        "Richiesta rifiutata.", ephemeral=True
    )


# ==========================================
# 4. MODULO & VISTA REGISTRAZIONE UTENTE
# ==========================================
class ModuloCittadinanza(discord.ui.Modal, title="🪪 Registrazione Passaporto"):
  nome_ic = discord.ui.TextInput(
      label="Nome e Cognome (In Game)",
      placeholder="Es. Mario Rossi",
      required=True,
      max_length=50,
  )

  eta_ic = discord.ui.TextInput(
      label="Età del Personaggio",
      placeholder="Es. 25",
      required=True,
      max_length=3,
  )

  data_nascita = discord.ui.TextInput(
      label="Data di Nascita IC",
      placeholder="Es. 15/04/1999",
      required=True,
      max_length=10,
  )

  famiglia = discord.ui.TextInput(
      label="A che famiglia appartieni?",
      placeholder="Scrivi il nome della tua famiglia...",
      required=True,
      max_length=100,
  )

  async def on_submit(self, interaction: discord.Interaction):
    await interaction.response.send_message(
        "✅ **Richiesta inviata all'Ufficio Immigrazione!** Lo staff valuterà i"
        " tuoi documenti prima dell'approvazione.",
        ephemeral=True,
    )

    guild = interaction.guild

    # Invio della richiesta nel canale STAFF
    canale_staff = guild.get_channel(ID_CANALE_STAFF)
    if canale_staff:
      embed_staff = discord.Embed(
          title="📥 Nuova Richiesta di Cittadinanza da Revisionare",
          description=(
              f"👤 **Utente Discord:** {interaction.user.mention}"
              f" (`{interaction.user.id}`)\n\n📝 **Nome IC:**"
              f" {self.nome_ic.value}\n📅 **Età IC:** {self.eta_ic.value}\n🎂"
              f" **Data di Nascita:** {self.data_nascita.value}\n🏠"
              f" **Famiglia:** {self.famiglia.value}"
          ),
          color=discord.Color.gold(),
      )
      embed_staff.set_footer(
          text="Valuta la richiesta prima che venga inviata nel Forum."
      )

      view = VistaStaffDecisione(
          utente_id=interaction.user.id,
          nome_ic=self.nome_ic.value,
          eta_ic=self.eta_ic.value,
          data_nascita=self.data_nascita.value,
          famiglia=self.famiglia.value,
      )
      await canale_staff.send(embed=embed_staff, view=view)
    else:
      print(
          "❌ ERRORE: Impossibile trovare il canale staff con ID"
          f" {ID_CANALE_STAFF}"
      )


class VistaCittadinanza(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(
      label="Ottieni Cittadinanza 🪪",
      style=discord.ButtonStyle.green,
      custom_id="btn_cittadinanza_perm",
  )
  async def apri_modulo(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    ruolo_cittadino = interaction.guild.get_role(ID_RUOLO_CITTADINO)

    # Controllo se l'utente possiede già il ruolo cittadino
    if ruolo_cittadino and ruolo_cittadino in interaction.user.roles:
      await interaction.response.send_message(
          "❌ **Possiedi già la cittadinanza!** Non puoi compilare nuovamente"
          " il modulo.",
          ephemeral=True,
      )
      return

    # Se non lo possiede, apre il modale
    await interaction.response.send_modal(ModuloCittadinanza())


# ==========================================
# 5. EVENTI DI AVVIO & COMANDO /tumore
# ==========================================
@bot.tree.command(
    name="tumore",
    description="Simula una brutta notizia per un membro del server",
)
@app_commands.describe(
    membro="Il membro a cui vuoi assegnare la notizia (opzionale)"
)
async def tumore(interaction: discord.Interaction, membro: discord.Member = None):
  # Se non viene taggato nessuno, sceglie casualmente un membro del server
  if membro is None:
    membro = random.choice(interaction.guild.members)

  # Prende l'avatar (foto profilo) dell'utente scelto
  avatar_url = (
      membro.avatar.url if membro.avatar else membro.default_avatar.url
  )

  # Crea il messaggio embed con la notizia e la foto
  embed = discord.Embed(
      title="⚠️ COMUNICATO UFFICIALE ⚠️",
      description=(
          f"Si informa tutto il server che {membro.mention} ha contratto una"
          " grave malattia: **il tumore**, e a breve purtroppo morirà. 棺"
      ),
      color=discord.Color.dark_red(),
  )
  embed.set_image(url=avatar_url)
  embed.set_footer(text="Riposa in pace... 棺")

  # Invia il messaggio nel canale
  await interaction.response.send_message(embed=embed)


@bot.event
async def on_ready():
  print(f"🔥 Bot online come: {bot.user.name} ({bot.user.id})")

  bot.add_view(VistaCittadinanza())

  try:
    synced = await bot.tree.sync()
    print(f"✅ Sincronizzati {len(synced)} comandi slash!")
  except Exception as e:
    print(f"❌ Errore sincronizzazione comandi: {e}")

  # Invio automatico del REGOLAMENTO
  canale_regole = bot.get_channel(ID_CANALE_REGOLAMENTO)
  if canale_regole:
    async for msg in canale_regole.history(limit=10):
      if msg.author == bot.user:
        break
    else:
      embed_regole = discord.Embed(
          title="📜 ── REGOLAMENTO GENERALE DELLE FAMIGLIE ── 🔥",
          description=(
              "⚠️ **ATTENZIONE A TUTTI I MEMBRI** ⚠️\n\n"
              "💬 *Oh, teste di cazzo, ascoltate bene. Visto che qui dentro ci"
              " sono diverse famiglie, vige una regola fondamentale: portate"
              " rispetto a tutti o vi spediamo a zappare terra e sabbia con il"
              " pisello.*\n\n"
              "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
              "### 🤝 1. RISPETTO TRA LE FAMIGLIE\n"
              "*(e niente guerre civili gratis)*\n"
              "📌 **Ogni famiglia ha il suo blocco e i suoi spazi.**\n"
              "💬 Potete sfottervi quanto volete, ma se si esagera con le"
              " offese pesanti o si rompono i coglioni fuori dai canali"
              " appositi, partono i provvedimenti. **La guerra si fa coi meme,"
              " non facendo i ritardati mentali.**\n\n"
              "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
              "### 🤫 2. MENO PIPPE MENTALI E CHIUDETE QUELLA FOGNA\n"
              "📌 **A nessuno frega un cazzo dei vostri drammi personali.**\n"
              "💬 Se avete problemi o crisi isteriche, andate a piangere da"
              " vostra madre. Qua dentro si viene per cazzeggiare, giocare e"
              " postare ignoranza.\n\n"
              "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
              "### 🚫 3. NIENTE SPAM O PORCHERIE IN GIRO\n"
              "📌 **Non intasate le chat generali con link di merda, spam o"
              " pubblicità non autorizzate.**\n"
              "👢 Chi rompe i maroni fuori posto viene defenestrato a calci in"
              " culo.\n\n"
              "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
              "### 🤡 4. CHI NON RIDE È UN PEZZO DI MERDA PATENTATO\n"
              "📌 **Se qualcuno manda un meme cringe o fa una battuta pessima,"
              " si ride per pietà, brutti stronzi.**\n"
              "🏷️ Chi fa il fighetto e rovina l'atmosfera viene marchiato a"
              " fuoco come infame.\n\n"
              "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
          ),
          color=discord.Color.from_rgb(255, 69, 0),
      )
      embed_regole.set_footer(
          text=(
              "Firmato: La superiorità di tutte le Famiglie. O le rispettate, o"
              " vi mandiamo a raccogliere pomodori marci con le orecchie."
              " 🤌🚜💨"
          )
      )
      await canale_regole.send(embed=embed_regole)

  # Invio automatico del PANNELLO CITTADINANZA
  canale_cittadinanza = bot.get_channel(ID_CANALE_RICHIESTA)
  if canale_cittadinanza:
    async for msg in canale_cittadinanza.history(limit=10):
      if msg.author == bot.user:
        print("ℹ️ Pannello cittadinanza già presente.")
        break
    else:
      embed_cittadinanza = discord.Embed(
          title="🪪 ── UFFICIO ANAGRAFE E CITTADINANZA ── 🏛️",
          description=(
              "Benvenuto nell'ufficio immigrazione e registrazione delle"
              " Famiglie.\n\nPer registrarti ufficialmente, ottenere i tuoi"
              " documentos ed accedere a tutti i canali della città, clicca sul"
              " pulsante verde qui sotto e compila la tua scheda personaggio!\n\n⚠️"
              " *Inserisci dati coerenti per velocizzare l'approvazione dello"
              " staff.*"
          ),
          color=discord.Color.blue(),
      )
      embed_cittadinanza.set_footer(
          text="Sistema di Registrazione Automatica • Chiocaro Bot 🤌"
      )
      await canale_cittadinanza.send(
          embed=embed_cittadinanza, view=VistaCittadinanza()
      )
      print("✅ Pannello cittadinanza inviato!")


# ==========================================
# 6. AVVIO APPLICAZIONE
# ==========================================
keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
  bot.run(TOKEN)
else:
  print("❌ ERRORE CRITICO: Variabile d'ambiente DISCORD_TOKEN mancante!")
