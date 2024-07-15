#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Owner'
    ST_BN1_URL = 'https://t.me/tellyhubsupports'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/tellycloud_bots'
    ST_BN3_NAME = 'SFW Group'
    ST_BN3_URL = 'https://t.me/leechcloud_sfw'
    ST_BN4_NAME = 'NSFW Group'
    ST_BN4_URL = 'https://t.me/leechcloud_nsfw'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own TELLYCLOUD-BOTS Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<blockquote><b><u>Generated Temporary Login Token!</u></b></blockquote>
<b><code>Temp Token :</code>{token}</b>
<b><code>Validity   :</code>{validity}</b>'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '<blockquote>✅️ Activated ✅</blockquote>'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<blockquote><b>Already Bot Login In!</b></blockquote>'
    INVALID_PASS = '<blockquote><b>Invalid Password!</b>\n\nKindly put the correct Password .</blockquote>'
    PASS_LOGGED = '<blockquote><b>Bot Permanent Login Successfully!</b></blockquote>'
    LOGIN_USED = '</blockquote><b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code></blockquote>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<blockquote>⌬ <b><i>BOT STATISTICS !</i></b>
<b><code>🟢Bot Uptime       :</code> {bot_uptime}</b>
<b><code>🎮RAM ( MEMORY ):</code>{ram_bar} {ram}%</b>
    <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}</blockquote>

<blockquote><b><code>🧱SWAP MEMORY :</code>{swap_bar} {swap}%</b>
    <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}</blockquote>

<blockquote><b><code>💾DISK :</code> {disk_bar} {disk}%</b>
<b><code>📀Total Disk Read  :</code> {disk_read}</b>
<b><code>💿Total Disk Write :</code> {disk_write}</b>
    <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</blockquote>
    
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>   
    '''
    SYS_STATS = '''<blockquote>⌬ <b><i>💻OS SYSTEM !</i></b>
<b><code>⌚OS Uptime     :</code> {os_uptime}</b>
<b><code>🪃OS Version    :</code> {os_version}</b>
<b><code>🪶OS Arch       :</code> {os_arch}</b></blockquote>

<blockquote><b><i>⌬ 📡NETWORK STATS !</i></b>
<b><code>📤Upload Data   :</code> {up_data}</b>
<b><code>📥Download Data :</code> {dl_data}</b>
<b><code>⏳Pkts Sent     :</code> {pkt_sent}k</b>
<b><code>⌛Pkts Received :</code> {pkt_recv}k</b>
<b><code>🛰Total I/O Data:</code> {tl_data}</b></blockquote>

<blockquote><b><code>🖥CPU :</code> {cpu_bar} {cpu}%</b>
<b><code>CPU Frequency   :</code> {cpu_freq}</b>
<b><code>System Avg Load :</code> {sys_load}</b>
<b><code>P-Core(s)       :</code> {p_core}</b>
<b><code>V-Core(s)       :</code> {v_core}</b>
<b><code>Total Core(s)   :</code> {total_core}</b>
<b><code>Usable CPU(s)   :</code> {cpu_use}</b></blockquote>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    REPO_STATS = '''<blockquote>⌬ <b><i>REPO STATISTICS !</i></b>
<code><b>Bot Updated     :</b> {last_commit}</code>
<code><b>Current Version :</b> {bot_version}</code>
<code><b>Latest Version  :</b> {lat_version}</code>
<code><b>Last ChangeLog  :</b> {commit_details}</code></blockquote>

⌬ <b>REMARKS :</b> <code>{remarks}</code>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    BOT_LIMITS = '''<blockquote>⌬ <b><i>BOT LIMITATIONS !</i></b>
<code><b>Direct Limit      :</b> {DL} GB</code>
<code><b>Torrent Limit     :</b> {TL} GB</code>
<code><b>GDrive Limit      :</b> {GL} GB</code>
<code><b>YT-DLP Limit      :</b> {YL} GB</code>
<code><b>Playlist Limit    :</b> {PL} GB</code>
<code><b>Mega Limit        :</b> {ML} GB</code>
<code><b>Clone Limit       :</b> {CL} GB</code>
<code><b>Leech Limit       :</b> {LL} GB</code></blockquote>

<blockquote><code><b>Token Validity     :</b> {TV}</code>
<code><b>User Time Limit    :</b> {UTI} / task</code>
<code><b>User Parallel Task :</b> {UT}</code>
<code><b>Bot Parallel Tasks :</b> {BT}</code></blockquote>
 
     <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<blockquote><i>Restarting.....</blockquote></i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<blockquote>⌬ <b><i>TellyCloud Bots Restarted Successfully!</i></b>
<code><b>Date     :</b> {date}</code>
<code><b>Time     :</b> {time}</code>
<code><b>TimeZone :</b> {timz}</code>
<code><b>Version  :</b> {version}</code></blockquote>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<blockquote><b>Pong</b>\n<code>🏓 {value} ms..</code></blockquote>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Task Started</i></b>
<code><b>💠Mode :</b> {Mode}</code>
<code><b>👤By   :</b> {Tag}</code></blockquote>\n\n"""
    LINKS_SOURCE = """<blockquote>➲ <b>Source:</b>
<b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------</blockquote>\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "<blockquote>➲ <b><u>Task Started :</u></b>\n│\n<b>Link:</b> <a href='{msg_link}'>Click Here</a></blockquote>"
    L_LOG_START =           "<blockquote>➲ <b><u>Leech Started :</u></b>\n│\n <b>User :</b> {mention} ( #ID{uid} )\n<b>Source :</b> <a href='{msg_link}'>Click Here</a></blockquote>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><blockquote>🏷️<i>{Name}</i></b></blockquote>\n'
    SIZE =                  '<code><b>💾Size        : </b>{Size}</code>\n'
    ELAPSE =                '<code><b>⌛️Elapsed     : </b>{Time}</code>\n'
    MODE =                  '<code><b>💠Mode        : </b>{Mode}</code>\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<code><b>📂Total Files : </b>{Files}</code>\n'
    L_CORRUPTED_FILES =     '<code><b>👹Crptd Files : </b>{Corrupt}</code>\n'
    L_CC =                  '<code><b>👤User By     : </b>{Tag}</code>\n\n'
    PM_BOT_MSG =            '<blockquote>➲ <b><i>File(s) have been Sent above</i></b></blockquote>'
    L_BOT_MSG =             '➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '<code><b>🔡Type       : </b>{Mimetype}</code>\n'
    M_SUBFOLD =             '<code><b>📁SubFolders : </b>{Folder}</code>\n'
    TOTAL_FILES =           '<code><b>📒Files      : </b>{Files}</code>\n'
    RCPATH =                '<code><b>📃Path       : </b>{RCpath}</code>\n'
    M_CC =                  '<code><b>👤By         : </b>{Tag}</code>\n\n'
    M_BOT_MSG =             '<blockquote>➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b></blockquote>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<blockquote><b><i>{Name}</i></b></blockquote>'

    #####---------PROGRESSIVE STATUS-------
    BAR =            '\n💫 {Bar}'
    PROCESSED =      '\n<code><b>🔄Sync     : </b>{Processed}</code>'
    STATUS =         '\n<code><b>🌐Status   : </b><a href="{Url}">{Status}</a> </code>'
    ETA =            '| <code><b>🍥ETA      : </b>{Eta}</code>'
    SPEED =          '\n<code><b>🚀Speed    : </b>{Speed} </code>'
    ELAPSED =        '| <code><b>👻Elapsed  : </b>{Elapsed}</code>'
    ENGINE =         '\n<code><b>⛓️Engine   : </b>{Engine}</code>'
    STA_MODE =       '\n<code><b>💠Mode     : </b>{Mode}</code>'
    SEEDERS  =       '\n<code><b>🌱Seeders  : </b>{Seeders} </code>'
    LEECHERS =       '| <code><b>🐌Leechers : </b>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<<code>b>📐Size     : </b>{Size}</code>'
    SEED_SPEED =     '\n<code><b>🚀Speed    : </b>{Speed} </code>'
    UPLOADED =       '| <code><b>📤Uploaded : </b>{Upload}</code>'                         
    RATIO =          '\n<code><b>📶Ratio    : </b>{Ratio} </code>'
    TIME =           '| <code><b>🕒Time     : </b>{Time}</code>'
    SEED_ENGINE =    '\n<code><b>⛓️Engine   : </b>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<code><b>📐Size     : </b>{Size}</code>'
    NON_ENGINE =     '\n<code><b>⛓️Engine   : </b>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =           '\n<code><b>👤User     : </b>{User}</code></code>'
    ID =             '\n<code><b>🆔ID       : </b>{Id}</code></code>'
    BTSEL =          '\n<b>🧲️Select :</b> {Btsel}'
    CANCEL =         '\n<b>❌Cancel :</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER =      '<blockquote>⌬ <b><i>Bot Stats</i></b></blockquote>'
    TASKS =          '\n<b>🧮Tasks:</b> {Tasks}'
    BOT_TASKS =      '\n<b>🥏Tasks:</b> {Tasks}/{Ttask} | <b>♟️AVL:</b> {Free}'
    Cpu =            '\n<b>🖥CPU:</b> {cpu}% |'
    FREE =             '<b>💿F:</b>{free}[{free_p}%]'
    Ram =            '\n<b>🎟RAM:</b>{ram}% | '
    uptime =           '<b>🟢UPTIME:</b>{uptime}'
    DL =             '\n<blockquote><b>🔻DL:</b> {DL}/s | '
    UL =                        '<b>🔺UL:</b> {UL}/s</blockquote>'

    ###--------BUTTONS-------
    PREVIOUS = '⏪Previous'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = 'Next⏩'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<blockquote>File/Folder is already available in Drive.\nHere are {content} list results:</blockquote>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG =  '<code><b>🔡Counting   : </b>{LINK}</code>'
    COUNT_NAME = '<code><b><i>{COUNT_NAME}</i></b></code>\n\n'
    COUNT_SIZE = '<code><b>📐Size       : </b>{COUNT_SIZE}</code>\n'
    COUNT_TYPE = '<code><b>🔡Type       : </b>{COUNT_TYPE}</code>\n'
    COUNT_SUB =  '<code><b>📁SubFolders : </b>{COUNT_SUB}</code>\n'
    COUNT_FILE = '<code><b>📒Files      : </b>{COUNT_FILE}</code>\n'
    COUNT_CC =   '<code><b>👤By         : </b>{COUNT_CC}</code>\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<blockquote><i>No Active Downloads!</i>
⌬ <b><i>Bot Stats</i></b>
<b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
<b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}</blockquote>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<blockquote>㊂ <b><u>User Settings :</u></b>
        
<code><b>👤Name         :</b> {NAME} [{ID}]</code> 
<code><b>🔮Telegram DC  :</b> {DC}</code> 
<code><b>🗣️Language     :</b> {LANG}</code></blockquote>

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    UNIVERSAL = '''<blockquote>㊂ <b><u>Universal Settings : {NAME}</u></b>

<code><b>🎥YT-DLP Options :</b> {YT}</code>
<code><b>🎯Daily Tasks    :</b> {DT}</code> per day
<code><b>🔛Last Bot Used  :</b> {LAST_USED}</code>
<code><b>🔑User Session   :</b> {USESS}</code>
<code><b>🎥MediaInfo Mode :</b> {MEDIAINFO}</code>
<code><b>🕵️Save Mode      :</b> {SAVE_MODE}</code>
<code><b>✉️User Bot PM    :</b> {BOT_PM}</code><blockquote>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    MIRROR = '''<blockquote>㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

<code><b>🧬RClone Config  :</b> <i>{RCLONE}</i></code>
<code><b>🅿Mirror Prefix  :</b> {MPREFIX}</code>
<code><b>💲Mirror Suffix  :</b> {MSUFFIX}</code>
<code><b>🌈Mirror Remname :</b> {MREMNAME}</code>
<code><b>🧿DDL Server(s)  :</b> <i>{DDL_SERVER}</i></code>
<code><b>📮User TD Mode   :</b> <i>{TMODE}</i></code>
<code><b>📝TotalUserTD(s) :</b> <i>{USERTD}</i></code>
<code><b>☁️Daily Mirror   :</b> {DM}</code> per day</blockquote>

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    LEECH = '''<blockquote>㊂ <b><u>Leech Settings for {NAME}</u></b>

<code><b>📂Daily Leech      :</b> {DL}</code> per day
<code><b>⚙️Leech Type       :</b> <i>{LTYPE}</i></code>
<code><b>🖼️Custom Thumbnail :</b> <i>{THUMB}</i></code>
<code><b>♈️Leech Split Size :</b> {SPLIT_SIZE}</code>
<code><b>♐️Equal Splits     :</b> <i>{EQUAL_SPLIT}</i></code>
<code><b>♒️Media Group      :</b> <i>{MEDIA_GROUP}</i></code>
<code><b>📄Leech Caption    :</b> {LCAPTION}</code>
<code><b>🅿Leech Prefix     :</b> {LPREFIX}</code>
<code><b>💲Leech Suffix     :</b> {LSUFFIX}</code>
<code><b>📦Leech Dumps      :</b> {LDUMP}</code>
<code><b>🌈Leech Remname    :</b> {LREMNAME}</code></blockquote>

    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''
