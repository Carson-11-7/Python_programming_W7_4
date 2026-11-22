DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    hour = 0
    consumption = 0.0
    price = 0.0

def readFile(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()
    filehandle = open(PFilename, "r", encoding="utf-8")
    firstLine = True
    for line in filehandle:
        if firstLine:       
            firstLine = False
            continue
        if line == "\n":       
            continue
        row = line.rstrip()
        columns = row.split(DELIMITER)
        timestamp = TIMESTAMP()
        timestamp.weekday = columns[0]
        timestamp.hour = int(columns[1])
        timestamp.consumption = float(columns[2])
        timestamp.price = float(columns[3])
        PTimestamps.append(timestamp)
        columns.clear()
    filehandle.close()
    return None

def analyseTimestamps(PTimestamps: list[TIMESTAMP], PResults: list[str]) -> None:
    PResults.append("Electricity usage:")
    for timestamp in PTimestamps:
        total = timestamp.price * timestamp.consumption
        PResults.append(
            f" - {timestamp.weekday} {timestamp.hour:02d}:00, "
            f"price {timestamp.price:.2f}, "
            f"consumption {timestamp.consumption:.2f} kWh, "
            f"total {total:.2f} €"
            )
    return None

def displayResults(PResults: list[str]) -> None:
    for line in PResults:
        print(line)
    return None

def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []
    results: list[str] = []
    filename = input("Insert filename: ")
    readFile(filename, timestamps)
    analyseTimestamps(timestamps, results)
    displayResults(results)
    timestamps.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
