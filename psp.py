def main(args):
    app=QApplication(args)
    win=HelloWindow()
    win.show()
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    app.exec_loop()

if __name__=="__main__":
    main(sys.argv)
