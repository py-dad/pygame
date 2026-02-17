import pyperclip as pc



clipboard = pc.paste()

cleaned = "-######-".join(clipboard.split())
cleaned = cleaned.strip()
cleaned = pc.copy(cleaned)
print(cleaned)



def clean_clipboard():
 text = pc.paste()
 cleaned = " ".join(text.split())
 cleaned = cleaned.strip().capitalize()

 pc.copy(cleaned)

 print(" Cleaned text copied back to clipboard:")
 print(cleaned)

if __name__ != "__main__":  # change operator to == to trigger condition that calls function
    clean_clipboard()