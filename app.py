#ONLY ONE THE KING OF COMMITTIY : DEVIL
#INSTAGRAM : @Devilh3x7
#YOUTUBE : @Devilh3x
#TELEGRAM : @devilh3x
#WARNINNG ALERT : YE CODE KISI BHI GANDU DOST KO N BHEJE
#WARNA WAH APANE AAP KO GANDU SAMAJHNE LGEDA 😂

import os, json, time, urllib3, asyncio, aiohttp, ssl, traceback, random
from aiohttp import web
from xDL import *
from autoup import *
from datetime import datetime
from Pb2 import MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------- متغيرات عامة ----------
login_url, ob, version = AuToUpDaTE()
Hr = {
    'User-Agent': Uaa(),
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': ob
}

# قائمة البوتات (ستحتوي على كائنات BotInstance)
bot_instances = []
# للـ Round‑Robin
rr_counter = 0

class BotInstance:
    def __init__(self, uid, password, index):
        self.index = index  # 1-based
        self.uid = uid
        self.password = password
        self.online_writer = None
        self.key = None
        self.iv = None
        self.region = None
        self.token = None
        self.account_uid = None
        self.is_ready = False
        self.task_queue = asyncio.Queue()  # طابور المهام الخاص بهذا البوت
        self.worker_task = None

# ---------- دوال التشفير والباكيت الأساسية ----------
async def encrypted_proto(encoded_hex):
    key_bytes = b'Yg&tc%DEuh6%Zc^8'
    iv_bytes = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = version
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string)

async def MajorLogin(payload):
    url = f"{login_url}MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(data):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(data)
    return proto

async def DecRypTLoGinDaTa(data):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(data)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 7:
        headers = '000000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": await Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("open_id"), data.get("access_token")
            return None, None

async def SEndPacKeT(writer, packet):
    if writer:
        writer.write(packet)
        await writer.drain()

# ---------- دوال الباكيت ----------
async def join_teamcode_packet(team_code, key, iv, region):
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {2: 800, 6: 11, 8: "1.111.1", 9: 5, 10: 1}
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def Emote_k(target_uid, emote_id, key, iv, region):
    fields = {
        1: 21,
        2: {
            1: 804266360,
            2: 909000001,
            5: {
                1: int(target_uid),
                3: int(emote_id)
            }
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

# ---------- مهمة الاتصال لبوت واحد ----------
async def bot_online_task(bot: BotInstance):
    while True:
        try:
            # تسجيل الدخول
            open_id, access_token = await GeNeRaTeAccEss(bot.uid, bot.password)
            if not open_id:
                raise Exception("Failed to get open_id")

            payload = await EncRypTMajoRLoGin(open_id, access_token)
            login_resp = await MajorLogin(payload)
            if not login_resp:
                raise Exception("MajorLogin failed")

            auth = await DecRypTMajoRLoGin(login_resp)
            token = auth.token
            if not token:
                raise Exception("No token")

            url = auth.url
            bot.region = getattr(auth, 'region', 'IND')
            bot.account_uid = auth.account_uid
            bot.key = auth.key
            bot.iv = auth.iv
            timestamp = auth.timestamp

            login_data = await GetLoginData(url, payload, token)
            if not login_data:
                raise Exception("GetLoginData failed")
            ports = await DecRypTLoGinDaTa(login_data)
            online_ip, online_port = ports.Online_IP_Port.split(":")

            auth_token = await xAuThSTarTuP(int(bot.account_uid), token, int(timestamp), bot.key, bot.iv)

            # الاتصال TCP
            reader, writer = await asyncio.open_connection(online_ip, int(online_port))
            bot.online_writer = writer
            writer.write(bytes.fromhex(auth_token))
            await writer.drain()
            bot.is_ready = True
            print(f"✅ Bot {bot.index} ({bot.uid}) online")

            # تشغيل معالج الطابور إذا لم يكن يعمل
            if not bot.worker_task or bot.worker_task.done():
                bot.worker_task = asyncio.create_task(queue_worker(bot))

            # حلقة القراءة
            while True:
                data = await reader.read(9999)
                if not data:
                    break
            # إذا وصلنا هنا، الاتصال انقطع
            bot.online_writer = None
            bot.is_ready = False
            writer.close()
            await writer.wait_closed()

        except Exception as e:
            print(f"❌ Bot {bot.index} error: {e}")
            bot.is_ready = False
            if bot.online_writer:
                bot.online_writer.close()
                await bot.online_writer.wait_closed()
                bot.online_writer = None
        await asyncio.sleep(5)  # انتظر قبل إعادة المحاولة

# ---------- معالج الطابور ----------
async def queue_worker(bot: BotInstance):
    print(f"⚙️ Worker started for bot {bot.index}")
    while True:
        try:
            task = await bot.task_queue.get()
            action = task['action']
            params = task['params']
            future = task['future']

            if not bot.is_ready or not bot.online_writer:
                future.set_exception(Exception("Bot not connected"))
                continue

            if action == 'squad5':
                uid = params['uid']
                PAc = await OpEnSq(bot.key, bot.iv, bot.region)
                await SEndPacKeT(bot.online_writer, PAc)
                await asyncio.sleep(0.5)
                C = await cHSq(5, uid, bot.key, bot.iv, bot.region)
                await SEndPacKeT(bot.online_writer, C)
                await asyncio.sleep(0.5)
                V = await SEnd_InV(5, uid, bot.key, bot.iv, bot.region)
                await SEndPacKeT(bot.online_writer, V)
                await asyncio.sleep(3)
                E = await ExiT(None, bot.key, bot.iv)
                await SEndPacKeT(bot.online_writer, E)
                future.set_result({'success': True, 'message': f'Squad5 via bot {bot.index}'})

            elif action == 'emote':
                team = params['team']
                uids = params['uids']
                emote = params['emote']
                join_pkt = await join_teamcode_packet(team, bot.key, bot.iv, bot.region)
                await SEndPacKeT(bot.online_writer, join_pkt)
                await asyncio.sleep(1.5)
                for uid in uids:
                    try:
                        emote_pkt = await Emote_k(int(uid), int(emote), bot.key, bot.iv, bot.region)
                        await SEndPacKeT(bot.online_writer, emote_pkt)
                        await asyncio.sleep(0.1 + random.uniform(0, 0.05))  # عشوائية بسيطة
                    except Exception as e:
                        print(f"Emote error: {e}")
                leave_pkt = await ExiT(None, bot.key, bot.iv)
                await SEndPacKeT(bot.online_writer, leave_pkt)
                future.set_result({'success': True, 'message': f'Emote via bot {bot.index}'})

        except Exception as e:
            if 'future' in locals():
                future.set_exception(e)
        finally:
            bot.task_queue.task_done()

# ---------- دوال مساعدة للـ API ----------
def get_bot_by_index(index):
    for bot in bot_instances:
        if bot.index == index and bot.is_ready:
            return bot
    return None

def get_next_available_bot():
    global rr_counter
    ready_bots = [b for b in bot_instances if b.is_ready]
    if not ready_bots:
        return None
    bot = ready_bots[rr_counter % len(ready_bots)]
    rr_counter += 1
    return bot

async def enqueue_task(bot: BotInstance, action, params):
    future = asyncio.Future()
    await bot.task_queue.put({
        'action': action,
        'params': params,
        'future': future
    })
    return await future

# ---------- API Handlers (عام + خاص بالإصدار) ----------

# --- عام (موازنة تلقائية) ---
async def handle_squad5_auto(request):
    bot = get_next_available_bot()
    if not bot:
        return web.json_response({'error': 'No bots available'}, status=503)
    uid = request.query.get('uid')
    if not uid:
        return web.json_response({'error': 'Missing uid'}, status=400)
    try:
        result = await enqueue_task(bot, 'squad5', {'uid': uid})
        return web.json_response(result)
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)

async def handle_emote_auto(request):
    bot = get_next_available_bot()
    if not bot:
        return web.json_response({'error': 'No bots available'}, status=503)
    team = request.query.get('team')
    uids = request.query.getall('uid')
    emote = request.query.get('emote')
    if not team or not uids or not emote:
        return web.json_response({'error': 'Missing parameters'}, status=400)
    try:
        result = await enqueue_task(bot, 'emote', {'team': team, 'uids': uids, 'emote': emote})
        return web.json_response(result)
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)

# --- إصدارات محددة (/v1, /v2, ...) ---
def create_versioned_handlers():
    handlers = {}
    for i in range(1, 6):
        async def squad5_v(request, index=i):
            bot = get_bot_by_index(index)
            if not bot:
                return web.json_response({'error': f'Bot {index} not available'}, status=503)
            uid = request.query.get('uid')
            if not uid:
                return web.json_response({'error': 'Missing uid'}, status=400)
            try:
                result = await enqueue_task(bot, 'squad5', {'uid': uid})
                return web.json_response(result)
            except Exception as e:
                return web.json_response({'error': str(e)}, status=500)

        async def emote_v(request, index=i):
            bot = get_bot_by_index(index)
            if not bot:
                return web.json_response({'error': f'Bot {index} not available'}, status=503)
            team = request.query.get('team')
            uids = request.query.getall('uid')
            emote = request.query.get('emote')
            if not team or not uids or not emote:
                return web.json_response({'error': 'Missing parameters'}, status=400)
            try:
                result = await enqueue_task(bot, 'emote', {'team': team, 'uids': uids, 'emote': emote})
                return web.json_response(result)
            except Exception as e:
                return web.json_response({'error': str(e)}, status=500)

        handlers[f'/v{i}/squad5'] = squad5_v
        handlers[f'/v{i}/emote'] = emote_v
    return handlers

# ---------- بدء الخادم ----------
async def start_api_server():
    app = web.Application()
    # عام
    app.router.add_get('/squad5', handle_squad5_auto)
    app.router.add_get('/emote', handle_emote_auto)
    # إصدارات
    versioned = create_versioned_handlers()
    for path, handler in versioned.items():
        app.router.add_get(path, handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5000)
    await site.start()
    print("🌐 API server started on http://0.0.0.0:5000")

# ---------- الدالة الرئيسية ----------
async def main():
    if not os.path.exists("accounts.json"):
        print("❌ accounts.json not found. Create it as a list of {\"uid\": \"...\", \"password\": \"...\"}")
        return

    with open("accounts.json", "r") as f:
        accounts = json.load(f)

    if not accounts:
        print("❌ accounts.json is empty")
        return

    # إنشاء كائنات البوتات
    for idx, acc in enumerate(accounts, start=1):
        bot = BotInstance(acc['uid'], acc['password'], idx)
        bot_instances.append(bot)

    # تشغيل مهام الاتصال
    tasks = [asyncio.create_task(bot_online_task(bot)) for bot in bot_instances]
    tasks.append(asyncio.create_task(start_api_server()))

    print(f"🚀 Starting {len(bot_instances)} bots...")
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())