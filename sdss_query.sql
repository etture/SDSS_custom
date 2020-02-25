SELECT
  S.ra, S.dec, S.mjd, S.fiberID, S.objType,
  P.type, 
  
  P.petroMag_u, P.petroMag_g, P.petroMag_r, P.petroMag_i, P.petroMag_z, 
  P.psfMag_u, P.psfMag_g, psfMag_r, P.psfMag_i, P.psfMag_z, 
  P.modelMag_u, P.modelMag_g, P.modelMag_r, P.modelMag_i, P.modelMag_z,
  P.fiberMag_u, P.fiberMag_g, P.fiberMag_r, P.fiberMag_i, P.fiberMag_z
  
INTO mydb.SDSSPhotoObjDR16Attempt1 FROM SpecObjAll S
  CROSS APPLY dbo.fGetNearestObjEq(S.ra, S.dec, 0.5) N, PhotoObj P
  WHERE N.objID = P.objID
  AND (P.modelMag_u > 10 AND P.modelMag_u < 25)
  AND (P.modelMag_g > 10 AND P.modelMag_g < 25)
  AND (P.modelMag_r > 10 AND P.modelMag_r < 25)
  AND (P.modelMag_i > 10 AND P.modelMag_i < 25)
  AND (P.modelMag_z > 10 AND P.modelMag_z < 25)
