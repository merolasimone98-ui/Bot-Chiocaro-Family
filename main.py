import os
from threading import Thread
import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask

# ==========================================
# 1. SERVER FLASK (RENDER FREE)
# ==========================================
app = Flask('')

@app.route('/')
def home():
    return "Chiocaro Bot è attivo e operativo!"

def run_flask():
    # Usiamo use_reloader=False per evitare doppi avvii e conflitti di porta
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, use_reloader=False)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

keep_alive()

# ==========================================
# 2. INIZIALIZZAZIONE BOT DISCORD & ID
# ==========================================

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATABASE_URL = os.getenv("DATABASE_URL")

ID_RUOLO_PORTO_DARMI = 1569836896312631356
ID_RUOLO_STAFF = 1569794230262693889
ID_RUOLO_ASSICURATO = 1569837091351699456
ID_RUOLO_FDO = 1569792506722525285
ID_RUOLO_VVF = 1569837191637499904
ID_RUOLO_CRI = 1569837248252481738

ID_RUOLO_PATENTI = {
    'patente_a': 1569837307433984141,
    'patente_b': 1569837330829672509,
    'patente_c': 1569837358138916915,
    'patente_d': 1569837367651733574
}

ID_FORUM_IMMATRICOLAZIONI = 1569837669905727660

ID_CANALE_COMANDO_RECENSIONI = 1569837763459555440  
ID_CANALE_LOG_RECENSIONI = 1569838024596922619     
LINK_IMMAGINE_RECENSIONE = "https://media.discordapp.net/attachments/1569724333704749107/1569838608347828304/Gemini_Generated_Image_jr98vmjr98vmjr98.jpg?ex=6af4e9a2&is=6af39822&hm=c9feb0602fe27105147d1f140d1ee0613abc4d8ba668d5f1880b684761e15503&=&format=webp"

ID_CANALE_REGISTRO_ARRESTI = 1569838174342221825
ID_CANALE_REGISTRO_MULTE = 1569838254247641128
ID_CANALE_CONTO_BANCARIO = 1569833371176276070
ID_CANALE_LOG_DOCUMENTI = 1569721095345405993  
ID_FORUM_DOCUMENTI = 1562891782415450183  

# ID CITTADINANZA & GENERALI
ID_CANALE_REGOLAMENTO = 1569483884465225861
ID_RUOLO_CITTADINO = 1569719339198845112
ID_CANALE_RICHIESTA = 1569720582474571806
ID_CANALE_STAFF = 1569720656541515866
ID_CANALE_FORUM = 1569721095345405993
ID_TAG_CITTADINANZA = 1569724498385571921
ID_RUOLO_AUTORIZZATO_TUMORE = 1569737774733721650
ID_CANALE_VOCALE_DESTINAZIONE = 1569502181080432731

# ID FAMIGLIA CHIOCARO
ID_CANALE_PANNELLO_CHIOCARO = 1569740451861504060
ID_CANALE_STAFF_CHIOCARO = 1569740933061156955
ID_RUOLO_STAFF_CHIOCARO = 1569480368246235167
ID_CANALE_ANNUNCI_CHIOCARO = 1569741365594816512
ID_RUOLO_MEMBRO_CHIOCARO = 1569480731116306533

# ID FAMIGLIA CATUOZZO (GIALLO)
ID_CANALE_PANNELLO_CATUOZZO = 1569743489447501865
ID_CANALE_STAFF_CATUOZZO = 1569743678648623216
ID_RUOLO_STAFF_CATUOZZO = 1569481117055328447
ID_CANALE_ANNUNCI_CATUOZZO = 1569743744306118666
ID_RUOLO_MEMBRO_CATUOZZO = 1569481434312212520

# ID FAMIGLIA LIFARDO (VIOLA)
ID_CANALE_PANNELLO_LIFARDO = 1569747038785245355
ID_CANALE_STAFF_LIFARDO = 1569747072108986629
ID_CANALE_ANNUNCI_LIFARDO = 1569747095173333002
ID_RUOLO_STAFF_LIFARDO = 1569496579218341958
ID_RUOLO_MEMBRO_LIFARDO = 1569496597014777886

# --- ID SISTEMA PATENTE B ---
ID_CANALE_PANNELLO_PATENTE = 1569832234800914494
ID_CANALE_ACCETTAZIONI_PATENTI = 1570086995496009799
ID_FORUM_PATENTI_ACCETTATE = 1570087208558272633
ID_RUOLO_PATENTE_B = 1569837307433984141

# --- ID SISTEMA IMMATRICOLAZIONE VEICOLI ---
ID_CANALE_PANNELLO_IMMATRICOLAZIONE = 1569833054334226482
ID_CANALE_ACCETTAZIONI_IMMATRICOLAZIONI = 1570090329304997959
ID_FORUM_IMMATRICOLAZIONI_ACCETTATE = 1569837669905727660

# --- ID SISTEMA PORTO D'ARMI ---
ID_CANALE_PANNELLO_PORTO_ARMI = 1569832623545520300
ID_CANALE_ACCETTAZIONI_PORTO_ARMI = 1570092906348412938
ID_FORUM_PORTO_ARMI_ACCETTATI = 1570093039052005497
ID_RUOLO_PORTO_ARMI = 1569836896312631356

# SISTEMA PATENTE A
# ==========================================
ID_CANALE_PANNELLO_PATENTE_A = 1570100083473514587
ID_CANALE_ACCETTAZIONI_PATENTE_A = 1570103682073366608
ID_FORUM_PATENTI_A_ACCETTATE = 1570103776751124581
ID_RUOLO_PATENTE_A = 1569837330829672509

# SISTEMA PATENTE C
# ==========================================
ID_CANALE_PANNELLO_PATENTE_C = 1570105110141337823
ID_CANALE_ACCETTAZIONI_PATENTE_C = 1570105987463905290
ID_FORUM_PATENTI_C_ACCETTATE = 1570105446688100553
ID_RUOLO_PATENTE_C = 1569837358138916915

# SISTEMA PATENTE D
# ==========================================
ID_CANALE_PANNELLO_PATENTE_D = 1570105238365667459
ID_CANALE_ACCETTAZIONI_PATENTE_D = 1570106059568447599
ID_FORUM_PATENTI_D_ACCETTATE = 1570105570940293130
ID_RUOLO_PATENTE_D = 1569837367651733574

class ModalRifiutoPatenteC(discord.ui.Modal, title="Motivazione Rifiuto Patente C"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Requisiti non idonei, test di guida non superato...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, nome_rp: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.nome_rp = nome_rp
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        try:
            embed_dm = discord.Embed(
                title="❌ Esito Richiesta Patente C",
                description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente C** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Motorizzazione Civile • Sezione Veicoli Pesanti")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Richiesta di {self.target_user.mention} rifiutata con successo.", ephemeral=True)

class ViewGestioneStaffPatenteC(discord.ui.View):
    def __init__(self, target_user_id: int, nome_rp: str, eta_rp: str, motivazione_richiesta: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.nome_rp = nome_rp
        self.eta_rp = eta_rp
        self.motivazione_richiesta = motivazione_richiesta

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_patente_c")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        ruolo = guild.get_role(ID_RUOLO_PATENTE_C)
        if member and ruolo:
            await member.add_roles(ruolo)

        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ ACCETTATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        forum_canale = guild.get_channel(ID_FORUM_PATENTI_C_ACCETTATE)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🚛 SCHEDA PATENTE C - {self.nome_rp.upper()}",
                description="Licenza di guida per autoveicoli pesanti e trasporto merci emessa dalla Motorizzazione.",
                color=discord.Color.dark_blue()
            )
            embed_forum.add_field(name="👤 Titolare (RP)", value=self.nome_rp, inline=True)
            embed_forum.add_field(name="🎂 Età RP", value=self.eta_rp, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=False)
            embed_forum.add_field(name="🎯 Motivazione", value=self.motivazione_richiesta, inline=False)
            embed_forum.add_field(name="📜 Stato Licenza", value="🟢 **ATTIVA / VALIDA**", inline=False)
            embed_forum.set_footer(text=f"Approvata da: {interaction.user.display_name}")

            await forum_canale.create_thread(name=f"🚛 Patente C - {self.nome_rp}", embed=embed_forum)

        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Congratulazioni! Patente C Approvata",
                    description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente C** è stata **ACCETTATA**!\nTi è stato assegnato il ruolo ufficiale ed è stata emessa la tua scheda nel Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Motorizzazione Civile • Sezione Veicoli Pesanti")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Patente C di <@{self.target_user_id}> accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_patente_c")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None
        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return
        await interaction.response.send_modal(ModalRifiutoPatenteC(target_user=member, nome_rp=self.nome_rp, messaggio_staff=interaction.message))

class ModalRichiestaPatenteC(discord.ui.Modal, title="Modulo Richiesta Patente C"):
    nome_rp = discord.ui.TextInput(label="Nome e Cognome RP", placeholder="Es. Mario Rossi", required=True, max_length=50)
    eta_rp = discord.ui.TextInput(label="Età RP", placeholder="Es. 25", required=True, max_length=3)
    motivo = discord.ui.TextInput(label="Motivazione richiesta", style=discord.TextStyle.paragraph, placeholder="Spiega perché richiedi la patente C...", required=True, max_length=300)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_PATENTE_C)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Canale accettazioni Patente C non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(
            title="🚛 NUOVA RICHIESTA PATENTE C",
            description="È pervenuta una nuova istanza per il conseguimento della Patente C (Veicoli Pesanti).",
            color=discord.Color.dark_blue()
        )
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="📝 Nome e Cognome RP", value=self.nome_rp.value, inline=True)
        embed_staff.add_field(name="🎂 Età RP", value=self.eta_rp.value, inline=True)
        embed_staff.add_field(name="📄 Motivazione", value=self.motivo.value, inline=False)
        embed_staff.set_footer(text="Usa i pulsanti sottostanti per gestire la richiesta.")

        view = ViewGestioneStaffPatenteC(interaction.user.id, self.nome_rp.value, self.eta_rp.value, self.motivo.value)
        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta per la **Patente C** è stata inviata allo staff!", ephemeral=True)

class ViewPannelloPatenteC(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Richiedi Patente C", style=discord.ButtonStyle.primary, emoji="🚚", custom_id="btn_richiedi_patente_c")
    async def richiedi(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Controllo se l'utente ha già il ruolo della Patente A
        ruolo = interaction.guild.get_role(ID_RUOLO_PATENTE_C)
        if ruolo and ruolo in interaction.user.roles:
            await interaction.response.send_message("❌ **Patente già attiva!** Risulti già in possesso di questo documento in città.", ephemeral=True)
            return

        # Se non ha il ruolo, apre regolarmente il modulo
        await interaction.response.send_modal(ModalRichiestaPatenteC())


class ModalRifiutoPatenteD(discord.ui.Modal, title="Motivazione Rifiuto Patente D"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Requisiti non idonei, esito negativo...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, nome_rp: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.nome_rp = nome_rp
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        try:
            embed_dm = discord.Embed(
                title="❌ Esito Richiesta Patente D",
                description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente D** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Motorizzazione Civile • Sezione Autobus")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Richiesta di {self.target_user.mention} rifiutata con successo.", ephemeral=True)

class ViewGestioneStaffPatenteD(discord.ui.View):
    def __init__(self, target_user_id: int, nome_rp: str, eta_rp: str, motivazione_richiesta: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.nome_rp = nome_rp
        self.eta_rp = eta_rp
        self.motivazione_richiesta = motivazione_richiesta

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_patente_d")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        ruolo = guild.get_role(ID_RUOLO_PATENTE_D)
        if member and ruolo:
            await member.add_roles(ruolo)

        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ ACCETTATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        forum_canale = guild.get_channel(ID_FORUM_PATENTI_D_ACCETTATE)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🚌 SCHEDA PATENTE D - {self.nome_rp.upper()}",
                description="Licenza di guida per autobus e trasporto passeggeri emessa dalla Motorizzazione Civile.",
                color=discord.Color.teal()
            )
            embed_forum.add_field(name="👤 Titolare (RP)", value=self.nome_rp, inline=True)
            embed_forum.add_field(name="🎂 Età RP", value=self.eta_rp, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=False)
            embed_forum.add_field(name="🎯 Motivazione", value=self.motivazione_richiesta, inline=False)
            embed_forum.add_field(name="📜 Stato Licenza", value="🟢 **ATTIVA / VALIDA**", inline=False)
            embed_forum.set_footer(text=f"Approvata da: {interaction.user.display_name}")

            await forum_canale.create_thread(name=f"🚌 Patente D - {self.nome_rp}", embed=embed_forum)

        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Congratulazioni! Patente D Approvata",
                    description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente D** è stata **ACCETTATA**!\nTi è stato assegnato il ruolo ufficiale ed è stata emessa la tua scheda nel Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Motorizzazione Civile • Sezione Autobus")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Patente D di <@{self.target_user_id}> accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_patente_d")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None
        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return
        await interaction.response.send_modal(ModalRifiutoPatenteD(target_user=member, nome_rp=self.nome_rp, messaggio_staff=interaction.message))

class ModalRichiestaPatenteD(discord.ui.Modal, title="Modulo Richiesta Patente D"):
    nome_rp = discord.ui.TextInput(label="Nome e Cognome RP", placeholder="Es. Mario Rossi", required=True, max_length=50)
    eta_rp = discord.ui.TextInput(label="Età RP", placeholder="Es. 28", required=True, max_length=3)
    motivo = discord.ui.TextInput(label="Motivazione richiesta", style=discord.TextStyle.paragraph, placeholder="Spiega perché richiedi la patente D...", required=True, max_length=300)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_PATENTE_D)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Canale accettazioni Patente D non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(
            title="🚌 NUOVA RICHIESTA PATENTE D",
            description="È pervenuta una nuova istanza per il conseguimento della Patente D (Autobus / Trasporto Persone).",
            color=discord.Color.teal()
        )
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="📝 Nome e Cognome RP", value=self.nome_rp.value, inline=True)
        embed_staff.add_field(name="🎂 Età RP", value=self.eta_rp.value, inline=True)
        embed_staff.add_field(name="📄 Motivazione", value=self.motivo.value, inline=False)
        embed_staff.set_footer(text="Usa i pulsanti sottostanti per gestire la richiesta.")

        view = ViewGestioneStaffPatenteD(interaction.user.id, self.nome_rp.value, self.eta_rp.value, self.motivo.value)
        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta per la **Patente D** è stata inviata allo staff!", ephemeral=True)

class ViewPannelloPatenteD(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Richiedi Patente D", style=discord.ButtonStyle.primary, emoji="🚌", custom_id="btn_richiedi_patente_d")
    async def richiedi(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Controllo se l'utente ha già il ruolo della Patente A
        ruolo = interaction.guild.get_role(ID_RUOLO_PATENTE_D)
        if ruolo and ruolo in interaction.user.roles:
            await interaction.response.send_message("❌ **Patente già attiva!** Risulti già in possesso di questo documento in città.", ephemeral=True)
            return

        # Se non ha il ruolo, apre regolarmente il modulo
        await interaction.response.send_modal(ModalRichiestaPatenteD())





# Modulo motivazione rifiuto Patente A
class ModalRifiutoPatenteA(discord.ui.Modal, title="Motivazione Rifiuto Patente A"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Requisiti non idonei, esito negativo alla prova...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, nome_rp: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.nome_rp = nome_rp
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        try:
            embed_dm = discord.Embed(
                title="❌ Esito Richiesta Patente A",
                description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente A** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Motorizzazione Civile • Sezione Motocicli")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Richiesta di {self.target_user.mention} rifiutata con successo.", ephemeral=True)


# Pulsanti Gestione Staff Patente A
class ViewGestioneStaffPatenteA(discord.ui.View):
    def __init__(self, target_user_id: int, nome_rp: str, eta_rp: str, motivazione_richiesta: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.nome_rp = nome_rp
        self.eta_rp = eta_rp
        self.motivazione_richiesta = motivazione_richiesta

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_patente_a")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        # Assegnazione Ruolo Patente A
        ruolo_patente_a = guild.get_role(ID_RUOLO_PATENTE_A)
        if member and ruolo_patente_a:
            await member.add_roles(ruolo_patente_a)

        # 1. Modifica embed nel canale staff
        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ ACCETTATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        # 2. Creazione post nel Forum
        forum_canale = guild.get_channel(ID_FORUM_PATENTI_A_ACCETTATE)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🏍️ SCHEDA PATENTE A - {self.nome_rp.upper()}",
                description="Licenza di guida per motoveicoli accreditata ed emessa dalla Motorizzazione Civile.",
                color=discord.Color.orange()
            )
            embed_forum.add_field(name="👤 Titolare (RP)", value=self.nome_rp, inline=True)
            embed_forum.add_field(name="🎂 Età RP", value=self.eta_rp, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=False)
            embed_forum.add_field(name="🎯 Motivazione", value=self.motivazione_richiesta, inline=False)
            embed_forum.add_field(name="📜 Stato Licenza", value="🟢 **ATTIVA / VALIDA**", inline=False)
            embed_forum.set_footer(text=f"Approvata da: {interaction.user.display_name}")

            await forum_canale.create_thread(
                name=f"🏍️ Patente A - {self.nome_rp}",
                embed=embed_forum
            )

        # 3. Invio DM all'utente
        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Congratulazioni! Patente A Approvata",
                    description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente A** è stata **ACCETTATA**!\nTi è stato assegnato il ruolo ufficiale ed è stata emessa la tua scheda nel Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Motorizzazione Civile • Sezione Motocicli")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Patente A di <@{self.target_user_id}> accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_patente_a")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return

        await interaction.response.send_modal(ModalRifiutoPatenteA(target_user=member, nome_rp=self.nome_rp, messaggio_staff=interaction.message))


# Modulo compilazione utente Patente A
class ModalRichiestaPatenteA(discord.ui.Modal, title="Modulo Richiesta Patente A"):
    nome_rp = discord.ui.TextInput(
        label="Nome e Cognome RP",
        placeholder="Es. Mario Rossi",
        required=True,
        max_length=50
    )
    eta_rp = discord.ui.TextInput(
        label="Età RP",
        placeholder="Es. 22",
        required=True,
        max_length=3
    )
    motivo = discord.ui.TextInput(
        label="Motivazione richiesta",
        style=discord.TextStyle.paragraph,
        placeholder="Spiega brevemente perché richiedi la patente A...",
        required=True,
        max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_PATENTE_A)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Canale accettazioni Patente A non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(
            title="🏍️ NUOVA RICHIESTA PATENTE A",
            description="È pervenuta una nuova istanza per il conseguimento della Patente A.",
            color=discord.Color.orange()
        )
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="📝 Nome e Cognome RP", value=self.nome_rp.value, inline=True)
        embed_staff.add_field(name="🎂 Età RP", value=self.eta_rp.value, inline=True)
        embed_staff.add_field(name="📄 Motivazione", value=self.motivo.value, inline=False)
        embed_staff.set_footer(text="Usa i pulsanti sottostanti per gestire la richiesta.")

        view = ViewGestioneStaffPatenteA(
            target_user_id=interaction.user.id,
            nome_rp=self.nome_rp.value,
            eta_rp=self.eta_rp.value,
            motivazione_richiesta=self.motivo.value
        )
        
        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta per la **Patente A** è stata inviata allo staff!", ephemeral=True)


# View Pannello Pubblico Patente A
class ViewPannelloPatenteA(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Richiedi Patente A", style=discord.ButtonStyle.primary, emoji="🏍️", custom_id="btn_richiedi_patente_a")
    async def richiedi(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Controllo se l'utente ha già il ruolo della Patente A
        ruolo = interaction.guild.get_role(ID_RUOLO_PATENTE_A)
        if ruolo and ruolo in interaction.user.roles:
            await interaction.response.send_message("❌ **Patente già attiva!** Risulti già in possesso di questo documento in città.", ephemeral=True)
            return

        # Se non ha il ruolo, apre regolarmente il modulo
        await interaction.response.send_modal(ModalRichiestaPatenteA())



# ==========================================
# 5. SISTEMA PORTO D'ARMI
# ==========================================
# Modulo motivazione rifiuto Porto d'Armi
class ModalRifiutoPortoArmi(discord.ui.Modal, title="Motivazione Rifiuto Porto d'Armi"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Precedenti penali, test psicologico non superato...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, nome_rp: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.nome_rp = nome_rp
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        try:
            embed_dm = discord.Embed(
                title="❌ Esito Richiesta Porto d'Armi",
                description=f"Gentile **{self.nome_rp}**, spiacenti di comunicarle che la sua richiesta per il **Porto d'Armi** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione Ufficiale", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Questura • Divisione Polizia Amministrativa e Sociale")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Richiesta di {self.target_user.mention} rifiutata con successo.", ephemeral=True)


# Pulsanti Gestione Staff Porto d'Armi
class ViewGestioneStaffPortoArmi(discord.ui.View):
    def __init__(self, target_user_id: int, nome_rp: str, eta_rp: str, motivazione_richiesta: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.nome_rp = nome_rp
        self.eta_rp = eta_rp
        self.motivazione_richiesta = motivazione_richiesta

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_porto_armi")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        # Assegnazione Ruolo Porto d'Armi
        ruolo_porto = guild.get_role(ID_RUOLO_PORTO_ARMI)
        if member and ruolo_porto:
            await member.add_roles(ruolo_porto)

        # 1. Modifica embed staff
        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ APPROVATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        # 2. Creazione post nel Forum
        forum_canale = guild.get_channel(ID_FORUM_PORTO_ARMI_ACCETTATI)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🛡️ PORTO D'ARMI - {self.nome_rp.upper()}",
                description="Licenza di porto d'armi rilasciata ufficialmente dalle autorità competenti.",
                color=discord.Color.dark_red()
            )
            embed_forum.add_field(name="👤 Titolare (RP)", value=self.nome_rp, inline=True)
            embed_forum.add_field(name="🎂 Età RP", value=self.eta_rp, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=False)
            embed_forum.add_field(name="🎯 Motivazione Dichiarata", value=self.motivazione_richiesta, inline=False)
            embed_forum.add_field(name="📜 Stato Licenza", value="🟢 **VALIDA / ATTIVA**", inline=False)
            embed_forum.set_footer(text=f"Rilasciato da: {interaction.user.display_name}")

            await forum_canale.create_thread(
                name=f"🛡️ Porto d'Armi - {self.nome_rp}",
                embed=embed_forum
            )

        # 3. Invio DM all'utente
        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Congratulazioni! Porto d'Armi Approvato",
                    description=f"Gentile **{self.nome_rp}**, la sua richiesta per il **Porto d'Armi** è stata **APPROVATA**!\nLe è stato assegnato il rispettivo ruolo ed è stata emessa la licenza ufficiale nel registro del Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Questura • Divisione Polizia Amministrativa e Sociale")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Porto d'armi di <@{self.target_user_id}> accettato con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_porto_armi")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return

        await interaction.response.send_modal(ModalRifiutoPortoArmi(target_user=member, nome_rp=self.nome_rp, messaggio_staff=interaction.message))


# Modulo compilazione utente
class ModalRichiestaPortoArmi(discord.ui.Modal, title="Richiesta Porto d'Armi"):
    nome_rp = discord.ui.TextInput(
        label="Nome e Cognome RP",
        placeholder="Es. John Doe",
        required=True,
        max_length=50
    )
    eta_rp = discord.ui.TextInput(
        label="Età RP",
        placeholder="Es. 30",
        required=True,
        max_length=3
    )
    arma = discord.ui.TextInput(
        label="Tipo di arma",
        placeholder="Es. Glock-17, G36",
        required=True,
        max_length=20
    )
    motivazione = discord.ui.TextInput(
        label="Motivazione del porto d'armi",
        style=discord.TextStyle.paragraph,
        placeholder="Spiega dettagliatamente perché richiedi il porto d'armi...",
        required=True,
        max_length=350
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_PORTO_ARMI)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Canale accettazioni porto d'armi non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(
            title="🛡️ NUOVA RICHIESTA PORTO D'ARMI",
            description="È pervenuta una nuova istanza per il rilascio della licenza di porto d'armi.",
            color=discord.Color.dark_gold()
        )
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="📝 Nome e Cognome RP", value=self.nome_rp.value, inline=True)
        embed_staff.add_field(name="🎂 Età RP", value=self.eta_rp.value, inline=True)
        embed_staff.add_field(name="🎯 Motivazione", value=self.motivazione.value, inline=False)
        embed_staff.set_footer(text="Valutare attentamente prima di procedere all'approvazione.")

        view = ViewGestioneStaffPortoArmi(
            target_user_id=interaction.user.id,
            nome_rp=self.nome_rp.value,
            eta_rp=self.eta_rp.value,
            motivazione_richiesta=self.motivazione.value
        )

        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta di porto d'armi è stata inoltrata agli uffici competenti!", ephemeral=True)


# View Pannello Pubblico
class ViewPannelloPortoArmi(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Richiedi Porto d'Armi", style=discord.ButtonStyle.danger, emoji="🛡️", custom_id="btn_richiedi_porto_armi")
    async def richiedi(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModalRichiestaPortoArmi())



# ==========================================
# 3. MODAL & VIEW IMMATRICOLAZIONE
# ==========================================

# Modulo invio motivazione in caso di Rifiuto
class ModalRifiutoImmatricolazione(discord.ui.Modal, title="Motivazione Rifiuto Immatricolazione"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Targa già esistente, dati non validi...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, targa: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.targa = targa
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        try:
            embed_dm = discord.Embed(
                title="❌ Esito Immatricolazione Veicolo",
                description=f"La richiesta di immatricolazione per il veicolo con targa **{self.targa.upper()}** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Motorizzazione Civile RP")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Immatricolazione di {self.target_user.mention} rifiutata.", ephemeral=True)


# Pulsanti Gestione Staff (Accetta / Rifiuta)
class ViewGestioneStaffImmatricolazione(discord.ui.View):
    def __init__(self, target_user_id: int, modello: str, tipo_veicolo: str, targa: str, intestatario: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.modello = modello
        self.tipo_veicolo = tipo_veicolo
        self.targa = targa
        self.intestatario = intestatario

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_immat")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        # 1. Modifica embed nel canale staff
        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ ACCETTATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        # 2. Creazione post nel Forum Immatricolazioni (senza assegnare ruoli)
        forum_canale = guild.get_channel(ID_FORUM_IMMATRICOLAZIONI_ACCETTATE)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🚙 LIBRETTO VEICOLO - TARGA: {self.targa.upper()}",
                description="Certificato ufficiale di immatricolazione registrato presso la Motorizzazione Civile.",
                color=discord.Color.purple()
            )
            embed_forum.add_field(name="🚘 Modello", value=self.modello, inline=True)
            embed_forum.add_field(name="🏷️ Categoria", value=self.tipo_veicolo, inline=True)
            embed_forum.add_field(name="🔢 Targa", value=self.targa.upper(), inline=True)
            embed_forum.add_field(name="👤 Intestatario (RP)", value=self.intestatario, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=True)
            embed_forum.add_field(name="📜 Stato", value="🟢 **REGOLARMENTE IMMATRICOLATO**", inline=False)
            embed_forum.set_footer(text=f"Registrato da: {interaction.user.display_name}")

            await forum_canale.create_thread(
                name=f"🚙 {self.targa.upper()} - {self.modello}",
                embed=embed_forum
            )

        # 3. Invio DM all'utente
        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Immatricolazione Approvata",
                    description=f"Il tuo veicolo (**{self.modello}** - Targa: **{self.targa.upper()}**) è stato regolarmente **IMMATRICOLATO**!\nLa scheda è stata pubblicata nel registro del Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Motorizzazione Civile RP")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Immatricolazione targa `{self.targa.upper()}` accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_immat")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return

        await interaction.response.send_modal(ModalRifiutoImmatricolazione(target_user=member, targa=self.targa, messaggio_staff=interaction.message))


# Modal che l'utente compila per richiedere l'immatricolazione
class ModalRichiestaImmatricolazione(discord.ui.Modal, title="Modulo Immatricolazione Veicolo"):
    modello = discord.ui.TextInput(
        label="Modello Veicolo",
        placeholder="Es. Volksburg Marin",
        required=True,
        max_length=50
    )
    tipo_veicolo = discord.ui.TextInput(
        label="Tipo Veicolo",
        placeholder="Es. Macchina, Moto o altro",
        required=True,
        max_length=30
    )
    targa = discord.ui.TextInput(
        label="Targa Veicolo",
        placeholder="Es. AB/CD/10",
        required=True,
        max_length=15
    )
    intestatario = discord.ui.TextInput(
        label="Intestatario (Nome e Cognome RP)",
        placeholder="Es. Mario Rossi",
        required=True,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_IMMATRICOLAZIONI)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Canale accettazioni immatricolazioni non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(title="📋 NUOVA RICHIESTA IMMATRICOLAZIONE", color=discord.Color.blurple())
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="🚘 Modello", value=self.modello.value, inline=True)
        embed_staff.add_field(name="🏷️ Tipo", value=self.tipo_veicolo.value, inline=True)
        embed_staff.add_field(name="🔢 Targa", value=self.targa.value.upper(), inline=True)
        embed_staff.add_field(name="👤 Intestatario RP", value=self.intestatario.value, inline=True)
        embed_staff.set_footer(text="Usa i pulsanti sottostanti per gestire l'immatricolazione.")

        view = ViewGestioneStaffImmatricolazione(
            target_user_id=interaction.user.id,
            modello=self.modello.value,
            tipo_veicolo=self.tipo_veicolo.value,
            targa=self.targa.value,
            intestatario=self.intestatario.value
        )

        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta di immatricolazione è stata inviata allo staff!", ephemeral=True)


# View con il pulsante pubblico nel canale richieste
class ViewPannelloImmatricolazione(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Immatricola Veicolo", style=discord.ButtonStyle.primary, emoji="🚙", custom_id="btn_immatricola_veicolo")
    async def immatricola(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModalRichiestaImmatricolazione())


# ==========================================
# 3. MODAL & VIEW SISTEMA PATENTI
# ==========================================

# Modulo invio motivazione in caso di Rifiuto
class ModalRifiutoPatente(discord.ui.Modal, title="Motivazione Rifiuto Patente B"):
    motivazione = discord.ui.TextInput(
        label="Motivo del rifiuto",
        style=discord.TextStyle.paragraph,
        placeholder="Es. Documentazione mancante, requisiti non soddisfatti...",
        required=True,
        max_length=500
    )

    def __init__(self, target_user: discord.Member, nome_rp: str, messaggio_staff: discord.Message):
        super().__init__()
        self.target_user = target_user
        self.nome_rp = nome_rp
        self.messaggio_staff = messaggio_staff

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        # 1. Modifica embed per lo staff
        embed_staff = self.messaggio_staff.embeds[0]
        embed_staff.color = discord.Color.red()
        embed_staff.set_footer(text=f"❌ RIFIUTATO da {interaction.user.display_name}")
        embed_staff.add_field(name="📌 Motivazione Rifiuto", value=self.motivazione.value, inline=False)
        await self.messaggio_staff.edit(embed=embed_staff, view=None)

        # 2. Invio DM all'utente
        try:
            embed_dm = discord.Embed(
                title="❌ Esito Richiesta Patente B",
                description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente B** è stata **RIFIUTATA**.",
                color=discord.Color.red()
            )
            embed_dm.add_field(name="📝 Motivazione", value=self.motivazione.value, inline=False)
            embed_dm.set_footer(text="Motorizzazione Civile RP")
            await self.target_user.send(embed=embed_dm)
        except discord.Forbidden:
            pass

        await interaction.followup.send(f"❌ Richiesta di {self.target_user.mention} rifiutata con successo.", ephemeral=True)


# Pulsanti Gestione Staff (Accetta / Rifiuta)
class ViewGestioneStaffPatente(discord.ui.View):
    def __init__(self, target_user_id: int, nome_rp: str, eta_rp: str):
        super().__init__(timeout=None)
        self.target_user_id = target_user_id
        self.nome_rp = nome_rp
        self.eta_rp = eta_rp

    @discord.ui.button(label="Accetta", style=discord.ButtonStyle.green, emoji="✅", custom_id="btn_accetta_patente_b")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)

        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        # Assegnazione Ruolo Patente B
        ruolo_patente = guild.get_role(ID_RUOLO_PATENTE_B)
        if member and ruolo_patente:
            await member.add_roles(ruolo_patente)

        # 1. Modifica embed nel canale staff
        embed_staff = interaction.message.embeds[0]
        embed_staff.color = discord.Color.green()
        embed_staff.set_footer(text=f"✅ ACCETTATO da {interaction.user.display_name}")
        await interaction.message.edit(embed=embed_staff, view=None)

        # 2. Creazione del post nel Forum Patenti Accettate
        forum_canale = guild.get_channel(ID_FORUM_PATENTI_ACCETTATE)
        if forum_canale and isinstance(forum_canale, discord.ForumChannel):
            embed_forum = discord.Embed(
                title=f"🚗 SCHEDA PATENTE B - {self.nome_rp.upper()}",
                description="Documento di guida accreditato ed emesso dalla Motorizzazione Civile.",
                color=discord.Color.blue()
            )
            embed_forum.add_field(name="👤 Titolare (RP)", value=self.nome_rp, inline=True)
            embed_forum.add_field(name="🎂 Età RP", value=self.eta_rp, inline=True)
            embed_forum.add_field(name="🆔 Utente Discord", value=f"<@{self.target_user_id}>", inline=False)
            embed_forum.add_field(name="📜 Stato Licenza", value="🟢 **ATTIVA / VALIDA**", inline=False)
            embed_forum.set_footer(text=f"Approvata da: {interaction.user.display_name}")

            await forum_canale.create_thread(
                name=f"📄 Patente B - {self.nome_rp}",
                embed=embed_forum
            )

        # 3. Invio DM all'utente
        if member:
            try:
                embed_dm = discord.Embed(
                    title="🎉 Congratulazioni! Patente B Approvata",
                    description=f"Ciao **{self.nome_rp}**, la tua richiesta per la **Patente B** è stata **ACCETTATA**!\nTi è stato assegnato il ruolo ufficiale ed è stata creata la tua scheda registro nel Forum.",
                    color=discord.Color.green()
                )
                embed_dm.set_footer(text="Motorizzazione Civile RP")
                await member.send(embed=embed_dm)
            except discord.Forbidden:
                pass

        await interaction.followup.send(f"✅ Patente B di <@{self.target_user_id}> accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta", style=discord.ButtonStyle.red, emoji="✖️", custom_id="btn_rifiuta_patente_b")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = guild.get_member(self.target_user_id)
        if not member:
            try:
                member = await guild.fetch_member(self.target_user_id)
            except discord.NotFound:
                member = None

        if not member:
            await interaction.response.send_message("❌ Utente non trovato nel server.", ephemeral=True)
            return

        await interaction.response.send_modal(ModalRifiutoPatente(target_user=member, nome_rp=self.nome_rp, messaggio_staff=interaction.message))


# Modal che l'utente compila quando richiede la patente
class ModalRichiestaPatenteB(discord.ui.Modal, title="Modulo Richiesta Patente B"):
    nome_rp = discord.ui.TextInput(
        label="Nome e Cognome RP",
        placeholder="Es. Mario Rossi",
        required=True,
        max_length=50
    )
    eta_rp = discord.ui.TextInput(
        label="Età RP",
        placeholder="Es. 25",
        required=True,
        max_length=3
    )
    motivo = discord.ui.TextInput(
        label="Motivazione richiesta",
        style=discord.TextStyle.paragraph,
        placeholder="Spiega brevemente perché ti serve la Patente B...",
        required=True,
        max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        canale_accettazioni = interaction.guild.get_channel(ID_CANALE_ACCETTAZIONI_PATENTI)
        if not canale_accettazioni:
            await interaction.followup.send("❌ Errore di configurazione: canale accettazioni non trovato.", ephemeral=True)
            return

        embed_staff = discord.Embed(
            title="📑 NUOVA RICHIESTA PATENTE B",
            color=discord.Color.gold()
        )
        embed_staff.add_field(name="👤 Utente Discord", value=interaction.user.mention, inline=True)
        embed_staff.add_field(name="📝 Nome e Cognome RP", value=self.nome_rp.value, inline=True)
        embed_staff.add_field(name="🎂 Età RP", value=self.eta_rp.value, inline=True)
        embed_staff.add_field(name="📄 Motivazione", value=self.motivo.value, inline=False)
        embed_staff.set_footer(text="Usa i pulsanti sottostanti per gestire la richiesta.")

        view = ViewGestioneStaffPatente(
            target_user_id=interaction.user.id,
            nome_rp=self.nome_rp.value,
            eta_rp=self.eta_rp.value
        )

        await canale_accettazioni.send(embed=embed_staff, view=view)
        await interaction.followup.send("✅ La tua richiesta per la **Patente B** è stata inviata allo staff con successo!", ephemeral=True)


# View con il pulsante principale
class ViewPannelloPatenteB(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Richiedi Patente B", style=discord.ButtonStyle.primary, emoji="🚗", custom_id="btn_richiedi_patente_b")
    async def richiedi(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Controllo se l'utente ha già il ruolo della Patente A
        ruolo = interaction.guild.get_role(ID_RUOLO_PATENTE_B)
        if ruolo and ruolo in interaction.user.roles:
            await interaction.response.send_message("❌ **Patente già attiva!** Risulti già in possesso di questo documento in città.", ephemeral=True)
            return

        # Se non ha il ruolo, apre regolarmente il modulo
        await interaction.response.send_modal(ModalRichiestaPatenteB())


# ==========================================
# 4. EVENTO ON_READY (INVIO AUTOMATICO)
# ==========================================
@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")
    bot.add_view(ViewPannelloPatenteB())

    # Invio automatico del pannello nel canale configurato
    canale = bot.get_channel(ID_CANALE_PANNELLO_PATENTE)
    if canale:
        # Controlla se il bot ha già inviato il pannello per evitare doppioni
        async for message in canale.history(limit=20):
            if message.author == bot.user and message.embeds and "MOTORIZZAZIONE CIVILE" in message.embeds[0].title:
                print("Pannello Patente B già presente nel canale.")
                break
        else:
            embed = discord.Embed(
                title="🚘 MOTORIZZAZIONE CIVILE - RICHIESTA PATENTE B",
                description=(
                    "Benvenuto nello sportello digitale della **Motorizzazione Civile**.\n\n"
                    "La **Patente B** ti autorizza alla guida di autoveicoli, autovetture private e mezzi di trasporto leggeri "
                    "all'interno del territorio di gioco.\n\n"
                    "📋 **REQUISITI E ISTRUZIONI:**\n"
                    "• Compila il modulo cliccando sul pulsante sottostante.\n"
                    "• Inserisci i dati della tua identità **Roleplay** con la massima accuratezza.\n"
                    "• Le richieste vengono revisionate in tempo reale dagli esaminatori preposti.\n\n"
                    "⚠️ *Eventuali dichiarazioni mendaci comportano il rigetto istantaneo della pratica.*"
                ),
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3202/3202003.png")
            embed.set_footer(text="Motorizzazione Civile • Sistema Licenze RP", icon_url=bot.user.display_avatar.url)

            await canale.send(embed=embed, view=ViewPannelloPatenteB())
            print("Pannello Patente B inviato automaticamente nel canale!")

    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi slash.")
    except Exception as e:
        print(f"Errore sincronizzazione comandi: {e}")


# ==========================================
# 3. SISTEMA CITTADINANZA
# ==========================================
class VistaStaffDecisione(discord.ui.View):
    def __init__(self, utente_id: int, nome_ic: str, eta_ic: str, data_nascita: str, famiglia: str):
        super().__init__(timeout=None)
        self.utente_id = utente_id
        self.nome_ic = nome_ic
        self.eta_ic = eta_ic
        self.data_nascita = data_nascita
        self.famiglia = famiglia

    @discord.ui.button(label="Accetta 🟢", style=discord.ButtonStyle.green, custom_id="staff_accetta")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ Non hai i permessi per eseguire questa azione.", ephemeral=True)
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
                        f"👤 **Nome e Cognome IC:** {self.nome_ic}\n"
                        f"📅 **Età IC:** {self.eta_ic}\n"
                        f"🎂 **Data di Nascita:** {self.data_nascita}\n"
                        f"🏠 **Famiglia:** {self.famiglia}\n\n"
                        f"🎮 **Utente Discord:** {f'<@{self.utente_id}>'}\n"
                        f"✅ **Approvato da:** {interaction.user.mention}"
                    ),
                    color=discord.Color.green()
                )
                tag_oggetti = [tag for tag in canale_forum.available_tags if tag.id == ID_TAG_CITTADINANZA]
                await canale_forum.create_thread(
                    name=f"CITTADINANZA = {self.nome_ic}",
                    embed=embed_forum,
                    applied_tags=tag_oggetti
                )
            except Exception as e:
                print(f"Errore creazione post nel forum: {e}")

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="✅ CITTADINANZA APPROVATA CON SUCCESSO",
                    description=(
                        f"Congratulazioni **{self.nome_ic}**! I tuoi documenti anagrafici sono stati rigorosamente verificati e **approvati** dal corpo di polizia e dallo staff.\n\n"
                        "📜 **Cosa è cambiato?**\n"
                        "• Ti è stato conferito ufficialmente il ruolo di **Cittadino**.\n"
                        "• È stato aperto il tuo fascicolo personale protetto all'interno del nostro canale Forum.\n"
                        "• Ora possiedi pieno accesso ai canali della comunità. Rispetta le leggi cittadine e goditi il soggiorno!"
                    ),
                    color=discord.Color.green()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.green()
        embed_modificato.add_field(name="Stato Pratica", value=f"🟢 **Accettato e Registrato nel Forum** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Richiesta accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta 🔴", style=discord.ButtonStyle.red, custom_id="staff_rifiuta")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("❌ Non hai i permessi per eseguire questa azione.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)
        if utente:
            try:
                embed_dm = discord.Embed(
                    title="❌ RICHIESTA DI CITTADINANZA RESPINTA",
                    description=(
                        "I tuoi documenti di identità presentati all'Ufficio Anagrafe sono stati **rifiutati** dagli ufficiali preposti.\n\n"
                        "📋 **Motivo comune di rigetto:** Dati incoerenti, età non valida o formattazione errata dei campi del passaporto.\n"
                        "💡 Ti invitiamo a rileggere attentamente le direttive cittadine prima di tentare una nuova registrazione."
                    ),
                    color=discord.Color.red()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.red()
        embed_modificato.add_field(name="Stato Pratica", value=f"🔴 **Rifiutato** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Richiesta rifiutata.", ephemeral=True)

class ModuloCittadinanza(discord.ui.Modal, title="🪪 Registrazione Passaporto e Identità"):
    nome_ic = discord.ui.TextInput(label="Nome e Cognome (In Game)", placeholder="Es. Mario Rossi", required=True, max_length=50)
    eta_ic = discord.ui.TextInput(label="Età del Personaggio", placeholder="Es. 25", required=True, max_length=3)
    data_nascita = discord.ui.TextInput(label="Data di Nascita IC", placeholder="Es. 15/04/1999", required=True, max_length=10)
    famiglia = discord.ui.TextInput(label="A che famiglia appartieni?", placeholder="Scrivi il nome della tua famiglia...", required=True, max_length=100)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ **Pratica inoltrata all'Ufficio Immigrazione!** La tua richiesta è in coda per l'approvazione.", ephemeral=True)
        canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF)
        if canale_staff:
            embed_staff = discord.Embed(
                title="📥 Fascicolo Anagrafico in Attesa di Revisione",
                description=(
                    f"Una nuova richiesta di passaporto richiede l'attenzione immediata dello staff amministrativo.\n\n"
                    f"👤 **Richiedente Discord:** {interaction.user.mention} (`{interaction.user.id}`)\n"
                    f"📝 **Nome e Cognome IC:** {self.nome_ic.value}\n"
                    f"📅 **Età Dichiarata:** {self.eta_ic.value}\n"
                    f"🎂 **Data di Nascita:** {self.data_nascita.value}\n"
                    f"🏠 **Affiliazione Familiare:** {self.famiglia.value}\n\n"
                    f"⚙️ *Verifica la congruenza dei dati inseriti prima di procedere con l'approvazione definitiva.*"
                ),
                color=discord.Color.gold()
            )
            view = VistaStaffDecisione(
                utente_id=interaction.user.id,
                nome_ic=self.nome_ic.value,
                eta_ic=self.eta_ic.value,
                data_nascita=self.data_nascita.value,
                famiglia=self.famiglia.value
            )
            await canale_staff.send(embed=embed_staff, view=view)

class VistaCittadinanza(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ottieni Cittadinanza 🪪", style=discord.ButtonStyle.green, custom_id="btn_cittadinanza_perm")
    async def apri_modulo(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_cittadino = interaction.guild.get_role(ID_RUOLO_CITTADINO)
        if ruolo_cittadino and ruolo_cittadino in interaction.user.roles:
            await interaction.response.send_message("❌ **Cittadinanza già attiva!** Risulti già in possesso dei documenti regolari in questa città.", ephemeral=True)
            return
        await interaction.response.send_modal(ModuloCittadinanza())


# ==========================================
# 4. SISTEMA FAMIGLIA CHIOCARO
# ==========================================
class VistaStaffChiocaro(discord.ui.View):
    def __init__(self, utente_id: int, conferma: str, motivo_ingresso: str, motivo_scelta: str):
        super().__init__(timeout=None)
        self.utente_id = utente_id
        self.conferma = conferma
        self.motivo_ingresso = motivo_ingresso
        self.motivo_scelta = motivo_scelta

    @discord.ui.button(label="Accetta 🟢", style=discord.ButtonStyle.green, custom_id="staff_chiocaro_accetta")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CHIOCARO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i gradi gerarchici necessari per gestire il reclutamento della Famiglia Chiocaro.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        ruolo_membro = guild.get_role(ID_RUOLO_MEMBRO_CHIOCARO)
        if utente and ruolo_membro:
            try:
                await utente.add_roles(ruolo_membro)
            except Exception as e:
                print(f"Errore assegnazione ruolo Chiocaro: {e}")

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="🐔 ACCETTAZIONE UFFICIALE - FAMIGLIA CHIOCARO",
                    description=(
                        "Le tue motivazioni hanno convinto i piani alti. La tua candidatura è stata accolta con estremo favore!\n\n"
                        "👑 **Benvenuto nel blocco dei Chiocaro.** Ti è stato assegnato il ruolo esclusivo e l'accesso completo alle aree riservate ai membri. Onora la famiglia e fai rispettare il nome ovunque tu vada!"
                    ),
                    color=discord.Color.from_rgb(255, 100, 100)
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        canale_annunci = guild.get_channel(ID_CANALE_ANNUNCI_CHIOCARO)
        if canale_annunci:
            embed_annuncio = discord.Embed(
                title="🔥 NUOVO AFFILIATO NELLA FAMIGLIA CHIOCARO 🔥",
                description=(
                    f"Il consiglio direttivo ha deliberato l'ingresso ufficiale di {utente.mention if utente else f'<@{self.utente_id}>'} all'interno della **Famiglia Chiocaro**.\n\n"
                    "💎 *Un nuovo pilastro si unisce alla nostra potenza. Rispettate il nuovo arrivato o preparatevi a subire le conseguenze.* 🐔👑"
                ),
                color=discord.Color.from_rgb(255, 100, 100)
            )
            if utente:
                embed_annuncio.set_thumbnail(url=utente.avatar.url if utente.avatar else utente.default_avatar.url)
            await canale_annunci.send(embed=embed_annuncio)

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.green()
        embed_modificato.add_field(name="Stato Pratica", value=f"🟢 **Candidatura Accettata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Chiocaro accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta 🔴", style=discord.ButtonStyle.red, custom_id="staff_chiocaro_rifiuta")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CHIOCARO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i gradi gerarchici necessari per gestire il reclutamento della Famiglia Chiocaro.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="❌ CANDIDATURA CHIOCARO RESPINTA",
                    description=(
                        "Il comitato direttivo ha esaminato con attenzione il tuo profilo ma ha deciso di non accogliere la tua richiesta di adesione.\n\n"
                        "💡 I posti nella Famiglia Chiocaro sono riservati a pochi eletti. Migliora la tua reputazione in città prima di riprovare in futuro."
                    ),
                    color=discord.Color.red()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.red()
        embed_modificato.add_field(name="Stato Pratica", value=f"🔴 **Candidatura Rifiutata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Chiocaro rifiutata.", ephemeral=True)

class ModuloChiocaro(discord.ui.Modal, title="🐔 Candidatura Ufficiale - Famiglia Chiocaro"):
    conferma = discord.ui.TextInput(label="Sei sicuro di voler entrare?", placeholder="Scrivi 'Sì' o conferma la tua decisione...", style=discord.TextStyle.short, required=True, max_length=50)
    motivo_ingresso = discord.ui.TextInput(label="Perché vuoi entrare?", placeholder="Motiva la tua scelta di unirti proprio a noi...", style=discord.TextStyle.paragraph, required=True, max_length=300)
    motivo_scelta = discord.ui.TextInput(label="Perché dovremmo scegliere te?", placeholder="Spiega cosa puoi offrire alla famiglia...", style=discord.TextStyle.paragraph, required=True, max_length=300)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ **Candidatura inoltrata alla dirigenza Chiocaro!** Verrai ricontattato in caso di esito positivo.", ephemeral=True)
        canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF_CHIOCARO)
        if canale_staff:
            embed_staff = discord.Embed(
                title="📥 Nuova Richiesta di Ingresso - Famiglia Chiocaro",
                description=(
                    f"Una nuova aspirante recluta ha inviato i propri dati per entrare a far parte della cerchia ristretta.\n\n"
                    f"👤 **Candidato:** {interaction.user.mention} (`{interaction.user.id}`)\n\n"
                    f"❓ **Conferma di voler entrare:**\n```{self.conferma.value}```\n"
                    f"💭 **Perché vuole entrare:**\n```{self.motivo_ingresso.value}```\n"
                    f"⭐ **Perché dovremmo scegliere lui/lei:**\n```{self.motivo_scelta.value}```\n\n"
                    f"⚖️ *Analizza attentamente le risposte prima di esprimere il tuo giudizio.*"
                ),
                color=discord.Color.from_rgb(255, 100, 100)
            )
            view = VistaStaffChiocaro(
                utente_id=interaction.user.id,
                conferma=self.conferma.value,
                motivo_ingresso=self.motivo_ingresso.value,
                motivo_scelta=self.motivo_scelta.value
            )
            await canale_staff.send(embed=embed_staff, view=view)

class VistaRichiestaChiocaro(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Entra nella Famiglia Chiocaro 🐔", style=discord.ButtonStyle.blurple, custom_id="btn_richiesta_chiocaro_perm")
    async def apri_modulo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModuloChiocaro())

# ==========================================
# 5. SISTEMA FAMIGLIA CATUOZZO (GIALLO)
# ==========================================
class VistaStaffCatuozzo(discord.ui.View):
    def __init__(self, utente_id: int, conferma: str, motivo_ingresso: str, motivo_scelta: str):
        super().__init__(timeout=None)
        self.utente_id = utente_id
        self.conferma = conferma
        self.motivo_ingresso = motivo_ingresso
        self.motivo_scelta = motivo_scelta

    @discord.ui.button(label="Accetta 🟢", style=discord.ButtonStyle.green, custom_id="staff_catuozzo_accetta")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CATUOZZO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i permessi necessari per approvare le richieste della Famiglia Catuozzo.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        ruolo_membro = guild.get_role(ID_RUOLO_MEMBRO_CATUOZZO)
        if utente and ruolo_membro:
            try:
                await utente.add_roles(ruolo_membro)
            except Exception as e:
                print(f"Errore assegnazione ruolo Catuozzo: {e}")

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="⚡ AMMISSIONE UFFICIALE - FAMIGLIA CATUOZZO",
                    description=(
                        "Il capofamiglia e i luogotenenti hanno esaminato la tua scheda. La tua determinazione è stata premiata!\n\n"
                        "🐺 **Fai ufficialmente parte della Famiglia Catuozzo.** Ti è stato conferito il ruolo ufficiale e l'accesso alle chat protette. Proteggi i tuoi fratelli e porta gloria al nostro stemma!"
                    ),
                    color=discord.Color.gold()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        canale_annunci = guild.get_channel(ID_CANALE_ANNUNCI_CATUOZZO)
        if canale_annunci:
            embed_annuncio = discord.Embed(
                title="⚡ NUOVO GUERRIERO NELLA FAMIGLIA CATUOZZO ⚡",
                description=(
                    f"Salutate degnamente {utente.mention if utente else f'<@{self.utente_id}>'}, da questo momento fratello ufficiale della **Famiglia Catuozzo**.\n\n"
                    "🛡️ *La nostra forza si espande. Chiunque osi mettersi contro di noi conoscerà la nostra furia implacabile.* ⚔️🐺"
                ),
                color=discord.Color.gold()
            )
            if utente:
                embed_annuncio.set_thumbnail(url=utente.avatar.url if utente.avatar else utente.default_avatar.url)
            await canale_annunci.send(embed=embed_annuncio)

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.green()
        embed_modificato.add_field(name="Stato Pratica", value=f"🟢 **Candidatura Accettata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Catuozzo accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta 🔴", style=discord.ButtonStyle.red, custom_id="staff_catuozzo_rifiuta")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_CATUOZZO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i permessi necessari per gestire le richieste della Famiglia Catuozzo.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="❌ CANDIDATURA CATUOZZO RESPINTA",
                    description=(
                        "La dirigenza della Famiglia Catuozzo ha valutato il tuo profilo ma ha deciso di declinare la tua offerta di adesione.\n\n"
                        "⚠️ Non scoraggiarti, ma affina le tue abilità e dimostra il tuo valore sul campo prima di avanzare un'altra richiesta."
                    ),
                    color=discord.Color.red()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.red()
        embed_modificato.add_field(name="Stato Pratica", value=f"🔴 **Candidatura Rifiutata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Catuozzo rifiutata.", ephemeral=True)

class ModuloCatuozzo(discord.ui.Modal, title="⚡ Candidatura Ufficiale - Famiglia Catuozzo"):
    conferma = discord.ui.TextInput(label="Sei sicuro di voler entrare?", placeholder="Conferma la tua intenzione...", style=discord.TextStyle.short, required=True, max_length=50)
    motivo_ingresso = discord.ui.TextInput(label="Perché vuoi entrare?", placeholder="Motiva la scelta di unirti alla nostra causa...", style=discord.TextStyle.paragraph, required=True, max_length=300)
    motivo_scelta = discord.ui.TextInput(label="Perché dovremmo scegliere te?", placeholder="Dimostra il tuo valore strategico...", style=discord.TextStyle.paragraph, required=True, max_length=300)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ **Candidatura inoltrata alla dirigenza Catuozzo!** Verrai valutato dai vertici.", ephemeral=True)
        canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF_CATUOZZO)
        if canale_staff:
            embed_staff = discord.Embed(
                title="📥 Nuova Candidatura - Famiglia Catuozzo",
                description=(
                    f"Un nuovo aspirante guerriero desidera entrare a far parte della nostra famiglia.\n\n"
                    f"👤 **Candidato:** {interaction.user.mention} (`{interaction.user.id}`)\n\n"
                    f"❓ **Conferma di voler entrare:**\n```{self.conferma.value}```\n"
                    f"💭 **Perché vuole entrare:**\n```{self.motivo_ingresso.value}```\n"
                    f"⭐ **Perché dovremmo scegliere lui/lei:**\n```{self.motivo_scelta.value}```\n\n"
                    f"⚖️ *Verifica le motivazioni prima di emettere il verdetto.*"
                ),
                color=discord.Color.gold()
            )
            view = VistaStaffCatuozzo(
                utente_id=interaction.user.id,
                conferma=self.conferma.value,
                motivo_ingresso=self.motivo_ingresso.value,
                motivo_scelta=self.motivo_scelta.value
            )
            await canale_staff.send(embed=embed_staff, view=view)

class VistaRichiestaCatuozzo(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Entra nella Famiglia Catuozzo ⚡", style=discord.ButtonStyle.blurple, custom_id="btn_richiesta_catuozzo_perm")
    async def apri_modulo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModuloCatuozzo())

# ==========================================
# 6. SISTEMA FAMIGLIA LIFARDO (VIOLA)
# ==========================================
class VistaStaffLifardo(discord.ui.View):
    def __init__(self, utente_id: int, conferma: str, motivo_ingresso: str, motivo_scelta: str):
        super().__init__(timeout=None)
        self.utente_id = utente_id
        self.conferma = conferma
        self.motivo_ingresso = motivo_ingresso
        self.motivo_scelta = motivo_scelta

    @discord.ui.button(label="Accetta 🟢", style=discord.ButtonStyle.green, custom_id="staff_lifardo_accetta")
    async def accetta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_LIFARDO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i permessi necessari per accettare le richieste della Famiglia Lifardo.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        ruolo_membro = guild.get_role(ID_RUOLO_MEMBRO_LIFARDO)
        if utente and ruolo_membro:
            try:
                await utente.add_roles(ruolo_membro)
            except Exception as e:
                print(f"Errore assegnazione ruolo Lifardo: {e}")

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="🦅 INVESTITURA UFFICIALE - FAMIGLIA LIFARDO",
                    description=(
                        "La nobile casata dei Lifardo ha esaminato la tua richiesta e ha deciso di accoglierti a braccia aperte.\n\n"
                        "⚜️ **Ora sei un membro effettivo della Famiglia Lifardo.** Indossa con fierezza il tuo nuovo ruolo e difendi l'onore della casata in ogni circostanza."
                    ),
                    color=discord.Color.purple()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        canale_annunci = guild.get_channel(ID_CANALE_ANNUNCI_LIFARDO)
        if canale_annunci:
            embed_annuncio = discord.Embed(
                title="🦅 NUOVO NOBILE NELLA FAMIGLIA LIFARDO 🦅",
                description=(
                    f"Diamo un caloroso e solenne benvenuto a {utente.mention if utente else f'<@{self.utente_id}>'}, nuovo membro ufficiale della **Famiglia Lifardo**.\n\n"
                    "🦁 *La nostra influenza cresce e il nostro blocco si rafforza. Onore e rispetto al nuovo alleato.* ⚜️"
                ),
                color=discord.Color.purple()
            )
            if utente:
                embed_annuncio.set_thumbnail(url=utente.avatar.url if utente.avatar else utente.default_avatar.url)
            await canale_annunci.send(embed=embed_annuncio)

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.green()
        embed_modificato.add_field(name="Stato Pratica", value=f"🟢 **Candidatura Accettata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Lifardo accettata con successo!", ephemeral=True)

    @discord.ui.button(label="Rifiuta 🔴", style=discord.ButtonStyle.red, custom_id="staff_lifardo_rifiuta")
    async def rifiuta(self, interaction: discord.Interaction, button: discord.ui.Button):
        ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_STAFF_LIFARDO)
        if not ruolo_autorizzato or ruolo_autorizzato not in interaction.user.roles:
            await interaction.response.send_message("❌ Non possiedi i permessi necessari per gestire le richieste della Famiglia Lifardo.", ephemeral=True)
            return

        guild = interaction.guild
        utente = guild.get_member(self.utente_id)

        if utente:
            try:
                embed_dm = discord.Embed(
                    title="❌ CANDIDATURA LIFARDO RESPINTA",
                    description=(
                        "Il consiglio dei Lifardo ha attentamente vagliato la tua candidatura, giudicandola al momento non idonea agli standard della casata.\n\n"
                        "🛡️ Lavora sulla tua posizione sociale e riprova quando sarai pronto a sostenere il peso del nostro nome."
                    ),
                    color=discord.Color.red()
                )
                await utente.send(embed=embed_dm)
            except Exception:
                pass

        embed_modificato = interaction.message.embeds[0]
        embed_modificato.color = discord.Color.red()
        embed_modificato.add_field(name="Stato Pratica", value=f"🔴 **Candidatura Rifiutata** da {interaction.user.mention}", inline=False)
        for child in self.children:
            child.disabled = True

        await interaction.message.edit(embed=embed_modificato, view=self)
        await interaction.response.send_message("Candidatura Lifardo rifiutata.", ephemeral=True)

class ModuloLifardo(discord.ui.Modal, title="🦅 Candidatura Ufficiale - Famiglia Lifardo"):
    conferma = discord.ui.TextInput(label="Sei sicuro di voler entrare?", placeholder="Conferma la tua ferrea volontà...", style=discord.TextStyle.short, required=True, max_length=50)
    motivo_ingresso = discord.ui.TextInput(label="Perché vuoi entrare?", placeholder="Spiega perché desideri unire le forze con noi...", style=discord.TextStyle.paragraph, required=True, max_length=300)
    motivo_scelta = discord.ui.TextInput(label="Perché dovremmo scegliere te?", placeholder="Illustra le tue qualità e competenze...", style=discord.TextStyle.paragraph, required=True, max_length=300)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ **Candidatura inoltrata alla dirigenza Lifardo!** Il consiglio esaminerà presto il tuo profilo.", ephemeral=True)
        canale_staff = interaction.guild.get_channel(ID_CANALE_STAFF_LIFARDO)
        if canale_staff:
            embed_staff = discord.Embed(
                title="📥 Nuova Candidatura - Famiglia Lifardo",
                description=(
                    f"Un nuovo candidato ha presentato domanda formale per entrare nella casata.\n\n"
                    f"👤 **Candidato:** {interaction.user.mention} (`{interaction.user.id}`)\n\n"
                    f"❓ **Conferma di voler entrare:**\n```{self.conferma.value}```\n"
                    f"💭 **Perché vuole entrare:**\n```{self.motivo_ingresso.value}```\n"
                    f"⭐ **Perché dovremmo scegliere lui/lei:**\n```{self.motivo_scelta.value}```\n\n"
                    f"⚖️ *Esamina con cura ogni dettaglio prima di votare.*"
                ),
                color=discord.Color.purple()
            )
            view = VistaStaffLifardo(
                utente_id=interaction.user.id,
                conferma=self.conferma.value,
                motivo_ingresso=self.motivo_ingresso.value,
                motivo_scelta=self.motivo_scelta.value
            )
            await canale_staff.send(embed=embed_staff, view=view)

class VistaRichiestaLifardo(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Entra nella Famiglia Lifardo 🦅", style=discord.ButtonStyle.blurple, custom_id="btn_richiesta_lifardo_perm")
    async def apri_modulo(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModuloLifardo())

# ==========================================
# 7. COMANDO /tumore
# ==========================================
@bot.tree.command(name="tumore", description="Simula una brutta notizia per un membro del server")
@app_commands.describe(membro="Il membro a cui vuoi assegnare la notizia (opzionale)")
async def tumore(interaction: discord.Interaction, membro: discord.Member = None):
    ruolo_autorizzato = interaction.guild.get_role(ID_RUOLO_AUTORIZZATO_TUMORE)
    if ruolo_autorizzato not in interaction.user.roles:
        await interaction.response.send_message("❌ Non hai i permessi necessari per eseguire questo comando.", ephemeral=True)
        return

    if membro is None:
        membro = random.choice(interaction.guild.members)

    avatar_url = membro.avatar.url if membro.avatar else membro.default_avatar.url

    embed = discord.Embed(
        title="⚠️ COMUNICATO UFFICIALE STRAORDINARIO ⚠️",
        description=(
            f"La direzione sanitaria della città è costretta a rilasciare un bollettino medico urgente.\n\n"
            f"Si informa solennemente tutto il server che l'individuo {membro.mention} è stato colto da una grave e inesorabile patologia: **il tumore fulminante**, e purtroppo le sue ore terrene sono giunte al termine. 🪦"
        ),
        color=discord.Color.dark_red()
    )
    embed.set_image(url=avatar_url)
    embed.set_footer(text="Un momento di raccoglimento per il defunto... 🪦")

    await interaction.response.send_message(embed=embed)

# ==========================================
# 8. EVENTI DI AVVIO (ON_READY)
# ==========================================
@bot.event
async def on_ready():
    print(f"🔥 Bot online come: {bot.user.name} ({bot.user.id})")

    bot.add_view(VistaCittadinanza())
    bot.add_view(VistaRichiestaChiocaro())
    bot.add_view(VistaRichiestaCatuozzo())
    bot.add_view(VistaRichiestaLifardo())

    # Sincronizzazione comandi
    for guild in bot.guilds:
        try:
            bot.tree.copy_global_to(guild=guild)
            await bot.tree.sync(guild=guild)
            print(f"✅ Sync per: {guild.name}")
        except Exception as e:
            print(f"❌ Errore sync {guild.name}: {e}")

    # 1. REGOLAMENTO AUTOMATICO (ARRICCHITO)
    canale_regole = bot.get_channel(ID_CANALE_REGOLAMENTO)
    if canale_regole:
        async for msg in canale_regole.history(limit=10):
            if msg.author == bot.user:
                break
        else:
            embed_regole = discord.Embed(
                title="📜 ── CODICE PENALE E REGOLAMENTO GENERALE DELLE FAMIGLIE ── 🔥",
                description=(
                    "⚠️ **AVVISO IMPORTANTE A TUTTI I CITTADINI E AFFILIATI** ⚠️\n\n"
                    "💬 *Ascoltate bene, teste di cazzo, leggete ogni singola riga perché qui non siamo all'asilo nido. "
                    "All'interno di questa metropoli operano diverse fazioni e famiglie mafiose, e vige una regola inderogabile: "
                    "portate rispetto a chiunque o verrete rispediti a zappare la terra arida con le vostre mani.*\n\n"
                    "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
                    "### 🤝 1. RISPETTO ASSOLUTO TRA LE FAMIGLIE\n"
                    "*(ovvero: evitate guerre civili inutili)*\n"
                    "📌 **Ogni famiglia gestisce il proprio blocco, i propri affari e i propri spazi dedicati.**\n"
                    "💬 Le prese per il culo e la rivalità sana sono ammesse, ma se superate il limite con offese personali pesanti o sconfinate dove non dovreste, scatteranno provvedimenti immediati. La supremazia si dimostra con i fatti e coi meme di classe, non facendo i ritardati mentali nelle chat altrui.\n\n"
                    "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
                    "### 🤫 2. MENO LAMENTTELE E CHIUDETE LA FOGNA\n"
                    "📌 **A nessuno frega un bene accetto dei vostri drammi esistenziali o crisi isteriche.**\n"
                    "💬 Se avete problemi sentimentali o piagnistei quotidiani, andate a lamentarvi da vostra madre. In questa comunità si entra esclusivamente per cazzeggiare, giocare in compagnia e condividere sana ignoranza.\n\n"
                    "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
                    "### 🚫 3. SPAM E PORCHERIE NON AUTORIZZATE\n"
                    "📌 **È severamente vietato intasare i canali pubblici con link spazzatura, spam di altri server o pubblicità illecite.**\n"
                    "👢 Chiunque provi a fare il furbo fuori posto verrà defenestrato a calci in culo senza alcuna possibilità di appello.\n\n"
                    "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n"
                    "### 🤡 4. LA LEGGE DEL MEME E DELL'UMORISMO\n"
                    "📌 **Se qualcuno pubblica un meme pessimo o fa una battuta di merda, si ride comunque per pietà umana, brutti stronzi.**\n"
                    "🏷️ Chi fa il sofisticato rovinando l'atmosfera goliardica verrà marchiato a fuoco come infame ufficiale della città.\n\n"
                    "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                ),
                color=discord.Color.from_rgb(255, 69, 0)
            )
            embed_regole.set_footer(
                text="Firmato: Il Cartello Supremo di Tutte le Famiglie. O rispettate le regole, o finite a raccogliere pomodori marci nei campi. 🤌🚜💨"
            )
            await canale_regole.send(embed=embed_regole)

    # 2. PANNELLO CITTADINANZA AUTOMATICO (ARRICCHITO)
    canale_cittadinanza = bot.get_channel(ID_CANALE_RICHIESTA)
    if canale_cittadinanza:
        async for msg in canale_cittadinanza.history(limit=10):
            if msg.author == bot.user:
                break
        else:
            embed_cittadinanza = discord.Embed(
                title="🪪 ── UFFICIO CENTRALE ANAGRAFE E RILASCIO PASSAPORTI ── 🏛️",
                description=(
                    "Benvenuto all'interno del portale ufficiale dell'Ufficio Immigrazione e Registrazione Cittadini.\n\n"
                    "Per poter circolare liberamente all'interno della città, ottenere i documenti legali di riconoscimento ed accedere a tutti i settori riservati della comunità, è obbligatorio registrare la tua identità.\n\n"
                    "📋 **Istruzioni operative:**\n"
                    "• Clicca sul pulsante verde sottostante.\n"
                    "• Compila con cura tutti i campi del modulo anagrafico inserendo dati coerenti e realistici.\n"
                    "• Attendi la revisione da parte del corpo di controllo.\n\n"
                    "⚠️ *Dichiarare false generalità comporterà l'immediato rigetto della pratica e sanzioni amministrative.*"
                ),
                color=discord.Color.blue()
            )
            embed_cittadinanza.set_footer(text="Sistema di Registrazione Automatizzato • Servizi Cittadini protetti 🤌")
            await canale_cittadinanza.send(embed=embed_cittadinanza, view=VistaCittadinanza())

    # 3. PANNELLO FAMIGLIA CHIOCARO AUTOMATICO (ROSSO CHIARO)
    canale_chiocaro = bot.get_channel(ID_CANALE_PANNELLO_CHIOCARO)
    if canale_chiocaro:
        async for msg in canale_chiocaro.history(limit=10):
            if msg.author == bot.user:
                break
        else:
            embed_chiocaro = discord.Embed(
                title="🐔 ── CENTRO RECLUTAMENTO UFFICIALE FAMIGLIA CHIOCARO ── 👑",
                description=(
                    "Sei pronto a fare il grande salto e giurare fedeltà alla fazione più temuta e influente della città?\n\n"
                    "La **Famiglia Chiocaro** apre ufficialmente le porte ai soggetti più ambiziosi, leali e determinati a scalare i vertici del potere criminale ed economico.\n\n"
                    "📜 **Cosa ti aspetta entrando tra di noi?**\n"
                    "• Protezione garantita all'interno del nostro blocco.\n"
                    "• Supporto costante da parte dei veterani della fazione.\n"
                    "• Accesso alle chat segrete e alle operazioni esclusive.\n\n"
                    "🎯 *Pensi di avere la stoffa giusta? Clicca sul pulsante sottostante per sottoporre la tua candidatura ufficiale direttamente ai capi.*"
                ),
                color=discord.Color.from_rgb(255, 100, 100)
            )
            embed_chiocaro.set_footer(text="Famiglia Chiocaro • Onore, Potenza e Rispetto 🐔")
            await canale_chiocaro.send(embed=embed_chiocaro, view=VistaRichiestaChiocaro())

    # 4. PANNELLO FAMIGLIA CATUOZZO AUTOMATICO (GIALLO)
    canale_catuozzo = bot.get_channel(ID_CANALE_PANNELLO_CATUOZZO)
    if canale_catuozzo:
        async for msg in canale_catuozzo.history(limit=10):
            if msg.author == bot.user:
                break
        else:
            embed_catuozzo = discord.Embed(
                title="⚡ ── CENTRO RECLUTAMENTO UFFICIALE FAMIGLIA CATUOZZO ── ⚔️",
                description=(
                    "La forza, la disciplina e la furia dei Catuozzo sono leggendarie in tutta la regione. Se cerchi una vera famiglia disposta a tutto per i propri fratelli, questo è il tuo posto.\n\n"
                    "Stiamo selezionando esclusivamente guerrieri valorosi e membri attivi che vogliano lasciare un segno indelebile nella storia di questa città.\n\n"
                    "🛡️ **I nostri valori fondamentali:**\n"
                    "• Fratellanza incrollabile in qualsiasi situazione di pericolo.\n"
                    "• Strategia, azione e controllo assoluto del territorio.\n"
                    "• Ricompense generose per chi dimostra valore sul campo.\n\n"
                    "⚡ *Non perdere tempo: premi il pulsante blu qui sotto per inviare il tuo modulo di arruolamento.*"
                ),
                color=discord.Color.gold()
            )
            embed_catuozzo.set_footer(text="Famiglia Catuozzo • Potenza e Fratellanza ⚡")
            await canale_catuozzo.send(embed=embed_catuozzo, view=VistaRichiestaCatuozzo())

# 5. PANNELLO FAMIGLIA LIFARDO AUTOMATICO (VIOLA)
    canale_lifardo = bot.get_channel(ID_CANALE_PANNELLO_LIFARDO)
    if canale_lifardo:
        async for msg in canale_lifardo.history(limit=10):
            if msg.author == bot.user:
                break
        else:
            embed_lifardo = discord.Embed(
                title="🦅 ── CENTRO RECLUTAMENTO UFFICIALE FAMIGLIA LIFARDO ── ⚜️",
                description=(
                    "Eleganza, prestigio, astuzia e controllo commerciale. La nobile casata dei **Lifardo** recluta nuove menti brillanti e braccia forti per espandere il proprio impero.\n\n"
                    "Se possiedi classe, rispetto per le gerarchie e una brama inarrestabile di successo, la nostra porta è aperta.\n\n"
                    "🦁 **Vantaggi dell'affiliazione:**\n"
                    "• Copertura diplomatica ad altissimi livelli.\n"
                    "• Gestione strategica dei traffici e dei mercati cittadini.\n"
                    "• Unione indissolubile con una casata d'élite.\n\n"
                    "⚜️ *Fai la scelta giusta per il tuo futuro: compila subito il modulo di ammissione tramite il pulsante.*"
                ),
                color=discord.Color.purple()
            )
            embed_lifardo.set_footer(text="Famiglia Lifardo • Eleganza e Potere 🦅")
            await canale_lifardo.send(embed=embed_lifardo, view=VistaRichiestaLifardo())
            print("✅ Tutti i pannelli e gli embed sono stati aggiornati con testi ricchi e dettagliati!")

# ==========================================
# CONTROLLO PERMESSO RUOLO
# ==========================================
def solo_ruolo_autorizzato():
    async def predicate(interaction: discord.Interaction):
        # L'ID del ruolo richiesto
        ID_RUOLO_NECESSARIO = 1569773078097960960
        
        # Controlla se l'utente ha il ruolo cercando tra i suoi ruoli nel server
        ha_ruolo = any(role.id == ID_RUOLO_NECESSARIO for role in interaction.user.roles)
        
        if not ha_ruolo:
            await interaction.response.send_message("❌ **Non hai i permessi necessari** per usare questo comando!", ephemeral=True)
            return False
        return True
    return app_commands.check(predicate)

# ==========================================
# COMANDI VOCALI CON RESTRIZIONE DI RUOLO
# ==========================================

@bot.tree.command(name="vocale", description="Fa entrare il bot nel canale vocale predefinito")
@solo_ruolo_autorizzato()
async def vocale(interaction: discord.Interaction):
    guild = interaction.guild
    canale_vocale = guild.get_channel(ID_CANALE_VOCALE_DESTINAZIONE)

    if not canale_vocale or not isinstance(canale_vocale, discord.VoiceChannel):
        await interaction.response.send_message("❌ **Errore:** Canale vocale non trovato o ID non valido.", ephemeral=True)
        return

    voice_client = guild.voice_client

    try:
        if voice_client is not None:
            if voice_client.channel.id == ID_CANALE_VOCALE_DESTINAZIONE:
                await interaction.response.send_message("🔊 Il bot si trova già in questo canale vocale!", ephemeral=True)
                return
            await voice_client.move_to(canale_vocale)
        else:
            await canale_vocale.connect()

        await interaction.response.send_message(f"🔊 **Bot connesso con successo al canale vocale:** {canale_vocale.mention}!", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"❌ Impossibile connettersi al canale vocale: `{e}`", ephemeral=True)

@bot.tree.command(name="esci", description="Disconnette il bot dal canale vocale")
@solo_ruolo_autorizzato()
async def esci(interaction: discord.Interaction):
    guild = interaction.guild
    voice_client = guild.voice_client

    if voice_client is not None:
        await voice_client.disconnect()
        await interaction.response.send_message("🔇 **Bot disconnesso dal canale vocale.**", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Il bot non è attualmente connesso a nessun canale vocale.", ephemeral=True)


# ==========================================
# 9. AVVIO APPLICAZIONE
# ==========================================
@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")
    
    # Registrazione delle View per rendere i pulsanti persistenti
    bot.add_view(ViewPannelloPatenteB())
    bot.add_view(ViewPannelloImmatricolazione())
    bot.add_view(ViewPannelloPortoArmi())
    bot.add_view(VistaCittadinanza())
    bot.add_view(VistaRichiestaChiocaro())
    bot.add_view(VistaRichiestaCatuozzo())
    bot.add_view(VistaRichiestaLifardo())
    bot.add_view(ViewPannelloPatenteA())
    bot.add_view(ViewPannelloPatenteC())
    bot.add_view(ViewPannelloPatenteD())
    
    # 1. Pannello Patente B
    canale_patente = bot.get_channel(ID_CANALE_PANNELLO_PATENTE)
    if canale_patente:
        try:
            embed_p = discord.Embed(
                title="🚘 MOTORIZZAZIONE CIVILE - RICHIESTA PATENTE B",
                description=(
                    "Benvenuto nello sportello digitale della **Motorizzazione Civile**.\n\n"
                    "La **Patente B** ti autorizza alla guida di autoveicoli, autovetture private e mezzi di trasporto leggeri "
                    "all'interno del territorio di gioco.\n\n"
                    "📋 **REQUISITI E ISTRUZIONI:**\n"
                    "• Compila il modulo cliccando sul pulsante sottostante.\n"
                    "• Inserisci i dati della tua identità **Roleplay** con la massima accuratezza.\n"
                    "• Le richieste vengono revisionate in tempo reale dagli esaminatori preposti.\n\n"
                    "⚠️ *Eventuali dichiarazioni mendaci comportano il rigetto istantaneo della pratica.*"
                ),
                color=discord.Color.blue()
            )
            embed_p.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3202/3202003.png")
            embed_p.set_footer(text="Motorizzazione Civile • Sistema Licenze RP", icon_url=bot.user.display_avatar.url)
            await canale_patente.send(embed=embed_p, view=ViewPannelloPatenteB())
            print("Pannello Patente B inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO PATENTE B: {e}")

    # 2. Pannello Immatricolazioni
    canale_immat = bot.get_channel(ID_CANALE_PANNELLO_IMMATRICOLAZIONE)
    if canale_immat:
        try:
            embed_i = discord.Embed(
                title="🚙 MOTORIZZAZIONE CIVILE - IMMATRICOLAZIONE VEICOLI",
                description=(
                    "Benvenuto allo sportello immatricolazioni digitale.\n\n"
                    "Registra qui il tuo veicolo per ottenere la targa e il libretto ufficiale di circolazione.\n\n"
                    "📋 **ISTRUZIONI:**\n"
                    "• Clicca sul pulsante sottostante per compilare il modulo.\n"
                    "• Inserisci modello, categoria veicolo, targa desiderata e nome dell'intestatario RP."
                ),
                color=discord.Color.purple()
            )
            embed_i.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/741/741407.png")
            embed_i.set_footer(text="Motorizzazione Civile • Registro Veicoli")
            await canale_immat.send(embed=embed_i, view=ViewPannelloImmatricolazione())
            print("Pannello Immatricolazione Veicoli inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO IMMATRICOLAZIONE: {e}")

    # 3. Pannello Porto d'Armi
    canale_porto = bot.get_channel(ID_CANALE_PANNELLO_PORTO_ARMI)
    if canale_porto:
        try:
            embed_pa = discord.Embed(
                title="🛡️ QUESTURA • SPORTELLO PORTO D'ARMI",
                description=(
                    "Benvenuto allo sportello ufficiale della **Divisione Polizia Amministrativa**.\n\n"
                    "Il **Porto d'Armi** è il documento ufficiale che autorizza il porto e la detenzione legale di armi da fuoco "
                    "nel pieno rispetto delle normative vigenti sul territorio.\n\n"
                    "📋 **REQUISITI E PROCEDURE:**\n"
                    "• Clicca sul pulsante sottostante per avviare la pratica.\n"
                    "• Compila rigorosamente i dati anagrafici con la tua identità **Roleplay**.\n"
                    "• Specifica con chiarezza e realismo la motivazione della richiesta.\n\n"
                    "⚠️ *Ogni falsa dichiarazione o uso improprio comporterà il ritiro immediato del titolo e sanzioni penali.*"
                ),
                color=discord.Color.dark_red()
            )
            embed_pa.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1041/1041916.png")
            embed_pa.set_footer(text="Questura • Divisione Polizia Amministrativa", icon_url=bot.user.display_avatar.url)
            await canale_porto.send(embed=embed_pa, view=ViewPannelloPortoArmi())
            print("Pannello Porto d'Armi inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO PORTO D'ARMI: {e}")

    # 4. Pannello Patente A
    canale_patente_a = bot.get_channel(ID_CANALE_PANNELLO_PATENTE_A)
    if canale_patente_a:
        try:
            embed_pa_a = discord.Embed(
                title="🏍️ MOTORIZZAZIONE CIVILE - RICHIESTA PATENTE A",
                description=(
                    "Benvenuto nello sportello dedicato al rilascio delle licenze di guida per motocicli.\n\n"
                    "La **Patente A** ti autorizza alla conduzione di motoveicoli e ciclomotori all'interno della città.\n\n"
                    "📋 **REQUISITI E ISTRUZIONI:**\n"
                    "• Clicca sul pulsante sottostante per avviare la richiesta.\n"
                    "• Compila il modulo con i dati reali del tuo personaggio (**Roleplay**).\n\n"
                    "⚠️ *Dichiarazioni mendaci comporteranno il rigetto immediato dell'istanza.*"
                ),
                color=discord.Color.orange()
            )
            embed_pa_a.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2554/2554932.png")
            embed_pa_a.set_footer(text="Motorizzazione Civile • Sezione Motocicli", icon_url=bot.user.display_avatar.url)
            await canale_patente_a.send(embed=embed_pa_a, view=ViewPannelloPatenteA())
            print("Pannello Patente A inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO PATENTE A: {e}")

    # Sincronizzazione comandi slash
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi slash.")
    except Exception as e:
        print(f"Errore sincronizzazione comandi: {e}")

    # 5. Pannello Patente C
    canale_patente_c = bot.get_channel(ID_CANALE_PANNELLO_PATENTE_C)
    if canale_patente_c:
        try:
            embed_pa_c = discord.Embed(
                title="🚛 MOTORIZZAZIONE CIVILE - RICHIESTA PATENTE C",
                description=(
                    "Benvenuto nello sportello dedicato al rilascio delle licenze per **Veicoli Pesanti e Merci**.\n\n"
                    "La **Patente C** abilita alla guida di camion e autocarri per il trasporto professionale.\n\n"
                    "📋 **REQUISITI E ISTRUZIONI:**\n"
                    "• Clicca sul pulsante sottostante per compilare il modulo.\n"
                    "• Inserisci i dati anagrafici del tuo personaggio (**Roleplay**).\n\n"
                    "⚠️ *Dichiarazioni mendaci comporteranno sanzioni e il rigetto immediato.*"
                ),
                color=discord.Color.dark_blue()
            )
            embed_pa_c.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/754/754859.png")
            embed_pa_c.set_footer(text="Motorizzazione Civile • Sezione Veicoli Pesanti", icon_url=bot.user.display_avatar.url)
            await canale_patente_c.send(embed=embed_pa_c, view=ViewPannelloPatenteC())
            print("Pannello Patente C inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO PATENTE C: {e}")

    # 6. Pannello Patente D
    canale_patente_d = bot.get_channel(ID_CANALE_PANNELLO_PATENTE_D)
    if canale_patente_d:
        try:
            embed_pa_d = discord.Embed(
                title="🚌 MOTORIZZAZIONE CIVILE - RICHIESTA PATENTE D",
                description=(
                    "Benvenuto nello sportello dedicato al rilascio delle licenze per **Autobus e Trasporto Passeggeri**.\n\n"
                    "La **Patente D** abilita alla conduzione di pullman e mezzi adibiti al trasporto pubblico o privato di persone.\n\n"
                    "📋 **REQUISITI E ISTRUZIONI:**\n"
                    "• Clicca sul pulsante sottostante per avviare la pratica.\n"
                    "• Compila accuratamente il modulo con i dati del tuo personaggio (**Roleplay**).\n\n"
                    "⚠️ *Dichiarazioni mendaci comporteranno sanzioni e il rigetto immediato.*"
                ),
                color=discord.Color.teal()
            )
            embed_pa_d.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/3067/3067417.png")
            embed_pa_d.set_footer(text="Motorizzazione Civile • Sezione Autobus", icon_url=bot.user.display_avatar.url)
            await canale_patente_d.send(embed=embed_pa_d, view=ViewPannelloPatenteD())
            print("Pannello Patente D inviato con successo!")
        except Exception as e:
            print(f"ERRORE INVIO PANNELLO PATENTE D: {e}")

    # Sincronizzazione comandi slash
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi slash.")
    except Exception as e:
        print(f"Errore sincronizzazione comandi: {e}")



keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERRORE CRITICO: Variabile d'ambiente DISCORD_TOKEN mancante!")
