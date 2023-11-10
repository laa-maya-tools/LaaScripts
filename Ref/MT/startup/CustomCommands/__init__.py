import CustomCommands.ToolContextCommands as ToolContextCommands
import CustomCommands.MayaImprovementsCommands as MayaImprovementsCommands
import CustomCommands.ExporterCommands as ExporterCommands
import CustomCommands.CinematicEditorCommands as CinematicEditorCommands
import CustomCommands.CustomToolsCommands as CustomToolsCommands
import CustomCommands.CommonCommands as CommonCommands
import CustomCommands.TravelCustomHierarchy as TravelCustomHierarchy
import CustomCommands.RigCommands as RigCommands
import CustomCommands.OrganiLayersCommands as OrganiLayersCommands
import CustomCommands.AnimToolsCommands as AnimToolsCommands

def init():
    MayaImprovementsCommands.register()
    ToolContextCommands.register()
    ExporterCommands.register()
    CinematicEditorCommands.register()
    CommonCommands.register()
    CustomToolsCommands.register()
    TravelCustomHierarchy.register()
    RigCommands.register()
    OrganiLayersCommands.register()
    AnimToolsCommands.register()
