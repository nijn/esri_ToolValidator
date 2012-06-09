class ToolValidator:
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    import arcpy
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parmater
    has been changed."""
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""

    # Tests if the output file already exists. If file exists and the
    # warning is ignored, the existing file will be overwritten.
    # @param 1 = output directory
    # @param 2 = filename / feature class name
    if self.params[2].altered:
      import os.path
      f = os.path.join(str(self.params[1].value), self.params[2].value)

      if arcpy.Exists(f):
        self.params[2].setWarningMessage('File already exists in the workspace. Ignore this message to overwrite.')
      #endif

    else:
      self.params[2].clearMessage()

    return
