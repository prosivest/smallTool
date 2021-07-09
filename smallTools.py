import renameFiles
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton, QLabel


class myQtwidget(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()  # 界面绘制交给InitUi方法


	def initUI(self):
		# w = self.QWidget()
		# resize()方法调整窗口的大小。这离是250px宽150px高
		self.resize(800, 500)
		# move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
		self.move(700, 300)
		# 设置窗口的标题
		self.setWindowTitle('Simple')
		# 显示在屏幕上

		# 选择文件夹按钮
		self.btn_confirm = QPushButton('请选择文件夹', self)
		self.btn_confirm.resize(100, 40)
		self.btn_confirm.move(400, 400)
		self.btn_confirm.clicked.connect(self.select_dic)

		# 显示
		self.label_show = QLabel(self)
		self.label_show.resize(100, 30)
		self.label_show.move(500, 400)
		self.label_show.setText("测试内容测试内容测试内容测试内容")

		# self.show()

		# 显示所选择文件夹路径
	def select_dic(self):
		directory = QFileDialog.getExistingDirectory(None, "getExistingDirectory", "./")
		self.label_show.setText(directory)


if __name__ == '__main__':
	# 创建应用程序和对象
	app = QApplication(sys.argv)
	ex = myQtwidget()
	ex.show()
	sys.exit(app.exec_())
