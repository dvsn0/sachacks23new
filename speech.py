from hume import HumeBatchClient
from hume.models.config import ProsodyConfig
from dotenv import load_dotenv
import os
import pprint
from utilities import print_emotions

#Load in API Key and use it in the client
load_dotenv()
apiKey = os.environ['API_KEY']
client = HumeBatchClient(apiKey)

#Define filepath and job
filepaths = ["sampleSpeech.mp3"]
config = ProsodyConfig()
job = client.submit_job(None, [config], files=filepaths)

#Run job
print(job)
print("Running...")

#Get job results
job.await_complete()
#predictions = job.get_predictions()
#print(predictions)

full_predictions = job.get_predictions()
for source in full_predictions:
    source_name = source["source"]
    predictions = source["results"]["predictions"]
    for prediction in predictions:
        print()
        print("Speech prosody")
        prosody_predictions = prediction["models"]["prosody"]["grouped_predictions"]
        for prosody_prediction in prosody_predictions:
            for segment in prosody_prediction["predictions"][:1]:
                print_emotions(segment["emotions"])

#Take out only data we need
## emotion_data = predictions[0]['results']['predictions'][0]['models']['face']['grouped_predictions'][0]['predictions'][0]['emotions']
## emotion_dict = {emotion['name']: emotion['score'] for emotion in emotion_data}

#Sort emotions from highest scores to lowest
## sorted_emotions = dict(sorted(emotion_dict.items(), key=lambda item: item[1], reverse=True))

## pprint.pprint(sorted_emotions)

# if emotion_dict["Anxiety"] > 0.2 or emotion_dict["Distress"] > 0.2 or emotion_dict["Doubt"] > 0.2 or emotion_dict["Sadness"] > 0.2 or emotion_dict["Guilt"] > 0.2:
#     send_alert_to_website("Do NOT purchase")
# else:
#     send_alert_to_website("Go ahead and purchase")

#Print sorted list of emotions to file
# output_file = "sorted_emotions.txt"
# with open(output_file, "w") as file:
#     for emotion, score in sorted_emotions.items():
#         file.write(f'{emotion}: {score}\n')

#Report finished
print("Done!")
scores = []
# output_file_2 = 'emotion_scores.txt'
# with open(output_file_2, "w") as file:
#     for emotion in emotion_dict:
#         file.write(f'{emotion_dict[emotion]},')
