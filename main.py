from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import random, re

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(x, y):
    g = gcd(x, y)
    return x // g, y // g

def generate():
    # 随机抽一种比例题型
    t = random.choice(['mul','per','frac','more'])
    if t=='mul':
        b=random.randint(2,9); k=random.randint(2,5)
        a=k*b; a2,b2=simplify_ratio(a,b)
        return f"A 是 B 的 {k} 倍，求 A : B", f"{a2}:{b2}"
    if t=='per':
        p=random.choice([20,25,40,50,60,75,80])
        a,b=p+100,100; a2,b2=simplify_ratio(a,b)
        return f"A 比 B 多 {p}%，求 A : B", f"{a2}:{b2}"
    if t=='frac':
        n,d=random.choice([1,2,3]),random.choice([2,3,4])
        a,b=n,d; a2,b2=simplify_ratio(a,b)
        return f"A 占 B 的 {n}/{d}，求 A : B", f"{a2}:{b2}"
    if t=='more':
        n,d=random.choice([1,2]),random.choice([3,4])
        a,b=d+n,d; a2,b2=simplify_ratio(a,b)
        return f"A 比 B 多 {n}/{d}，求 A : B", f"{a2}:{b2}"

class RatioApp(App):
    def build(self):
        self.question, self.answer = generate()
        root = BoxLayout(orientation='vertical', padding='20dp', spacing='15dp')
        self.lab = Label(text=self.question, font_size='24sp')
        root.add_widget(self.lab)
        self.inp = TextInput(hint_text='输入比例 如 3:4', font_size='24sp', multiline=False)
        root.add_widget(self.inp)
        btn = Button(text='提交', font_size='24sp')
        btn.bind(on_release=self.check)
        root.add_widget(btn)
        self.res = Label(font_size='22sp', color=(1,1,0,1))
        root.add_widget(self.res)
        return root

    def check(self, *_):
        u = self.inp.text.strip()
        if re.fullmatch(r'\d+:\d+', u):
            a,b = map(int, u.split(':'))
            g = gcd(a,b)
            user = f"{a//g}:{b//g}"
            if user == self.answer:
                self.res.text = '✅ 正确！'
            else:
                self.res.text = f'❌ 错误！答案：{self.answer}'
        else:
            self.res.text = '格式错误，请输入如 3:4'
        # 下一题
        self.question, self.answer = generate()
        self.lab.text = self.question
        self.inp.text = ''

if __name__ == '__main__':
    RatioApp().run()