import py_midicsv as pm

#convert csv-mid format into arduino tones() formatted nested list
def midCsvToArduinoParser(csv_string, track_n):
    csv_string = list(map(lambda s: s.strip(), csv_string))
    tones_arduino = list()
    for j in range (len(csv_string)):
        element = csv_string[j-1]
        internal_list = element.split(", ")
        if internal_list[0] == str(track_n):
            if len(internal_list) >= 4:
                instruction_name = internal_list[2]
                if instruction_name == "Note_off_c" or instruction_name == "Note_on_c":
                    time_previous = int(csv_string[j - 2].split(", ")[1])
                    time_current = int(internal_list[1])
                    if instruction_name == "Note_on_c":
                        rest_duration = time_current - time_previous
                        if rest_duration > 0:
                            tones_arduino.append(["0", rest_duration])
                    elif instruction_name == "Note_off_c":
                        tone_mid = internal_list[4]
                        tone_duration = time_current - time_previous
                        tone_arduino = tones_dict[tone_mid]
                        tones_arduino.append([tone_arduino, tone_duration])
    return tones_arduino


# dictionary containing realtions between .mid format notes ()
tones_dict = {'111': 'NOTE_DS8', '110': 'NOTE_D8', '109': 'NOTE_CS8', '108': 'NOTE_C8', '107': 'NOTE_B7', '106': 'NOTE_AS7', '105': 'NOTE_A7', '104': 'NOTE_GS7', '103': 'NOTE_G7', '102': 'NOTE_FS7', '101': 'NOTE_F7', '100': 'NOTE_E7', '99': 'NOTE_DS7', '98': 'NOTE_D7', '97': 'NOTE_CS7', '96': 'NOTE_C7', '95': 'NOTE_B6', '94': 'NOTE_AS6', '93': 'NOTE_A6', '92': 'NOTE_GS6', '91': 'NOTE_G6', '90': 'NOTE_FS6', '89': 'NOTE_F6', '88': 'NOTE_E6', '87': 'NOTE_DS6', '86': 'NOTE_D6', '85': 'NOTE_CS6', '84': 'NOTE_C6', '83': 'NOTE_B5', '82': 'NOTE_AS5', '81': 'NOTE_A5', '80': 'NOTE_GS5', '79': 'NOTE_G5', '78': 'NOTE_FS5', '77': 'NOTE_F5', '76': 'NOTE_E5', '75': 'NOTE_DS5', '74': 'NOTE_D5', '73': 'NOTE_CS5', '72': 'NOTE_C5', '71': 'NOTE_B4', '70': 'NOTE_AS4', '69': 'NOTE_A4', '68': 'NOTE_GS4', '67': 'NOTE_G4', '66': 'NOTE_FS4', '65': 'NOTE_F4', '64': 'NOTE_E4', '63': 'NOTE_DS4', '62': 'NOTE_D4', '61': 'NOTE_CS4', '60': 'NOTE_C4', '59': 'NOTE_B3', '58': 'NOTE_AS3', '57': 'NOTE_A3', '56': 'NOTE_GS3', '55': 'NOTE_G3', '54': 'NOTE_FS3', '53': 'NOTE_F3', '52': 'NOTE_E3', '51': 'NOTE_DS3', '50': 'NOTE_D3', '49': 'NOTE_CS3', '48': 'NOTE_C3', '47': 'NOTE_B2', '46': 'NOTE_AS2', '45': 'NOTE_A2', '44': 'NOTE_GS2', '43': 'NOTE_G2', '42': 'NOTE_FS2', '41': 'NOTE_F2', '40': 'NOTE_E2', '39': 'NOTE_DS2', '38': 'NOTE_D2', '37': 'NOTE_CS2', '36': 'NOTE_C2', '35': 'NOTE_B1', '34': 'NOTE_AS1', '33': 'NOTE_A1', '32': 'NOTE_GS1', '31': 'NOTE_G1', '30': 'NOTE_FS1', '29': 'NOTE_F1', '28': 'NOTE_E1', '27': 'NOTE_DS1', '26': 'NOTE_D1', '25': 'NOTE_CS1', '24': 'NOTE_C1', '23': 'NOTE_B0'}

# Load the MIDI file and parse it into CSV format
#csv_string = pm.midi_to_csv("example.mid")
input_name = "example_rest_in_the beginning"
csv = pm.midi_to_csv(input_name + ".mid")

#write converted csv into file (for testing purposes only)
with open("example_with_rest_converted.csv", "w") as f:
    f.writelines(csv)


result = midCsvToArduinoParser(csv, 2)
print(result)




