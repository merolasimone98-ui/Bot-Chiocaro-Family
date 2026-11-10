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

# ID CITTADINANZA & GENERALI
ID_CANALE_REGOLAMENTO = 1569483884465225861
ID_RUOLO_CITTADINO = 1569719339198845112
ID_CANALE_RICHIESTA = 1569720582474571806
ID_CANALE_STAFF = 1569720656541515866
ID_CANALE_FORUM = 1569721095345405993
ID_TAG_CITTADINANZA = 1569724498385571921
ID_RUOLO_AUTORIZZATO_TUMORE = 1569737774733721650

# ID FAMIGLIA CHIOCARO
ID_CANALE_PANNELLO_CHIOCARO = 1569740451861504060
ID_CANALE_STAFF_CHIOCARO = 1569740933061156955
ID_RUOLO_STAFF_CHIOCARO = 1569480368246235167
ID_CANALE_ANNUNCI_CHIOCARO = 1569741365594816512


# ==========================================
# 3. SISTEMA CITTADINANZA (STAFF & MODULO)
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

    if utente and ruolo:
      try:
        await utente.add_roles(ruolo)
      except Exception as e:
        print(f"Errore assegnazione ruolo: {e}")

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
        tag_oggetti = [
            tag
            for tag in canale_forum.available_tags
            if tag.id == ID_TAG_CITTADINANZA
        ]
        await canale_forum.create_thread(
            name=f"CITTADINANZA = {self.nome_ic}",
            embed=embed_forum,
            applied_tags=tag_oggetti,
        )
      except Exception as e:
        print(f"Errore creazione post nel forum: {e}")

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
        "Richiesta accettata con successo!", ephemeral=True
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
    if utente:
      try:
        embed_dm = discord.Embed(
            title="❌ CITTADINANZA RIFIUTATA",
            description=(
                "I tuoi documenti per la cittadinanza sono stati"
                " **rifiutati** dallo staff."
            ),
            color=discord.Color.red(),
        )
        await utente.send(embed=embed_dm)
      except Exception:
        pass

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
        " tuoi documenti.",
        ephemeral=True,
    )
    canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF)
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
      view = VistaStaffDecisione(
          utente_id=interaction.user.id,
          nome_ic=self.nome_ic.value,
          eta_ic=self.eta_ic.value,
          data_nascita=self.data_nascita.value,
          famiglia=self.famiglia.value,
      )
      await canale_staff.send(embed=embed_staff, view=view)


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
    if ruolo_cittadino and ruolo_cittadino in interaction.user.roles:
      await interaction.response.send_message(
          "❌ **Possiedi già la cittadinanza!**", ephemeral=True
      )
      return
    await interaction.response.send_modal(ModuloCittadinanza())


# ==========================================
# 4. SISTEMA FAMIGLIA CHIOCARO
# ==========================================
class VistaStaffChiocaro(discord.ui.View):

  def __init__(
      self,
      utente_id: int,
      conferma: str,
      motivo_ingresso: str,
      motivo_scelta: str,
  ):
    super().__init__(timeout=None)
    self.utente_id = utente_id
    self.conferma = conferma
    self.motivo_ingresso = motivo_ingresso
    self.motivo_scelta = motivo_scelta

  @discord.ui.button(
      label="Accetta 🟢",
      style=discord.ButtonStyle.green,
      custom_id="staff_chiocaro_accetta",
  )
  async def accetta(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CHIOCARO)

    # Controllo che solo chi ha il ruolo specifico possa cliccare
    if (
        not ruolo_autorizzato
        or ruolo_autorizzato not in interaction.user.roles
    ):
      await interaction.response.send_message(
          "❌ Non hai il ruolo autorizzato per gestire le richieste della"
          " Famiglia Chiocaro.",
          ephemeral=True,
      )
      return

    guild = interaction.guild
    utente = guild.get_member(self.utente_id)

    # 1. Invia DM all'utente accettato
    if utente:
      try:
        embed_dm = discord.Embed(
            title="🎉 BENVENUTO NELLA FAMIGLIA CHIOCARO!",
            description=(
                "La tua richiesta di adesione è stata **approvata**!\n"
                "Ora fai ufficialmente parte della **Famiglia Chiocaro**."
            ),
            color=discord.Color.gold(),
        )
        await utente.send(embed=embed_dm)
      except Exception:
        pass

    # 2. Invia Embed di Annuncio nel Canale dedicato
    canale_annunci = guild.get_channel(ID_CANALE_ANNUNCI_CHIOCARO)
    if canale_annunci:
      embed_annuncio = discord.Embed(
          title="🔥 NUOVO MEMBRO IN FAMIGLIA CHIOCARO 🔥",
          description=(
              f"Diamo tutti il benvenuto a {utente.mention if utente else f'<@{self.utente_id}>'} "
              "che si è ufficialmente unito alla **Famiglia Chiocaro**! 🐔👑"
          ),
          color=discord.Color.gold(),
      )
      if utente:
        embed_annuncio.set_thumbnail(
            url=utente.avatar.url if utente.avatar else utente.default_avatar.url
        )
      await canale_annunci.send(embed=embed_annuncio)

    # 3. Modifica il messaggio dello staff
    embed_modificato = interaction.message.embeds[0]
    embed_modificato.color = discord.Color.green()
    embed_modificato.add_field(
        name="Stato Pratica",
        value=f"🟢 **Accettato** da {interaction.user.mention}",
        inline=False,
    )
    for child in self.children:
      child.disabled = True

    await interaction.message.edit(embed=embed_modificato, view=self)
    await interaction.response.send_message(
        "Candidatura accettata e annuncio inviato!", ephemeral=True
    )

  @discord.ui.button(
      label="Rifiuta 🔴",
      style=discord.ButtonStyle.red,
      custom_id="staff_chiocaro_rifiuta",
  )
  async def rifiuta(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CHIOCARO)

    if (
        not ruolo_autorizzato
        or ruolo_autorizzato not in interaction.user.roles
    ):
      await interaction.response.send_message(
          "❌ Non hai il ruolo autorizzato per gestire le richieste della"
          " Famiglia Chiocaro.",
          ephemeral=True,
      )
      return

    guild = interaction.guild
    utente = guild.get_member(self.utente_id)

    # DM di Rifiuto
    if utente:
      try:
        embed_dm = discord.Embed(
            title="❌ RICHIESTA CHIOCARO RIFIUTATA",
            description=(
                "La tua candidatura per entrare nella **Famiglia Chiocaro** è"
                " stata **respinta**."
            ),
            color=discord.Color.red(),
        )
        await utente.send(embed=embed_dm)
      except Exception:
        pass

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
        "Candidatura rifiutata.", ephemeral=True
    )


class ModuloChiocaro(
    discord.ui.Modal, title="🐔 Candidatura Famiglia Chiocaro"
):
  conferma = discord.ui.TextInput(
      label="Sei sicuro di voler entrare?",
      style=discord.TextStyle.short,
      required=True,
      max_length=50,
  )
  motivo_ingresso = discord.ui.TextInput(
      label="Perché vuoi entrare?",
      style=discord.TextStyle.paragraph,
      required=True,
      max_length=300,
  )
  motivo_scelta = discord.ui.TextInput(
      label="Perché dovremmo scegliere te?",
      style=discord.TextStyle.paragraph,
      required=True,
      max_length=300,
  )

  async def on_submit(self, interaction: discord.Interaction):
    await interaction.response.send_message(
        "✅ **Candidatura inviata con successo!** La dirigenza della Famiglia"
        " Chiocaro valuterà la tua richiesta.",
        ephemeral=True,
    )

    canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF_CHIOCARO)
    if canale_staff:
      embed_staff = discord.Embed(
          title="📥 Nuova Candidatura - Famiglia Chiocaro",
          description=(
              f"👤 **Candidato:** {interaction.user.mention}"
              f" (`{interaction.user.id}`)\n\n❓ **Conferma di voler"
              f" entrare:**\n```{self.conferma.value}```\n💭 **Perché vuole"
              f" entrare:**\n```{self.motivo_ingresso.value}```\n⭐ **Perché"
              f" dovremmo scegliere lui/lei:**\n```{self.motivo_scelta.value}```"
          ),
          color=discord.Color.gold(),
      )
      view = VistaStaffChiocaro(
          utente_id=interaction.user.id,
          conferma=self.conferma.value,
          motivo_ingresso=self.motivo_ingresso.value,
          motivo_scelta=self.motivo_scelta.value,
      )
      await canale_staff.send(embed=embed_staff, view=view)


class VistaRichiestaChiocaro(discord.ui.View):

  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(
      label="Entra nella Famiglia Chiocaro 🐔",
      style=discord.ButtonStyle.blurple,
      custom_id="btn_richiesta_chiocaro_perm",
  )
  async def apri_modulo(
      self, interaction: discord.Interaction, button: discord.ui.Button
  ):
    await interaction.response.send_modal(ModuloChiocaro())


# ==========================================
# 5. COMANDO /tumore
# ==========================================
@bot.tree.command(
    name="tumore",
    description="Simula una brutta notizia per un membro del server",
)
@app_commands.describe(
    membro="Il membro a cui vuoi assegnare la notizia (opzionale)"
)
async def tumore(interaction: discord.Interaction, membro: discord.Member = None):
  ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_AUTORIZZATO_TUMORE)
  if ruolo_autorizzato not in interaction.user.roles:
    await interaction.response.send_message(
        "❌ Non hai i permessi per usare questo comando.", ephemeral=True
    )
    return

  if membro is None:
    membro = random.choice(interaction.guild.members)

  avatar_url = (
      membro.avatar.url if membro.avatar else membro.default_avatar.url
  )

  embed = discord.Embed(
      title="⚠️ COMUNICATO UFFICIALE ⚠️",
      description=(
          f"Si informa tutto il server che {membro.mention} ha contratto una"
          " grave malattia: **il tumore**, e a breve purtroppo morirà. 🪦"
      ),
      color=discord.Color.dark_red(),
  )
  embed.set_image(url=avatar_url)
  embed.set_footer(text="Riposa in pace... 🪦")

  await interaction.response.send_message(embed=embed)


# ==========================================
# 6. EVENTI DI AVVIO (ON_READY)
# ==========================================
@bot.event
async def on_ready():
  print(f"🔥 Bot online come: {bot.user.name} ({bot.user.id})")

  bot.add_view(VistaCittadinanza())
  bot.add_view(VistaRichiestaChiocaro())

  # Sincronizzazione comandi
  for guild in bot.guilds:
    try:
      bot.tree.copy_global_to(guild=guild)
      await bot.tree.sync(guild=guild)
      print(f"✅ Sync per: {guild.name}")
    except Exception as e:
      print(f"❌ Errore sync {guild.name}: {e}")

  # 1. REGOLAMENTO AUTOMATICO
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
              "📌 **Ogni famiglia ha il suo blocco e i suoi spazi.**\n\n"
              "### 🤫 2. MENO PIPPE MENTALI E CHIUDETE QUELLA FOGNA\n"
              "📌 **A nessuno frega un cazzo dei vostri drammi personali.**\n\n"
              "### 🚫 3. NIENTE SPAM O PORCHERIE IN GIRO\n"
              "📌 **Non intasate le chat generali con link di merda.**\n\n"
              "### 🤡 4. CHI NON RIDE È UN PEZZO DI MERDA PATENTATO\n"
              "📌 **Se qualcuno manda un meme cringe, si ride per pietà.**"
          ),
          color=discord.Color.from_rgb(255, 69, 0),
      )
      await canale_regole.send(embed=embed_regole)

  # 2. PANNELLO CITTADINANZA AUTOMATICO
  canale_cittadinanza = bot.get_channel(ID_CANALE_RICHIESTA)
  if canale_cittadinanza:
    async for msg in canale_cittadinanza.history(limit=10):
      if msg.author == bot.user:
        break
    else:
      embed_cittadinanza = discord.Embed(
          title="🪪 ── UFFICIO ANAGRAFE E CITTADINANZA ── 🏛️",
          description=(
              "Benvenuto nell'ufficio immigrazione.\nClicca sul pulsante per"
              " compilare la tua scheda personaggio!"
          ),
          color=discord.Color.blue(),
      )
      await canale_cittadinanza.send(
          embed=embed_cittadinanza, view=VistaCittadinanza()
      )

  # 3. PANNELLO FAMIGLIA CHIOCARO AUTOMATICO
  canale_chiocaro = bot.get_channel(ID_CANALE_PANNELLO_CHIOCARO)
  if canale_chiocaro:
    async for msg in canale_chiocaro.history(limit=10):
      if msg.author == bot.user:
        break
    else:
      embed_chiocaro = discord.Embed(
          title="🐔 ── RECLUTAMENTO FAMIGLIA CHIOCARO ── 👑",
          description=(
              "Vuoi far parte della Famiglia Chiocaro?\n\n"
              "Clicca sul pulsante blu qui sotto per inviare la tua"
              " candidatura ufficiale alla dirigenza!"
          ),
          color=discord.Color.gold(),
      )
      embed_chiocaro.set_footer(text="Famiglia Chiocaro • Reclutamento Ufficiale")
      await canale_chiocaro.send(
          embed=embed_chiocaro, view=VistaRichiestaChiocaro()
      )
      print("✅ Pannello Chiocaro inviato in automatico!")


# ==========================================
# 7. AVVIO APPLICAZIONE
# ==========================================
keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
  bot.run(TOKEN)
else:
  print("❌ ERRORE CRITICO: Variabile d'ambiente DISCORD_TOKEN mancante!")
