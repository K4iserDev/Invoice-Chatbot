from openai import OpenAI

from config import API_KEY, EXCEL_PATH
from excel_reader import read_factures

client = OpenAI(api_key=API_KEY)
context = read_factures(EXCEL_PATH)

system_prompt = f"Your role: You are an assistant who answers questions about invoices.When citing a specific value (invoice number, date, issuer, total), copy it exactly as it appears next to its label in the source data — do not reorder, reformat, or swap values between fields. If you do not know a specific detail or cannot find the information, you must not invent anything; if you cannot find the information, inform the user that you were unable to locate what they requested.You must derive all information from this source.{context}"
messages = [
    {"role": "system", "content": system_prompt},
]
while True:
    question = input("Ask a question about the invoices->\n")
    question = question.lower()
    if question == "exit" or question == "salir":
        break
    else:
        messages.append({"role": "user", "content": question})
        completion = client.chat.completions.create(
            model="gpt-5-mini", messages=messages
        )
        response = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        print(response)
