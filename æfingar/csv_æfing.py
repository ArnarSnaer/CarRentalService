import csv

def main():

    new_video = [["Back to the future 1","Adventure; action; Romance; sci-fi", 74]]
    with open("videos.csv","r") as video_file:

        # csv_writer = csv.writer(video_file, delimiter=";")

        #for video in new_video:
        #   csv_writer.writerow(video)

        csv_reader = csv.reader(video_file, delimiter=";")
        for line in csv_reader:
            print(line)

main()