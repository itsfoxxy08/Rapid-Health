import spacy
import tkinter as tk
import time

class HcB:
    def __init__(self, a,b,c):
        try:
            self.n = spacy.load("en_core_web_md")
        except Exception:
            raise
        self.st = "h1"
        self.a = a
        self.b = b
        self.c = c
        self.d = {
            "fever":{"s":"high temperature, chills, sweating","r":"Drink plenty of fluids, rest, and use paracetamol."},
            "cold":{"s":"runny nose, sneezing, sore throat","r":"Stay hydrated, inhale steam, and use cold medicine."},
            "malaria":{"s":"high fever, chills, sweating, headache, nausea","r":"Take antimalarial meds, hydrate, rest."},
            "chickenpox":{"s":"itchy rash, fever, tiredness, loss of appetite","r":"Use antihistamines, calamine lotion."},
            "pneumonia":{"s":"cough with phlegm, chest pain, fever, breathing issues","r":"Use antibiotics if needed, rest."},
            "diabetes":{"s":"urination freq, thirst, fatigue, blurred vision","r":"Monitor sugar, eat healthy, meds."},
            "tuberculosis":{"s":"cough, night sweats, weight loss, fatigue","r":"Complete TB medicine properly."},
            "hypertension":{"s":"headache, dizziness, breathless, nosebleeds","r":"Reduce salt, exercise, BP meds."},
            "asthma":{"s":"short breath, wheeze, chest tightness, cough","r":"Use inhalers, avoid triggers."},
            "gastroenteritis":{"s":"vomiting, diarrhea, stomach cramps, nausea","r":"Hydrate, avoid heavy food."}
        }
        self.u = {}
        self.k = None
        self.fin = False
        self._tmp = 0

    def o(self, m, who='b'):
        f = tk.Frame(self.b, bg="#001f3f", pady=5)
        lbl = tk.Label(f, text=m, fg="white", bg="green" if who=='u' else "grey",
                       font=("Arial",12), padx=10, pady=5, wraplength=300, relief="solid", bd=1)
        lbl.pack()
        w = self.a.winfo_width()
        bb = self.a.bbox("all")
        if bb:
            y = bb[3] + 10
        else:
            y = 10
        if who == 'u':
            x = w - 10
            anc = "ne"
        else:
            x = 10
            anc = "nw"
        self.a.create_window((x,y), window=f, anchor=anc)
        self.a.update_idletasks()
        self.a.config(scrollregion=self.a.bbox("all"))
        try:
            self.a.yview_moveto(1)
        except Exception:
            pass
        self._tmp += 1

    def q(self, txt):
        t = txt.strip().lower()
        if self.st == "h1":
            if t in ["hi","hello","hey"]:
                self.o("hey! what's up? how can i help?")
                self.o("1) docs
2) tell symptoms")
                self.st = "c2"
            else:
                self.o("say hi first")
        elif self.st == "c2":
            if t == "1":
                self.o("ok name?")
                self.st = "g1"
                self.k = "n"
            elif t == "2":
                self.o("age please")
                self.st = "g2"
                self.k = "a"
            else:
                self.o("pick 1 or 2")
        elif self.st == "g1":
            self.u[self.k] = t
            if self.k == "n":
                self.o("nice, phone?")
                self.k = "p"
            elif self.k == "p":
                self.o("age now?")
                self.k = "a"
            elif self.k == "a":
                self.o("cool, we'll get a doc to you soon")
                self.st = "end"
        elif self.st == "g2":
            self.u[self.k] = t
            if self.k == "a":
                self.o("weight?")
                self.k = "w"
            elif self.k == "w":
                self.o("height?")
                self.k = "h"
            elif self.k == "h":
                self.o("tell symptoms in a sentence")
                self.st = "m1"
        elif self.st == "m1":
            try:
                d1 = self.n(t)
            except Exception:
                d1 = None
            best = None
            sc = -1
            for kk,vv in self.d.items():
                try:
                    d2 = self.n(vv["s"])
                    s = d1.similarity(d2) if d1 else 0
                except Exception:
                    s = 0
                if s > sc:
                    sc = s
                    best = kk
            if sc > 0.45:
                self.o("hmm...looks like " + best.capitalize() + ". " + self.d[best]["r"])
            else:
                self.o("i dunno, please see a doc")
            self.fin = True
            self._ask()
        else:
            self.o("i'm a bit lost")

    def _ask(self):
        if self.fin:
            self.o("type 'exit' to close or 'doctor' to connect")
            self.st = "end"

    def z(self, txt):
        t = txt.strip().lower()
        if t == "exit":
            try:
                root.destroy()
            except:
                pass
        elif t == "doctor":
            self.o("connecting you... one sec")
            time.sleep(0.5)
            try:
                root.destroy()
            except:
                pass
        else:
            self.o("type exit or doctor")

def main():
    global root
    root = tk.Tk()
    root.title("HC Bot")
    root.geometry("600x600")
    root.configure(bg="#001f3f")
    f0 = tk.Frame(root)
    f0.pack(fill=tk.BOTH, expand=True)
    c0 = tk.Canvas(f0, bg="#001f3f")
    c0.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    s0 = tk.Scrollbar(f0, orient="vertical", command=c0.yview)
    s0.pack(side=tk.RIGHT, fill=tk.Y)
    c0.config(yscrollcommand=s0.set)
    i0 = tk.Frame(root, bg="#001f3f")
    i0.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
    t0 = tk.Entry(i0, bg="white", fg="black", font=("Arial", 12))
    t0.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    bot = HcB(c0, f0, s0)
    def snd(b):
        tx = t0.get().strip()
        t0.delete(0, tk.END)
        if not tx:
            return
        b.o(tx, who='u')
        if b.st == "end":
            b.z(tx)
        else:
            b.q(tx)
    btn = tk.Button(i0, text="Send", command=lambda: snd(bot), bg="#0074D9", fg="white", font=("Arial", 12, "bold"))
    btn.pack(side=tk.RIGHT, padx=5)
    root.mainloop()

if __name__ == "__main__":
    main()
