import os
import random
from threading import Thread
import discord
from discord import app_commands
from discord.ext import commands
from flask import Flask
import psycopg2

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

ID_CANALE_COMANDO_RECENSIONI = 1569837763459555440  # Sostituisci con l'ID del canale recensioni
ID_CANALE_LOG_RECENSIONI = 1569838024596922619     # Canale Forum Recensioni
LINK_IMMAGINE_RECENSIONE = "https://media.discordapp.net/attachments/1569724333704749107/1569838608347828304/Gemini_Generated_Image_jr98vmjr98vmjr98.jpg?ex=6af4e9a2&is=6af39822&hm=c9feb0602fe27105147d1f140d1ee0613abc4d8ba668d5f1880b684761e15503&=&format=webp"

ID_CANALE_REGISTRO_ARRESTI = 1569838174342221825
ID_CANALE_REGISTRO_MULTE = 1569838254247641128
ID_CANALE_CONTO_BANCARIO = 1569833371176276070
ID_CANALE_LOG_DOCUMENTI = 1569721095345405993  # Canale Accettazione / Log Documenti
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
ID_RUOLO_MEMBRO_CHIOCARO = 1569486576214478919

# ID FAMIGLIA CATUOZZO (GIALLO)
ID_CANALE_PANNELLO_CATUOZZO = 1569743489447501865
ID_CANALE_STAFF_CATUOZZO = 1569743678648623216
ID_RUOLO_STAFF_CATUOZZO = 1569481117055328447
ID_CANALE_ANNUNCI_CATUOZZO = 1569743744306118666
ID_RUOLO_MEMBRO_CATUOZZO = 1569486737649041408

# ID FAMIGLIA LIFARDO (VIOLA)
ID_CANALE_PANNELLO_LIFARDO = 1569747038785245355
ID_CANALE_STAFF_LIFARDO = 1569747072108986629
ID_CANALE_ANNUNCI_LIFARDO = 1569747095173333002
ID_RUOLO_STAFF_LIFARDO = 1569496579218341958
ID_RUOLO_MEMBRO_LIFARDO = 1569496594892595210

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

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATABASE_URL = os.getenv("DATABASE_URL")
ID_CANALE_CONTO_BANCARIO = 1569833371176276070
ID_RUOLO_STAFF = 1569773078097960960

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require', connect_timeout=5)

# --- FUNZIONE UNICA E SICURA PER GESTIRE L'ACCOUNT ---
def get_or_create_user_account(user_id):
    """Crea l'account se non esiste o restituisce i dati aggiornati."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Controlla se l'utente esiste già nel database
        cur.execute("SELECT cash, bank, account_open FROM economy WHERE user_id = %s", (user_id,))
        row = cur.fetchone()
        
        if not row:
            # Se non esiste affatto, lo crea direttamente con conto aperto e 1500 di bonus
            cur.execute(
                "INSERT INTO economy (user_id, cash, bank, account_open) VALUES (%s, %s, %s, %s)",
                (user_id, 1500.0, 0.0, True)
            )
            conn.commit()
            cash, bank, account_open = 1500.0, 0.0, True
        else:
            cash, bank, account_open = float(row[0]), float(row[1]), row[2]
            # Se per qualsiasi motivo il conto non risultava aperto ma l'utente esiste, lo attiviamo
            if not account_open:
                cur.execute("UPDATE economy SET account_open = TRUE WHERE user_id = %s", (user_id,))
                conn.commit()
                account_open = True
                
        cur.close()
        conn.close()
        return {"cash": cash, "bank": bank, "open": account_open}
    except Exception as e:
        print(f"Errore database unificato: {e}")
        return {"cash": 1500.0, "bank": 0.0, "open": True}

def save_user_balances(user_id, cash, bank):
    """Salva i nuovi saldi sul database."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE economy SET cash = %s, bank = %s WHERE user_id = %s", (cash, bank, user_id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Errore salvataggio saldi: {e}")

# --- MODALE APERTURA CONTO ---
class ModalAperturaConto(discord.ui.Modal, title="Banca Centrale - Apertura Conto"):
    nome_cognome = discord.ui.TextInput(
        label="Nome e Cognome (RP)",
        placeholder="Es. Mario Rossi",
        required=True,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        user_id = interaction.user.id
        
        # Questa funzione apre o verifica l'account in modo infallibile
        account = get_or_create_user_account(user_id)
        
        embed = discord.Embed(
            title="🏦 Conto Bancario Aperto con Successo!",
            description=f"Benvenuto nel sistema finanziario, **{self.nome_cognome.value}**.\nIl tuo conto è stato registrato.\n\n🎁 **Bonus di Benvenuto:** Ti sono stati accreditati **€1,500.00** in contanti!",
            color=discord.Color.green()
        )
        embed.add_field(name="💵 Contanti", value=f"€{account['cash']:,.2f}", inline=True)
        embed.add_field(name="🏦 Banca", value=f"€{account['bank']:,.2f}", inline=True)
        
        await interaction.followup.send(embed=embed, ephemeral=True)

# --- VIEW PER IL PANNELLO ---
class ViewPannelloBanca(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="💳 Apri Conto Bancario", style=discord.ButtonStyle.green, custom_id="btn_apri_conto")
    async def apri_conto(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ModalAperturaConto())

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user}")
    bot.add_view(ViewPannelloBanca())
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizzati {len(synced)} comandi slash.")
    except Exception as e:
        print(f"Errore sincronizzazione comandi: {e}")

@bot.tree.command(name="setup_banca", description="Invia il pannello per aprire il conto bancario nel canale")
@app_commands.checks.has_role(ID_RUOLO_STAFF)
async def setup_banca(interaction: discord.Interaction):
    canale = bot.get_channel(ID_CANALE_CONTO_BANCARIO)
    if not canale:
        await interaction.response.send_message("❌ Canale conto bancario non trovato!", ephemeral=True)
        return

    embed = discord.Embed(
        title="🏛️ BANCA CENTRALE - SPORTELLO APERTURA CONTI",
        description="Benvenuto allo sportello bancario ufficiale.\nClicca sul pulsante sottostante per registrare i tuoi dati, aprire ufficialmente il tuo conto corrente e ricevere il capitale iniziale.",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Sistema Finanziario integrato")

    await canale.send(embed=embed, view=ViewPannelloBanca())
    await interaction.response.send_message("✅ Pannello della banca inviato con successo nel canale!", ephemeral=True)

# --- COMANDI ECONOMICI ---
@bot.tree.command(name="portafoglio", description="Controlla il tuo saldo in contanti e in banca")
async def portafoglio(interaction: discord.Interaction, membro: discord.Member = None):
    await interaction.response.defer(ephemeral=True)
    target = membro or interaction.user
    
    # Se l'utente non ha mai aperto il conto, lo creiamo automaticamente così non dà mai errore
    account = get_or_create_user_account(target.id)
    
    embed = discord.Embed(
        title=f"💳 Portafoglio di {target.display_name}",
        color=discord.Color.gold()
    )
    embed.add_field(name="💵 Contanti", value=f"€{account['cash']:,.2f}", inline=True)
    embed.add_field(name="🏦 Banca", value=f"€{account['bank']:,.2f}", inline=True)
    embed.add_field(name="💰 Patrimonio Totale", value=f"€{(account['cash'] + account['bank']):,.2f}", inline=False)
    
    await interaction.followup.send(embed=embed, ephemeral=True)

@bot.tree.command(name="deposita", description="Deposita i contanti in banca")
async def deposita(interaction: discord.Interaction, importo: float):
    if importo <= 0:
        await interaction.response.send_message("❌ L'importo deve essere maggiore di zero!", ephemeral=True)
        return
        
    await interaction.response.defer(ephemeral=True)
    account = get_or_create_user_account(interaction.user.id)
    
    if account["cash"] < importo:
        await interaction.followup.send("❌ Non hai abbastanza contanti con te!", ephemeral=True)
        return
        
    account["cash"] -= importo
    account["bank"] += importo
    save_user_balances(interaction.user.id, account["cash"], account["bank"])
    
    await interaction.followup.send(f"✅ Hai depositato **€{importo:,.2f}** in banca.\n💵 Contanti rimanenti: €{account['cash']:,.2f}\n🏦 Banca: €{account['bank']:,.2f}", ephemeral=True)

@bot.tree.command(name="preleva", description="Preleva denaro dalla banca in contanti")
async def preleva(interaction: discord.Interaction, importo: float):
    if importo <= 0:
        await interaction.response.send_message("❌ L'importo deve essere maggiore di zero!", ephemeral=True)
        return
        
    await interaction.response.defer(ephemeral=True)
    account = get_or_create_user_account(interaction.user.id)
    
    if account["bank"] < importo:
        await interaction.followup.send("❌ Non hai abbastanza fondi in banca!", ephemeral=True)
        return
        
    account["bank"] -= importo
    account["cash"] += importo
    save_user_balances(interaction.user.id, account["cash"], account["bank"])
    
    await interaction.followup.send(f"✅ Hai prelevato **€{importo:,.2f}**.\n💵 Contanti: €{account['cash']:,.2f}\n🏦 Banca rimanente: €{account['bank']:,.2f}", ephemeral=True)

@bot.tree.command(name="paga", description="Paga dei contanti a un altro utente")
async def paga(interaction: discord.Interaction, destinatario: discord.Member, importo: float):
    if importo <= 0:
        await interaction.response.send_message("❌ L'importo deve essere maggiore di zero!", ephemeral=True)
        return
    if destinatario.id == interaction.user.id:
        await interaction.response.send_message("❌ Non puoi pagare te stesso!", ephemeral=True)
        return
        
    await interaction.response.defer(ephemeral=True)
    acc_mittente = get_or_create_user_account(interaction.user.id)
    acc_dest = get_or_create_user_account(destinatario.id)
    
    if acc_mittente["cash"] < importo:
        await interaction.followup.send("❌ Non hai abbastanza contanti!", ephemeral=True)
        return
        
    acc_mittente["cash"] -= importo
    acc_dest["cash"] += importo
    
    save_user_balances(interaction.user.id, acc_mittente["cash"], acc_mittente["bank"])
    save_user_balances(destinatario.id, acc_dest["cash"], acc_dest["bank"])
    
    await interaction.followup.send(f"✅ Hai pagato **€{importo:,.2f}** a {destinatario.mention}.", ephemeral=True)

@bot.tree.command(name="bonifico", description="Effettua un bonifico bancario a un altro utente")
async def bonifico(interaction: discord.Interaction, destinatario: discord.Member, importo: float):
    if importo <= 0:
        await interaction.response.send_message("❌ L'importo deve essere maggiore di zero!", ephemeral=True)
        return
    if destinatario.id == interaction.user.id:
        await interaction.response.send_message("❌ Non puoi fare un bonifico a te stesso!", ephemeral=True)
        return
        
    await interaction.response.defer(ephemeral=True)
    acc_mittente = get_or_create_user_account(interaction.user.id)
    acc_dest = get_or_create_user_account(destinatario.id)
    
    if acc_mittente["bank"] < importo:
        await interaction.followup.send("❌ Non hai abbastanza fondi in banca per il bonifico!", ephemeral=True)
        return
        
    acc_mittente["bank"] -= importo
    acc_dest["bank"] += importo
    
    save_user_balances(interaction.user.id, acc_mittente["cash"], acc_mittente["bank"])
    save_user_balances(destinatario.id, acc_dest["cash"], acc_dest["bank"])
    
    await interaction.followup.send(f"✅ Bonifico di **€{importo:,.2f}** effettuato con successo a {destinatario.mention}.", ephemeral=True)

# --- COMANDI STAFF ---
@bot.tree.command(name="aggiungi_soldi", description="[STAFF] Aggiunge denaro al conto o contanti di un utente")
@app_commands.checks.has_role(ID_RUOLO_STAFF)
async def aggiungi_soldi(interaction: discord.Interaction, destinatario: discord.Member, importo: float, conto: str = "banca"):
    await interaction.response.defer(ephemeral=True)
    acc = get_or_create_user_account(destinatario.id)
        
    if conto.lower() == "contanti":
        acc["cash"] += importo
    else:
        acc["bank"] += importo
        
    save_user_balances(destinatario.id, acc["cash"], acc["bank"])
    await interaction.followup.send(f"✅ Aggiunti **€{importo:,.2f}** ({conto}) a {destinatario.mention}.", ephemeral=True)

@bot.tree.command(name="rimuovi_soldi", description="[STAFF / MULTE] Rimuove denaro a un utente")
@app_commands.checks.has_role(ID_RUOLO_STAFF)
async def rimuovi_soldi(interaction: discord.Interaction, destinatario: discord.Member, importo: float, conto: str = "contanti"):
    await interaction.response.defer(ephemeral=True)
    acc = get_or_create_user_account(destinatario.id)
        
    if conto.lower() == "banca":
        if acc["bank"] < importo:
            await interaction.followup.send("❌ L'utente non ha abbastanza soldi in banca.", ephemeral=True)
            return
        acc["bank"] -= importo
    else:
        if acc["cash"] < importo:
            await interaction.followup.send("❌ L'utente non ha abbastanza contanti.", ephemeral=True)
            return
        acc["cash"] -= importo
        
    save_user_balances(destinatario.id, acc["cash"], acc["bank"])
    await interaction.followup.send(f"✅ Rimossi **€{importo:,.2f}** ({conto}) a {destinatario.mention}.", ephemeral=True)

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
keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERRORE CRITICO: Variabile d'ambiente DISCORD_TOKEN mancante!")
