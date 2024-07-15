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
<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

<b><code>🧱SWAP MEMORY :</code>{swap_bar} {swap}%</b>
<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

<b><code>💾DISK :</code> {disk_bar} {disk}%</b>
<b><code>📀Total Disk Read  :</code> {disk_read}</b>
<b><code>💿Total Disk Write :</code> {disk_write}</b>
<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</blockquote>
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>   
    '''
    SYS_STATS = '''⌬ <blockquote><b><i>💻OS SYSTEM !</i></b>
<b><code>⌚OS Uptime  :</code> {os_uptime}</b>
<b><code>🪃OS Version  :</code> {os_version}</b>
<b><code>🪶OS Arch     :</code> {os_arch}</b>

<b><i>⌬ 📡NETWORK STATS !</i></b>
<b><code>📤Upload Data   :</code> {up_data}</b>
<b><code>📥Download Data :</code> {dl_data}</b>
<b><code>⏳Pkts Sent     :</code> {pkt_sent}k</b>
<b><code>⌛Pkts Received :</code> {pkt_recv}k</b>
<b><code>🛰Total I/O Data:</code> {tl_data}</b>

<b><code>🖥CPU           :</code> {cpu_bar} {cpu}%</b>
<b><code>CPU Frequency   :</code> {cpu_freq}</b>
<b><code>System Avg Load :</code> {sys_load}</b>
<b><code>P-Core(s)       :</code> {p_core}</b>
<b><code>V-Core(s)       :</code> {v_core}</b>
<b><code>Total Core(s)   :</code> {total_core}</b>
<b><code>Usable CPU(s)   :</code> {cpu_use}</b></blockquote>
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    REPO_STATS = '''⌬ <blockquote><b><i>REPO STATISTICS !</i></b>
<b>Bot Updated     :</b> {last_commit}
<b>Current Version :</b> {bot_version}
<b>Latest Version  :</b> {lat_version}
<b>Last ChangeLog  :</b> {commit_details}</blockquote>

    ⌬ <b>REMARKS :</b> <code>{remarks}</code>
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    BOT_LIMITS = '''<blockquote>⌬ <b><i>BOT LIMITATIONS :</i></b>
    <b>Direct Limit  :</b> {DL} GB
    <b>Torrent Limit :</b> {TL} GB
    <b>GDrive Limit  :</b> {GL} GB
    <b>YT-DLP Limit  :</b> {YL} GB
    <b>Playlist Limit:</b> {PL} GB
    <b>Mega Limit    :</b> {ML} GB
    <b>Clone Limit   :</b> {CL} GB
    <b>Leech Limit   :</b> {LL} GB</blockquote>

    <blockquote><b>Token Validity      :</b> {TV}
    <b>User Time Limit     :</b> {UTI} / task
    <b>User Parallel Tasks :</b> {UT}
    <b>Bot Parallel Tasks  :</b> {BT}</blockquote>
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<blockquote><i>Restarting.....</blockquote></i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<blockquote>⌬ <b><i>TellyCloud Bots Restarted Successfully!</i></b>
    <b>Date     :</b> {date}
    <b>Time     :</b> {time}
    <b>TimeZone :</b> {timz}
    <b>Version  :</b> {version}</blockquote>
    <a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<blockquote><b>Pong</b>\n<code>🏓 {value} ms..</code></blockquote>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<blockquote><b><i>Task Started</i></b>
<b>Mode :</b> {Mode}
<b>By   :</b> {Tag}\n\n</blockquote>"""
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
    SIZE =                  '<b>💾Size       : </b>{Size}'
    ELAPSE =                '<b>⌛️Elapsed    : </b>{Time}\n'
    MODE =                  '<b>💠Mode       : </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>📂Total Files : </b>{Files}\n'
    L_CORRUPTED_FILES =     '<b>👹Corrupted Files : </b>{Corrupt}\n'
    L_CC =                  '<b>👤User By : </b>{Tag}\n\n'
    PM_BOT_MSG =            '<blockquote>➲ <b><i>File(s) have been Sent above</i></b></blockquote>'
    L_BOT_MSG =             '➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>Type : </b>{Mimetype}\n'
    M_SUBFOLD =             '<b>SubFolders : </b>{Folder}\n'
    TOTAL_FILES =           '<b>Files : </b>{Files}\n'
    RCPATH =                '<b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>By : </b>{Tag}\n\n'
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
    BAR =            '\n 💫 {Bar}'
    PROCESSED =      '\n<blockquote><b>🔄Sync:</b> {Processed}</blockquote>'
    STATUS =         '\n<b>🌐Status:</b> <a href="{Url}">{Status}</a> | '
    ETA =            '<b>🍥ETA:</b> {Eta}'
    SPEED =          '\n<blockquote><b>🚀Speed:</b> {Speed} | '
    ELAPSED =                                        '<b>👻Elapsed:</b> {Elapsed}</blockquote>'
    ENGINE =         '\n<blockquote><b>⛓️Engine:</b> {Engine}</blockquote>'
    STA_MODE =       '\n<b>💠Mode:</b> {Mode}'
    SEEDERS  =       '\n<b>🌱Seeders:</b> {Seeders} | '
    LEECHERS =                                        '<b>🐌Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>📐Size : </b>{Size}'
    SEED_SPEED =     '\n<b>🚀Speed : </b> {Speed}'
    UPLOADED =       '\n<b>📤Uploaded : </b> {Upload}'                         
    RATIO =          '\n<b>📶Ratio : </b> {Ratio}'
    TIME =           '\n<b>🕒Time : </b> {Time}'
    SEED_ENGINE =    '\n<b>⛓️Engine :</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>📐Size : </b>{Size}'
    NON_ENGINE =     '\n<b>⛓️Engine :</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =           '\n<blockquote><b>👤User :</b> <code>{User}</code> | '
    ID =                                                 '<b>🆔ID :</b> <code>{Id}</code></blockquote>'
    BTSEL =          '\n<b>🧲️Select :</b> {Btsel}'
    CANCEL =         '\n<b>❌Cancel :</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER =      '<blockquote>⌬ <b><i>Bot Stats</i></b></blockquote>\n'
    TASKS =          '<b>🧮Tasks:</b> {Tasks}\n'
    BOT_TASKS =      '<b>🥏Tasks:</b> {Tasks}/{Ttask} | <b>♟️AVL:</b> {Free}\n'
    Cpu =            '<b>🖥CPU:</b> {cpu}% |'
    FREE =                      '<b>💿F:</b>{free}[{free_p}%]\n'
    Ram =          '<b>🎟RAM:</b>{ram}% | '
    uptime =                     '<b>🟢UPTIME:</b>{uptime}\n'
    DL =           '<blockquote><b>🔻DL:</b> {DL}/s | '
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
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n│\n'
    COUNT_SIZE = '<b>📐Size : </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '<b>🔡Type : </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '<b>📁SubFolders : </b>{COUNT_SUB}\n'
    COUNT_FILE = '<b>📒Files : </b>{COUNT_FILE}\n'
    COUNT_CC =   '<b>👤By : </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
<blockquote>⌬ <b><i>Bot Stats</i></b>
<b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
<b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}</blockquote>

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<blockquote>㊂ <b><u>User Settings :</u></b>
        
<b>👤Name :</b> {NAME} ( <code>{ID}</code> )
<b>🔮Telegram DC :</b> {DC}
<b>🗣️Language :</b> {LANG}</blockquote>

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    UNIVERSAL = '''<blockquote>㊂ <b><u>Universal Settings : {NAME}</u></b>

<b>🎥YT-DLP Options :</b> <b><code>{YT}</code></b>
<b>🎯Daily Tasks :</b> <code>{DT}</code> per day
<b>🔛Last Bot Used :</b> <code>{LAST_USED}</code>
<b>🔑User Session :</b> <code>{USESS}</code>
<b>🎥MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
<b>🕵️Save Mode :</b> <code>{SAVE_MODE}</code>
<b>✉️User Bot PM :</b> <code>{BOT_PM}</code><blockquote>

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    MIRROR = '''<blockquote>㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

<b>🧬RClone Config :</b> <i>{RCLONE}</i>
<b>🅿Mirror Prefix :</b> <code>{MPREFIX}</code>
<b>💲Mirror Suffix :</b> <code>{MSUFFIX}</code>
<b>🌈Mirror Remname :</b> <code>{MREMNAME}</code>
<b>🧿DDL Server(s) :</b> <i>{DDL_SERVER}</i>
<b>📮User TD Mode :</b> <i>{TMODE}</i>
<b>📝Total User TD(s) :</b> <i>{USERTD}</i>
<b>☁️Daily Mirror :</b> <code>{DM}</code> per day</blockquote>

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''

    LEECH = '''<blockquote>㊂ <b><u>Leech Settings for {NAME}</u></b>

<b>📂Daily Leech :</b><code>{DL}</code> per day
<b>⚙️Leech Type :</b> <i>{LTYPE}</i>
<b>🖼️Custom Thumbnail :</b> <i>{THUMB}</i>
<b>♈️Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
<b>♐️Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
<b>♒️Media Group :</b> <i>{MEDIA_GROUP}</i>
<b>📄Leech Caption :</b> <code>{LCAPTION}</code>
<b>🅿Leech Prefix :</b> <code>{LPREFIX}</code>
<b>💲Leech Suffix :</b> <code>{LSUFFIX}</code>
<b>📦Leech Dumps :</b> <code>{LDUMP}</code>
<b>🌈Leech Remname :</b> <code>{LREMNAME}</code></blockquote>

<a href="https://t.me/TELLYCLOUD_Bots"><b>🫧💗✨𝐓𝐄𝐋𝐋𝐘𝐂𝐋𝐎𝐔𝐃 𝐁𝐎𝐓𝐒™🫧💗✨</b></a>'''
