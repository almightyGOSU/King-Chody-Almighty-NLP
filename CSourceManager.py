import CDALSource
import CFileManager
from CCorpusManager import CCorpusManager
from CSource import CSource
from flask import url_for
import CDALType

def addNewSource(pJsonSource):

	objSource = CSource(pJsonSource["URL"], 
				pJsonSource["Content"],
				pJsonSource["Source"])

	intId = CDALSource.insertNewSource(
				objSource
			);

	if intId < 0:
		return None

##	CCorpusManager.addTokens(objSource.getTypes());
	CDALType.insertNewTypes(objSource.getTypes())

	return url_for('getSource', source_id=intId, _external=True)

def getSource(pIntId):
	objRow = CDALSource.getSource(pIntId)

	objRow[0] = CFileManager.readFromFile(str(objRow[0]))

	return objRow