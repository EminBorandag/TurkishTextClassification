import string
from trnlp import TrnlpWord
obj = TrnlpWord()


yapim_ekleri = {"lük", "lık", "li", "lı", "suz", "sız", "siz", "cü", "çı", "cu", "çi", "çe", "ce", "ça", "çıl", "çil", "daş", "üncü", "inci", "msı", "msi", "cil", "cıl", "şın", "sal", "ıt", "cağız", "cık", "cük", "tı", "la", "le", "al", "l", "a", "e", "ar", "da", "de", "et", "ik", "ımsa", "se", "mse", "kır", "len", "la", "laş", "leş", "sa", "se", "ce", "ecek", "acak", "ak", "ge", "kan", "gan", "gi", "gı", "kı", "giç", "gıç", "gun", "gin", "ı", "ü", "u", "ıcı", "ücü", "ıcı", "ik", "ık", "ük", "ım", "im", "üm", "ın", "ün", "ünç", "inç", "ıntı", "inti", "ıntı", "üntü", "ır", "ir", "er", "ur", "uş", "üş", "it", "ıt", "üt", "im", "mek", "ti", "tı"}
 
cekim_ekleri = {"lar", "ler", "ı", "i", "den", "de", "da", "a", "dan", "ta", "te", "tın", "tin", "ım", "ımız", "ınız", "ları", "ın", "in", "un", "ün", "ca", "ce", "im","im","um","üm","mız","miz","muz","müz","nız","niz","nuz","nüz","ları","leri" "sin","sın","sun","sün" "dir", "iz", "siniz", "dır", "ler", "l", "man", "men", "kak", "kek", "gın", "gin", "dük", "duk", "mış", "miş","muş","müş", "gen", "gan", "an", "en", "r","er","ar" "mak", "mek", "ma", "me", "ş", "iş", "e","ü","u","n","layın","leyin","p","lap","yor","ki","la","le","se","sa","meli","malı","dı","di","du","dü","erek","arak","ınca","ince","dıkça","dikçe","madan","meden","alı","eli","ken","meksizin","asiye","esiye","dığında","duğunda","leri",}
 
cekim_ekleri_sorted = sorted(cekim_ekleri, key=len, reverse=True)
yapim_ekleri_sorted = sorted(yapim_ekleri, key=len, reverse=True)


for i in range(1, 601):
   
    dosya_yolu = f"ekonomi/c ({i}).txt"
    cumle = ""
    yeni_cumle=""
 
    try:
        with open(dosya_yolu, "r", encoding='utf-8') as dosya:
            cumle = dosya.read()
         
 
    except FileNotFoundError:
        print(f"{dosya_yolu} dosyası bulunamadı.")
 
    except Exception as ex:
        print(f"{dosya_yolu} dosyası okunurken bir hata oluştu: {ex}")
 
    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stop_words = set([line.strip() for line in f])
   
 
    # Kelimeleri ayırdık
    words = cumle.translate(str.maketrans('', '', string.punctuation)).split()
 
    # Stop wordsta olmayan kelimeleri seçiyoruz
    filtered_words = [word for word in words if word not in stop_words]
 
    # seçtiğimiz kelimeleri birleştirdik
    cumle = ' '.join(filtered_words)
 
    cumle = cumle.split()
 
    for kelime in cumle:
 
        yeni_kelime = kelime
        son_ek = []
 
        while any(yeni_kelime.endswith(ek) for ek in cekim_ekleri_sorted if len(yeni_kelime) > 3):
 
            for ek in cekim_ekleri_sorted:
                if yeni_kelime.endswith(ek):
                    yeni_kelime = yeni_kelime[:-len(ek)]
                    son_ek.append(ek)
                    break
            continue
 
        while any(yeni_kelime.endswith(ek) for ek in yapim_ekleri_sorted if len(yeni_kelime) > 3):
 
            for ek in yapim_ekleri_sorted:
                if yeni_kelime.endswith(ek):
                    yeni_kelime = yeni_kelime[:-len(ek)]
                    son_ek.append(ek)
                    break
            continue
 
        while True:
            obj.setword(yeni_kelime)
            uzunluk = len(str(obj))
            if uzunluk == 0 or len(yeni_kelime) < 3:
                if len(son_ek) > 0:
                    ek = son_ek.pop()
                    yeni_kelime += ek
                else:
                    break    
            else:
                yeni_cumle= yeni_cumle.__add__(yeni_kelime + " ")
                with open(dosya_yolu, "w", encoding='utf-8') as dosya:
                    dosya.write(yeni_cumle)
            break