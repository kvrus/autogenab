from __future__ import print_function

from ab_tests_parser import parseTableToClass
from google_sheet_api import getService

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
GOOGLE_SHEET_ID = '1ER-GoEaiNPyHRVCBDDuSLSO_QC8McfSlirtfgjED0Cg'

def main():
    service = getService(CLIENT_SECRET_FILE, SCOPES)

    spreadsheetId = GOOGLE_SHEET_ID
    rangeName = 'abtest!A2:M'

    print(parseTableToClass(service, spreadsheetId, rangeName))

if __name__ == '__main__':
    main()
