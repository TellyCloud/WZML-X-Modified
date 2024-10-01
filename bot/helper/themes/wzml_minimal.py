#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Owner'
    ST_BN1_URL = 'https://t.me/tellyhubsupports'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/tellycloud_bots'
    ST_BN3_NAME = 'SFW Group'
    ST_BN3_URL = 'https://t.me/LeechCloud_SFW'
    ST_BN4_NAME = 'NSFW Group'
    ST_BN4_URL = 'https://t.me/LeechCloud_NSFW'
    ST_MSG = '''<blockquote><i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b></blockquote>'''
    ST_BOTPM = '''<blockquote><i>Now, This bot will send all your files and links here. Start Using ...</i></blockquote>'''
    ST_UNAUTH = '''<blockquote><i>You Are not authorized user! Deploy your own TELLYCLOUD-BOTS Mirror-Leech bot</i></blockquote>'''
    OWN_TOKEN_GENERATE = '''<blockquote><b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i></blockquote>'''
    USED_TOKEN = '''<blockquote><b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i></blockquote>'''
    LOGGED_PASSWORD = '''<blockquote><b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i></blockquote>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<blockquote><b><u>Generated Temporary Login Token!</u></b>
<b><code>Temp Token :</code>{token}</b>
<b><code>Validity   :</code>{validity}</b></blockquote>'''

   
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<blockquote><b>Already Bot Login In!</b></blockquote>'
    INVALID_PASS = '<blockquote><b>Invalid Password!</b>\n\nKindly put the correct Password .</blockquote>'
    PASS_LOGGED = '<blockquote><b>Bot Permanent Login Successfully!</b></blockquote>'
    LOGIN_USED = '</blockquote><b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code></blockquote>'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py

    HELP_HEADER = "<blockquote>㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b></blockquote>"
    # ----- BUTTONS -------
    CLOUD_LINK        =        '☁️ 𝐂𝐥𝐨𝐮𝐝 \n𝐋𝐢𝐧𝐤'
    SAVE_MSG          =        '📨 𝐒𝐚𝐯𝐞 \n𝐌𝐞𝐬𝐬𝐚𝐠𝐞'
    RCLONE_LINK       =        '♻️ 𝐑𝐂𝐥𝐨𝐧𝐞 \n𝐋𝐢𝐧𝐤'
    DDL_LINK          =        '📎 {Serv} \n𝐋𝐢𝐧𝐤'
    SOURCE_URL        =        '🔐 𝐒𝐨𝐮𝐫𝐜𝐞 \n𝐋𝐢𝐧𝐤'
    INDEX_LINK_F      =        '🗂 𝐈𝐧𝐝𝐞𝐱 \n𝐋𝐢𝐧𝐤'
    INDEX_LINK_D      =        '⚡ 𝐈𝐧𝐝𝐞𝐱 \n𝐋𝐢𝐧𝐤'
    VIEW_LINK         =        '🌐 𝐕𝐢𝐞𝐰 \n𝐋𝐢𝐧𝐤'
    CHECK_PM          =        '📥 𝐕𝐢𝐞𝐰 𝐢𝐧 𝐁𝐨𝐭 𝐏𝐌'
    CHECK_LL          =        '🖇 𝐕𝐢𝐞𝐰 𝐢𝐧 \n 𝐋𝐢𝐧𝐤𝐬 𝐋𝐨𝐠'
    MEDIAINFO_LINK    =        '📃 𝐌𝐞𝐝𝐢𝐚𝐈𝐧𝐟𝐨'
    SCREENSHOTS       =        '🖼 𝐒𝐜𝐫𝐞𝐞𝐧𝐒𝐡𝐨𝐭𝐬'
    PREVIOUS          =        '⏪ 𝐏𝐫𝐞𝐯𝐢𝐨𝐮𝐬'
    REFRESH           =        'ᴘᴀɢᴇs\n{Page}'
    NEXT              =        '𝐍𝐞𝐱𝐭 ⏩'
    ACTIVATED         =        '✅️ 𝐀𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝 ✅'
    BASIC_BT          =        '𝐁𝐚𝐬𝐢𝐜'
    USER_BT           =        '𝐔𝐬𝐞𝐫𝐬'
    MICS_BT           =        '𝐌𝐢𝐜𝐬'
    O_S_BT            =        '𝐎𝐰𝐧𝐞𝐫 & 𝐒𝐮𝐝𝐨𝐬'
    CLOSE_BT          =        '𝐂𝐥𝐨𝐬𝐞'
    LOG_DISPLAY_BT    =        '📑 𝐋𝐨𝐠 𝐃𝐢𝐬𝐩𝐥𝐚𝐲'
    WEB_PASTE_BT      =        '📨 𝐖𝐞𝐛 𝐏𝐚𝐬𝐭𝐞 (𝐒𝐁)'
    # ---------------------
    # async def stats(client, message):
    BOT_STATS = '''<blockquote>⌬ <b><i>BOT STATISTICS !</i></b>
<b><code>🟢Bot Uptime      :</code> {bot_uptime}</b>
<b><code>🎮RAM ( MEMORY ):</code>{ram_bar} {ram}%</b>
    <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}</blockquote>

<blockquote><b><code>🧱SWAP MEMORY :</code>{swap_bar} {swap}%</b>
    <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}</blockquote>

<blockquote><b><code>💾DISK :</code> {disk_bar} {disk}%</b>
<b><code>📀Total Disk Read  :</code> {disk_read}</b>
<b><code>💿Total Disk Write :</code> {disk_write}</b>
    <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</blockquote>
    
    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>  
    '''
    SYS_STATS = '''<blockquote>⌬ <b><i>💻OS SYSTEM !</i></b>
<b><code>⌚OS Uptime    :</code> {os_uptime}</b>
<b><code>🪃OS Version   :</code> {os_version}</b>
<b><code>🪶OS Arch      :</code> {os_arch}</b></blockquote>

<blockquote><b><i>⌬ 📡NETWORK STATS !</i></b>
<b><code>📤Upload Data  :</code> {up_data}</b>
<b><code>📥Download Data:</code> {dl_data}</b>
<b><code>⏳Pkts Sent    :</code> {pkt_sent}k</b>
<b><code>⌛Pkts Received:</code> {pkt_recv}k</b>
<b><code>🛰Total I/O Data:</code> {tl_data}</b></blockquote>

<blockquote><b><code>🖥CPU :</code> {cpu_bar} {cpu}%</b>
<b><code>CPU Frequency  :</code> {cpu_freq}</b>
<b><code>System Avg Load:</code> {sys_load}</b>
<b><code>P-Core(s)      :</code> {p_core}</b>
<b><code>V-Core(s)      :</code> {v_core}</b>
<b><code>Total Core(s)  :</code> {total_core}</b>
<b><code>Usable CPU(s)  :</code> {cpu_use}</b></blockquote>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>
    '''
    REPO_STATS = '''<blockquote>⌬ <b><i>REPO STATISTICS !</i></b>
<code><b>Bot Updated    :</b> {last_commit}</code>
<code><b>Current Version:</b> {bot_version}</code>
<code><b>Latest Version :</b> {lat_version}</code>
<code><b>Last ChangeLog :</b> {commit_details}</code></blockquote>

⌬ <b>REMARKS :</b> <code>{remarks}</code>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>
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

<blockquote><code><b>Token Validity    :</b> {TV}</code>
<code><b>User Time Limit   :</b> {UTI} / task</code>
<code><b>User Parallel Task:</b> {UT}</code>
<code><b>Bot Parallel Tasks:</b> {BT}</code></blockquote>

     <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<blockquote><i>Restarting.....</blockquote></i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<blockquote>⌬ <b><i>TellyCloud Bots Restarted Successfully!</i></b>
<code><b>Date    :</b> {date}</code>
<code><b>Time    :</b> {time}</code>
<code><b>TimeZone:</b> {timz}</code>
<code><b>Version :</b> {version}</code></blockquote>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<blockquote><b>Pong</b>\n<code>🏓 {value} ms..</code></blockquote>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Task Started</i></b>
<code><b>💠Mode:</b>{Mode}</code>
<code><b>👤By  :</b> {Tag}</code></blockquote>\n\n"""
    LINKS_SOURCE = """<blockquote>➲ <b>Source:</b>
<b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------</blockquote>\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START          ="<blockquote>➲ <b><u>Task Started :</u></b>\n│\n<b>Link:</b> <a href='{msg_link}'>Click Here</a></blockquote>"
    L_LOG_START       ="<blockquote>➲ <b><u>Leech Started :</u></b>\n│\n <b>User :</b> {mention} ( #ID{uid} )\n<b>Source :</b> <a href='{msg_link}'>Click Here</a></blockquote>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME              ='<b><blockquote>🏷️<i>{Name}</i></b></blockquote>\n\n'
    SIZE              ='<b><code>💾Size    : </code>{Size}</b>\n'
    ELAPSE            ='<b><code>⌛️Elapsed : </code>{Time}</b>\n'
    MODE              ='<b><code>💠Mode    :</code>{Mode}</b>\n'

    # ----- LEECH -------
    L_TOTAL_FILES     ='<b><code>📂FS Total: </code>{Files}</b>\n'
    L_CORRUPTED_FILES ='<b><code>👹CrptdFls: </code>{Corrupt}</b>'
    L_CC              ='<b><code>👤User By : </code>{Tag}</b>\n\n'
    PM_BOT_MSG        ='<blockquote>➲ <b><i>File(s) have been Sent above</i></b></blockquote>'
    L_BOT_MSG         ='<blockquote>➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b></blockquote>'
    L_LL_MSG          ='<blockquote>➲ <b><i>File(s) have been Sent. Access via Links...</i></b></blockquote>\n'
    
    # ----- MIRROR -------
    M_TYPE            ='<b><code>🔡Type     : </code>{Mimetype}</b>\n'
    M_SUBFOLD         ='<b><code>📁SubFolder: </code>{Folder}</b>\n'
    TOTAL_FILES       ='<b><code>📒Files    : </code>{Files}</b>\n'
    RCPATH            ='<b><code>📃Path     : </code>{RCpath}</b>\n'
    M_CC              ='<b><code>👤By       : </code>{Tag}</b>\n\n'
    M_BOT_MSG         ='<blockquote>➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b></blockquote>'

    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME       ='<blockquote><b><i>{Name}</i></b></blockquote>\n'

    #####---------PROGRESSIVE STATUS-------
    BAR               =' {Bar}\n'
    PROCESSED         ='<b><code>🔄Sync    : </code>{Processed}</b>\n'
    STATUS            ='<b><code>🌐Status  : </code><a href="{Url}">{Status}</a></b>\n'
    ETA               ='<b><code>🍥ETA     : </code>{Eta}</b>\n'
    SPEED             ='<b><code>🚀Speed   : </code>{Speed}</b>\n'
    ELAPSED           ='<b><code>👻Elapsed : </code>{Elapsed}</b>\n'
    ENGINE            ='<b><code>⛓️Engine  : </code>{Engine}</b>\n'
    STA_MODE          ='<b><code>💠Mode    :</code>{Mode}</b>\n'
    SEEDERS           ='<b><code>🌱Seeders : </code>{Seeders} | </b>'
    LEECHERS          ='<b><code>🐌Leechers: </code>{Leechers}</b>\n'

    ####--------SEEDING----------
    SEED_SIZE         ='<b><code>📐Size    : </code>{Size}</b>\n'
    SEED_SPEED        ='<b><code>🚀Speed   : </code>{Speed}</b>\n'
    UPLOADED          ='<b><code>📤Uploaded: </code>{Upload}</b>\n'                         
    RATIO             ='<b><code>📶Ratio   : </code>{Ratio}</b>\n'
    TIME              ='<b><code>🕒Time    : </code>{Time}</b>\n'
    SEED_ENGINE       ='<b><code>⛓️Engine  : </code>{Engine}</b>\n'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE       ='<b><code>📐Size    : </code>{Size}</b>\n'
    NON_ENGINE        ='<b><code>⛓️Engine  : </code>{Engine}</b>\n'

    ####--------OVERALL MSG FOOTER----------
    USER              ='<b><code><b>👤User    : </code><tg-spoiler>{User}</tg-spoiler></b>\n'
    ID                ='<b><code><b>🆔ID      : </code>{Id}</b>\n'
    BTSEL             ='<b>🧲️Select  : {Btsel}</b>\n'
    CANCEL            ='<b>❌Cancel : {Cancel}</b>\n\n'

    ####------FOOTER--------
    FOOTER            ='\n<blockquote>⌬ <b><i>Bot Stats</i></b></blockquote>'
    TASKS             ='\n<b>🧮Tasks :</b> {Tasks}'
    BOT_TASKS         ='\n<b>🥏Tasks :</b> {Tasks}/{Ttask} | <b>♟️AVL :</b> {Free}'
    Cpu               ='\n<b>🖥CPU :</b> {cpu}% |'
    FREE              ='<b>💿F :</b>{free}[{free_p}%]'
    Ram               ='\n<b>🎟RAM :</b>{ram}% | '
    uptime            ='<b>🟢UPTIME :</b>{uptime}'
    DL                ='\n<blockquote><b>🔻DL :</b> {DL}/s | '
    UL                ='<b>🔺UL :</b> {UL}/s</blockquote>'
    

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE    = '<blockquote>File/Folder is already available in Drive.\nHere are {content} list results:</blockquote>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG         ='<b><code>🔡Counting : </code>{LINK}</b>\n'
    COUNT_NAME        ='<b><code><i>{COUNT_NAME}</i></b></b>\n'
    COUNT_SIZE        ='<b><code>📐Size     : </code>COUNT_SIZE}</b>\n'
    COUNT_TYPE        ='<b><code>🔡Type     : </code>{COUNT_TYPE}</b>\n'
    COUNT_SUB         ='<b><code>📁SubFolder: </code>{COUNT_SUB}</b>\n'
    COUNT_FILE        ='<b><code>📒Files    : </code>{COUNT_FILE}</b>\n'
    COUNT_CC          ='<b><code>👤By       : </code>{COUNT_CC}</b>\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING    ='<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND        ='<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND    ='No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL      = '''<blockquote><i>No Active Downloads!</i>
⌬ <b><i>Bot Stats</i></b>
<b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
<b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}</blockquote>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<blockquote>㊂ <b><u>User Settings :</u></b>
        
<code><b>👤Name        :</b> {NAME} [{ID}]</code> 
<code><b>🔮Telegram DC :</b> {DC}</code> 
<code><b>🗣️Language    :</b> {LANG}</code></blockquote>

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>'''

    UNIVERSAL = '''<blockquote>㊂ <b><u>Universal Settings : {NAME}</u></b>

<code><b>🎥YT-DLP Options:</b> {YT}</code>
<code><b>🎯Daily Tasks   :</b> {DT}</code> per day
<code><b>🔛Last Bot Used :</b> {LAST_USED}</code>
<code><b>🔑User Session  :</b> {USESS}</code>
<code><b>🎥MediaInfo Mode:</b> {MEDIAINFO}</code>
<code><b>🕵️Save Mode     :</b> {SAVE_MODE}</code>
<code><b>✉️User Bot PM   :</b> {BOT_PM}</code><blockquote>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>'''

    MIRROR = '''<blockquote>㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

<code><b>🧬RClone Config :</b> <i>{RCLONE}</i></code>
<code><b>🅿Mirror Prefix :</b> {MPREFIX}</code>
<code><b>💲Mirror Suffix  :</b> {MSUFFIX}</code>
<code><b>🌈Mirror Remname:</b> {MREMNAME}</code>
<code><b>🧿DDL Server(s) :</b> <i>{DDL_SERVER}</i></code>
<code><b>📮User TD Mode  :</b> <i>{TMODE}</i></code>
<code><b>📝TotalUserTD(s):</b> <i>{USERTD}</i></code>
<code><b>☁️Daily Mirror  :</b> {DM}</code> per day</blockquote>

<blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>'''

    LEECH = '''<blockquote>㊂ <b><u>Leech Settings for {NAME}</u></b>

<code><b>📂Daily Leech     :</b> {DL}</code> per day
<code><b>⚙️Leech Type      :</b> <i>{LTYPE}</i></code>
<code><b>🖼️Custom Thumbnail:</b> <i>{THUMB}</i></code>
<code><b>♈️Leech Split Size:</b> {SPLIT_SIZE}</code>
<code><b>♐️Equal Splits    :</b> <i>{EQUAL_SPLIT}</i></code>
<code><b>♒️Media Group     :</b> <i>{MEDIA_GROUP}</i></code>
<code><b>📄Leech Caption   :</b> {LCAPTION}</code>
<code><b>🅿Leech Prefix    :</b> {LPREFIX}</code>
<code><b>💲Leech Suffix    :</b> {LSUFFIX}</code>
<code><b>📦Leech Dumps     :</b> {LDUMP}</code>
<code><b>🌈Leech Remname   :</b> {LREMNAME}</code></blockquote>

    <blockquote><a href="https://t.me/TELLYCLOUD_Bots"><b>✅ 𝗣𝗢𝗪𝗘𝗥 𝗕𝗬 𝗧𝗘𝗟𝗟𝗬𝗖𝗟𝗢𝗨𝗗 𝗕𝗢𝗧𝗦 🤖</b></a></blockquote>'''
