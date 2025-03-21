import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

questions = [
    {
        "question": "İklim değişikliğinin başlıca nedeni nedir??",
        "options": ["A) Volkanik patlamar", "B) Güneş patlamaları", "C) Sera gazları", "D) Dünya'nın yörüngesindeki doğal değişimler", "E)İneklerin Oluşturduğu metan gazları"],
        "answer": "C"
    },
    {
        "question": "Aşağıdaki gazlardan hangisi önemli bir sera gazı DEĞİLDİR?",
        "options": ["A) Karbondioksit (CO2)", "B) Metan (CH4)", "C) Karbon monoksit (CO)", "D) Diazot monoksit (N2O)", "E) Dihydrogen Monoxide (H20)"],
        "answer": "E"
    },
    {
        "question": " Küresel sera gazı emisyonlarına en fazla hangi sektör katkıda bulunur??",
        "options": ["A) Ulaşım", "B) Tarım", "C)  Enerji üretimi (kömür, petrol, gaz gibi)", "D) Ormansızlaşma", "E) Madencilik"],
        "answer": "C"
    },
    {
        "question": "Bireyler karbon ayak izini nasıl azaltabilir? (EN İYİ seçenek hangisidir?)",
        "options": ["A) Toplu taşıma, bisiklet veya yürüyüş yapmak", "B) Geri dönüşüm yapmak ve atıkları azaltmak", "C) Yenilenebilir enerji kaynaklarına geçmek", "D) Su, elektrik gibi ihtiyaçları ziyan etmemek", "E) Hepsi"],
        "answer": "E"
    },
    {
        "question": "Karbon denkleştirme nedir?",
        "options": ["A)Karbonun yer altına depolanması", "B) Kendi emisyonlarınızı dengelemek için CO2 azaltan projelere yatırım yapmak", "C)Daha fazla karbon emen bitkiler ekmek", "D)Elektrikli araçlar kullanarak araba emisyonlarını azaltmak", "E) Doğaya daha fazla karbon vermek"],
        "answer": "B"
    },
    {
        "question": "Evde su ve enerji tasarrufu sağlayan en etkili günlük alışkanlık hangisidir?",
        "options": ["A) Daha kısa duş almak", "B) Çamaşırları soğuk suyla yıkamak", "C) LED ampuller kullanmak", "D)  Diş fırçalarken musluğu kapatmak", "E) daha az tuvaleti kullanmak"],
        "answer": "B"
    },
    {
        "question": "Ormansızlaşma iklim değişikliğini nasıl etkiler?",
        "options": ["A) Karbondioksit emilimini azaltır ", "B) Hava sıcaklıklarını düşürür", "C) Atmosfere oksijen ekler", "D) Yağış miktarını artırır", "E) Hepsi"],
        "answer": "A"
    },
    {
        "question": " Aşağıdakilerden hangisi iklim değişikliğiyle mücadele için bireysel bir adım olabilir?",
        "options": ["A)Yerel ve organik ürünler tüketmek", "B)Plastik kullanımını azaltmak", "C)Enerji tasarruflu cihazlar kullanmak", "D) Hybrid yada elektrikli araç kullanmak", "E) hepsi"],
        "answer": "E"
    },
    {
        "question": "Aşağıdaki iklim modellerinden hangisi, belirli bir bölgenin uzun vadeli sıcaklık ve yağış eğilimlerini en doğru şekilde tahmin etmek için kullanılır?",
        "options": ["A)GCM (Küresel İklim Modeli)", "B) RCM (Bölgesel İklim Modeli) ", "C)ENSO (El Niño-Güney Salınımı)", "D) IPCC (Hükümetlerarası İklim Değişikliği Paneli)", "E) PDO (Pasifik Dekadal Salınımı) "],
        "answer": "B"
    },
    {
        "question": "Okyanusların asitlenmesi, iklim değişikliğinin dolaylı etkilerinden biridir. Bu olayın temel nedeni nedir?",
        "options": ["A)Deniz seviyesinin yükselmesi", "B) Plastik kirliliğinin artması", "C) Atmosferdeki karbondioksitin (CO2) okyanus suyunda çözünmesi", "D)Fosfat ve nitrat gibi tarım kimyasallarının okyanusa karışması", "E)Okyanus akıntılarının hızlanması"],
        "answer": "C"
    }
    ]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def iklim(ctx):
    try:
        with open("iklim.txt", "r", encoding="utf-8") as file:
            content = file.read()  
        chunk_size = 2000
        for i in range(0, len(content), chunk_size):
            await ctx.send(content[i:i + chunk_size]) 

    except FileNotFoundError:
        await ctx.send("Sorry, I couldn't find the file `iklim.txt`.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        
@bot.command()
async def linkler(ctx):
    try:
        with open("link.txt", "r", encoding="utf-8") as file:
            content = file.read()  
        chunk_size = 2000
        for i in range(0, len(content), chunk_size):
            await ctx.send(content[i:i + chunk_size]) 

    except FileNotFoundError:
        await ctx.send("Sorry, I couldn't find the file `iklim.txt`.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        

@bot.command(name='quiz')
async def start_quiz(ctx):
    score = 0

    for i, q in enumerate(questions, start=1):
        question_text = f"**Q{i}: {q['question']}**\n"
        for option in q["options"]:
            question_text += f"{option}\n"

        await ctx.send(question_text)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.upper() in ["A", "B", "C", "D", "E"]

        try:
            response = await bot.wait_for("message", timeout=30.0, check=check)
        except TimeoutError:
            await ctx.send("⏰ Çabuk hızlan!")
            continue

        if response.content.upper() == q["answer"]:
            await ctx.send("✅ Doğru cevap!")
            score += 1
        else:
            await ctx.send(f"❌ yanlış cevap, cevap: {q['answer']}.")

    await ctx.send(f"🎉 quiz bitmiştir, skorun: {score}/{len(questions)}")

bot.run("bot token")

