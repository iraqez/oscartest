from NovaPoshta.ApiModels.ScanSheet import ScanSheet
from NovaPoshta.MethodParameters.ScanSheet_getScanSheet import ScanSheet_getScanSheet
from NovaPoshta.MethodParameters.ScanSheet_printScanSheet import ScanSheet_printScanSheet
from NovaPoshta.MethodParameters.ScanSheet_removeDocuments import ScanSheet_removeDocuments

__author__ = 'chen'


def save():
    scanSheets = ['70ec0f61-bf6b-11e4-a77a-005056887b8d', '70ec0f33-bf6b-11e4-a77a-005056887b8d']

    scanSheet = ScanSheet()
    scanSheet.setDate('16.09.2015')
    scanSheet.setDocumentRefs(scanSheets)
    # или
    scanSheet.addDocumentRef('70ec0f2a-bf6b-11e4-a77a-005056887b8d')
    scanSheet.addDocumentRef('70ec0f42-bf6b-11e4-a77a-005056887b8d')

    return scanSheet.save()

def update():
    scanSheet = ScanSheet()
    scanSheet.setRef('1c65213d-c00b-11e4-ac12-005056801333')
    scanSheet.setDate('16.09.2015')
    scanSheet.addDocumentRef('70ec0dfd-bf6b-11e4-a77a-005056887b8d')
    scanSheet.addDocumentRef('9d014a5e-bf43-11e4-a77a-005056887b8d')

    return scanSheet.update()

def delete():
    scanSheet = ScanSheet()
    scanSheet.setRef('9d868cfe-012e-11e5-ad08-005056801333')

    return scanSheet.delete()

def removeDocuments():
    arrayDocuments = ['70ec0f61-bf6b-11e4-a77a-005056887b8d', '70ec0f33-bf6b-11e4-a77a-005056887b8d']

    data = ScanSheet_removeDocuments()

    data.setDocumentRefs(arrayDocuments)

    # или

    data.addDocumentRef('70ec0f42-bf6b-11e4-a77a-005056887b8d')
    data.addDocumentRef('70ec0f61-bf6b-11e4-a77a-005056887b8d')

    return ScanSheet.removeDocuments(data)

def getScanSheet():
    data = ScanSheet_getScanSheet()
    data.setRef('b107a458-c6fe-11e4-ac12-005056801333')

    return ScanSheet.getScanSheet(data)

def getScanSheetList():
    return ScanSheet.getScanSheetList()

def printScanSheet():
    # todo not working
    data = ScanSheet_printScanSheet()

    data.addDocumentRef('39d5aadd-c5ed-11e4-ac12-005056801333')
    # или
    # data.setDocumentRefs(array('39d5aadd-c5ed-11e4-ac12-005056801333'))
    # или
    # data.addNumber('105-0002898')

    data.setType(ScanSheet.PRINT_TYPE_PDF)

    return ScanSheet.printScanSheet(data)
