from ExporterActor.ActorExporterWindow import ActorExporterWindow

def show():
    global exporterActorWindow
    try:
        if exporterActorWindow.isVisible():
            exporterActorWindow.close()
    except NameError:
        pass
    exporterActorWindow = ActorExporterWindow()
    exporterActorWindow.show()