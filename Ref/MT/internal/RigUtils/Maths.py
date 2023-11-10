def CalculateNiceRotation(degrees):
    """Given a rotation in degrees, calculates the matching angle in between -180 and 180
    
    Args:
        degrees (float): Angle to work
    
    Returns:
        float: Simplified angle in between -180 and 180
    """
    n = int(degrees/360)
    tauDegrees = degrees - (n * 360)
    if (tauDegrees > 180 or tauDegrees < -180):
        if (tauDegrees > 0):
            cleanResult = -360 + tauDegrees
        else:
            cleanResult = 360 + tauDegrees
    else:
        cleanResult = tauDegrees
    
    return cleanResult