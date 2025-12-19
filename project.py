import wx

words = [
    ("cat", "A small animal"),
    ("ball", "A round toy"),
    ("apple", "A fruit"),
    ("sun", "Gives light"),
    ("fish", "Lives in water"),
    ("bat", "A flying mammal")
]

class SpellingGame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Spelling Game", size=(400, 300))

        self.index = 0
        self.score = 0

        panel = wx.Panel(self)
        panel.SetBackgroundColour("#A0C4FF")

        self.score_text = wx.StaticText(panel, label="Score: 0")
        self.hint_text = wx.StaticText(panel, label="")
        self.word_text = wx.StaticText(panel, label="")
        self.input_box = wx.TextCtrl(panel)
        submit_btn = wx.Button(panel, label="Submit")

        submit_btn.Bind(wx.EVT_BUTTON, self.check_answer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.score_text, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.hint_text, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.word_text, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.input_box, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(submit_btn, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        self.load_word()
        self.Show()

    def hide_word(self, word):
        return word[0] + "_" * (len(word) - 2) + word[-1]

    def load_word(self):
        word, hint = words[self.index]
        self.hint_text.SetLabel("Hint: " + hint)
        self.word_text.SetLabel(self.hide_word(word))
        self.input_box.SetValue("")

    def check_answer(self, event):
        word, _ = words[self.index]
        answer = self.input_box.GetValue().lower()

        if answer == word:
            self.score += 1
            wx.MessageBox("Correct!", "Result")
        else:
            wx.MessageBox("Wrong! Correct word is: " + word, "Result")

        self.index += 1
        self.score_text.SetLabel(f"Score: {self.score}")

        if self.index < len(words):
            self.load_word()
        else:
            wx.MessageBox(
                f"Game Over!\nFinal Score: {self.score}/{len(words)}",
                "Finished"
            )
            self.Close()

app = wx.App()
SpellingGame()
app.MainLoop()
