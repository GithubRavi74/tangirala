

import os
from groq import Groq

# ✅ Check if API key is loaded
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found! Make sure you added it in Streamlit secrets or environment variables.")

print("✅ Groq API Key found (starts with):", api_key[:5] + "*****")

client = Groq(api_key=api_key)

def generate_response(user_question):
    """
    Takes only the user question and generates
    counsellor advice using a predefined conflict text.
    """

    family_conflict_text = """
    Ravi,50 years man is single who is indian but works in malaysia from many years. Shankar is his elder brother who left india to USA after getting married in india
    and working there from many years. But currently he is going through divorce  and is very disturbed. Ravi and shankars parents live in india with Phani who is younger
    to shankar and elder brother to Ravi. in 2021 ravi resigned job in malaysia and migrated back to india. He has not yet decided where to rent house in india But initially 
    he landed in parents house which is an apartment just in next block to phani's aparment. Its in chennai. But after he started staying there, soon he got covid. Phani and parents 
    discussed and asked ravi to stay quarantined in parents house and so parents shifted temporarily to phani's house. While in quarantine ravi shared this news to shankar 
    in usa by email. Shankar got very angry on ravi and he angrily told ravi that how can he make parents leave their own house and asked ravi how can he encroach parents house. he said ravi you
    should be shifting to hotel and get quarantined there. Ravi told shankar that he is already patient and he just followed family decision. shankar told, ravi you had put 
    my parents at risk and inconvience. From then shankar made strong bad impression on ravi. Morover though ravi has plans for his next job and working on it , but shankar
    saw him as jobless and was cautious that ravi might stay with family for indefinite period and become burden. Later ravi recovered and he shifted to hyderabad. phani got job in banglore and he 
    and parents shifted to banglore and were living together. Then on jun 6 th next year its was birthday of phani and dad also. So phani invited ravi too. Shankar happened to 
    be in india at that time and he was already in phanis house. At that time Ravi was planning to shift to banglore and so he arrived on june 6th to phanis house with extra 
    luggage. Shankar saw that luggage and had realized that ravi's visit wont be short but little longer and started aurgument immedeatly within 10 mins of ravis arrival saying too many guests will burden phani's wife 
    chandrika and he suggested ravi to stay in hotel and said he also can join ravi if needed. Ravi felt shankar is trying to pull him away from family with fear of overstay and burden to them. Ravi
    actually just planned to stay for a week so that he can find a room in banglore. But shankar was strictly against. There was aurgument and phani ended it saying since he invited
    ravi so he is ok with ravi staying. Shankar couldnt say anything. From then shankar behaved different with ravi. Latter ravi took hostel in banglore and stayed 2 months but didnt like banglore and shifted back to hyderabad.
    Shankar one day came from usa as he had some work in hyderabad and visited hyderabad with parents and stayed in hotel but didnt communicate or let ravi meet them. They left hyderabad too without saying bye to 
    ravi. Ravi was very hurt. Then shankar after sometime migrated back from usa to banglore and took house besides phanis house and kept parents with him. His divorced wife
    and his kids stayed in usa. When ravi wanted to visit banglore then shankar kept rule that in his house ravi can visit parents in day time but cannot stay even 1 night.
    Ravi was very hurt for seeing him as a problem and he sent few long emotional mails to shankar with CC to whole family about this offensive treatments right from time he 
    got covid . But shankar didnt answer even 1 mail nor he acknowledged. Ravi got more hurt and wrote a very very nasty mail in red font scolding shankar while all in CC. That
    made shankar more angry and he totally banned ravi and strongly told family not to talk about ravi with him. Latter after the emotion cooled down ravi sent few sorry emails 
    to shankar with all in CC. But shankar reamained stubborn and not coperative for communication with anyone regarding this conflict. Now ravi whenever felt like meeting
    family in banglore is unable to come since shankar is in same aparment building. And slowly ravi getting frustrated as he is unable to come. Phani and his wife said they 
    tried to solve but shankar told them not to talk that topic. and so they adviced me to solve the conflict myself. Parents too tried and told the same. Ravi was not happy as
    he expected family not to listen to shankar and keep quite but to protect ravi and force shankar to talk and get from him the justification in his treatment towards ravi. 
    But instead ,  since they are all in banglore so they occassionally are socializing. Thats making ravi even more disturbed and always fighting with parents and phani 
    saying to them that how  can they socialize with shankar who is not co operativing with them and continuing ban on me and causing so much pain to me. 
    But parents and phani and his wife saying you both are important to us and we cannot do anything. With this ravi is not going banglore at all and left out from 
    family and felt neglected and disturbed.
    """

    prompt = f"""
You are a compassionate and experienced family counsellor.
A family is facing the following conflict:
{family_conflict_text}

The user asked: "{user_question}"

Give practical, empathetic, and step-by-step advice to help this family.
"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a professional family counsellor."},
                {"role": "user", "content": prompt},
            ],
        )

       # return response.choices[0].message["content"] #in the latest Groq SDK, the returned message is an object, not a dictionary so this code commented
        response.choices[0].message.content
    except Exception as e:
        return f"❌ LLM Error: {str(e)}"





