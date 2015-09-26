import CDBManager

def insertNewSource(pObjSource):

	if pObjSource.getSource() == "Social" and pObjSource.getTokenCount() < 20:
		return -99

	if pObjSource.getSource() == "Web" and pObjSource.getSentenceCount() < 5 and pObjSource.getTokenCount() < 80:
		return -99

	objConnection = CDBManager.getDBConnection()

	try:
		with objConnection.cursor() as objCursor:
			strSQL = "INSERT INTO `tblCorpus`(`strUrl`, `intTokenCount`, `intSentenceCount`, `intTypeCount`) VALUES (%s, %s, %s, %s)"
			objCursor.execute(strSQL, (pObjSource.getURL(),
								pObjSource.getTokenCount(), pObjSource.getSentenceCount(), 
								pObjSource.getTypeCount()))
			objConnection.commit()

			strSQL = "SELECT LAST_INSERT_ID()"

			objCursor.execute(strSQL)

			intId = objCursor.fetchone()[0]
	except:
		intId = -99
	finally:
		objConnection.close()

	return intId