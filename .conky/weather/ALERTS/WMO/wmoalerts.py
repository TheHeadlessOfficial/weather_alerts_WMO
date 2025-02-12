import os, sys
import requests
import textwrap
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_alertswmo.lock"
# create lock file
try:
    open(lock_file, 'w').close()
    ################################ my API url forecast (insert it between apostrophe, DON'T delete apostrophes)
    urlwmo = 'https://severeweather.wmo.int/v2/json/wmo_all.json?_=1619520362240'
    reswmo = requests.get(urlwmo).json()
    datawmo = reswmo
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set variables for Italy (you need to set your regions based on your country)
    country = 'Italy'
    region = 'Veneto'
    ################################ country regions for Italy (you need to set your regions based on your country)
    regionspatterns = ['Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia e Romagna', 'Friuli Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia', 'Marche', 'Molise', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana', 'Trentino Alto Adige', 'Umbria', "Val d'Aosta", 'Veneto']
    ################################ create variables and array for WMO ALERTS data
    block = 18 # block of rows in the -wmoalertsworld.txt file foir each event
    temp = []
    text2 = '-'
    wmoitemCount = 0
    wmocount = 5
    wmolastUpdated = ''
    wmoid = []
    wmoevent = []
    wmoheadline = []
    wmosent = []
    wmoexpires = []
    wmoareaDesc = []
    wmomid = []
    wmora = []
    wmos = []
    wmou = []
    wmoc = []
    wmourl = []
    wmoeff = []
    # set the numbers of alerts you want for WORLD, COUNTRY, REGION
    numalertsw = 3
    numalertsc = 2
    numalertsr = 2
    ################################ set path
    home = '/home/'
    conky = '/.conky/'
    ################################ set the paths for the ALERTS section (from world)
    palertswmo = home + homename + conky + 'weather/ALERTS/WMO/-wmoalertsworld.txt'
    ################################ set the paths for the ALERTS for conky statements (from world)
    palertswmoc = home + homename + conky + 'weather/ALERTS/WMO/wmoalertsworldconky.txt'
    ################################ set the paths for the ALERTS for conky statements (general data)
    palertswmogen = home + homename + conky + 'weather/ALERTS/WMO/wmoalertsgenconky.txt'
    ################################ set the paths for the ALERTS section (from your country)
    palertswmocountry = home + homename + conky + 'weather/ALERTS/WMO/-wmoalertscountry.txt'
    ################################ set the paths for the ALERTS for conky statements (from your country)
    palertswmocountryc = home + homename + conky + 'weather/ALERTS/WMO/wmoalertscountryconky.txt'
    ################################ set the paths for the ALERTS section (from your region)
    palertswmoregion = home + homename + conky + 'weather/ALERTS/WMO/-wmoalertsregion.txt'
    ################################ set the paths for the ALERTS for conky statements (from your region)
    palertswmoregionc = home + homename + conky + 'weather/ALERTS/WMO/wmoalertsregionconky.txt'
    ################################ get data for WMO ALERTS section
    wmoitemCount = datawmo['itemCount']
    wmolastUpdated = datawmo['lastUpdated']
    for i in range(0, wmoitemCount):
        wmoid.append(datawmo['items'][i]['id'])
        try:
            wmoevent.append(datawmo['items'][i]['event'])
        except:
            wmoevent = text2
        try:
            wmoheadline.append(datawmo['items'][i]['headline'])
        except:
            wmoheadline = text2
        try:
            wmosent.append(datawmo['items'][i]['sent'])
        except:
            wmosent = text2
        try:
            wmoexpires.append(datawmo['items'][i]['expires'])
        except:
            wmoexpires = text2
        try:
            wmoareaDesc.append(datawmo['items'][i]['areaDesc'])
        except:
            wmoareaDesc.append(text2)
        try:
            wmomid.append(datawmo['items'][i]['mid'])
        except:
            wmomid = text2
        try:
            wmora.append(datawmo['items'][i]['ra'])
        except:
            wmora = text2
        try:
            wmos.append(datawmo['items'][i]['s'])
        except:
            wmos = text2
        try:
            wmou.append(datawmo['items'][i]['u'])
        except:
            wmou = text2
        try:
            wmoc.append(datawmo['items'][i]['c'])
        except:
            wmoc = text2
    #                   URL is an option (the field name can change into capURL)
        try:
            wmourl.append(datawmo['items'][i]['url'])
        except:
            wmourl.append(text2)
        try:
            wmourl.append(datawmo['items'][i]['capURL'])
        except:
            wmourl.append(text2)
        try:
            wmoeff.append(datawmo['items'][i]['effective'])
        except:
            wmoeff = text2
    ################################ write raw data for WMO ALERTS (all)
    def writedata(counter):
        i = counter
        z = 0
        j = 0
        y = 0
        nchars = 55
        myrowsev = 2
        myrowshl = 2
        myrowsad = 4
        fo.write('id: {}\n'.format(wmoid[i]))
        #                 format wmoevent and it writes 2 rows for it (you can change the number of rows you want)
        wmoevent[i] = wmoevent[i].replace("\n", " ")
        strlenght = len(wmoevent[i])
        if strlenght == 0:
            wmoevent[i] = text2
        wrapper = textwrap.TextWrapper(width=nchars, max_lines=(myrowsev))
        word_list = wrapper.wrap(text=wmoevent[i])
        for element in word_list:
            fo.write('{}\n'.format(element))
            z = z + 1
            if (strlenght <= nchars) and (z == 1):
                fo.write('{}\n'.format(text2))
            z = 0
        #                 format wmoheadline and it writes 2 rows for it (you can change the number of rows you want)
        strlenght = len(wmoheadline[i])
        if strlenght == 0:
            wmoheadline[i] = text2
        wrapper = textwrap.TextWrapper(width=nchars, max_lines=(myrowshl))
        word_list = wrapper.wrap(text=wmoheadline[i])
        for element in word_list:
            fo.write('{}\n'.format(element))
            j = j + 1
            if (strlenght <= nchars) and (j == 1):
                fo.write('{}\n'.format(text2))
            j = 0
        #              for l in textwrap.wrap(line, width=55)))
        fo.write('{}\n'.format(wmosent[i]))
        fo.write('{}\n'.format(wmoexpires[i]))
        #                 format wmoareaDesc and it writes 4 rows for it (you can change the number of rows you want)
        wmoareaDesc[i] = wmoareaDesc[i].replace("\n", " ")
        strlenght = len(wmoareaDesc[i])
        if strlenght == 0:
            wmoareaDesc[i] = text2
        wrapper = textwrap.TextWrapper(width=nchars, max_lines=(myrowsad))
        word_list = wrapper.wrap(text=wmoareaDesc[i])
        for element in word_list:
            fo.write('{}\n'.format(element))
            y = y + 1
            if (strlenght <= nchars) and (y == 1):
                fo.write('{}\n'.format(text2))
                y = y + 1
            if (strlenght <= nchars*2) and (y == 2):
                fo.write('{}\n'.format(text2))
                y = y + 1
            if (strlenght <= nchars*3) and (y == 3):
                fo.write('{}\n'.format(text2))
                y = y + 1
            if y == 4:
                y = 0
        #              for l in textwrap.wrap(line, width=55)))
        fo.write('mid: {}\n'.format(wmomid[i]))
        fo.write('ra: {}\n'.format(wmora[i]))
        if wmos[i] == 0:
            wmos[i] = 'unknown'
        elif wmos[i] == 1:
            wmos[i] = 'minor'
        elif wmos[i] == 2:
            wmos[i] = 'moderate'
        elif wmos[i] == 3:
            wmos[i] = 'severe'
        elif wmos[i] == 4:
            wmos[i] = 'extreme'
        fo.write('{}\n'.format(wmos[i]))
        if wmou[i] == 0:
            wmou[i] = 'unknown'
        elif wmou[i] == 1:
            wmou[i] = 'past'
        elif wmou[i] == 2:
            wmou[i] = 'future'
        elif wmou[i] == 3:
            wmou[i] = 'expected'
        elif wmou[i] == 4:
            wmou[i] = 'immediate'
        fo.write('{}\n'.format(wmou[i]))
        if wmoc[i] == 0:
            wmoc[i] = 'unknown'
        elif wmoc[i] == 1:
            wmoc[i] = 'unlikely'
        elif wmoc[i] == 2:
            wmoc[i] = 'possible'
        elif wmoc[i] == 3:
            wmoc[i] = 'likely'
        elif wmoc[i] == 4:
            wmoc[i] = 'observed'
        fo.write('{}\n'.format(wmoc[i]))
        #                   URL is an option (the field name can change into capURL)
        fo.write('url: {}\n'.format(wmourl[i]))
        fo.write('effective: {}\n'.format(wmoeff[i]))
    ################################ write raw data for WMO ALERTS section (first n alerts from world)
    fo = open(palertswmo, 'w')
    for i in range(0, wmocount):
        writedata(i)
    fo.close()
    ################################ write raw data for WMO ALERTS section (first n alerts from your country)
    fo = open(palertswmocountry, 'w')
    for i in range(0, wmoitemCount):
        if country in wmoheadline[i]: 
            writedata(i)
    fo.close()
    ################################ write raw data for WMO ALERTS section (first n alerts from your region)
    fo = open(palertswmoregion, 'w')
    for i in range(0, wmoitemCount):
        if region in wmoheadline[i]: 
            writedata(i)
    fo.close()
    ################################ write conky statements for general info
    def conkygen(filewrite):
        row1 = "${color2}${font URW Gothic L:size=8}${alignc}__________WORLD METEOROLOGICAL ORGANIZATION ALERTS__________"
        row2 = "${font URW Gothic L:size=6}${color}${alignc}S=severity;  U=urgency;  C=certainty${font}"
        row3 = "${voffset -10}${alignc}--------------------------------------------------"    
        fw = open(filewrite, 'w')
        fw.write('{}\n'.format(row1))
        fw.write('{}\n'.format(row2))
        fw.write('{}\n'.format(row3))
        fw.close()
    conkygen(palertswmogen)
    ################################ write conky statements for WORLD, COUNTRY, REGIONE alerts (based on the 3 variables you set above, see row 47)
    def writeconkystatement(fileread, filewrite, numalertsf):
        j = 1
        row = 1
        row4 = "${color3}${font URW Gothic L:size=7}${alignc}----- WORLD ALERTS -----"
        row5 = "${color3}${font URW Gothic L:size=7}${alignc}----- COUNTRY ALERTS -----"
        row6 = "${color3}${font URW Gothic L:size=7}${alignc}----- REGION ALERTS -----"
        with open(fileread, 'r') as fr, open(filewrite, 'w') as  fw:
            if fileread == palertswmo:
                fw.write('{}\n'.format(row4))
            elif fileread == palertswmocountry:
                fw.write('{}\n'.format(row5))
            elif fileread == palertswmoregion:
                fw.write('{}\n'.format(row6))
            for i, line in enumerate(fr): # i starts from zero so row 2 in file is row 1 in script
            #event
                if i == row:
                    strlenght = len(line.rstrip('\n'))
                    if strlenght > 1:
                        fw.write("${color2}Event: ${color}" + line)
                # use next "if" if you want 2 rows for event (uncomment the if block)
                # if i == row + 1:
                #     strlenght = len(line.rstrip('\n'))
                #     #print(strlenght)
                #     if strlenght > 1:
                #         print(line)
                #         fw.write(line)
            #headline
                if i == row + 2:
                    strlenght = len(line.rstrip('\n'))
                    if strlenght > 1:
                        fw.write("${color2}Headline: ${color}" + line)
                # use next "if" if you want 2 rows for headline (uncomment the if block)
                # if i == row + 3:
                #     strlenght = len(line.rstrip('\n'))
                #     #print(strlenght)
                #     if strlenght > 1:
                #         print(line)
                #         fw.write(line)
            #date
                if i == row + 4:
                    strlenght = len(line.rstrip('\n'))
                    line = line.rstrip('\n')
                    if strlenght > 1:
                        fw.write("${color2}start: ${color}" + str(line))
                if i == row + 5:
                    strlenght = len(line.rstrip('\n'))
                    if strlenght > 1:
                        fw.write("${color2}${goto 200}end: ${color}" + str(line))
            #areadesc
                if i == row + 6:
                    fw.write("${color1}Area: ${color}${font URW Gothic L:size=6}" + line)
                if i == row + 7:
                    strlenght = len(line.rstrip('\n'))
                    if strlenght > 1:
                        fw.write(line)
                # use next two "if" if you want 4 rows for areadesc (uncomment the two if block)
                # if i == row + 8:
                #     strlenght = len(line.rstrip('\n'))
                #     #print(strlenght)
                #     if strlenght > 1:
                #         print(line)
                #         fw.write(line)
                # if i == row + 9:
                #     strlenght = len(line.rstrip('\n'))
                #     #print(strlenght)
                #     if strlenght > 1:
                #         print(line)
                #         fw.write(line)
            #suc
                if i == row + 12:
                    strlenght = len(line.rstrip('\n'))
                    line = line.rstrip('\n')
                    if strlenght > 1:
                        fw.write("${goto 80}${font URW Gothic L:size=6}${color2}S=${color}" + line)
                if i == row + 13:
                    strlenght = len(line.rstrip('\n'))
                    line = line.rstrip('\n')
                    if strlenght > 1:
                        fw.write("${goto 180}${color2}U=${color}" + line + "${goto 300}")
                if i == row + 14:
                    strlenght = len(line.rstrip('\n'))
                    if strlenght > 1:
                        fw.write("${color2}C=${color}" + line + "${font URW Gothic L:size=7}")
            #block control
                if i == (block * j) and j < numalertsf:
                    row = (block * j) + 1
                    j = j + 1
    writeconkystatement(palertswmo, palertswmoc, numalertsw)
    writeconkystatement(palertswmocountry, palertswmocountryc, numalertsc)
    writeconkystatement(palertswmoregion, palertswmoregionc, numalertsr)
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed