import math

def vectorProjection(vector, target, normalize=True):
    if normalize:
        target = target.normal()
        
    return (vector * target) * target

def vectorRejection(vector, normal, normalize=True):
    if normalize:
        normal = normal.normal()
        
    return vector - (vector * normal) * normal

def vectorReflection(vector, normal, normalize=True):
    if normalize:
        normal = normal.normal()
        
    return vector - 2 * (vector * normal) * normal

def rayIntersectionOnLine(rayOrigin, rayDirection, lineOrigin, lineDirection, normalize=True):
    if normalize:
        rayDirection = rayDirection.normal()
        lineDirection = lineDirection.normal()
    
    normal = (lineDirection ^ rayDirection).normal()
    originVector = lineOrigin - rayOrigin
    projection = vectorProjection(originVector, rayDirection, normalize=False)
    rejection = vectorRejection(originVector, normal, normalize=False)
    
    s = rejection - projection
    d = lineDirection * s
    if d != 0:
        # Not a true intersection, since it is almost impossible.
        # Instead, this returns the closest point on the line to the ray.
        t = (s * s) / d
        result = lineOrigin - t * lineDirection
        intersection = True
    else:
        # The ray is parallel to the line, defaults to the projection of the ray origin on the line
        result = lineOrigin + vectorProjection(originVector, lineDirection, normalize=False)
        intersection = False
    
    return result, intersection

def rayIntersectionOnPlane(rayOrigin, rayDirection, planeOrigin, planeNormal, normalize=True):
    if normalize:
        rayDirection = rayDirection.normal()
        planeNormal = planeNormal.normal()
            
    originVector = planeOrigin - rayOrigin
    d = planeNormal * rayDirection
    if d != 0:
        t = (planeNormal * originVector) / d
        result = rayOrigin + t * rayDirection
        intersection = True
    else:
        # The line is parallel to the plane, defaults to the projection of the line origin on the plane
        result = planeOrigin + vectorRejection(originVector, planeNormal, normalize=False)
        intersection = False
        
    return result, intersection

def rayIntersectionOnSphere(rayOrigin, rayDirection, sphereOrigin, sphereRadius, normalize=True):
    if normalize:
        rayDirection = rayDirection.normal()
    
    l = sphereOrigin - rayOrigin
    p = l * rayDirection
    t = rayOrigin + p * rayDirection
    d = t - sphereOrigin
    c = sphereRadius * sphereRadius - d * d
    if c < 0:
        # The line doesn't intersect the sphere, returns the closest point on the sphere
        c = 0
        intersection = False
    else:
        intersection = True
    result = t - math.sqrt(c) * rayDirection
        
    return result, intersection
