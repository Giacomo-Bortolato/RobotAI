import os
import sys, getopt
import signal
import time
from edge_impulse_linux.audio import AudioImpulseRunner
MODELPATH = "/home/arduino/.ei-linux-runner/models/929457/v6-quantized-runner-linux-aarch64/model.eim"
parametriMain=[MODELPATH,"2"]
runner = None

def signal_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def help():
    print('python classify.py <path_to_model.eim> <audio_device_ID, optional>' )

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

    if len(args) == 0:
        help()
        sys.exit(2)

    model = args[0]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    with AudioImpulseRunner(modelfile) as runner:
        try:
            model_info = runner.init()
            # model_info = runner.init(debug=True, timeout=60) # to get debug print out and set longer timeout
            labels = model_info['model_parameters']['labels']
            print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')

            #Let the library choose an audio interface suitable for this model, or pass device ID parameter to manually select a specific audio interface
            selected_device_id = None
            if len(args) >= 2:
                selected_device_id=int(args[1])
                print("Device ID "+ str(selected_device_id) + " has been provided as an argument.")
                print("In ascolto!!")

            for res, audio in runner.classifier(device_id=selected_device_id):
                if "classification" in res["result"].keys():
                    for label in labels:
                        score = res['result']['classification'][label]
                        if label == "Hey Arduino" and score >= 0.80:
                                print("Hey Arduino spotted!!")
                                runner.stop()
                                return True
                                


                                
                            
        finally:
            if (runner):
                runner.stop()

if __name__ == '__main__':
    main(parametriMain)