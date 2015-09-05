import wx



app = wx.App()
GUI(None, "Ceiling")
app.MainLoop()


class GUI(wx.Frame):

	def __init__(self, parent, title):
		super(GUI, self).__init__(parent, title-title,
			size=(300, 250))

		self.initUI(self)
		self.Show()

		def initUI(self):
			gs = wx.GridSizer(7, 7, 7, 7, 7)
			gs.AddMany([
				(WIDGET, 0, wx.EXPAND),





				])

			self.setSizer(gs)
