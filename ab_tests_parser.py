import re
import copy
from mustache_templates import generateExperimentClass

def getClassData(data):

    experiments = []
    variants = []
    values = []

    variantName = ""
    variantDescription = ""
    experimentName = ""

    for row in data:
        if row[2]:
            if (len(values) > 0 and variantName):
                v = copy.copy(values)
                variants.append({'experimentVariantName': variantName, 'experimentVariantConfigValue': variantName, 'experimentVariantDescription': variantDescription, 'experimentValues': v})
                values = []
            variantName = row[2]
            variantDescription = row[3]

        valueName = row[4]
        valueType = row[5]
        value = row[6]
        values.append({'experimentValueName': valueName, 'experimentValueType': valueType, 'experimentValue': value})

        if row[1]:
            if experimentName :
                default = variants[0]['experimentValues']
                v = copy.copy(variants[1:len(variants)])
                experiments.append({'experimentName': experimentName, 'variants': v, 'defaultValues': default})
                variants = []
            experimentName = row[1]

    return experiments

def parseTableToClass(service, spreadsheetId, rangeName):
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return 'No data found.'
    else:
        return generateExperimentClass( getClassData(values)[0] )
