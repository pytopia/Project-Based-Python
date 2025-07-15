from pathlib import Path

WELCOME_MESSAGE = "👋 سلام به ربات سوالات متداول پایتوپیا خوش آمدید 🤖🎉"
WAITING_MESSAGE = "💡 ربات در حال جستجوی پاسخ شماست..."
MAX_RESPONSE_LENGTH = 500
LLM_MODEL = "gpt-4o"


context = Path("src/context.txt").read_text()

SYSTEM_PROMPT = f"""You are a helpful assistant.
- Only use valid markdown in your response and do not use any other formatting.
- Always respond briefly. This is for a telegram group chat.
- Use emojis and markdown formatting such as bold, italic, underline, code blocks, links, etc to make your response more engaging and informative.

Use this context to answer the questions
(if the question is not related to this context,
ignore the context and answer the question as best as you can and as short as possible):
Context: {context}
"""

REPLY_SYSTEM_PROMPT = SYSTEM_PROMPT + """
Answer the following question according to the guideline.
Guideline: {reply_guideline}
"""

# emojis
LIKE_EMOJI = ":thumbs_up:"
DISLIKE_EMOJI = ":thumbs_down:"
BOT_EMOJI = ":moai:"
CRY_EMOJI = ":crying_face:"
QUESTION_EMOJI = ":question:"
HEART_EMOJI = ":red_heart:"
PILE_OF_POO_EMOJI = ":pile_of_poo:"
THINKING_EMOJI = ":thinking_face:"
HIGH_VOLTAGE_EMOJI = ":high_voltage:"

# auto reply messages
DONT_ASK_TO_ASK_MESSAGE = """
از مشارکت شما در این گروه قدردانی می‌کنیم. برای اینکه بحث‌های ما کارآمدتر و مفیدتر باشد، *لطفا سؤالات خود را مستقیماً بپرسید*.

مثلا به جای گفتن:
❌ آیا کسی می‌تونه واسه یه کد پایتون به من کمک کنه؟
بهتر است سؤال خاص خود را فوراً بپرسید:
✅️️️️️️️ چطور می‌تونم تو پایتون حلقه‌ی بی‌نهایت بزنم؟

برای اطلاعات بیشتر در مورد این مفهوم، می‌توانید به این لینک مراجعه کنید:
https://dontasktoask.com
"""
