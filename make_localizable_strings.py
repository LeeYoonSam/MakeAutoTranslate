# google spread sheet Library
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os

def makeStringResources():
    DEFINE_KEY_COL = 4

    iOS_BASE_PATH = os.path.join(os.path.dirname(__file__), "iOS")

    KO_PATH = os.path.join(iOS_BASE_PATH, "ko.lproj")
    EN_PATH = os.path.join(iOS_BASE_PATH, "Base.lproj")
    ZH_PATH = os.path.join(iOS_BASE_PATH, "zh-Hans.lproj")

    # 폴더가 없으면 만들어준다
    if not os.path.exists(iOS_BASE_PATH):
        os.makedirs(iOS_BASE_PATH)

    if not os.path.exists(KO_PATH):
        os.makedirs(KO_PATH)

    if not os.path.exists(EN_PATH):
        os.makedirs(EN_PATH)

    if not os.path.exists(ZH_PATH):
        os.makedirs(ZH_PATH)

    DEFINE_KO_FILE = os.path.join(KO_PATH, "Localizable.strings")
    DEFINE_EN_FILE = os.path.join(EN_PATH, "Localizable.strings")
    DEFINE_ZH_FILE = os.path.join(ZH_PATH, "Localizable.strings")

    # Create iOS strings file
    ko_ios_file = open(DEFINE_KO_FILE, "w+", encoding="utf-8")
    en_ios_file = open(DEFINE_EN_FILE, "w+", encoding="utf-8")
    zh_ios_file = open(DEFINE_ZH_FILE, "w+", encoding="utf-8")


    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('AutoTranslate-e0b894d394a1.json', scope)
    # oauth 인증
    client = gspread.authorize(creds)

    # AndroidFilter 시트 가져오기
    sheet = client.open("AndroidFilter").sheet1

    cells = sheet._fetch_cells()

    names = sheet.col_values(DEFINE_KEY_COL)
    print(names)

    for cell in cells:
        try:
            cellRow = cell.row - 1

            if (cell.col == 1):
                # 한국어 추가
                ko_ios_file.write('"{}" = "{}";\n'.format(names[cellRow], cell.value))
            elif (cell.col == 2):
                # 영어 추가
                en_ios_file.write('"{}" = "{}";\n'.format(names[cellRow], cell.value))
            elif (cell.col == 3):
                # 중국어 추가
                zh_ios_file.write('"{}" = "{}";\n'.format(names[cellRow], cell.value))

        except IndexError:
            print("Index Error")

if __name__=='__main__': makeStringResources()